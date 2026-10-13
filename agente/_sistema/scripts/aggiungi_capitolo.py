"""Aggiunge un capitolo (scritto in un file .md semplice) in fondo a un Word di riassunti,
replicando la formattazione dei tuoi documenti.

Uso:
    python aggiungi_capitolo.py "Riassunto Algebra lineare.docx" capitolo.md
    python aggiungi_capitolo.py ... capitolo.md --dry-run     # non scrive, mostra solo l'esito

Formato del .md:
    # 7. Titolo del capitolo            -> grassetto rosso (come i tuoi capitoli)
    ## Sottotitolo                      -> grassetto arancione
    testo con **grassetto** e *corsivo*
    - elenco puntato
    1. elenco numerato (resta testo con numero)
    riga vuota = nuovo paragrafo

Sicurezza: prima di scrivere fa una copia in _sistema/backup/ e si rifiuta di lavorare se il
file e' aperto in Word (esiste il file di blocco ~$...).
"""
import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt, RGBColor

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from percorsi_word import trova  # noqa: E402
UNI = BASE.parent.parent  # cartella UNI con le 4 materie (BASE = UNI/agente/_sistema)
RED = RGBColor(0xEE, 0x00, 0x00)
ORANGE = RGBColor(0xE9, 0x71, 0x32)
# l'apice puo' contenere un pedice annidato (es. e^{iθ_{1}}): in Word non si puo' avere apice+pedice,
# quindi dentro l'apice il pedice viene scritto come testo normale (θ1).
TOKEN = re.compile(r"(\*\*|~|`|\^\{(?:[^{}]|\{[^}]*\})*\}|_\{[^}]*\})")
STAR = ""  # segnaposto per l'asterisco letterale \*
NESTED = re.compile(r"_\{([^}]*)\}")


def bullet_numid(doc: Document):
    """Trova un numId di elenco puntato gia' presente nel documento."""
    try:
        numbering = doc.part.numbering_part.element
    except Exception:
        return None
    bullet_abs = set()
    for a in numbering.findall(qn("w:abstractNum")):
        lvl = a.find(qn("w:lvl"))
        fmt = lvl.find(qn("w:numFmt")) if lvl is not None else None
        if fmt is not None and fmt.get(qn("w:val")) == "bullet":
            bullet_abs.add(a.get(qn("w:abstractNumId")))
    for n in numbering.findall(qn("w:num")):
        ref = n.find(qn("w:abstractNumId"))
        if ref is not None and ref.get(qn("w:val")) in bullet_abs:
            return n.get(qn("w:numId"))
    return None


def add_runs(par, text, color=None, bold=False):
    """**grassetto**, ~corsivo~, ^{apice}, _{pedice}; per un asterisco letterale si scrive backslash+asterisco."""
    b, i, code = bold, False, False
    for tok in TOKEN.split(text.replace("\\*", STAR)):
        if not tok:
            continue
        if tok == "**":
            b = not b
            continue
        if tok == "~":
            i = not i
            continue
        if tok == "`":      # testo di codice/comando in linea: Consolas
            code = not code
            continue
        sup = tok.startswith("^{")
        sub = tok.startswith("_{")
        body = tok[2:-1] if (sup or sub) else tok
        if sup:
            body = NESTED.sub(r"\1", body)
        run = par.add_run(body.replace(STAR, "*"))
        run.bold = True if (b or color is not None) else None
        run.italic = True if i else None
        if code:
            run.font.name = "Consolas"
            rf = run._r.get_or_add_rPr().find(qn("w:rFonts"))
            if rf is not None:
                rf.set(qn("w:hAnsi"), "Consolas"); rf.set(qn("w:cs"), "Consolas")
        if sup:
            run.font.superscript = True
        if sub:
            run.font.subscript = True
        if color is not None:
            run.font.color.rgb = color


def style_by_id(doc, style_id):
    for st in doc.styles:
        if st.style_id == style_id:
            return st
    return None


def doc_has_heading_styles(doc) -> bool:
    """Usa Titolo 1/2 solo se il documento ha gia' i titoli con stile (dopo stili_word.py): niente miscele."""
    return any(p.style.style_id in ("Titolo1", "Titolo2") for p in doc.paragraphs)


def set_bullet(par, numid):
    pPr = par._p.get_or_add_pPr()
    numPr = OxmlElement("w:numPr")
    ilvl = OxmlElement("w:ilvl"); ilvl.set(qn("w:val"), "0")
    nid = OxmlElement("w:numId"); nid.set(qn("w:val"), str(numid))
    numPr.append(ilvl); numPr.append(nid)
    pPr.append(numPr)


