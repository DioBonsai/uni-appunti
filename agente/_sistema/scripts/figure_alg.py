"""Figure del Word di Algebra lineare (capitoli 1-13). Genera i PNG in _sistema/figure/alg/ e scrive figure/alg/piano.json.
Uso: python figure_alg.py
"""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_math import BLU, ROSSO, VERDE, ARANCIO, GRIGIO, OUT, np, plt, Circle, Ellipse, Arc, FancyArrowPatch, _salva

C = lambda x, y: complex(x, y)


def piano(figsize=(4.4, 4.2), L=3.2, griglia=True, etich=True):
    fig, ax = plt.subplots(figsize=figsize); ax.set_aspect("equal")
    ax.axhline(0, color="black", lw=0.9); ax.axvline(0, color="black", lw=0.9)
    ax.set_xlim(-L, L); ax.set_ylim(-L, L)
    if griglia:
        ax.grid(True, color="#e3e3e3", lw=0.6)
    for sp in ("top", "right", "left", "bottom"):
        ax.spines[sp].set_visible(False)
    if etich:
        ax.text(L, -0.06 * L, "Re", ha="right", va="top", fontsize=11); ax.text(0.04 * L, L * 0.9, "Im", va="top", fontsize=11)
    return fig, ax


def freccia(ax, z, col=BLU, lw=1.8, w=None):
    ax.annotate("", xy=(z.real, z.imag), xytext=(0, 0) if w is None else (w.real, w.imag),
                arrowprops=dict(arrowstyle="-|>", color=col, lw=lw, shrinkA=0, shrinkB=0))


def punto(ax, z, et, col=BLU, off=(7, 6), fs=11):
    ax.plot(z.real, z.imag, "o", color=col, ms=5, zorder=5)
    ax.annotate(et, (z.real, z.imag), textcoords="offset points", xytext=off, fontsize=fs, color=col)


def ang(ax, r, t1, t2, col=ROSSO, et=None, fs=12):
    ax.add_patch(Arc((0, 0), 2 * r, 2 * r, theta1=math.degrees(t1), theta2=math.degrees(t2), color=col, lw=1.6))
    if et:
        m = (t1 + t2) / 2; ax.text(1.35 * r * math.cos(m), 1.35 * r * math.sin(m), et, color=col, fontsize=fs, ha="center", va="center")


# ---------------------------------------------------------------- capitolo 1
def somma_vettori():
    fig, ax = piano(figsize=(4.2, 3.6), L=4.4, griglia=False, etich=False); ax.set_xlim(-0.5, 5); ax.set_ylim(-0.5, 4)
    u, v = C(3, 1), C(1, 2.5)
    freccia(ax, u, BLU); freccia(ax, v, ROSSO); freccia(ax, u + v, VERDE, lw=2.2)
    ax.plot([u.real, u.real + v.real], [u.imag, u.imag + v.imag], ls="--", color=GRIGIO, lw=1); ax.plot([v.real, u.real + v.real], [v.imag, u.imag + v.imag], ls="--", color=GRIGIO, lw=1)
    ax.text(1.7, 0.1, "u", color=BLU, fontsize=13, style="italic"); ax.text(0.15, 1.5, "v", color=ROSSO, fontsize=13, style="italic")
    ax.text(2.0, 2.3, "u + v", color=VERDE, fontsize=13, style="italic", bbox=dict(fc="white", ec="none", pad=1.5))
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("Somma di vettori: regola del parallelogramma", fontsize=10)
    return _salva(fig, "alg/ch01_parallelogramma")


# ---------------------------------------------------------------- capitoli 2-3
def insiemi_numerici():
    fig, ax = plt.subplots(figsize=(5.4, 3.6)); ax.set_aspect("equal"); ax.axis("off")
    nomi = ["ℂ", "ℝ", "ℚ", "ℤ", "ℕ"]; cols = ["#8e44ad", "#c0392b", "#d35400", "#1e8449", "#1f4e9c"]
    ws = [8.6, 7.0, 5.4, 3.8, 2.2]; hs = [5.8, 4.8, 3.8, 2.8, 1.8]
    for n, c, w, h in zip(nomi, cols, ws, hs):
        ax.add_patch(Ellipse((0, 0), w, h, fill=False, ec=c, lw=2))
        ax.text(0, h / 2 - 0.27, n, color=c, fontsize=14, ha="center", va="center")
    ax.text(0, -0.3, "0, 1, 2, …", fontsize=10, ha="center", va="center")
    ax.set_xlim(-4.5, 4.5); ax.set_ylim(-3.0, 3.1)
    ax.set_title("ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ", fontsize=12)
    return _salva(fig, "alg/ch03_insiemi_numerici")


