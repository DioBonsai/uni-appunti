"""Figure dei capitoli 23-26 di Algebra lineare (dipendenza lineare, basi, dimensione). PNG in _sistema/figure/alg/.
Uso: python figure_alg3.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_math import BLU, ROSSO, VERDE, ARANCIO, GRIGIO, np, plt, FancyArrowPatch, _salva


def _assi(ax, lim=(-2.6, 2.6), ylim=(-1.8, 2.6)):
    ax.set_aspect("equal"); ax.set_xlim(*lim); ax.set_ylim(*ylim)
    ax.axhline(0, color="black", lw=0.8); ax.axvline(0, color="black", lw=0.8)
    for sp in ("top", "right", "left", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])


def _freccia(ax, p, col, lab, off=(0.08, 0.08), lw=2.2):
    ax.add_patch(FancyArrowPatch((0, 0), p, arrowstyle="-|>", mutation_scale=14, color=col, lw=lw))
    ax.text(p[0] + off[0], p[1] + off[1], lab, color=col, fontsize=11, fontweight="bold")


def generatori_ridondanti():
    fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.8))
    ax = axs[0]; _assi(ax)
    _freccia(ax, (1.8, 0), BLU, "v₁ = (1, 0)", off=(-0.1, -0.35))
    _freccia(ax, (-1.8, 0), ROSSO, "v₂ = (−1, 0)", off=(-0.95, -0.35))
    _freccia(ax, (0, 1.8), VERDE, "v₃ = (0, 1)", off=(0.1, 0.0))
    ax.set_title("v₁, v₂, v₃ generano ℝ², ma v₂ = −v₁: uno è di troppo", fontsize=9.5)
    ax = axs[1]; _assi(ax)
    t = np.linspace(-2.1, 2.1, 10); ax.plot(t, t, color=ARANCIO, lw=1.4, linestyle="--")
    _freccia(ax, (1.2, 1.2), ARANCIO, "w = (1, 1)", off=(0.08, -0.25))
    ax.text(-2.5, -2.1, "Span(w) = { (a, a) } è solo una retta: w da solo non genera ℝ²", fontsize=9, color=GRIGIO)
    ax.set_title("un solo vettore non nullo: indipendente, ma non basta", fontsize=9.5)
    return _salva(fig, "alg/generatori_ridondanti")


def coordinate_base():
    fig, ax = plt.subplots(figsize=(5.6, 4.0)); _assi(ax, lim=(-0.6, 4.2), ylim=(-0.6, 3.2))
    _freccia(ax, (1, 0), BLU, "e₁", off=(0.05, -0.3), lw=2.6)
    _freccia(ax, (0, 1), VERDE, "e₂", off=(-0.3, 0.05), lw=2.6)
    ax.add_patch(FancyArrowPatch((0, 0), (3, 2), arrowstyle="-|>", mutation_scale=14, color=ROSSO, lw=2.2))
    ax.plot([3, 3], [0, 2], color=GRIGIO, lw=1, linestyle=":"); ax.plot([0, 3], [2, 2], color=GRIGIO, lw=1, linestyle=":")
    ax.annotate("", xy=(3, -0.2), xytext=(0, -0.2), arrowprops=dict(arrowstyle="<->", color=BLU, lw=1.2))
    ax.text(1.5, -0.5, "3·e₁", color=BLU, ha="center", fontsize=10)
    ax.text(3.15, 1.0, "2·e₂", color=VERDE, fontsize=10)
    ax.text(3.05, 2.1, "v = (3, 2) = 3e₁ + 2e₂", color=ROSSO, fontsize=10.5, fontweight="bold")
    ax.set_title("coordinate di v nella base canonica: 3 e 2", fontsize=10)
    return _salva(fig, "alg/coordinate_base")


if __name__ == "__main__":
    for f in (generatori_ridondanti, coordinate_base):
        print(f())
