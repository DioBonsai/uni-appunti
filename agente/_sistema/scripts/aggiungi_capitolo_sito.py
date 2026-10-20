"""Aggiunge un capitolo (scritto in una bozza .md) ai riassunti del sito: da quando i Word non si usano più, i contenuti
stanno in <repo sito>/contenuti/<materia>.json e le pagine si costruiscono da lì (pubblica_quaderno.py).

Uso:
    python aggiungi_capitolo_sito.py <materia> bozza.md [--dry-run] [--repo CARTELLA_SITO]
    materia: algebra | matematica-discreta (o mate) | fondamenti | programmazione | laboratorio

Sintassi della bozza (la stessa di prima):
    # N. Titolo            (Programmazione/Laboratorio: # Capitolo N: Titolo)
    ## sottotitolo
    - elenco puntato
    una riga = un paragrafo; "(In parole povere: ...)" diventa il riquadro verde
    **grassetto**   ~corsivo~   `codice`   ^{apice}   _{pedice}   (backslash+asterisco = * letterale)
    ```  blocchi di codice  ```
    ![didascalia](figure/percorso.png|larghezza_cm)     (percorso relativo a _sistema/)
Le evidenziazioni non si toccano: un capitolo nuovo parte senza evidenziazioni.
"""
import argparse
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from migra_word import html_parti, numero, riquadro_pp, testo  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
REPO = Path.home() / "Documents" / "GitHub" / "quaderno-privato"
ALIAS = {"mate": "matematica-discreta", "matematica": "matematica-discreta", "matematica discreta": "matematica-discreta",
         "algebra lineare": "algebra", "fondamenti info": "fondamenti", "lab": "laboratorio"}
TOKEN = re.compile(r"(\*\*|~|`|\^\{(?:[^{}]|\{[^}]*\})*\}|_\{[^}]*\})")
STAR = "\x00"
NESTED = re.compile(r"_\{([^}]*)\}")


def parti_da_testo(riga):
    """Testo con marcatori -> parti con gli stessi campi dei Word (b, i, sup, sub, code)."""
    b = i = code = False
    parts = []
    for tok in TOKEN.split(riga.replace("\\*", STAR)):
        if not tok:
            continue
        if tok == "**":
            b = not b; continue
        if tok == "~":
            i = not i; continue
        if tok == "`":
            code = not code; continue
        sup, sub = tok.startswith("^{"), tok.startswith("_{")
        corpo = tok[2:-1] if (sup or sub) else tok
        if sup:
            corpo = NESTED.sub(r"\1", corpo)
        parts.append({"t": corpo.replace(STAR, "*"), "b": b, "i": i, "sup": sup, "sub": sub, "code": code, "mk": False})
    return parts


def figura(percorso, larg_cm, repo):
    img = Path(percorso)
    if not img.is_absolute():
        img = BASE / img
    if not img.exists():
        sys.exit(f"Figura non trovata: {img}")
    blob = img.read_bytes()
    nome = hashlib.sha1(blob).hexdigest()[:14] + img.suffix.lower()
    dest = repo / "contenuti" / "img"
    dest.mkdir(parents=True, exist_ok=True)
    (dest / nome).write_bytes(blob)
    from PIL import Image
    with Image.open(img) as im:
        w, h = im.size
    px = int(round(float(larg_cm or 11) * 96 / 2.54))
    return {"t": "fig", "src": nome, "w": px, "cx": w, "cy": h}