# ---------------------------------------------------------------- capitoli 5-6
def piano_complesso_z():
    fig, ax = piano(L=3.6)
    z = C(2.5, 1.8); zc = z.conjugate()
    freccia(ax, z); freccia(ax, zc, ROSSO)
    ax.plot([z.real, z.real], [z.imag, 0], ls="--", color=GRIGIO, lw=1); ax.plot([0, z.real], [z.imag, z.imag], ls="--", color=GRIGIO, lw=1)
    ax.plot([zc.real, zc.real], [zc.imag, 0], ls=":", color=GRIGIO, lw=1)
    punto(ax, z, "z = a + bi", BLU, (6, 6)); punto(ax, zc, "z̄ = a − bi", ROSSO, (6, -14))
    ax.text(1.0, 1.35, "|z|", color=BLU, fontsize=12, rotation=math.degrees(math.atan2(z.imag, z.real)), style="italic")
    ax.text(z.real, -0.32, "a", ha="center", fontsize=11); ax.text(-0.22, z.imag, "b", va="center", ha="center", fontsize=11)
    ax.set_title("Un numero complesso, il suo modulo e il suo coniugato", fontsize=10)
    return _salva(fig, "alg/ch06_piano_complesso")


def somma_complessi():
    fig, ax = piano(L=4.6)
    z1, z2 = C(3, 1), C(1, 2.5); s = z1 + z2
    freccia(ax, z1, BLU); freccia(ax, z2, ROSSO); freccia(ax, s, VERDE, lw=2.2)
    ax.plot([z1.real, s.real], [z1.imag, s.imag], ls="--", color=GRIGIO, lw=1); ax.plot([z2.real, s.real], [z2.imag, s.imag], ls="--", color=GRIGIO, lw=1)
    punto(ax, z1, "z₁", BLU, (6, -14)); punto(ax, z2, "z₂", ROSSO, (-18, 4)); punto(ax, s, "z₁ + z₂", VERDE, (6, 4))
    ax.set_xlim(-0.8, 5.2); ax.set_ylim(-0.8, 4.8)
    ax.set_title("La somma di numeri complessi è la somma di vettori", fontsize=10)
    return _salva(fig, "alg/ch06_somma_complessi")


# ---------------------------------------------------------------- capitolo 7
def coordinate_polari():
    fig, ax = piano(L=3.6)
    z = C(2.3, 1.7); r = abs(z); t = math.atan2(z.imag, z.real)
    freccia(ax, z)
    ax.plot([z.real, z.real], [z.imag, 0], ls="--", color=GRIGIO, lw=1)
    ang(ax, 0.8, 0, t, ROSSO, "θ"); punto(ax, z, "P = (a, b)", BLU, (6, 6))
    ax.text(1.05, 1.2, "r", color=BLU, fontsize=13, style="italic")
    ax.text(z.real / 2, -0.35, "a = r cos θ", ha="center", fontsize=10); ax.text(z.real + 0.12, z.imag / 2, "b = r sen θ", fontsize=10, va="center")
    ax.set_title("Coordinate polari: distanza r e angolo θ", fontsize=10)
    return _salva(fig, "alg/ch07_polari")


def quadranti_argomento():
    fig, ax = piano(figsize=(5.0, 4.3), L=3.0, griglia=False)
    testi = {(1.5, 1.6): "a > 0, b ≥ 0\nθ = arctan(b/a)", (-1.5, 1.6): "a < 0\nθ = arctan(b/a) + π", (-1.5, -1.6): "a < 0\nθ = arctan(b/a) + π", (1.5, -1.6): "a > 0, b < 0\nθ = arctan(b/a) + 2π"}
    for (x, y), t in testi.items():
        ax.text(x, y, t, ha="center", va="center", fontsize=9.5, color=BLU if x > 0 else ROSSO)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("Come ricavare θ: dipende dal quadrante", fontsize=10)
    return _salva(fig, "alg/ch07_quadranti")


def circonferenza_unitaria():
    fig, ax = piano(L=1.55, griglia=False)
    ax.add_patch(Circle((0, 0), 1, fill=False, ec=GRIGIO, lw=1.2))
    t = math.radians(55); z = C(math.cos(t), math.sin(t)); freccia(ax, z); ang(ax, 0.3, 0, t, ROSSO, "θ", 11)
    punto(ax, z, "$e^{iθ}$ = cos θ + i sen θ", BLU, (6, 6), 10)
    for zz, et, off in ((C(1, 0), "1 = $e^{0}$", (6, 8)), (C(-1, 0), "−1 = $e^{iπ}$", (-30, -18)), (C(0, 1), "i = $e^{iπ/2}$", (6, 4)), (C(0, -1), "−i = $e^{i3π/2}$", (10, -12))):
        punto(ax, zz, et, VERDE, off, 9)
    ax.set_title("I numeri $e^{iθ}$ sono i punti della circonferenza unitaria", fontsize=10)
    return _salva(fig, "alg/ch07_circonferenza_unitaria")


