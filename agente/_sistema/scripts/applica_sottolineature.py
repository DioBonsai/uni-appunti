"""Applica ai Word le sottolineature fatte nel Quaderno (da tablet, telefono o PC).

Legge:  _sistema/sottolineature.json  {"v": 1, "items": [{id, m, q, p, s, h, t}]}
        m = materia (slug di pagina_studio/riassunti/), q = testo sottolineato, p/s = qualche carattere prima/dopo
        nello stesso blocco, h = titolo piu' vicino, t = data
Scrive: evidenziazione gialla (stessa dei Word: w:highlight yellow) sui run che contengono q. Non cambia il testo,
        non toglie ne' sposta evidenziazioni esistenti. Prima copia il Word in _sistema/backup/.
Poi:    toglie dal JSON le sottolineature applicate (o gia' evidenziate), lascia quelle non trovate e le elenca.

Uso:  python applica_sottolineature.py [--dry-run] [--file altro.json]
Dopo: python costruisci_riassunti.py  (ricostruisce le pagine web) e commit.
"""
import argparse
import copy
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

from docx import Document
from docx.enum.text import WD_COLOR_INDEX
from docx.oxml.ns import qn

BASE = Path(__file__).resolve().parent.parent          # _sistema
UNI = BASE.parent.parent
FILE = BASE / "sottolineature.json"
WORD = {  # slug -> Word (gli stessi di costruisci_riassunti.py)
    "algebra-lineare": "Riassunto Algebra lineare.docx",
    "fondamenti-informatica": "Riassunto Fondamenti Informatica.docx",
    "laboratorio": "Riassunto Laboratorio.docx",
    "matematica-discreta": "Riassunto Matematica discreta.docx",
    "programmazione": "Riassunto Programmazione.docx",
}


def norm_map(s: str):
    """Testo con spazi ridotti a uno (NBSP compresi) e, per ogni carattere, la sua posizione nell'originale."""
    out, idx, prev_sp = [], [], False
    for i, ch in enumerate(s):
        sp = ch.isspace() or ch == " "
        if sp:
            if prev_sp:
                continue
            ch = " "
        out.append(ch)
        idx.append(i)
        prev_sp = sp
    return "".join(out), idx


def norm(s: str) -> str:
    return norm_map(s)[0]


def tutti_i_paragrafi(doc):
    """Paragrafi del corpo, delle tabelle e delle celle annidate, nell'ordine del documento."""
    from docx.text.paragraph import Paragraph
    for p in doc.element.body.iter(qn("w:p")):
        yield Paragraph(p, doc)


def e_titolo(p) -> bool:
    n = (p.style.name if p.style is not None else "") or ""
    return n.lower().startswith(("heading", "titolo"))


def run_semplice(r) -> bool:
    """Run con solo testo (niente tab, a capo, immagini): si puo' spezzare senza perdere nulla."""
    return all(c.tag in (qn("w:rPr"), qn("w:t")) for c in r._r)


def spezza(par, pos: int):
    """Garantisce che esista un confine di run alla posizione pos (in caratteri di par.text). Ritorna False se impossibile."""
    t = 0
    for r in par.runs:
        n = len(r.text)
        if t < pos < t + n:
            if not run_semplice(r):
                return False
            k = pos - t
            nuovo = copy.deepcopy(r._r)
            r._r.addnext(nuovo)
            tx = r.text
            r.text = tx[:k]
            from docx.text.run import Run
            Run(nuovo, par).text = tx[k:]
            for rr in (r._r, nuovo):          # i w:t con spazi iniziali/finali vogliono xml:space="preserve"
                for w in rr.iter(qn("w:t")):
                    w.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
            return True
        t += n
    return True


def evidenzia(par, a: int, b: int) -> bool:
    if not spezza(par, a) or not spezza(par, b):
        return False
    t = 0
    for r in par.runs:
        n = len(r.text)
        if n and t >= a and t + n <= b:
            r.font.highlight_color = WD_COLOR_INDEX.YELLOW
        t += n
    return True


def gia_evidenziato(par, a: int, b: int) -> bool:
    t, tot, hl = 0, 0, 0
    for r in par.runs:
        n = len(r.text)
        lo, hi = max(a, t), min(b, t + n)
        if hi > lo:
            tot += hi - lo
            if r.font.highlight_color is not None:
                hl += hi - lo
        t += n
    return tot > 0 and hl == tot