def blocchi_da_bozza(src, repo, cap_id):
    out, n = [], 0
    in_code, codice = False, []

    def nuovo():
        nonlocal n
        n += 1
        return f"{cap_id}.{n}"

    titolo = None
    for raw in src.read_text(encoding="utf-8").splitlines():
        riga = raw.rstrip()
        if riga.lstrip().startswith("```"):
            if in_code and codice:
                out.append({"t": "pre", "b": nuovo(), "h": chr(10).join(html_parti(parti_da_testo_codice(r), codice=False) for r in codice)})
                codice = []
            in_code = not in_code
            continue
        if in_code:
            codice.append(raw.rstrip(chr(10)))
            continue
        if not riga.strip():
            continue
        m = re.match(r"^!\[(.*?)\]\((.+?)\)\s*$", riga.strip())
        if m:
            didascalia, spec = m.group(1).strip(), m.group(2).strip()
            percorso, _, larg = spec.partition("|")
            f = figura(percorso, larg.strip(), repo)
            if didascalia:
                f["cap"] = didascalia
            out.append(f)
            continue
        if riga.startswith("## "):
            parts = parti_da_testo(riga[3:].strip())
            neutri = [{**p, "b": False, "i": False, "code": False} for p in parts]
            out.append({"t": "h3", "b": nuovo(), "h": html_parti(neutri)})
        elif riga.startswith("# "):
            titolo = riga[2:].strip()
        elif re.match(r"^\s*[-*] ", riga):
            parts = parti_da_testo(re.sub(r"^\s*[-*] ", "", riga))
            out.append({"t": "li", "b": nuovo(), "h": html_parti(parts), "k": "ul", "l": 0})
        else:
            parts = parti_da_testo(riga.strip())
            pp = riquadro_pp(parts)
            blk = {"t": "p", "b": nuovo(), "h": html_parti(parts)}
            if pp:
                blk["c"] = "pp"
            out.append(blk)
    return titolo, out


def parti_da_testo_codice(riga):
    return [{"t": riga, "b": False, "i": False, "sup": False, "sub": False, "code": True, "mk": False}]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("materia")
    ap.add_argument("bozza")
    ap.add_argument("--repo", default=str(REPO))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    slug = ALIAS.get(a.materia.lower(), a.materia.lower())
    repo = Path(a.repo)
    fj = repo / "contenuti" / f"{slug}.json"
    if not fj.exists():
        sys.exit(f"Materia sconosciuta o contenuti mancanti: {fj}")
    src = Path(a.bozza)
    if not src.exists():
        sys.exit(f"Bozza non trovata: {src}")
    dati = json.loads(fj.read_text(encoding="utf-8"))
    # titolo e numero dalla prima riga "# "
    prima = next((r for r in src.read_text(encoding="utf-8").splitlines() if r.startswith("# ")), None)
    if not prima:
        sys.exit("La bozza deve iniziare con '# N. Titolo'")
    titolo = re.sub(r"\s+", " ", prima[2:]).strip()
    n = numero(titolo)
    if n is None:
        sys.exit("Il titolo deve avere il numero del capitolo (es. '# 29. Titolo' o '# Capitolo 23: Titolo')")
    if any(c["num"] == n for c in dati["capitoli"]):
        sys.exit(f"Esiste già il capitolo {n} in {slug}: scegli il numero successivo (ultimo: {max(c['num'] for c in dati['capitoli'] if c['num'])})")
    cap_id = f"cap{n}"
    _t, blocks = blocchi_da_bozza(src, repo, cap_id)
    n_hl = sum(1 for b in blocks if b["t"] in ("p", "li", "pre"))
    if a.dry_run:
        print(f"[dry-run] aggiungerei il capitolo {n} «{titolo}» a {slug}: {len(blocks)} blocchi ({n_hl} di testo)")
        return
    bk = BASE / "backup"
    bk.mkdir(exist_ok=True)
    shutil.copy2(fj, bk / f"{slug}_contenuti_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    dati["capitoli"].append({"id": cap_id, "num": n, "titolo": titolo, "blocks": blocks})
    fj.write_text(json.dumps(dati, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"OK: capitolo {n} «{titolo}» aggiunto a {slug} ({len(blocks)} blocchi). Ora: python pubblica_quaderno.py --push")


if __name__ == "__main__":
    main()