# ---------------------------------------------------------------- capitolo 8
def prodotto_polare():
    fig, ax = piano(L=2.8)
    z = C(1, 1); w = z * z   # (1+i)^2 = 2i
    freccia(ax, z, BLU); freccia(ax, w, VERDE, lw=2.2)
    ang(ax, 0.55, 0, math.pi / 4, BLU, "π/4", 9); ang(ax, 0.95, 0, math.pi / 2, VERDE, "", 9)
    punto(ax, z, "1 + i\nmodulo √2, arg π/4", BLU, (8, -26), 9); punto(ax, w, "(1 + i)² = 2i\nmodulo 2, arg π/2", VERDE, (8, 4), 9)
    ax.set_xlim(-1, 3.6); ax.set_ylim(-0.8, 3.0)
    ax.set_title("Prodotto: i moduli si moltiplicano, gli angoli si sommano", fontsize=10)
    return _salva(fig, "alg/ch08_prodotto")


def coniugato_inverso():
    fig, ax = piano(L=2.2)
    r, t = 1.6, math.radians(40); z = r * np.exp(1j * t); zc = z.conjugate(); inv = (1 / r) * np.exp(-1j * t)
    ax.add_patch(Circle((0, 0), 1, fill=False, ec=GRIGIO, lw=1, ls="--"))
    freccia(ax, z, BLU); freccia(ax, zc, ROSSO); freccia(ax, inv, VERDE, lw=2)
    punto(ax, z, "z = r $e^{iθ}$", BLU, (6, 6), 10); punto(ax, zc, "z̄ = r $e^{−iθ}$", ROSSO, (6, -14), 10); punto(ax, inv, "z⁻¹ = (1/r) $e^{−iθ}$", VERDE, (-62, -40), 10)
    ax.set_xlim(-1.2, 3.4); ax.set_ylim(-2.0, 2.0)
    ax.set_title("Coniugato: stesso modulo, angolo −θ. Inverso: modulo 1/r, angolo −θ", fontsize=9)
    return _salva(fig, "alg/ch08_coniugato_inverso")


# ---------------------------------------------------------------- capitolo 9
def radici(n, raggio, fase, nome, etich, titolo, L):
    fig, ax = piano(L=L, griglia=False)
    ax.add_patch(Circle((0, 0), raggio, fill=False, ec=GRIGIO, lw=1, ls="--"))
    pts = [raggio * np.exp(1j * (fase + 2 * math.pi * k / n)) for k in range(n)]
    ax.plot([p.real for p in pts] + [pts[0].real], [p.imag for p in pts] + [pts[0].imag], color=BLU, lw=1.5)
    for k, p in enumerate(pts):
        ax.plot([0, p.real], [0, p.imag], color="#cfd8e6", lw=0.8, zorder=1)
        ax.plot(p.real, p.imag, "o", color=ROSSO, ms=6, zorder=5)
        o = (8 if p.real > 0.05 else (-8 if p.real < -0.05 else 0), 6 if p.imag >= -0.05 else -16)
        ax.annotate(etich[k], (p.real, p.imag), textcoords="offset points", xytext=o, fontsize=9.5, ha="left" if o[0] >= 0 else "right")
    ax.set_title(titolo, fontsize=10)
    return _salva(fig, nome)


def radici_8():
    return radici(3, 2, 0, "alg/ch09_radici_di_8", ["w₀ = 2", "w₁ = −1 + i√3", "w₂ = −1 − i√3"], "Le tre radici terze di 8", 3.2)


def radici_meno8():
    return radici(3, 2, math.pi / 3, "alg/ch09_radici_di_meno8", ["1 + i√3", "−2", "1 − i√3"], "Le soluzioni di z³ = −8", 3.2)


def radici_unita6():
    return radici(6, 1, 0, "alg/ch09_radici_unita", ["1", "$e^{iπ/3}$", "$e^{i2π/3}$", "−1", "$e^{i4π/3}$", "$e^{i5π/3}$"], "Radici seste dell'unità: esagono regolare", 1.7)


