"""Converte la raccolta dei quiz di Fondamenti (esami.i-learn.unito.it, JSON grezzo) in:
  - _sistema/esami/fondamenti_quiz.md              banca di domande con risposta e spiegazione (per /esame)
  - _sistema/flashcard/Fondamenti Info.quiz.md     schede D:/R: per Anki e per la pagina di studio
  - _sistema/esami/FONDAMENTI_MAPPA.md             quante domande per gruppo di lezioni e per tipo

Input: _sistema/esami/fondamenti_raw/quiz_bank.json (prodotto dal browser). Uso: python converti_quiz_fondamenti.py
"""
import collections
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
RAW = BASE / "esami" / "fondamenti_raw" / "quiz_bank.json"
GROUPS = {
    "L01-06": "circuiti e rappresentazione binaria (lezioni 1-6)",
    "L07-13": "logica proposizionale e quantificatori (lezioni 7-13)",
    "L14-18": "prove con quantificatori (lezioni 14-18)",
    "L19-23": "invarianti e induzione (lezioni 19-23)",
    "L24-26": "sequenze e relazioni (lezioni 24-26)",
    "L27-30": "algebre di Boole (lezioni 27-30)",
    "L31-35": "logica sequenziale, automi, grammatiche (lezioni 31-35)",
    "Sim2023": "simulazioni d'esame 2023",
    "Esami2026": "esami 2026", "Esami2025": "esami 2025", "Esami2024": "esami 2024",
}
PREFIX = re.compile(r"^\s*La risposta corretta (?:è|sono)\s*:?\s*", re.I)
TAIL = re.compile(r"\s*Pagina:\s*Lezioni?.*$", re.S)


def clean(s: str) -> str:
    s = TAIL.sub("", s or "").replace("\u00a0", " ")
    return re.sub(r"[ \t]+", " ", s).strip()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    bank = json.loads(RAW.read_text(encoding="utf-8"))
    md = ["# Banca di domande di Fondamenti dell'Informatica (quiz del sito esami, a.a. 2026/27)", "",
          "Fonte: esami.i-learn.unito.it, corso «Esami di Fondamenti di Informatica A+B+C». Quiz di ripasso per lezione e prove d'esame 2023-2026 «solo per esercitarsi». "
          "Risposta e spiegazione sono quelle mostrate dal sito dopo la correzione.", ""]
    cards = []
    stat_g, stat_t, n = collections.Counter(), collections.Counter(), 0
    for q in bank:
        qs = q.get("questions") or []
        if not qs:
            continue
        title = clean(q.get("linkTitle") or q.get("title") or "")
        src = q.get("src")
        if not src:
            m = re.search(r"Lezion[ei]\s*0?(\d+)", title)
            if m:
                k = int(m.group(1))
                src = next((g for g, (a, b) in {"L01-06": (1, 6), "L07-13": (7, 13), "L14-18": (14, 18), "L19-23": (19, 23), "L24-26": (24, 26), "L27-30": (27, 30), "L31-35": (31, 35)}.items() if a <= k <= b), None)
        group = GROUPS.get(src, "altro")
        for i, x in enumerate(qs, 1):
            right = PREFIX.sub("", clean(x.get("right")))
            if not right or x.get("type") == "essay":
                continue
            text = clean(x.get("text"))
            opts = [clean(o) for o in x.get("options", [])] if x.get("type") in ("multichoice", "multichoiceset", "oumultiresponse", "truefalse") else []
            fb = clean(x.get("feedback"))
            n += 1; stat_g[group] += 1; stat_t[x["type"]] += 1
            qid = f"fond-{q['cmid']}-Q{i}"
            md += [f"## [{qid}] argomenti: {group} | tipo: {x['type']} | quiz: {title}", text]
            md += [f"- {o}" for o in opts]
            md += [f"RISPOSTA: {right}", f"SPIEGAZIONE: {fb}" if fb else "SPIEGAZIONE: (nessuna nel sito)", ""]
            front = text + ("\n" + "\n".join(f"- {o}" for o in opts) if opts else "")
            back = right + (f"\n{fb}" if fb else "")
            cards.append(f"## {title[:60]} ({group.split(' (')[0]})\nD: {front}\nR: {back}\n")
    (BASE / "esami" / "fondamenti_quiz.md").write_text("\n".join(md), encoding="utf-8")
    (BASE / "flashcard" / "Fondamenti Info.quiz.md").write_text("\n".join(cards), encoding="utf-8")
    mp = ["# Banca quiz di Fondamenti: mappa", "", f"{n} domande con risposta, da {sum(1 for q in bank if q.get('questions'))} quiz.", "",
          "| Gruppo di lezioni | Domande |", "|---|---|"] + [f"| {g} | {c} |" for g, c in stat_g.most_common()] + \
         ["", "| Tipo di domanda | Domande |", "|---|---|"] + [f"| {t} | {c} |" for t, c in stat_t.most_common()]
    (BASE / "esami" / "FONDAMENTI_MAPPA.md").write_text("\n".join(mp), encoding="utf-8")
    print(f"{n} domande -> esami/fondamenti_quiz.md, {len(cards)} schede -> flashcard/Fondamenti Info.quiz.md")
    for g, c in stat_g.most_common():
        print(f"  {c:3d}  {g}")


if __name__ == "__main__":
    main()
