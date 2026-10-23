"""Figure dei capitoli 27-30 di Algebra lineare (trasposta, rango, prodotto fra matrici). PNG in _sistema/figure/alg/.
Uso: python figure_alg4.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_math import BLU, ROSSO, VERDE, ARANCIO, GRIGIO, plt, Rectangle, FancyArrowPatch, _salva


def _griglia(ax, x0, y0, righe, cw=0.9, ch=0.8, evid=None, col_evid="#FFF3C4", ec="#4a6fa5", fs=13, coloriC=None):
    """Disegna una matrice con la cella (0,0) in alto a sinistra a (x0, y0). evid: {(i,j): colore}"""
    evid = evid or {}
    for i, r in enumerate(righe):
        for j, v in enumerate(r):
            fc = evid.get((i, j), "white")
            ax.add_patch(Rectangle((x0 + j * cw, y0 - (i + 1) * ch), cw, ch, fc=fc, ec=ec, lw=1.3))
            ax.text(x0 + j * cw + cw / 2, y0 - (i + 0.5) * ch, str(v), ha="center", va="center", fontsize=fs)
    return len(righe[0]) * cw, len(righe) * ch


def trasposta():
    fig, ax = plt.subplots(figsize=(7.2, 3.0)); ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.3, 9.6); ax.set_ylim(-3.4, 0.9)
    A = [[3, 0], [2, 5], [1, 6]]
    AT = [[3, 2, 1], [0, 5, 6]]
    ax.text(0.9, 0.55, "A  (3 × 2)", ha="center", fontsize=11, color=BLU, fontweight="bold")
    _griglia(ax, 0, 0, A, evid={(1, 0): "#FFE08A"})
    ax.text(5.1, 0.55, "ᵗA  (2 × 3)", ha="center", fontsize=11, color=BLU, fontweight="bold")
    _griglia(ax, 3.9, 0, AT, evid={(0, 1): "#FFE08A"})
    ax.add_patch(FancyArrowPatch((2.2, -1.2), (3.7, -0.4), arrowstyle="-|>", mutation_scale=14, color=GRIGIO, lw=1.6, connectionstyle="arc3,rad=-0.25"))
    ax.text(2.95, -1.35, "righe ↔ colonne", ha="center", fontsize=9.5, color=GRIGIO)
    ax.text(0.0, -3.1, "(ᵗA)ᵢⱼ = Aⱼᵢ :  l'elemento 2 di A (riga 2, colonna 1) sta in ᵗA nella riga 1, colonna 2", fontsize=9.5, color=ROSSO)
    return _salva(fig, "alg/trasposta_esempio")


def prodotto_riga_colonna():
    fig, ax = plt.subplots(figsize=(7.6, 4.2)); ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.3, 11.2); ax.set_ylim(-5.2, 2.7)
    A = [[3, 1, 1], [2, 0, 5]]
    C = [[2, -1], [1, 1], [0, 1]]
    P = [[7, -1], [4, 3]]
    cw, ch = 0.95, 0.8
    # C in alto a destra, A a sinistra, prodotto sotto C
    xA, yA = 0.0, -1.7
    xC, yC = 3.4, 1.9
    xP, yP = 3.4, -1.7
    gialloR = {(0, 0): "#FDE7B0", (0, 1): "#FDE7B0", (0, 2): "#FDE7B0"}
    azzC = {(0, 0): "#CFE3FA", (1, 0): "#CFE3FA", (2, 0): "#CFE3FA"}
    ax.text(xA + 1.4, yA + 0.3, "A (2 × 3)", ha="center", fontsize=10.5, color=BLU, fontweight="bold")
    _griglia(ax, xA, yA, A, cw, ch, evid=gialloR)
    ax.text(xC + 0.95, yC + 0.3, "C (3 × 2)", ha="center", fontsize=10.5, color=BLU, fontweight="bold")
    _griglia(ax, xC, yC, C, cw, ch, evid=azzC)
    ax.text(xP + 2.6, yP + 0.3, "A·C (2 × 2)", ha="center", fontsize=10.5, color=BLU, fontweight="bold")
    _griglia(ax, xP, yP, P, cw, ch, evid={(0, 0): "#FFD7D0"})
    ax.annotate("", xy=(xP + 0.1, yP - 0.4), xytext=(xA + 3 * cw + 0.1, yA - 0.4), arrowprops=dict(arrowstyle="-|>", color="#B25A00", lw=1.8))
    ax.annotate("", xy=(xP + 0.47, yP + 0.02), xytext=(xC + 0.47, yC - 3 * ch - 0.05), arrowprops=dict(arrowstyle="-|>", color=BLU, lw=1.8))
    ax.text(7.2, -2.4, "elemento in riga 1, colonna 1:\n3·2 + 1·1 + 1·0 = 7", fontsize=10, color=ROSSO, va="center")
    ax.text(7.2, -3.9, "colonne di A (3) = righe di C (3):\nil prodotto si può fare", fontsize=9.5, color=GRIGIO, va="center")
    return _salva(fig, "alg/prodotto_riga_colonna")


if __name__ == "__main__":
    for f in (trasposta, prodotto_riga_colonna):
        print(f())
