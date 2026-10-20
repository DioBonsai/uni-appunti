"""Figure dei capitoli 26-28 di Matematica discreta (combinazioni semplici, problemi con più scelte, combinazioni con ripetizione).
Uso: python figure_mate_comb2.py   (genera i PNG in _sistema/figure/mate/)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_math import BLU, ROSSO, VERDE, ARANCIO, GRIGIO, plt, _salva
from figure_mate_comb import _ramo, _nodo
from matplotlib.patches import FancyBboxPatch, Rectangle

CH = "#eaf1fb"


def _cella(ax, x, y, testo, w=0.9, h=0.9, fc=CH, ec="#444", fs=12, col="black", bold=False):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=ec, lw=1.3, zorder=2))
    ax.text(x + w / 2, y + h / 2, testo, ha="center", va="center", fontsize=fs, color=col, zorder=3, fontweight="bold" if bold else "normal")


# ------------------------------------------------------------------ cap. 26
def sottoinsieme_riordinamenti():
    """Le 3! = 6 scritture ordinate dello stesso sottoinsieme {c, e, f}."""
    fig, ax = plt.subplots(figsize=(7.6, 3.9)); ax.axis("off")
    ax.set_xlim(-0.2, 10.4); ax.set_ylim(-1.4, 6.4)
    ax.text(1.8, 6.0, "6 disposizioni diverse", ha="center", fontsize=10.5, color=BLU)
    ax.text(8.3, 6.0, "1 sola combinazione", ha="center", fontsize=10.5, color=ROSSO)
    scritture = ["c, e, f", "c, f, e", "e, c, f", "e, f, c", "f, c, e", "f, e, c"]
    for i, t in enumerate(scritture):
        y = 5.0 - i * 0.95
        ax.add_patch(FancyBboxPatch((0.3, y - 0.3), 3.0, 0.6, boxstyle="round,pad=0.02,rounding_size=0.1", fc=CH, ec="#444", lw=1.2))
        ax.text(1.8, y, "(" + t + ")", ha="center", va="center", fontsize=11)
        ax.annotate("", xy=(6.6, 2.55), xytext=(3.4, y), arrowprops=dict(arrowstyle="-|>", color=GRIGIO, lw=1.0))
    ax.add_patch(FancyBboxPatch((6.7, 2.05), 3.2, 1.0, boxstyle="round,pad=0.02,rounding_size=0.15", fc="#fbeed3", ec=ROSSO, lw=1.8))
    ax.text(8.3, 2.55, "S = {c, e, f}", ha="center", va="center", fontsize=13, color=ROSSO, weight="bold")
    ax.text(5.0, -0.9, "3! = 6 riordinamenti dello stesso sottoinsieme: si divide per 3!", ha="center", fontsize=10.5, color="black")
    return _salva(fig, "mate/ch26_riordinamenti")


# ------------------------------------------------------------------ cap. 27
def albero_ballo():
    fig, ax = plt.subplots(figsize=(7.6, 3.9)); ax.axis("off")
    r = (0, 0); _nodo(ax, r, "black", 7)
    ys = [3.2, 1.3, -1.3, -3.2]
    for y in ys:
        _ramo(ax, r, (3.0, y)); _nodo(ax, (3.0, y))
    ax.text(3.0, 0.0, "⋮", fontsize=14, ha="center", va="center")
    p = (3.0, 3.2)
    for y in (4.4, 3.5, 2.0):
        _ramo(ax, p, (6.0, y)); _nodo(ax, (6.0, y), ROSSO, 4)
    ax.text(6.0, 2.85, "⋮", fontsize=12, ha="center", va="center")
    ax.text(0.0, -4.4, "primo passo: (10 su 4) = 210 scelte di 4 uomini", ha="left", fontsize=10, color=BLU, va="center")
    ax.text(0.0, -5.2, "secondo passo, da ogni ramo: (12 su 4) = 495 scelte di 4 donne", ha="left", fontsize=10, color=BLU, va="center")
    ax.text(6.8, 0.0, "stesso numero di rami\nda ogni nodo:\n210 · 495 = 103 950", fontsize=12, color=ROSSO, weight="bold", va="center")
    ax.set_xlim(-0.5, 10.6); ax.set_ylim(-5.8, 5.4)
    return _salva(fig, "mate/ch27_albero_ballo")


def albero_gelato():
    fig, ax = plt.subplots(figsize=(7.6, 3.9)); ax.axis("off")
    r = (0, 0); _nodo(ax, r, "black", 7)
    for y, nome, n in ((2.4, "cono piccolo", "15"), (0.0, "cono medio", "105"), (-2.4, "cono grande", "455")):
        _ramo(ax, r, (3.0, y)); _nodo(ax, (3.0, y))
        ax.text(3.15, y + 0.5, nome, fontsize=9.5, ha="left", va="bottom")
        for dy in (-0.45, 0.0, 0.45):
            _ramo(ax, (3.0, y), (6.0, y + dy)); _nodo(ax, (6.0, y + dy), ROSSO, 3.5)
        ax.text(6.35, y, "⋮  " + n + " scelte di gusti", fontsize=10.5, ha="left", va="center", color=BLU)
    ax.text(0.0, -4.4, "a ogni ramo corrisponde un numero diverso di scelte:", fontsize=10, ha="left", color="black")
    ax.text(0.0, -5.2, "i punti finali si SOMMANO:  15 + 105 + 455 = 575", fontsize=12, ha="left", color=ROSSO, weight="bold")
    ax.set_xlim(-0.5, 12.5); ax.set_ylim(-5.8, 3.8)
    return _salva(fig, "mate/ch27_albero_gelato")


# ------------------------------------------------------------------ cap. 28
def caselle_separatori():
    fig, ax = plt.subplots(figsize=(8.0, 4.6)); ax.axis("off")
    ax.set_xlim(-2.6, 12.9); ax.set_ylim(-5.6, 5.6)
    # riga 1: 10 caselle con le lettere, monomio x^3 y^2 z^5
    lettere = list("xxxyyzzzzz")
    col = {"x": ARANCIO, "y": VERDE, "z": BLU}
    ax.text(-2.5, 4.6, "10 scelte: x³ y² z⁵", fontsize=10.5, color="black", va="center", ha="left")
    for i, c in enumerate(lettere):
        _cella(ax, i * 1.0 + 0.2, 3.4, c, w=0.95, h=0.95, fc="white", col=col[c], bold=True)
    for xs in (3.15, 5.15):
        ax.plot([xs, xs], [3.25, 4.5], color=ROSSO, lw=2.2)
    ax.text(0.2, 2.75, "i separatori stanno fra una casella e l'altra", fontsize=9.5, color=ROSSO, va="center", ha="left")
    # riga 2: 12 caselle, le separazioni occupano una casella
    ax.text(-2.5, 1.0, "12 caselle: x³ y² z⁵", fontsize=10.5, color="black", va="center", ha="left")
    seq = ["x", "x", "x", "•", "y", "y", "•", "z", "z", "z", "z", "z"]
    for i, c in enumerate(seq):
        if c == "•":
            _cella(ax, i * 0.95 + 0.2, -0.3, "", w=0.9, h=0.9, fc="#f6c6c0", ec=ROSSO)
        else:
            _cella(ax, i * 0.95 + 0.2, -0.3, c, w=0.9, h=0.9, fc="white", col=col[c], bold=True)
    ax.text(0.2, -1.2, "due caselle su dodici sono riservate ai separatori (in rosso)", fontsize=9.5, color=ROSSO, va="center", ha="left")
    # riga 3: x^10 y^0 z^0 -> separatori in fondo, ma in caselle distinte
    ax.text(-2.5, -3.0, "x² z⁸ (manca la y)", fontsize=10.5, color="black", va="center", ha="left")
    seq = ["x", "x", "•", "•", "z", "z", "z", "z", "z", "z", "z", "z"]
    for i, c in enumerate(seq):
        if c == "•":
            _cella(ax, i * 0.95 + 0.2, -4.3, "", w=0.9, h=0.9, fc="#f6c6c0", ec=ROSSO)
        else:
            _cella(ax, i * 0.95 + 0.2, -4.3, c, w=0.9, h=0.9, fc="white", col=col[c], bold=True)
    ax.text(0.2, -5.1, "se manca una variabile, i due separatori sono vicini ma in caselle distinte", fontsize=9.5, color=ROSSO, va="center", ha="left")
    return _salva(fig, "mate/ch28_caselle_separatori")


def tutte():
    for f in (sottoinsieme_riordinamenti, albero_ballo, albero_gelato, caselle_separatori):
        print(f.__name__, "->", f())


if __name__ == "__main__":
    tutte()
