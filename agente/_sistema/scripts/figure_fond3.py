"""Figura del capitolo 23 di Fondamenti (insiemi annidati P ⊆ Q ⊆ D). PNG in _sistema/figure/fond/.
Uso: python figure_fond3.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_math import BLU, ROSSO, VERDE, GRIGIO, plt, _salva
from matplotlib.patches import FancyBboxPatch, Ellipse


def insiemi_annidati():
    fig, ax = plt.subplots(figsize=(6.4, 4.0)); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 6.2)
    ax.add_patch(FancyBboxPatch((0.2, 0.2), 9.6, 5.8, boxstyle="round,pad=0.02,rounding_size=0.3", fc="#EEF3FB", ec=BLU, lw=2))
    ax.text(0.5, 5.6, "D: iscritti a un'università italiana", fontsize=11, color=BLU, fontweight="bold", va="center")
    ax.add_patch(Ellipse((4.3, 2.9), 7.0, 3.9, fc="#FBF1E1", ec="#C47A12", lw=2))
    ax.text(4.3, 4.45, "Q: iscritti a Torino", fontsize=10.5, color="#9A5C0A", fontweight="bold", ha="center")
    ax.add_patch(Ellipse((3.6, 2.5), 3.2, 1.9, fc="#E3F3E8", ec=VERDE, lw=2))
    ax.text(3.6, 2.5, "P: iscritti a\nInformatica a Torino", fontsize=9.5, color=VERDE, fontweight="bold", ha="center", va="center")
    ax.plot(5.35, 2.1, "o", color=ROSSO, ms=6); ax.text(5.5, 2.1, "iscritto a Legge:" + chr(10) + "Q vera, P falsa", fontsize=8.2, color=ROSSO, va="center")
    ax.plot(8.9, 1.0, "o", color=ROSSO, ms=6); ax.text(8.75, 1.45, "studente a Milano:\nQ falsa, P falsa", fontsize=8.5, color=ROSSO, ha="right", va="center")
    return _salva(fig, "fond/insiemi_annidati")


if __name__ == "__main__":
    print(insiemi_annidati())