# ---------------------------------------------------------------- capitoli 10-13
def polinomio_radice_doppia():
    x = np.linspace(-0.6, 2.0, 400); y = x ** 3 - 2 * x ** 2 + x
    fig, ax = plt.subplots(figsize=(4.4, 3.2)); ax.axhline(0, color="black", lw=0.8); ax.axvline(0, color="black", lw=0.8)
    ax.plot(x, y, color=BLU, lw=2); ax.plot([0, 1], [0, 0], "o", color=ROSSO, ms=7, zorder=5)
    ax.annotate("radice semplice: 0", (0, 0), textcoords="offset points", xytext=(-8, 22), color=ROSSO, fontsize=9, ha="center", arrowprops=dict(arrowstyle="-", color=ROSSO, lw=0.8))
    ax.annotate("radice doppia: 1\n(il grafico tocca l'asse\ne non lo attraversa)", (1, 0), textcoords="offset points", xytext=(32, -42), color=ROSSO, fontsize=9, ha="center", arrowprops=dict(arrowstyle="-", color=ROSSO, lw=0.8))
    ax.set_xlim(-0.6, 2.0); ax.set_ylim(-0.9, 1.6); ax.set_xlabel("x"); ax.set_ylabel("p(x)", rotation=0, labelpad=18)
    ax.set_title("p(x) = x³ − 2x² + x = (x − 1)² x", fontsize=10)
    return _salva(fig, "alg/ch12_radice_doppia")


def discriminante():
    x = np.linspace(-3, 3, 300)
    def mk(c, tit, pts):
        def f(ax):
            ax.axhline(0, color="black", lw=0.8); ax.axvline(0, color="black", lw=0.8); ax.plot(x, x ** 2 + c, color=BLU, lw=2)
            for px in pts:
                ax.plot(px, 0, "o", color=ROSSO, ms=6, zorder=5)
            ax.set_ylim(-3, 6); ax.set_xlim(-3, 3); ax.set_title(tit, fontsize=9.5); ax.set_xticks([]); ax.set_yticks([])
        return f
    d = [mk(-2, "Δ > 0: due radici reali", (-math.sqrt(2), math.sqrt(2))), mk(0, "Δ = 0: una radice\n(molteplicità 2)", (0,)), mk(2, "Δ < 0: nessuna radice reale", ())]
    fig, axs = plt.subplots(1, 3, figsize=(10.2, 2.9), gridspec_kw=dict(wspace=0.12))
    for a, f in zip(axs, d):
        f(a)
    return _salva(fig, "alg/ch13_discriminante")


def tutte():
    plan = [
        (4, somma_vettori, "La somma di due vettori con la regola del parallelogramma.", 8.0),
        (48, insiemi_numerici, "Gli insiemi numerici come scatole una dentro l'altra.", 9.0),
        (132, somma_complessi, "La somma di due numeri complessi nel piano di Argand-Gauss.", 8.5),
        (134, piano_complesso_z, "z = a + bi nel piano complesso: il modulo è la lunghezza del vettore, il coniugato è il simmetrico rispetto all'asse reale.", 8.5),
        (147, coordinate_polari, "Coordinate polari di un punto: distanza r dall'origine e angolo θ.", 8.5),
        (158, quadranti_argomento, "Quale formula usare per θ a seconda del quadrante.", 9.5),
        (168, circonferenza_unitaria, "I punti della circonferenza unitaria sono i numeri cos θ + i sen θ.", 8.5),
        (196, prodotto_polare, "(1 + i)² = 2i: il modulo passa da √2 a 2, l'argomento da π/4 a π/2.", 8.0),
        (202, coniugato_inverso, "Coniugato e inverso in forma polare.", 9.0),
        (234, radici_8, "Le radici terze di 8 sono i vertici di un triangolo equilatero di raggio 2.", 7.5),
        (238, radici_meno8, "Le soluzioni di z³ = −8: stesso triangolo, ruotato di π/3.", 7.5),
        (239, radici_unita6, "Le radici seste dell'unità formano un esagono regolare.", 7.5),
        (313, polinomio_radice_doppia, "Una radice doppia: il grafico tocca l'asse x senza attraversarlo.", 8.5),
        (336, discriminante, "I tre casi del discriminante per un polinomio di grado 2.", 14.0),
    ]
    PIANO = []
    for dopo, fn, did, larg in plan:
        PIANO.append(dict(dopo=dopo, figura=fn(), didascalia=did, larghezza=larg))
    (OUT / "alg").mkdir(exist_ok=True)
    (OUT / "alg" / "piano.json").write_text(json.dumps(PIANO, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(PIANO)} figure in {OUT / 'alg'}")


if __name__ == "__main__":
    tutte()
