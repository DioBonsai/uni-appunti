"""Figure dei capitoli 23-26 di Programmazione (array e stringhe). PNG in _sistema/figure/prog/.
Uso: python figure_array.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_info import vuoto, BLU, ROSSO, VERDE, GRIGIO, plt, _salva
from matplotlib.patches import Rectangle


def _cella(ax, x, y, w, h, testo, fc="#E8EFFA", ec="#4a6fa5", fs=13, bold=False, col="black"):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=ec, lw=1.6))
    ax.text(x + w / 2, y + h / 2, testo, ha="center", va="center", fontsize=fs, fontweight="bold" if bold else None, color=col)


def array_memoria():
    """int numeri[4] in celle contigue: indici, valori (due noti), indirizzi crescenti."""
    fig, ax = vuoto(8.4, 3.0, (-1.6, 9.6), (-1.9, 1.9))
    vals = ["??", "??", "20", "10"]
    # in memoria l'indice 0 e' all'indirizzo piu' basso: lo si disegna a sinistra
    for i, (v, ind) in enumerate(zip(["10", "20", "??", "??"], range(4))):
        x = i * 2.2
        _cella(ax, x, -0.4, 2.2, 0.8, v, fc="#E8EFFA" if v != "??" else "#F1F1F1", bold=v != "??")
        ax.text(x + 1.1, 0.8, f"numeri[{ind}]", ha="center", fontsize=11, color=BLU)
        ax.text(x + 1.1, -0.85, hex(0x1000 + 4 * ind).upper().replace("X", "x"), ha="center", fontsize=10.5, color=GRIGIO)
    ax.text(-0.15, 0.0, "int numeri[4]", ha="right", va="center", fontsize=11.5, fontweight="bold")
    ax.annotate("", xy=(8.9, -1.45), xytext=(0, -1.45), arrowprops=dict(arrowstyle="-|>", color=GRIGIO, lw=1.2))
    ax.text(4.4, -1.8, "indirizzi di memoria crescenti (ogni int occupa 4 byte)", ha="center", fontsize=10.5, color=GRIGIO)
    ax.text(8.95, 0.0, "(?? = valore\nindeterminato)", ha="left", va="center", fontsize=9.5, color=ROSSO)
    return _salva(fig, "prog/array_memoria")


def stringa_terminatore():
    """char txt[] = "ciao": 5 celle, l'ultima e' '\\0'."""
    fig, ax = vuoto(7.6, 2.6, (-1.9, 9.2), (-1.5, 1.7))
    for i, c in enumerate(["'c'", "'i'", "'a'", "'o'", "'\\0'"]):
        x = i * 1.6
        fin = i == 4
        _cella(ax, x, -0.4, 1.6, 0.8, c, fc="#FBE9E7" if fin else "#E8EFFA", ec=ROSSO if fin else "#4a6fa5", bold=fin, col=ROSSO if fin else "black")
        ax.text(x + 0.8, 0.75, f"txt[{i}]", ha="center", fontsize=11, color=ROSSO if fin else BLU)
    ax.text(-0.15, 0.0, 'char txt[] = "ciao";', ha="right", va="center", fontsize=11, fontweight="bold")
    ax.text(4 * 1.6 + 0.8, -0.95, "terminatore NUL\n(il compilatore lo aggiunge)", ha="center", fontsize=10, color=ROSSO)
    ax.text(1.6 * 2, -1.35, "4 lettere  →  array di 5 elementi", ha="center", fontsize=10.5, color=GRIGIO)
    return _salva(fig, "prog/stringa_terminatore")


if __name__ == "__main__":
    for f in (array_memoria, stringa_terminatore):
        print(f())
