"""Applica gli stili di titolo veri di Word (Titolo 1 / Titolo 2) ai titoli dei tuoi riassunti,
senza cambiarne l'aspetto, cosi' compaiono nel Pannello di navigazione e si puo' inserire un indice.

Riconosce i titoli dalla formattazione che gia' usi: capitolo = grassetto rosso (EE0000),
sottotitolo = grassetto arancione (E97132). L'aspetto non cambia: lo stile viene "neutralizzato"
(stessa dimensione, font e spaziatura del testo normale) e il colore resta quello della formattazione diretta.

Uso:
    python stili_word.py --dry-run [materia]     # mostra cosa cambierebbe
    python stili_word.py [materia]               # applica (con backup in _sistema/backup)
"""
import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BASE = Path(__file__).resolve().parent.parent
UNI = BASE.parent.parent
WORDS = {
    "Algebra lineare": "Riassunto Algebra lineare.docx",
    "Matematica discreta": "Appunti matematica discreta.docx",
    "Fondamenti Info": "Fondamenti Informatica.docx",
    "Programmazione": "Riassunto Programmazione.docx",
    "Programmazione/Laboratorio": "Laboratorio.docx",
}
RED, ORANGE = "EE0000", "E97132"


def find_style(doc, style_id):
    for st in doc.styles:
        if st.style_id == style_id:
            return st
    return None


def neutralize(style, level):
    """Svuota la formattazione dello stile (resta basato su Normale) e imposta solo struttura."""
    el = style.element
    for tag in ("w:pPr", "w:rPr"):
        for child in el.findall(qn(tag)):
            el.remove(child)
    pPr = OxmlElement("w:pPr")
    keep = OxmlElement("w:keepNext"); pPr.append(keep)
    ol = OxmlElement("w:outlineLvl"); ol.set(qn("w:val"), str(level)); pPr.append(ol)
    el.append(pPr)


def run_color(p):
    for r in p.runs:
        c = r.font.color
        if c is not None and c.rgb is not None:
            return str(c.rgb)
    return None


def classify(p):
    t = p.text.strip()
    if not t or len(t) > 140 or not p.runs or not all(r.bold for r in p.runs if r.text.strip()):
        return None
    col = run_color(p)
    if col == RED:
        return 1
    if col == ORANGE:
        return 2
    return None


def process(materia, dry):
    path = UNI / materia.split("/")[0] / WORDS[materia]
    doc = Document(str(path))
    s1, s2 = find_style(doc, "Titolo1"), find_style(doc, "Titolo2")
    todo = [(p, classify(p)) for p in doc.paragraphs]
    todo = [(p, lv) for p, lv in todo if lv]
    n1 = sum(1 for _, lv in todo if lv == 1)
    n2 = sum(1 for _, lv in todo if lv == 2)
    print(f"{materia}: titoli rossi (cap.) = {n1}, arancioni (sottotitoli) = {n2}; stili Titolo1/2 presenti: {bool(s1)}/{bool(s2)}")
    if dry or not todo:
        return
    if not (s1 and s2):
        print("  stili di titolo assenti nel documento: salto")
        return
    bk = BASE / "backup"; bk.mkdir(exist_ok=True)
    shutil.copy2(path, bk / f"{path.stem}_prima-stili_{datetime.now():%Y%m%d_%H%M%S}{path.suffix}")
    neutralize(s1, 0); neutralize(s2, 1)
    for p, lv in todo:
        p.style = s1 if lv == 1 else s2
    doc.save(str(path))
    print(f"  applicati: {n1} Titolo 1, {n2} Titolo 2 (backup creato)")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("materia", nargs="*")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    for m in a.materia or WORDS:
        process(m, a.dry_run)


if __name__ == "__main__":
    main()
