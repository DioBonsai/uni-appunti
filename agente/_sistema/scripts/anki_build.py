"""Costruisce mazzi Anki (.apkg) da file Markdown di flashcard e dalle banche di quiz degli esami.

Uso:
    python anki_build.py                 # costruisce tutti i mazzi
    python anki_build.py "Algebra lineare"

Input (in _sistema/flashcard/):  <materia>.md  con schede cosi':
    ## Titolo opzionale della scheda
    D: domanda (puo' occupare piu' righe)
    R: risposta (anche piu' righe; sono ammessi elenchi con "- ")
Per Matematica discreta, in piu' importa i quiz digitalizzati in _sistema/esami/quiz_*.md.
Output: _sistema/anki/<materia>.apkg  (si importa con doppio clic in Anki, oppure Anki > File > Importa).
Gli ID di mazzo e schede sono stabili: reimportando si aggiornano le schede senza duplicarle.
"""
import hashlib
import html
import re
import sys
from pathlib import Path

import genanki

BASE = Path(__file__).resolve().parent.parent
CARDS = BASE / "flashcard"
EXAMS = BASE / "esami"
OUT = BASE / "anki"

MODEL = genanki.Model(
    1607392319,
    "UNI Domanda/Risposta",
    fields=[{"name": "Domanda"}, {"name": "Risposta"}, {"name": "Fonte"}],
    templates=[{
        "name": "Scheda",
        "qfmt": "{{Domanda}}",
        "afmt": "{{FrontSide}}<hr id=answer>{{Risposta}}<br><br><small>{{Fonte}}</small>",
    }],
    css=".card{font-family:Arial;font-size:18px;text-align:left;color:#222;background:#fff}",
)


def stable_id(text: str) -> int:
    return int(hashlib.sha1(text.encode()).hexdigest()[:8], 16)


def h(text: str) -> str:
    """Testo -> HTML sicuro: a capo e semplici elenchi."""
    lines, out, in_list = text.strip().split("\n"), [], False
    for ln in lines:
        if re.match(r"^\s*[-•] ", ln):
            if not in_list:
                out.append("<ul>"); in_list = True
            out.append("<li>" + html.escape(re.sub(r"^\s*[-•] ", "", ln)) + "</li>")
        else:
            if in_list:
                out.append("</ul>"); in_list = False
            out.append(html.escape(ln) + "<br>")
    if in_list:
        out.append("</ul>")
    return "".join(out)


def parse_cards(path: Path):
    cards, q, a, mode, title = [], [], [], None, ""
    def flush():
        if q and a:
            cards.append((title, "\n".join(q), "\n".join(a)))
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("## "):
            flush(); q, a, mode, title = [], [], None, raw[3:].strip()
        elif raw.startswith("D:"):
            flush(); q, a, mode = [raw[2:].strip()], [], "q"
        elif raw.startswith("R:"):
            a, mode = [raw[2:].strip()], "a"
        elif mode == "q" and raw.strip():
            q.append(raw.rstrip())
        elif mode == "a" and raw.strip():
            a.append(raw.rstrip())
    flush()
    return cards


def parse_quiz(path: Path):
    """Quiz digitalizzati dagli esami (formato ## [id] argomenti: ... / testo / 1..5 / RISPOSTA / SPIEGAZIONE)."""
    cards, blocks = [], re.split(r"(?m)^## ", path.read_text(encoding="utf-8"))
    for b in blocks[1:]:
        head, _, body = b.partition("\n")
        m = re.match(r"\[([^\]]+)\]", head)
        r = re.search(r"(?m)^RISPOSTA:\s*(\d)", body)
        if not m or not r:
            continue
        text = body.split("RISPOSTA:")[0].strip()
        spieg = re.search(r"(?ms)^SPIEGAZIONE:\s*(.*?)(?=^ATTENZIONE:|\Z)", body)
        opts = re.findall(r"(?m)^(\d)\.\s+(.*)$", text)
        corr = dict(opts).get(r.group(1), r.group(1))
        back = f"Risposta {r.group(1)}: {corr}\n" + (spieg.group(1).strip() if spieg else "")
        cards.append((m.group(1), text, back))
    return cards


def build(materia: str) -> int:
    safe = materia.replace(" ", "_")
    deck = genanki.Deck(stable_id("UNI::" + materia), f"UNI::{materia}")
    n = 0
    src = CARDS / f"{materia}.md"
    items = parse_cards(src) if src.exists() else []
    extra = CARDS / f"{materia}.quiz.md"
    if extra.exists():
        items += parse_cards(extra)
    if materia == "Matematica discreta":
        for q in sorted(EXAMS.glob("quiz_*.md")):
            items += [(f"Esame {t}", a, b) for t, a, b in parse_quiz(q)]
    for title, q, a in items:
        note = genanki.Note(model=MODEL, fields=[h(q), h(a), html.escape(title)],
                            guid=genanki.guid_for(materia, q))
        deck.add_note(note); n += 1
    if n:
        OUT.mkdir(exist_ok=True)
        genanki.Package(deck).write_to_file(str(OUT / f"{safe}.apkg"))
    print(f"{materia}: {n} schede -> anki/{safe}.apkg" if n else f"{materia}: nessuna scheda")
    return n


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    materie = sys.argv[1:] or ["Algebra lineare", "Matematica discreta", "Fondamenti Info", "Programmazione"]
    for m in materie:
        build(m)


if __name__ == "__main__":
    main()
