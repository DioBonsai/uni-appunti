"""Figure dei capitoli 20-24 di Matematica discreta (funzioni inverse, inclusione-esclusione, conteggio).
Uso: python figure_mate_comb.py   (genera i PNG in _sistema/figure/mate/)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_math import (BLU, ROSSO, VERDE, ARANCIO, GRIGIO, np, plt, Circle, Ellipse, Rectangle, FancyArrowPatch,
                         ovali_ax, venn_ax, _salva)


# ------------------------------------------------------------------ cap. 20
def una_composizione():
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.6))
    # esempio 1: proiezione
    ov = [dict(nome="ℤ", elems=["1"], cx=1.6, w=2.0, h=3.2),
          dict(nome="ℤ × ℤ", elems=["(1, 0)", "(1, 1)"], cx=8.0, w=3.0, h=4.0)]
    fr = [dict(da=(0, "1"), a=(1, "(1, 0)"), col=BLU, lab="f"),
          dict(da=(1, "(1, 0)"), a=(0, "1"), col=ROSSO, tratt=True, rad=0.45),
          dict(da=(1, "(1, 1)"), a=(0, "1"), col=ROSSO, tratt=True, rad=-0.15)]
    ovali_ax(axs[0], ov, fr, titolo="π₁ ∘ f = id (blu, poi rosso)\nma f ∘ π₁ ≠ id: (1, 1) → (1, 0)", fs=10)
    ov2 = [dict(nome="A", elems=["a", "b", "c", "d"], cx=1.8, w=2.2, h=5.0),
           dict(nome="Q", elems=["{a, b}", "{c, d}"], cx=8.2, w=3.0, h=3.4)]
    fr2 = [dict(da=(0, "a"), a=(1, "{a, b}")), dict(da=(0, "b"), a=(1, "{a, b}")),
           dict(da=(0, "c"), a=(1, "{c, d}")), dict(da=(0, "d"), a=(1, "{c, d}")),
           dict(da=(1, "{a, b}"), a=(0, "a"), col=ROSSO, tratt=True, rad=0.3),
           dict(da=(1, "{c, d}"), a=(0, "c"), col=ROSSO, tratt=True, rad=0.3)]
    ovali_ax(axs[1], ov2, fr2, titolo="f ∘ g = id_Q, ma g ∘ f ≠ id_A (b → a)", fs=10)
    fig.subplots_adjust(wspace=0.12)
    return _salva(fig, "mate/ch20_una_composizione")


# ------------------------------------------------------------------ cap. 21
def contributi_due():
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Circle((-0.6, 0), 1.1, fill=False, ec=BLU, lw=2)); ax.add_patch(Circle((0.6, 0), 1.1, fill=False, ec=ROSSO, lw=2))
    ax.text(-1.5, 1.2, "A", color=BLU, fontsize=14, style="italic"); ax.text(1.5, 1.2, "B", color=ROSSO, fontsize=14, style="italic")
    for x, y, t in [(-1.1, 0, "a"), (0, 0, "x"), (1.1, 0, "b")]:
        ax.plot(x, y, "o", color="black", ms=5); ax.text(x, y + 0.25, t, ha="center", fontsize=12)
    rows = [("", "|A ∪ B|", "|A| + |B|"), ("a", "1", "1 + 0 = 1"), ("b", "1", "0 + 1 = 1"), ("x", "1", "1 + 1 = 2")]
    for i, (e, c1, c2) in enumerate(rows):
        y = 1.0 - i * 0.55
        col = ROSSO if e == "x" else "black"
        ax.text(2.6, y, e, fontsize=11, ha="center", color=col, weight="bold" if i == 0 else None)
        ax.text(3.4, y, c1, fontsize=11, ha="center", color=col, weight="bold" if i == 0 else None)
        ax.text(4.9, y, c2, fontsize=11, ha="center", color=col, weight="bold" if i == 0 else None)
    ax.text(3.6, -1.35, "x è contato due volte: si toglie |A ∩ B|", fontsize=10, color=ROSSO, ha="center")
    ax.set_xlim(-2.3, 6.2); ax.set_ylim(-1.7, 1.7)
    return _salva(fig, "mate/ch21_contributi_due")


def numeri_3000():
    fig, ax = plt.subplots(figsize=(5.2, 3.6))
    ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Rectangle((-2.3, -1.7), 4.6, 3.4, fill=False, ec="black", lw=1.5))
    ax.text(-2.2, 1.45, "I₃₀₀₀: 3000", fontsize=10, style="italic")
    ax.add_patch(Circle((-0.55, 0), 1.0, fc=BLU, alpha=0.15, ec=BLU, lw=2)); ax.add_patch(Circle((0.55, 0), 1.0, fc=ROSSO, alpha=0.15, ec=ROSSO, lw=2))
    ax.text(-1.15, 0.1, "1000\n− 200 = 800", ha="center", va="center", fontsize=9, color=BLU)
    ax.text(0, 0.1, "200\n(D₁₅)", ha="center", va="center", fontsize=9)
    ax.text(1.15, 0.1, "600\n− 200 = 400", ha="center", va="center", fontsize=9, color=ROSSO)
    ax.text(-1.1, 1.2, "D₃", color=BLU, fontsize=13, style="italic"); ax.text(1.1, 1.2, "D₅", color=ROSSO, fontsize=13, style="italic")
    ax.text(0, -1.2, "|D₃ ∪ D₅| = 1000 + 600 − 200 = 1400\n3000 − 1400 = 1600", ha="center", va="center", fontsize=9)
    ax.set_xlim(-2.4, 2.4); ax.set_ylim(-1.8, 1.8)
    return _salva(fig, "mate/ch21_numeri_3000")


def venn3():
    fig, axs = plt.subplots(1, 2, figsize=(9.2, 3.8), gridspec_kw=dict(width_ratios=[1.1, 1]))
    ax = axs[0]
    ax.set_aspect("equal"); ax.axis("off")
    centri = [(-0.6, 0.35), (0.6, 0.35), (0, -0.6)]
    for (cx, cy), nm, col in zip(centri, "ABC", [BLU, ROSSO, VERDE]):
        ax.add_patch(Circle((cx, cy), 1.1, fill=False, ec=col, lw=2))
    ax.text(-1.5, 1.3, "A", color=BLU, fontsize=14, style="italic"); ax.text(1.5, 1.3, "B", color=ROSSO, fontsize=14, style="italic")
    ax.text(0, -1.95, "C", color=VERDE, fontsize=14, style="italic", ha="center")
    for x, y, t in [(-1.1, 0.6, "a"), (1.1, 0.6, "b"), (0, -1.4, "c"), (0, 0.85, "x"), (-0.65, -0.35, "z"), (0.65, -0.35, "y"), (0, 0.1, "s")]:
        ax.plot(x, y, "o", color="black", ms=4); ax.text(x + 0.12, y + 0.12, t, fontsize=11)
    ax.set_xlim(-2.2, 2.2); ax.set_ylim(-2.2, 1.8)
    t = axs[1]; t.axis("off")
    t.set_xlim(0, 10); t.set_ylim(0, 6)
    cols_x = [4.6, 7.2, 9.2]
    t.text(1.0, 5.4, "contributo a:", fontsize=10, style="italic")
    for x, h in zip([5.6, 8.4], ["x, y, z", "s"]):
        t.text(x, 5.4, h, fontsize=11, ha="center", weight="bold")
    righe = [("|A ∪ B ∪ C|", "1", "1"), ("|A| + |B| + |C|", "2", "3"), ("− |A∩B| − |A∩C| − |B∩C|", "−1", "−3"), ("+ |A∩B∩C|", "0", "+1")]
    for i, (r, a, b) in enumerate(righe):
        y = 4.5 - i * 0.95
        t.text(0.1, y, r, fontsize=9.5, va="center")
        t.text(5.6, y, a, fontsize=11, ha="center", va="center"); t.text(8.4, y, b, fontsize=11, ha="center", va="center")
    t.plot([0, 10], [1.0, 1.0], color="black", lw=0.8)
    t.text(0.1, 0.45, "totale", fontsize=10, va="center", style="italic")
    t.text(4.9, 0.45, "2 − 1 = 1", fontsize=10, ha="center", va="center", color=VERDE)
    t.text(8.6, 0.45, "3 − 3 + 1 = 1", fontsize=10, ha="center", va="center", color=VERDE)
    fig.subplots_adjust(wspace=0.05)
    return _salva(fig, "mate/ch21_venn3")


# ------------------------------------------------------------------ cap. 22-24: alberi
def _ramo(ax, p, q, col="black"):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=col, lw=1)


def _nodo(ax, p, col=BLU, ms=5):
    ax.plot(p[0], p[1], "o", color=col, ms=ms, zorder=3)


def albero_menu():
    fig, ax = plt.subplots(figsize=(8.4, 4.8))
    ax.axis("off")
    X = [0, 2.6, 5.2, 7.8]
    r = (X[0], 0)
    _nodo(ax, r, "black", 7)
    # livello 1: panino 1, panino 2, ⋮, panino 12
    y1 = {"1": 6, "2": 2, "12": -6}
    for k, y in y1.items():
        _ramo(ax, r, (X[1], y)); _nodo(ax, (X[1], y))
        ax.text(X[1], y + 0.5, "panino " + k, fontsize=9, ha="center", va="bottom")
    ax.text(X[1], -2.3, "⋮", fontsize=14, ha="center", va="center")
    # livello 2 dal primo panino: bibita 1, bibita 2, ⋮, bibita 5
    p1 = (X[1], 6)
    y2 = {"1": 8.0, "2": 6.2, "5": 3.4}
    for k, y in y2.items():
        _ramo(ax, p1, (X[2], y)); _nodo(ax, (X[2], y))
        ax.text(X[2], y + 0.35, "bibita " + k, fontsize=8.5, ha="center", va="bottom")
    ax.text(X[2], 4.8, "⋮", fontsize=13, ha="center", va="center")
    # livello 3 dalla prima bibita: dolce 1, dolce 2, ⋮, dolce 4
    p2 = (X[2], 8.0)
    y3 = {"1": 9.6, "2": 8.6, "4": 7.0}
    for k, y in y3.items():
        _ramo(ax, p2, (X[3], y)); _nodo(ax, (X[3], y), ROSSO, 4)
        ax.text(X[3] + 0.15, y, "dolce " + k, fontsize=8.5, ha="left", va="center")
    ax.text(X[3], 7.9, "⋮", fontsize=12, ha="center", va="center")
    for x, t in [(1.3, "12 scelte"), (3.9, "5 scelte"), (6.5, "4 scelte")]:
        ax.text(x, -8.2, t, ha="center", fontsize=10, color=BLU)
    ax.text(8.9, -3.0, "12 · 5 · 4 = 240\nmenù", fontsize=12, color=ROSSO, weight="bold", va="center")
    ax.set_xlim(-0.4, 10.8); ax.set_ylim(-8.8, 10.3)
    return _salva(fig, "mate/ch22_albero_menu")


def albero_permutazioni():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    ax.axis("off")
    ax.plot(0, 0, "o", color="black", ms=6)
    tut = ["a", "b", "c"]
    y0s = [2.6, 0, -2.6]
    foglie = 0
    ypos = []
    ordine = [("a", "b", "c"), ("a", "c", "b"), ("b", "a", "c"), ("b", "c", "a"), ("c", "a", "b"), ("c", "b", "a")]
    ys3 = [2.5 - i * 1.0 for i in range(6)]
    for i, (p, s, t) in enumerate(ordine):
        y3 = ys3[i]
        y1 = {"a": (ys3[0] + ys3[1]) / 2, "b": (ys3[2] + ys3[3]) / 2, "c": (ys3[4] + ys3[5]) / 2}[p]
        y2 = y3
        ax.plot([0, 2], [0, y1], color="black", lw=1)
        ax.plot([2, 4], [y1, y2], color="black", lw=1)
        ax.plot([4, 6], [y2, y3], color="black", lw=1)
        ax.plot(2, y1, "o", color=BLU, ms=4); ax.plot(4, y2, "o", color=BLU, ms=4); ax.plot(6, y3, "o", color=ROSSO, ms=4)
        ax.text(2, y1 + 0.18, p, fontsize=10, ha="center", color=BLU)
        ax.text(6.2, y3, f"({p}, {s}, {t})", fontsize=10, va="center")
        ax.text(4, y2 + 0.18, s, fontsize=10, ha="center", color=BLU)
    ax.text(1, -3.65, "3 scelte", ha="center", fontsize=10, color=BLU); ax.text(3, -3.65, "2 scelte", ha="center", fontsize=10, color=BLU)
    ax.text(5, -3.65, "1 scelta", ha="center", fontsize=10, color=BLU); ax.text(7.5, -3.65, "3 · 2 · 1 = 6", ha="center", fontsize=11, color=ROSSO, weight="bold")
    ax.set_xlim(-0.5, 9.2); ax.set_ylim(-4.0, 3.3)
    return _salva(fig, "mate/ch23_albero_permutazioni")


def albero_ripetizione():
    fig, ax = plt.subplots(figsize=(7.6, 4.8))
    ax.axis("off")
    ax.plot(0, 0, "o", color="black", ms=6)
    ys2 = [3.75 - i * 0.5 for i in range(16)]
    for i in range(4):
        y1 = (ys2[4 * i] + ys2[4 * i + 3]) / 2
        ax.plot([0, 2], [0, y1], color="black", lw=1); ax.plot(2, y1, "o", color=BLU, ms=4)
        ax.text(1.0, (0 + y1) / 2 + 0.15, f"colore {i + 1}" if False else "", fontsize=8)
        for j in range(4):
            y2 = ys2[4 * i + j]
            ax.plot([2, 4], [y1, y2], color="black", lw=1); ax.plot(4, y2, "o", color=ROSSO, ms=3.5)
            ax.plot([4, 4.9], [y2, y2], color="gray", lw=0.8, ls=":")
    ax.text(5.1, 0, "…  (ogni punto si dirama\nancora in 4)", fontsize=9, va="center", color="gray")
    ax.text(1, -4.6, "4 scelte", ha="center", fontsize=10, color=BLU); ax.text(3, -4.6, "4 · 4 = 16", ha="center", fontsize=10, color=BLU)
    ax.text(5.6, -4.6, "al livello k: 4^k", ha="center", fontsize=11, color=ROSSO, weight="bold")
    ax.set_xlim(-0.5, 8.0); ax.set_ylim(-5.1, 4.3)
    return _salva(fig, "mate/ch24_albero_ripetizione")


def albero_podio():
    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    ax.axis("off")
    X = [0, 2.6, 5.2, 7.8]
    r = (X[0], 0)
    _nodo(ax, r, "black", 7)
    y1 = [6, 3, 0, -3, -6]
    for y in y1:
        _ramo(ax, r, (X[1], y)); _nodo(ax, (X[1], y))
    # sottoalbero del primo atleta: 4 scelte per il secondo posto
    p1 = (X[1], 6)
    y2 = [7.8, 6.6, 5.4, 4.2]
    for y in y2:
        _ramo(ax, p1, (X[2], y)); _nodo(ax, (X[2], y))
    # sottoalbero del primo secondo: 3 scelte per il terzo posto
    p2 = (X[2], 7.8)
    for y in [8.6, 7.8, 7.0]:
        _ramo(ax, p2, (X[3], y)); _nodo(ax, (X[3], y), ROSSO, 4)
    # nodi non espansi
    for y in y1[1:]:
        ax.text(X[1] + 0.25, y, "…", fontsize=12, va="center")
    for y in y2[1:]:
        ax.text(X[2] + 0.25, y, "…", fontsize=12, va="center")
    for x, t in [(1.3, "5 scelte"), (3.9, "4 scelte"), (6.5, "3 scelte")]:
        ax.text(x, -7.6, t, ha="center", fontsize=10, color=BLU)
    ax.text(8.9, -1.5, "5 · 4 · 3 = 60", fontsize=12, color=ROSSO, weight="bold", va="center")
    ax.text(8.9, -3.2, "primo, secondo e terzo\nposto tra 5 atleti", fontsize=9, color="gray", va="center")
    ax.set_xlim(-0.4, 11.4); ax.set_ylim(-8.2, 9.3)
    return _salva(fig, "mate/ch24_albero_podio")

def griglia_AxB():
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    ax.axis("off")
    m, n = 4, 5
    xs = list(range(n)); ys = list(range(m))
    for i in range(m):
        for j in range(n):
            ax.add_patch(Rectangle((j, -i), 0.92, 0.82, fc="#E8EFFA", ec=BLU, lw=1))
            nome_a = f"a{i + 1}" if i < m - 1 else "a_m"
            nome_b = f"b{j + 1}" if j < n - 1 else "b_n"
            ax.text(j + 0.46, -i + 0.41, f"({nome_a}, {nome_b})", ha="center", va="center", fontsize=8)
    ax.text(-0.15, -1.5, "m righe\n(una per ogni a)", ha="right", va="center", fontsize=9, color=BLU)
    ax.text(2.4, 1.2, "n colonne (una per ogni b)", ha="center", fontsize=9, color=ROSSO)
    ax.text(2.4, -3.75, "m · n coppie in totale", ha="center", fontsize=10, weight="bold")
    ax.set_xlim(-1.8, 5.2); ax.set_ylim(-4.1, 1.7)
    return _salva(fig, "mate/ch22_griglia")


def diagonali():
    fig, ax = plt.subplots(figsize=(4.6, 4.2))
    ax.axis("off")
    N = 5
    ordine = sorted(((a, b) for a in range(N) for b in range(N) if a + b < N), key=lambda t: (t[0] + t[1], t[0]))
    for k, (a, b) in enumerate(ordine):
        ax.add_patch(Rectangle((b, -a), 0.9, 0.9, fc="#E8EFFA", ec=BLU, lw=1))
        ax.text(b + 0.45, -a + 0.45, str(k), ha="center", va="center", fontsize=11)
    for a in range(N):
        ax.text(-0.25, -a + 0.45, str(a), ha="right", va="center", fontsize=10, color=BLU)
        ax.text(a + 0.45, 1.15, str(a), ha="center", va="bottom", fontsize=10, color=ROSSO)
    ax.text(-0.9, 1.2, "a ↓  b →", fontsize=9, ha="right")
    ax.text(2.4, -4.55, "casella (a, b): posto nella lista", ha="center", fontsize=9)
    ax.set_xlim(-1.8, 5.2); ax.set_ylim(-4.9, 1.9)
    return _salva(fig, "mate/ch25_diagonali")


def tutte():
    out = [una_composizione(), contributi_due(), numeri_3000(), venn3(), griglia_AxB(), albero_menu(),
           albero_permutazioni(), albero_ripetizione(), albero_podio(), diagonali()]
    print("\n".join(out))


if __name__ == "__main__":
    tutte()