def post_controlli(target: Path) -> None:
    """Dopo l'inserimento: controllo qualita' del Word e backup su OneDrive (non bloccano mai)."""
    import subprocess
    here = Path(__file__).resolve().parent
    py = sys.executable
    for script, args in (("verifica_word.py", []), ("backup_onedrive.py", [])):
        try:
            r = subprocess.run([py, str(here / script), *args], capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=180)
            out = (r.stdout or "").strip()
            if out:
                print(out)
            if r.returncode and script == "verifica_word.py":
                print("ATTENZIONE: il controllo ha trovato errori nel Word (vedi sopra).")
        except Exception as e:  # noqa: BLE001
            print(f"({script} non eseguito: {e})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx"); ap.add_argument("md")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    target = Path(a.docx)
    if not target.is_absolute():
        target = UNI / target
    if not target.exists():  # i Word possono stare sciolti in UNI\ (nuovo nome) invece che nelle sottocartelle
        target = trova(UNI, target.parent.name, target.name)
    src = Path(a.md)
    if not target.exists() or not src.exists():
        sys.exit(f"File non trovato: {target if not target.exists() else src}")

    # Word crea "~$" + nome senza i primi 2 caratteri mentre il file e' aperto
    lock = target.with_name("~$" + target.name[2:])
    if lock.exists() and not a.dry_run:
        sys.exit(f"Il Word e' aperto ({lock.name}). Chiudilo e riprova: non scrivo per non rovinarlo.")

    doc = Document(str(target))
    numid = bullet_numid(doc)
    h1, h2 = style_by_id(doc, "Titolo1"), style_by_id(doc, "Titolo2")
    n_par = 0
    in_code = False
    for raw in src.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.lstrip().startswith("```"):
            if in_code:           # fine del blocco: riga vuota come nei tuoi Word
                doc.add_paragraph(); n_par += 1
            in_code = not in_code
            continue
        if in_code:               # codice: un paragrafo per riga, Consolas 8,5 pt, senza spaziatura
            p = doc.add_paragraph(); n_par += 1
            r = p.add_run(raw.rstrip("\n"))
            r.font.name = "Consolas"; r.font.size = Pt(8.5)
            rpr = r._r.get_or_add_rPr()
            rf = rpr.find(qn("w:rFonts"))
            if rf is not None:
                rf.set(qn("w:hAnsi"), "Consolas"); rf.set(qn("w:cs"), "Consolas")
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            continue
        if not line.strip():
            continue
        im = re.match(r"^!\[(.*?)\]\((.+?)\)\s*$", line.strip())
        if im:                     # figura: ![didascalia](figure/nome.png|larghezza_cm), percorso relativo a _sistema/
            didascalia, spec = im.group(1).strip(), im.group(2).strip()
            percorso, _, larg = spec.partition("|")
            img = Path(percorso)
            if not img.is_absolute():
                img = BASE / img
            if not img.exists():
                sys.exit(f"Figura non trovata: {img}")
            pf = doc.add_paragraph(); n_par += 1
            pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
            pf.paragraph_format.keep_with_next = bool(didascalia)
            pf.add_run().add_picture(str(img), width=Cm(float(larg) if larg.strip() else 11))
            if didascalia:
                pc = doc.add_paragraph(); n_par += 1
                pc.alignment = WD_ALIGN_PARAGRAPH.CENTER
                rc = pc.add_run(didascalia); rc.italic = True; rc.font.size = Pt(9)
            continue
        p = doc.add_paragraph()
        n_par += 1
        if line.startswith("## "):
            add_runs(p, line[3:].strip(), color=ORANGE)
            if h2 is not None and doc_has_heading_styles(doc):
                p.style = h2
        elif line.startswith("# "):
            add_runs(p, line[2:].strip(), color=RED)
            if h1 is not None and doc_has_heading_styles(doc):
                p.style = h1
        elif re.match(r"^\s*[-*] ", line):
            add_runs(p, re.sub(r"^\s*[-*] ", "", line))
            if numid:
                set_bullet(p, numid)
        else:
            add_runs(p, line.strip())

    if a.dry_run:
        print(f"[dry-run] aggiungerei {n_par} paragrafi a {target.name} (elenco puntato: {'si' if numid else 'no'})")
        return

    bk = BASE / "backup"
    bk.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copy2(target, bk / f"{target.stem}_{stamp}{target.suffix}")
    doc.save(str(target))
    print(f"OK: {n_par} paragrafi aggiunti a {target.name} (backup in _sistema/backup)")
    post_controlli(target)


if __name__ == "__main__":
    main()
