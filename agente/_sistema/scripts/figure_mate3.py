"""Figure dei capitoli 29-31 di Matematica discreta (proprieta' dei coefficienti binomiali, Stiefel, Tartaglia, binomio).
PNG in _sistema/figure/mate/.  Uso: python figure_mate3.py
"""
import sys
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_math import BLU, ROSSO, VERDE, ARANCIO, GRIGIO, plt, _salva
from matplotlib.patches import Circle, Ellipse


def tartaglia():
    N = 7
    fig, ax = plt.subplots(figsize=(7.4, 4.4)); ax.axis("off"); ax.set_xlim(-0.4, 2 * N + 1.4); ax.set_ylim(-N - 0.9, 1.0)
    for n in range(N):
        y = -n
        ax.text(-0.3, y, f"n = {n}", ha="right", va="center", fontsize=9, color=GRIGIO)
        for k in range(n + 1):
            x = N - n + 2 * k
            col = BLU
            if n == 5 and k == 2:
                col = ROSSO
            ax.add_patch(Circle((x, y), 0.46, fc="#E8EFFA" if col == BLU else "#FBE9E7", ec=col, lw=1.4))
            ax.text(x, y, str(comb(n, k)), ha="center", va="center", fontsize=10.5, color="black", fontweight="bold" if col == ROSSO else None)
    # Stiefel: C(4,1)+C(4,2)=C(5,2)
    for (n, k) in [(4, 1), (4, 2)]:
        x = N - n + 2 * k
        ax.add_patch(Circle((x, -n), 0.46, fc="#E3F3E8", ec=VERDE, lw=2.2))
        ax.text(x, -n, str(comb(n, k)), ha="center", va="center", fontsize=10.5)
    ax.text(2 * N + 1.3, -2.0, "ogni numero è la somma\ndei due che ha sopra\n(formula di Stiefel):\n4 + 6 = 10", ha="right", va="center", fontsize=9.5, color=VERDE)
    ax.text(N + 0.0, 0.85, "Triangolo di Tartaglia (o di Pascal): righe = n, posizioni = k", ha="center", fontsize=10, color=BLU)
    return _salva(fig, "mate/tartaglia")


def stiefel_tipi():
    fig, ax = plt.subplots(figsize=(6.0, 3.6)); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 6)
    ax.add_patch(Circle((3.2, 3.0), 2.8, fc="#EEF3FB", ec=BLU, lw=2))
    ax.text(3.2, 5.5, "A  (n elementi)", ha="center", fontsize=10, color=BLU, fontweight="bold")
    ax.plot(4.6, 3.0, "o", color=ROSSO, ms=7); ax.text(4.8, 3.1, "x", color=ROSSO, fontsize=11, fontweight="bold")
    ax.add_patch(Ellipse((2.6, 2.4), 3.0, 1.4, fc="none", ec=VERDE, lw=2))
    ax.text(2.2, 1.35, "T: x ∉ T  (2° tipo)", fontsize=8.5, color=VERDE)
    ax.add_patch(Ellipse((4.2, 3.0), 2.0, 1.2, fc="none", ec=ARANCIO, lw=2, linestyle="--"))
    ax.text(3.0, 4.2, "S: x ∈ S  (1° tipo)", fontsize=8.5, color="#B25A00")
    ax.text(6.6, 4.3, "B = A ∖ {x}", fontsize=10.5, color=BLU, fontweight="bold")
    ax.text(6.6, 3.4, "|B| = n − 1", fontsize=10, color=BLU)
    ax.text(6.6, 2.1, "1° tipo ↔ sottoinsiemi di B\ncon k − 1 elementi:  C(n−1, k−1)", fontsize=9, color="#B25A00")
    ax.text(6.6, 0.9, "2° tipo = sottoinsiemi di B\ncon k elementi:  C(n−1, k)", fontsize=9, color=VERDE)
    return _salva(fig, "mate/stiefel_tipi")


if __name__ == "__main__":
    for f in (tartaglia, stiefel_tipi):
        print(f())
