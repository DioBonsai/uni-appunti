"""Figura del capitolo 25 di Fondamenti (tre versioni di «x ama y»). PNG in _sistema/figure/fond/.
Uso: python figure_fond4.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_math import BLU, ROSSO, VERDE, ARANCIO, GRIGIO, plt, FancyArrowPatch, _salva


def amore_quantificatori():
    fig, axs = plt.subplots(1, 3, figsize=(10.4, 3.6))
    pts = {0: (0.6, 2.4), 1: (0.6, 1.2), 2: (0.6, 0.0), 3: (2.6, 2.4), 4: (2.6, 1.2), 5: (2.6, 0.0)}   # sinistra = chi ama, destra = amati
    schemi = [
        ("∀x ∃y L(x, y)\nogni persona ama qualcuno", [(0, 3), (1, 3), (2, 4)], VERDE),
        ("∃x ∀y L(x, y)\nc'è qualcuno che ama tutti", [(0, 3), (0, 4), (0, 5)], BLU),
        ("∃y ∀x L(x, y)\nc'è qualcuno amato da tutti", [(0, 4), (1, 4), (2, 4)], ROSSO),
    ]
    for ax, (tit, archi, col) in zip(axs, schemi):
        ax.set_xlim(-0.6, 3.5); ax.set_ylim(-0.6, 3.1); ax.axis("off"); ax.set_aspect("equal")
        for k, (x, y) in pts.items():
            ax.plot(x, y, "o", color="white", mec=GRIGIO, mew=1.6, ms=11, zorder=3)
        for a, b in archi:
            ax.add_patch(FancyArrowPatch(pts[a], pts[b], arrowstyle="-|>", mutation_scale=13, color=col, lw=1.8, shrinkA=7, shrinkB=7, zorder=2))
        ax.text(0.6, 3.0, "x", ha="center", fontsize=10, color=GRIGIO); ax.text(2.6, 3.0, "y", ha="center", fontsize=10, color=GRIGIO)
        ax.set_title(tit, fontsize=9.5, color=col)
    return _salva(fig, "fond/amore_quantificatori")


if __name__ == "__main__":
    print(amore_quantificatori())
