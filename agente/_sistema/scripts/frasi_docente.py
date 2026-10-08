"""Estrae dalle trascrizioni le frasi in cui il docente segnala cose importanti per l'esame.

Cerca parole-spia ("all'esame", "attenzione", "errore", "trabocchetto", "ricordate", "importante", "fondamentale",
"sapere", "capita", "uscire"...) e salva, per ogni trascrizione, un file `_sistema/trascrizioni/da_esame/<nome>.md`
con timestamp, frase e contesto (frase precedente e successiva). Le trascrizioni possono contenere errori di
riconoscimento: i passaggi vanno verificati sulle fonti prima di usarli nei riassunti.

Uso: python frasi_docente.py                 # tutte le trascrizioni complete
     python frasi_docente.py algebra_L1.txt
"""
import re
import sys
from pathlib import Path

TR = Path(__file__).resolve().parent.parent / "trascrizioni"
OUT = TR / "da_esame"
KEYS = {
    "esame": r"\besam[ei]\b|all'esame|compito|prova scritta|quiz",
    "attenzione": r"\battenzione\b|\battenti\b|\bcuriosi?\b|\bstate attent",
    "errore tipico": r"\berrore\b|\berrori\b|\bsbagli|\btranello\b|\btrabocchett|\bconfond",
    "da ricordare": r"\bricordate\b|\bricordatevi\b|\btenete a mente\b|\bimportante\b|\bfondamentale\b|\bessenziale\b|\bda sapere\b|\bimparate\b|\bsapere a memoria\b",
    "dimostrazione": r"\bdimostrazion|\bdimostrare\b|\bteorema\b|\bproposizione\b",
    "esercizio": r"\besercizi[o]?\b|\bpotete provare\b|\bprovate a\b|\bper casa\b",
}
RX = {k: re.compile(v, re.I) for k, v in KEYS.items()}


def load(path: Path):
    items = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\[(\d+:\d+(?::\d+)?)\]\s*(.*)", line)
        if not m:
            continue
        ts, text = m.groups()
        for sent in re.split(r"(?<=[.!?])\s+", text):
            if sent.strip():
                items.append((ts, sent.strip()))
    return items


def process(path: Path) -> int:
    items = load(path)
    hits = {k: [] for k in KEYS}
    for i, (ts, s) in enumerate(items):
        for k, rx in RX.items():
            if rx.search(s) and len(s) > 25:
                prev = items[i - 1][1] if i else ""
                nxt = items[i + 1][1] if i + 1 < len(items) else ""
                hits[k].append((ts, prev, s, nxt))
    OUT.mkdir(parents=True, exist_ok=True)
    lines = [f"# Frasi del docente da tenere d'occhio: {path.stem}", "",
             "Estratte automaticamente dalla trascrizione (possibili errori di riconoscimento). Il timestamp serve per riascoltare il punto.", ""]
    total = 0
    for k, lst in hits.items():
        if not lst:
            continue
        lines.append(f"## {k} ({len(lst)})")
        seen = set()
        for ts, prev, s, nxt in lst:
            if s in seen:
                continue
            seen.add(s); total += 1
            lines.append(f"- **[{ts}]** {s}")
            ctx = " ".join(x for x in (prev, nxt) if x)
            if ctx:
                lines.append(f"  - contesto: {ctx[:260]}")
        lines.append("")
    (OUT / f"{path.stem}.md").write_text("\n".join(lines), encoding="utf-8")
    return total


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    files = [TR / a for a in sys.argv[1:]] or sorted(TR.glob("*.txt"))
    if not files:
        print("Nessuna trascrizione completa ancora.")
        return
    for f in files:
        print(f"{f.name}: {process(f)} frasi -> trascrizioni/da_esame/{f.stem}.md")


if __name__ == "__main__":
    main()
