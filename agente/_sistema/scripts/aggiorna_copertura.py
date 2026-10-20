"""Scrive in COPERTURA.md l'elenco dei capitoli di ogni Word con lo stato di studio, ricavato dai Word stessi.

Le tabelle scritte a mano nel resto del file restano com'erano; questo blocco (tra i due marcatori) si rigenera ogni volta
e fa fede per «cosa c'è nel Word» e «cosa è studiato» (evidenziazioni gialle: >= 3 paragrafi = studiato).
Uso:  python aggiorna_copertura.py
"""
import re
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import costruisci_pagina_studio as C  # noqa: E402

INI, FINE = "<!-- AUTO:inizio -->", "<!-- AUTO:fine -->"
SEGNO = {2: "studiato", 1: "iniziato", 0: "da studiare"}


def blocco():
    avanz, _ = C.avanzamento()
    righe = [INI, f"## Capitoli nei Word e stato di studio (generato il {date.today():%d/%m/%Y}, non modificare a mano)", ""]
    righe.append("Fanno fede questo blocco e il Quaderno; le tabelle più sotto sono state scritte a mano l'8 ottobre e possono essere indietro.")
    for mat, a in avanz.items():
        righe += ["", f"### {mat}: {a['studiati']}/{a['capitoli']} capitoli studiati", a["prossimo"], "",
                  "| Cap. | Titolo | Paragrafi evidenziati | Stato |", "|---|---|---|---|"]
        for c in a["elenco"]:
            righe.append(f"| {c['n']} | {c['t'].replace('|', '/')} | {c['hl']}/{c['tot']} | {SEGNO[c['s']]} |")
    righe.append(FINE)
    return "\n".join(righe)


def main():
    f = HERE.parent.parent / "COPERTURA.md"
    t = f.read_text(encoding="utf-8")
    b = blocco()
    if INI in t and FINE in t:
        t = re.sub(re.escape(INI) + r".*?" + re.escape(FINE), lambda _: b, t, flags=re.S)
    else:
        prima, _, resto = t.partition("\n")          # dopo il titolo
        t = prima + "\n\n" + b + "\n" + resto
    f.write_text(t, encoding="utf-8")
    print("COPERTURA.md aggiornato")


if __name__ == "__main__":
    main()
