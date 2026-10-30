"""Figure dei capitoli 31-34 di Algebra lineare (determinante). PNG in _sistema/figure/alg/.
Uso: python figure_alg5.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_math import BLU, ROSSO, VERDE, ARANCIO, GRIGIO, plt, Rectangle, _salva


def _mat(ax, x0, y0, scelte, titolo, col, cw=0.95, ch=0.85):
    n = 3
    ax.text(x0 + n * cw / 2, y0 + 0.35, titolo, ha="center", fontsize=10, color=col, fontweight="bold")
    for i in range(n):
        for j in range(n):
            ev = scelte[i] == j
            ax.add_patch(Rectangle((x0 + j * cw, y0 - (i + 1) * ch), cw, ch, fc=("#FFF1D6" if ev else "white"), ec="#4a6fa5", lw=1.3))
            ax.text(x0 + j * cw + cw / 2, y0 - (i + 0.5) * ch, f"a{i + 1}{j + 1}", ha="center", va="center", fontsize=11.5,
                    color=(col if ev else "black"), fontweight=("bold" if ev else None))


def det_permutazioni():
    fig, ax = plt.subplots(figsize=(10.6, 3.9)); ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.2, 15.2); ax.set_ylim(-3.5, 1.1)
    # [1 2 3]: identita', segno +; [2 3 1]: due trasposizioni, segno +; [3 2 1]: una trasposizione, segno -
    _mat(ax, 0.0, 0.0, [0, 1, 2], "σ = [1 2 3]  (segno +)", VERDE)
    ax.text(1.4, -3.1, "a₁₁ a₂₂ a₃₃", ha="center", fontsize=10.5, color=VERDE)
    _mat(ax, 5.2, 0.0, [1, 2, 0], "σ = [2 3 1]  (segno +)", VERDE)
    ax.text(6.6, -3.1, "a₁₂ a₂₃ a₃₁", ha="center", fontsize=10.5, color=VERDE)
    _mat(ax, 10.4, 0.0, [2, 1, 0], "σ = [3 2 1]  (segno −)", ROSSO)
    ax.text(11.8, -3.1, "− a₁₃ a₂₂ a₃₁", ha="center", fontsize=10.5, color=ROSSO)
    ax.text(7.5, -3.45, "Ogni termine della somma sceglie un elemento in ogni riga e in ogni colonna", ha="center", fontsize=9.5, color=GRIGIO)
    return _salva(fig, "alg/det_permutazioni")


def laplace_scacchiera():
    fig, ax = plt.subplots(figsize=(5.4, 3.6)); ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.2, 8.4); ax.set_ylim(-3.6, 1.0)
    cw, ch = 0.95, 0.8
    ax.text(1.5, 0.4, r"segno $(-1)^{i+j}$ della casella $(i, j)$", ha="left", fontsize=10, color=BLU, fontweight="bold")
    for i in range(4):
        for j in range(4):
            pos = (i + j) % 2 == 0
            ax.add_patch(Rectangle((0.0 + j * cw, 0 - (i + 1) * ch), cw, ch, fc=("#E3F3E8" if pos else "#FBE9E7"), ec="#9aa7bd", lw=1))
            ax.text(j * cw + cw / 2, -(i + 0.5) * ch, "+" if pos else "−", ha="center", va="center", fontsize=14, color=(VERDE if pos else ROSSO), fontweight="bold")
    ax.text(4.3, -1.3, "i segni si alternano\ncome su una scacchiera,\ncon + in alto a sinistra", fontsize=10, color=GRIGIO, va="center")
    return _salva(fig, "alg/laplace_scacchiera")


if __name__ == "__main__":
    for f in (det_permutazioni, laplace_scacchiera):
        print(f())
