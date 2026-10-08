"""Misura lo stile dei capitoli dei Word per non scivolare nel "troppo bullet" (o nel muro di testo).

Per ogni capitolo: paragrafi di testo, quota di elenchi puntati, lunghezza media dei paragrafi in parole,
numero di paragrafi molto lunghi (> 110 parole). Confronta con la media di Emanuele (i capitoli che ha accettato)
e segnala gli scostamenti forti.

Uso: python misura_stile.py [materia]
"""
import statistics
import sys
from pathlib import Path

from docx import Document

UNI = Path(__file__).resolve().parent.parent.parent.parent
WORDS = {
    "Algebra lineare": "Riassunto Algebra lineare.docx",
    "Matematica discreta": "Appunti matematica discreta.docx",
    "Fondamenti Info": "Fondamenti Informatica.docx",
    "Programmazione": "Riassunto Programmazione.docx",
    "Programmazione/Laboratorio": "Laboratorio.docx",
}


def is_bullet(p) -> bool:
    return p._p.pPr is not None and p._p.pPr.numPr is not None


def chapter_stats(P):
    heads = [i for i, p in enumerate(P) if p.style.name == "Heading 1"] or [0]
    out = []
    for k, i in enumerate(heads):
        j = heads[k + 1] if k + 1 < len(heads) else len(P)
        seg = [p for p in P[i + 1:j] if p.text.strip() and not p.style.name.startswith("Heading")
               and not any((r.font.name or "").lower() in ("consolas", "courier new") for r in p.runs)]
        if not seg:
            continue
        b = sum(1 for p in seg if is_bullet(p))
        words = [len(p.text.split()) for p in seg if not is_bullet(p)] or [0]
        out.append(dict(titolo=P[i].text[:46], n=len(seg), bullet=100 * b / len(seg),
                        media=statistics.mean(words), lunghi=sum(1 for w in words if w > 110)))
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sel = sys.argv[1:] or list(WORDS)
    allstats = {m: chapter_stats(Document(str(UNI / m.split("/")[0] / WORDS[m])).paragraphs) for m in sel}
    flat = [c for v in allstats.values() for c in v]
    ref_b = statistics.median(c["bullet"] for c in flat)
    ref_m = statistics.median(c["media"] for c in flat)
    print(f"Riferimento (mediana di tutti i capitoli): {ref_b:.0f}% elenchi, paragrafi da {ref_m:.0f} parole\n")
    for m, st in allstats.items():
        print(f"== {m}")
        for c in st:
            flag = []
            if c["bullet"] > max(2 * ref_b, 55):
                flag.append("troppi elenchi")
            if c["media"] > 1.8 * ref_m or c["lunghi"] >= 3:
                flag.append("paragrafi lunghi")
            print(f"  {c['titolo']:48s} {c['n']:3d} par  {c['bullet']:3.0f}% elenchi  media {c['media']:4.0f} parole  lunghi {c['lunghi']}"
                  + (f"   <-- {', '.join(flag)}" if flag else ""))


if __name__ == "__main__":
    main()
