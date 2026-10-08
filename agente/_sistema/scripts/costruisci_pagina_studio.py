"""Costruisce la pagina di studio interattiva (HTML unico) con i dati veri: quiz degli esami, flashcard e avanzamento.

Legge:  _sistema/esami/quiz_*.md, _sistema/flashcard/*.md, il modello _sistema/pagina_studio/template.html
Scrive: _sistema/pagina_studio/index.html  (da pubblicare come Artifact privato)

Aggiornare il dizionario AVANZAMENTO qui sotto quando cambia lo stato di studio (coerente con STATO.md).
Uso: python costruisci_pagina_studio.py
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from anki_build import parse_cards  # noqa: E402

AVANZAMENTO = {
    "Algebra lineare":     dict(capitoli=9,  studiati=0, lezioni="3 di 26", prossimo="Studiare i cap. 1-9 (campi, numeri complessi, forma polare, radici). Poi la lezione 4: Polinomi."),
    "Matematica discreta": dict(capitoli=9,  studiati=0, lezioni="3 fatte", prossimo="Studiare i cap. 1-9, soprattutto appartenenza/inclusione e funzioni (escono spesso). Il resto del corso è ancora da fare."),
    "Fondamenti Info":     dict(capitoli=11, studiati=7, lezioni="cap. 1 del libro", prossimo="Da studiare: cap. 5 (architettura e RAM), 6 (codifica dei dati), 7 (sistema binario), 11 (errori)."),
    "Programmazione":      dict(capitoli=8,  studiati=7, lezioni="slide 00-02B", prossimo="Da studiare: cap. 5 (dal linguaggio macchina al C). Poi riassumere le slide 02C (puntatori) e Lab01."),
}
FREQ = [  # (tema, quiz su 150, problemi su 30, nel Word)
    ("Permutazioni: cicli, tipo, periodo", 48, 14, False), ("Aritmetica modulare e congruenze", 21, 10, False),
    ("Z_N moltiplicativo (inversi, φ di Eulero)", 16, 9, False), ("Omomorfismi tra gruppi", 1, 9, False),
    ("Coefficienti binomiali e combinatoria", 15, 15, False), ("Gruppi, sottogruppi, generatori", 29, 11, False),
    ("Parità delle permutazioni", 6, 6, False), ("MCD e algoritmo di Euclide", 1, 7, False),
    ("Funzioni, composizione, iniettività", 33, 4, False), ("Appartenenza, inclusione, insiemi", 37, 0, True),
    ("Prodotto cartesiano, operazioni sugli insiemi", 21, 4, True), ("Relazioni, equivalenze, induzione", 0, 0, True),
]


def parse_quizzes():
    out = []
    for f in sorted((BASE / "esami").glob("quiz_*.md")):
        prova = ""
        for blk in re.split(r"(?m)^(?=#{1,2} )", f.read_text(encoding="utf-8")):
            if blk.startswith("# "):
                prova = blk.splitlines()[0][2:].strip()
                continue
            if not blk.startswith("## ["):
                continue
            head, _, body = blk.partition("\n")
            m = re.match(r"## \[([^\]]+)\]\s*argomenti:\s*(.*)", head)
            r = re.search(r"(?m)^RISPOSTA:\s*(\d)", body)
            if not m or not r:
                continue
            pre, _, post = body.partition("RISPOSTA:")
            lines = pre.strip().splitlines()
            first_opt = next((i for i, l in enumerate(lines) if re.match(r"^1\.\s", l)), None)
            if first_opt is None:
                continue
            opts = [re.sub(r"^\d\.\s*", "", l).strip() for l in lines[first_opt:] if re.match(r"^[1-5]\.\s", l)]
            if len(opts) != 5:
                continue
            sp = re.search(r"(?ms)SPIEGAZIONE:\s*(.*?)(?=^ATTENZIONE:|\Z)", post)
            at = re.search(r"(?ms)ATTENZIONE:\s*(.*)", post)
            out.append(dict(id=m.group(1), prova=prova, args=[a.strip() for a in m.group(2).split(",") if a.strip()],
                            q="\n".join(lines[:first_opt]).strip(), o=opts, a=int(r.group(1)),
                            s=(sp.group(1).strip() if sp else ""), w=(at.group(1).strip() if at else "")))
    return out


def parse_all_cards():
    out = []
    for mat in AVANZAMENTO:
        p = BASE / "flashcard" / f"{mat}.md"
        if p.exists():
            for i, (t, q, a) in enumerate(parse_cards(p)):
                out.append(dict(id=f"{mat[:3]}{i}", m=mat, t=t, d=q, r=a))
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    data = dict(oggi=str(date.today()), quiz=parse_quizzes(), cards=parse_all_cards(),
                materie=AVANZAMENTO, freq=FREQ)
    tpl = (BASE / "pagina_studio" / "template.html").read_text(encoding="utf-8")
    html = tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
    out = BASE / "pagina_studio" / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"{len(data['quiz'])} domande, {len(data['cards'])} schede -> {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
