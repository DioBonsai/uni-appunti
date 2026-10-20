"""Un solo comando per rimettere in ordine il Quaderno dopo aver cambiato i Word, le schede o i quiz.

Fa, nell'ordine: mazzi Anki (solo se le schede sono cambiate) -> pagine dei riassunti (pandoc) -> pagina del Quaderno ->
COPERTURA.md -> controllo dei Word -> collaudo del sistema. Non pubblica niente: alla fine dice cosa resta da fare (commit/push e
ripubblicazione dell'artefatto, che si chiede a Claude con /pubblica).

Uso:  python aggiorna_tutto.py [--salta-riassunti]
"""
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def passo(titolo, script, *args, obbligatorio=True):
    print(f"\n== {titolo} ==")
    r = subprocess.run([sys.executable, str(HERE / script), *args], stdin=subprocess.DEVNULL)
    if r.returncode and obbligatorio:
        print(f"   -> FALLITO ({script}, codice {r.returncode})")
    return r.returncode == 0


def main():
    salta = "--salta-riassunti" in sys.argv
    esiti = []
    try:
        import genanki  # noqa: F401
        esiti.append(("mazzi Anki", passo("Mazzi Anki", "anki_build.py")))
    except ImportError:
        print("\n== Mazzi Anki ==\n   saltati: manca la libreria genanki (pip install genanki)")
    if salta or not shutil.which("pandoc"):
        print("\n== Riassunti web ==\n   saltati" + ("" if salta else ": pandoc non trovato (https://pandoc.org), restano le pagine già nel repository"))
    else:
        esiti.append(("riassunti web", passo("Riassunti web (dai Word)", "costruisci_riassunti.py")))
    esiti.append(("pagina del Quaderno", passo("Pagina del Quaderno", "costruisci_pagina_studio.py")))
    esiti.append(("copertura", passo("Copertura dei Word (COPERTURA.md)", "aggiorna_copertura.py")))
    esiti.append(("controllo Word", passo("Controllo dei Word", "verifica_word.py")))
    esiti.append(("collaudo", passo("Collaudo del sistema", "test_sistema.py")))
    print("\n== Riepilogo ==")
    for nome, ok in esiti:
        print(f"  [{'OK' if ok else 'ERRORE'}] {nome}")
    print("\nResta da fare: git add -A, commit e push; poi, per la pagina su claude.ai, /pubblica (Claude la ripubblica).")
    sys.exit(0 if all(ok for _, ok in esiti) else 1)


if __name__ == "__main__":
    main()
