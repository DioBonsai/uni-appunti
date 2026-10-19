"""Figure dei capitoli 19-22 di Algebra lineare (matrici, sottospazi, Span). PNG in _sistema/figure/alg/.
Uso: python figure_alg2.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from matplotlib.patches import Polygon
from figure_math import BLU, ROSSO, VERDE, ARANCIO, GRIGIO, np, plt, Rectangle, FancyArrowPatch, _salva


def matrice_indici():
    m, n = 4, 5
    fig, ax = plt.subplots(figsize=(6.4, 4.0)); ax.axis("off"); ax.set_xlim(-2.4, 6.6); ax.set_ylim(-4.9, 1.3)
    i, j = 2, 3   # riga e colonna evidenziate (1-based)
    for r in range(m):
        for c in range(n):
            col = "#FBE9E7" if (r + 1 == i and c + 1 == j) else ("#E8EFFA" if (r + 1 == i or c + 1 == j) else "white")
            ax.add_patch(Rectangle((c, -r - 0.9), 0.95, 0.85, fc=col, ec="#9aa7bd", lw=1))
            nome = "$a_{" + (str(r + 1) if r < m - 1 else "m") + (str(c + 1) if c < n - 1 else "n") + "}$"
            ax.text(c + 0.475, -r - 0.475, nome, ha="center", va="center", fontsize=10, color=ROSSO if (r + 1 == i and c + 1 == j) else "black",
                    fontweight="bold" if (r + 1 == i and c + 1 == j) else None)
    ax.text(-0.15, -(i - 1) - 0.475, "i-esima riga", ha="right", va="center", fontsize=10, color=BLU)
    ax.text(j - 1 + 0.475, 0.25, "j-esima colonna", ha="center", fontsize=10, color=BLU)
    ax.text(n * 0.5 - 0.5, -4.35, "m righe (si legge prima la riga) · n colonne", ha="center", fontsize=10, color=GRIGIO)
    ax.text(-0.25, 0.9, "A =", fontsize=15, ha="right", va="center")
    return _salva(fig, "alg/matrice_indici")


def sottospazi_piani():
    fig, ax = plt.subplots(figsize=(6.6, 4.0)); ax.axis("off"); ax.set_xlim(-3.0, 7.6); ax.set_ylim(-0.9, 3.4)
    ax.annotate("", xy=(-1.6, 3.2), xytext=(-1.6, -0.6), arrowprops=dict(arrowstyle="-|>", color="black", lw=1.2))
    ax.text(-1.45, 3.1, "z", fontsize=12)
    for z, col, lab in [(0.0, BLU, "W₁: z = 0"), (1.0, ROSSO, "W₂: z = 1")]:
        ax.add_patch(Rectangle((-1.2, z - 0.02), 6.6, 0.04, fc=col, ec=col))
        ax.text(5.55, z + 0.08, lab, fontsize=11, color=col, va="bottom")
    ax.plot(-1.6, 0, "o", color="black", ms=6); ax.text(-1.8, 0.0, "origine 0", fontsize=10, va="center", ha="right")
    ax.text(5.55, -0.36, "contiene l'origine: sottospazio", fontsize=9, color=BLU)
    ax.text(5.55, 0.62, "non contiene l'origine", fontsize=9, color=ROSSO)
    ax.plot(0.6, 1.0, "o", color=ROSSO, ms=7); ax.text(0.6, 1.14, "(1, 1, 1) ∈ W₂", fontsize=10, color=ROSSO, ha="center")
    ax.plot(0.6, 2.0, "o", color="white", mec=ROSSO, mew=2, ms=7); ax.text(0.6, 2.14, "2·(1, 1, 1) = (2, 2, 2) ∉ W₂", fontsize=10, color=ROSSO, ha="center")
    ax.add_patch(FancyArrowPatch((0.6, 1.1), (0.6, 1.9), arrowstyle="-|>", mutation_scale=12, color=ROSSO, lw=1.3, linestyle="--"))
    return _salva(fig, "alg/sottospazi_piani")


def sottospazi_esempi_piano():
    fig, axs = plt.subplots(1, 3, figsize=(10.4, 3.7))
    for ax in axs:
        ax.set_aspect("equal"); ax.axhline(0, color="black", lw=0.8); ax.axvline(0, color="black", lw=0.8)
        ax.set_xlim(-2.2, 2.2); ax.set_ylim(-1.7, 2.7)
        for sp in ("top", "right", "left", "bottom"):
            ax.spines[sp].set_visible(False)
        ax.set_xticks([]); ax.set_yticks([])
    # parabola
    ax = axs[0]; x = np.linspace(-1.55, 1.55, 200); ax.plot(x, x ** 2, color=BLU, lw=2)
    ax.plot(1, 1, "o", color=BLU); ax.text(1.08, 1.0, "w = (1, 1)", fontsize=9, va="center", color=BLU)
    ax.plot(0.5, 0.5, "o", color="white", mec=ROSSO, mew=2, ms=7); ax.text(0.85, 0.2, "½·w ∉ W", fontsize=9, color=ROSSO)
    ax.set_title("parabola (x, x²): non è un sottospazio", fontsize=9.5, color=ROSSO)
    # semiretta
    ax = axs[1]; ax.plot([0, 2.1], [0, 0], color=BLU, lw=3); ax.plot(0, 0, "o", color=BLU)
    ax.plot(1, 0, "o", color=BLU); ax.text(1.0, 0.18, "(1, 0)", fontsize=9, color=BLU, ha="center")
    ax.plot(-1, 0, "o", color="white", mec=ROSSO, mew=2, ms=7); ax.text(-1.0, 0.18, "(−1, 0) ∉ W", fontsize=9, color=ROSSO, ha="center")
    ax.set_title("semiretta x ≥ 0: non è un sottospazio", fontsize=9.5, color=ROSSO)
    # retta
    ax = axs[2]; ax.plot([-1.7, 1.7], [-1.7, 1.7], color=BLU, lw=2)
    ax.plot(0, 0, "o", color=BLU); ax.plot(0.7, 0.7, "o", color=BLU); ax.plot(1.4, 1.4, "o", color=BLU)
    ax.text(0.8, 0.45, "somma e multipli\nrestano sulla retta", fontsize=9, color=VERDE)
    ax.set_title("retta y = x: è un sottospazio", fontsize=9.5, color=VERDE)
    fig.subplots_adjust(wspace=0.05)
    return _salva(fig, "alg/sottospazi_esempi_piano")


def matrici_speciali():
    n = 4
    tipi = [("diagonale", lambda i, j: "z" if i != j else "l"),
            ("triangolare\nsuperiore", lambda i, j: "z" if i > j else "l"),
            ("triangolare\ninferiore", lambda i, j: "z" if i < j else "l"),
            ("simmetrica", lambda i, j: "s" if i != j else "l"),
            ("antisimmetrica", lambda i, j: "z" if i == j else ("s" if i < j else "a"))]
    fig, axs = plt.subplots(1, 5, figsize=(11.6, 2.9))
    for ax, (nome, f) in zip(axs, tipi):
        ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-0.1, n + 0.1); ax.set_ylim(-n - 0.1, 0.9)
        for i in range(n):
            for j in range(n):
                t = f(i, j)
                fc = {"z": "#e6e6e6", "l": "#cfe0f7", "s": "#f9dcc4", "a": "#f4cccc"}[t]
                ax.add_patch(Rectangle((j, -i - 1), 0.94, 0.94, fc=fc, ec="white"))
                txt = {"z": "0", "l": "*", "s": "", "a": ""}[t]
                if nome == "simmetrica" and i != j:
                    txt = "b" if i < j else "b"
                if nome == "antisimmetrica" and i != j:
                    txt = "b" if i < j else "−b"
                ax.text(j + 0.47, -i - 0.53, txt, ha="center", va="center", fontsize=11)
        ax.plot([0, n], [0, -n], color=BLU, lw=1.2, alpha=0.6)
        ax.set_title(nome, fontsize=10, pad=6)
    fig.text(0.5, 0.01, "grigio = zero obbligato · azzurro = entrata libera · arancio = entrate uguali (simmetrica) o opposte (antisimmetrica); la diagonale principale va dall'alto a sinistra al basso a destra",
             ha="center", fontsize=8.5, color=GRIGIO)
    fig.subplots_adjust(wspace=0.05, bottom=0.12)
    return _salva(fig, "alg/matrici_speciali")


def span_piano():
    fig = plt.figure(figsize=(5.0, 4.2)); ax = fig.add_subplot(111, projection="3d")
    ax.add_collection3d(__import__("mpl_toolkits.mplot3d.art3d", fromlist=["Poly3DCollection"]).Poly3DCollection(
        [[(-1.4, -1.4, 0), (1.6, -1.4, 0), (1.6, 1.6, 0), (-1.4, 1.6, 0)]], facecolors=[(0.19, 0.4, 0.78, 0.18)], edgecolors=[BLU]))
    for v, col, lab in [((1, 0, 0), ROSSO, "v₁"), ((0, 1, 0), VERDE, "v₂")]:
        ax.quiver(0, 0, 0, *v, color=col, arrow_length_ratio=0.12, lw=2)
        ax.text(v[0] * 1.15, v[1] * 1.15, 0.05, lab, color=col, fontsize=12)
    ax.quiver(0, 0, 0, 0, 0, 1.3, color="black", arrow_length_ratio=0.1, lw=1)
    ax.text(0, 0, 1.45, "z", fontsize=11)
    ax.text(0.9, -1.35, 0, "Span(v₁, v₂)", color=BLU, fontsize=11)
    ax.set_xlim(-1.5, 1.7); ax.set_ylim(-1.5, 1.7); ax.set_zlim(-0.3, 1.5)
    ax.set_axis_off(); ax.view_init(elev=24, azim=-58)
    return _salva(fig, "alg/span_piano")


def tutte():
    for f in (matrice_indici, sottospazi_piani, sottospazi_esempi_piano, matrici_speciali, span_piano):
        print(f())


if __name__ == "__main__":
    tutte()