def posizioni(testo: str, it: dict):
    """Posizioni (in 'testo' originale) in cui compare q; se p/s ci sono, tiene quelle col contesto giusto."""
    nt, idx = norm_map(testo)
    q = norm(it["q"])
    if not q:
        return []
    trovate = []
    i = nt.find(q)
    while i != -1:
        trovate.append(i)
        i = nt.find(q, i + 1)
    p, s = norm(it.get("p", "")), norm(it.get("s", ""))
    buone = [i for i in trovate if nt[:i].endswith(p) and nt[i + len(q):].startswith(s)]
    scelte = buone or trovate
    return [(idx[i], idx[i + len(q) - 1] + 1, len(buone) > 0 or (not p and not s)) for i in scelte]


def applica_a_word(path: Path, items: list, dry: bool):
    """Ritorna (applicate, gia, non_trovate, ambigue) come liste di id."""
    doc = Document(str(path))
    pars = list(tutti_i_paragrafi(doc))
    testi_prima = [p.text for p in pars]
    titolo_corr, titoli = "", []
    for p in pars:
        if e_titolo(p) and p.text.strip():
            titolo_corr = norm(p.text).strip()
        titoli.append(titolo_corr)
    ok, gia, no, amb = [], [], [], []
    for it in items:
        cand = []
        for k, p in enumerate(pars):
            for a, b, ctx in posizioni(p.text, it):
                cand.append((k, a, b, ctx))
        if not cand:
            no.append(it["id"])
            continue
        h = norm(it.get("h", "")).strip()
        for filtro in (lambda c: c[3] and titoli[c[0]] == h, lambda c: c[3], lambda c: titoli[c[0]] == h, lambda c: True):
            sel = [c for c in cand if filtro(c)]
            if sel:
                break
        k, a, b, _ = sel[0]
        if len(sel) > 1:
            amb.append(it["id"])
        if gia_evidenziato(pars[k], a, b):
            gia.append(it["id"])
        elif evidenzia(pars[k], a, b):
            ok.append(it["id"])
        else:
            no.append(it["id"])
    if [p.text for p in pars] != testi_prima:
        raise RuntimeError("il testo del Word sarebbe cambiato: non salvo niente")
    if ok and not dry:
        doc.save(str(path))
    return ok, gia, no, amb


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--file", default=str(FILE))
    a = ap.parse_args()
    f = Path(a.file)
    if not f.exists():
        print("Nessuna sottolineatura da applicare.")
        return
    dati = json.loads(f.read_text(encoding="utf-8"))
    items = dati.get("items", [])
    if not items:
        print("Nessuna sottolineatura da applicare.")
        return
    da_togliere, report = set(), []
    for slug in sorted({i["m"] for i in items}):
        mie = [i for i in items if i["m"] == slug]
        nome = WORD.get(slug)
        path = UNI / nome if nome else None
        if not path or not path.exists():
            report.append(f"{slug}: Word non trovato, {len(mie)} sottolineature lasciate in attesa")
            continue
        if (path.parent / ("~$" + path.name[2:])).exists() or list(path.parent.glob("~$*" + path.name[2:])):
            report.append(f"{slug}: il Word e' aperto (file ~$), chiudilo e riprova")
            continue
        if not a.dry_run:
            bk = BASE / "backup"
            bk.mkdir(exist_ok=True)
            shutil.copy2(path, bk / f"{path.stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{path.suffix}")
        ok, gia, no, amb = applica_a_word(path, mie, a.dry_run)
        da_togliere |= set(ok) | set(gia)
        report.append(f"{slug}: {len(ok)} applicate, {len(gia)} gia' evidenziate, {len(no)} non trovate"
                      + (f", {len(amb)} con piu' corrispondenze (applicata la prima nel titolo giusto)" if amb else ""))
        for i in mie:
            if i["id"] in no:
                report.append(f"   non trovata: «{i['q'][:70]}» (sotto «{i.get('h', '')[:50]}»)")
    print("\n".join(report))
    if a.dry_run:
        print("[dry-run] niente salvato")
        return
    dati["items"] = [i for i in items if i["id"] not in da_togliere]
    f.write_text(json.dumps(dati, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Tolte dal file {len(da_togliere)} sottolineature; restano {len(dati['items'])}.")
    print("Ora: python costruisci_riassunti.py  (e commit). Chiedi a Claude di togliere le stesse dal database del Quaderno.")
    if da_togliere:
        print("IDS_APPLICATE=" + ",".join(sorted(da_togliere)))


if __name__ == "__main__":
    sys.exit(main())
