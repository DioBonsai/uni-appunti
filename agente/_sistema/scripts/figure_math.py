"""Figure matematiche per i riassunti (inserite nei Word con ![didascalia](figure/nome.png|larghezza_cm)).

Tutte le funzioni salvano un PNG in _sistema/figure/ (200 dpi, fondo bianco, stile pulito) e restituiscono il percorso
relativo da usare nella bozza, per esempio "figure/funzione_frecce.png". Esempio d'uso:

    python -c "import figure_math as f; print(f.diagramma_funzione(['a','b','c','d'], [1,2,3], {'a':2,'b':2,'c':3,'d':1}, 'f_esempio'))"

Tipi disponibili:
  diagramma_funzione   due insiemi (ovali) con le frecce di una funzione A -> B
  scacchiera_grafico   il grafico di una funzione come caselle segnate in A x B
  grafico_funzione     grafico cartesiano di una funzione (punti, rette, intervalli evidenziati)
  controimmagine_x2    parabola y = x^2 con l'intervallo [m^2, k^2] e la sua controimmagine
  venn                 diagramma di Venn a 2 o 3 insiemi con le regioni etichettate
  piano_complesso      piano di Argand con numeri complessi, moduli e argomenti
  radici_unita         le radici n-esime di un numero complesso come vertici di un poligono regolare
  polinomio            grafico di un polinomio con le radici reali segnate
Controllo: aprire il PNG con lo strumento Read prima di inserirlo nel Word.
"""
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, FancyArrowPatch, Circle, Arc, Rectangle

OUT = Path(__file__).resolve().parent.parent / "figure"
BLU, ROSSO, VERDE, ARANCIO, GRIGIO = "#1f4e9c", "#c0392b", "#1e8449", "#d35400", "#7f8c8d"
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False, "mathtext.default": "regular",
                     "font.family": "DejaVu Sans"})


def _salva(fig, nome):
    OUT.mkdir(exist_ok=True)
    p = OUT / f"{nome}.png"
    fig.savefig(p, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return f"figure/{nome}.png"


def diagramma_funzione(A, B, mappa, nome, nomeA="A", nomeB="B", nomef="f", colore=BLU):
    """Due ovali con gli elementi di A e B e una freccia per ogni a -> f(a). mappa: dict elemento di A -> elemento di B."""
    fig, ax = plt.subplots(figsize=(5.2, 3.4)); ax.set_xlim(0, 10); ax.set_ylim(0, 6.2); ax.axis("off")
    for cx, nm in ((2.2, nomeA), (7.8, nomeB)):
        ax.add_patch(Ellipse((cx, 3.0), 3.0, 5.2, fill=False, ec="black", lw=1.4))
        ax.text(cx, 5.85, nm, ha="center", va="center", fontsize=13, style="italic")
    def pos(lst, cx):
        n = len(lst); ys = np.linspace(4.5, 1.5, n) if n > 1 else [3.0]
        return {e: (cx, y) for e, y in zip(lst, ys)}
    pa, pb = pos(list(A), 2.2), pos(list(B), 7.8)
    for e, (x, y) in {**pa, **pb}.items():
        ax.plot(x, y, "o", color="black", ms=4); ax.text(x + (0.25 if x < 5 else 0.25), y + 0.02, str(e), va="center", fontsize=12)
    for a, b in mappa.items():
        ax.add_patch(FancyArrowPatch((pa[a][0] + 0.1, pa[a][1]), (pb[b][0] - 0.12, pb[b][1]), arrowstyle="-|>", mutation_scale=12, color=colore, lw=1.4,
                                     connectionstyle="arc3,rad=0.0", shrinkA=18, shrinkB=18))
    ax.text(5, 6.0, nomef, ha="center", fontsize=13, color=colore, style="italic")
    return _salva(fig, nome)


def scacchiera_grafico(A, B, coppie, nome, nomeA="A", nomeB="B"):
    """Il prodotto cartesiano A x B come scacchiera; le caselle in `coppie` (lista di (a, b)) sono segnate in colore."""
    fig, ax = plt.subplots(figsize=(0.9 + 0.7 * len(A), 0.8 + 0.6 * len(B)))
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            on = (a, b) in coppie
            ax.add_patch(Rectangle((i, j), 1, 1, fc=BLU if on else "white", ec="#555", lw=1, alpha=0.85 if on else 1))
    ax.set_xlim(0, len(A)); ax.set_ylim(0, len(B)); ax.set_aspect("equal")
    ax.set_xticks([i + 0.5 for i in range(len(A))]); ax.set_xticklabels([str(a) for a in A], fontsize=12)
    ax.set_yticks([j + 0.5 for j in range(len(B))]); ax.set_yticklabels([str(b) for b in B], fontsize=12)
    ax.tick_params(length=0); [s.set_visible(False) for s in ax.spines.values()]
    ax.set_xlabel(nomeA, fontsize=12, style="italic"); ax.set_ylabel(nomeB, fontsize=12, style="italic", rotation=0, labelpad=14)
    return _salva(fig, nome)


def grafico_funzione(f, xmin, xmax, nome, titolo=None, punti=None, orizzontali=None, intervallo_y=None, intervallo_x=None, ymin=None, ymax=None, etichetta=None):
    """Grafico di f(x). punti: [(x, y, 'etichetta')]; orizzontali: [y]; intervallo_y/x: (a, b) evidenziati sull'asse."""
    x = np.linspace(xmin, xmax, 600); y = f(x)
    fig, ax = plt.subplots(figsize=(4.6, 3.4))
    ax.axhline(0, color="black", lw=0.8); ax.axvline(0, color="black", lw=0.8)
    ax.plot(x, y, color=BLU, lw=2, label=etichetta)
    for yy in orizzontali or []:
        ax.axhline(yy, color=GRIGIO, lw=1, ls="--")
    for px, py, lab in punti or []:
        ax.plot(px, py, "o", color=ROSSO, ms=5)
        if lab:
            ax.annotate(lab, (px, py), textcoords="offset points", xytext=(6, 6), fontsize=10, color=ROSSO)
    if intervallo_y:
        ax.add_patch(Rectangle((xmin, intervallo_y[0]), 0.12 * (xmax - xmin), intervallo_y[1] - intervallo_y[0], color=VERDE, alpha=0.5, lw=0))
    if intervallo_x:
        ax.plot(intervallo_x, [0, 0], color=ARANCIO, lw=5, alpha=0.7, solid_capstyle="butt")
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin if ymin is not None else min(y.min(), 0) - 0.5, ymax if ymax is not None else y.max() + 0.5)
    ax.set_xlabel("x"); ax.set_ylabel("y", rotation=0)
    if titolo:
        ax.set_title(titolo, fontsize=11)
    if etichetta:
        ax.legend(frameon=False, loc="upper center")
    return _salva(fig, nome)


def controimmagine_x2(m, k, nome):
    """f(x) = x^2: l'intervallo [m^2, k^2] sull'asse y e la sua controimmagine [-k,-m] U [m,k] sull'asse x."""
    xs = np.linspace(-k - 1, k + 1, 600); fig, ax = plt.subplots(figsize=(4.8, 3.6))
    ax.axhline(0, color="black", lw=0.8); ax.axvline(0, color="black", lw=0.8)
    ax.plot(xs, xs ** 2, color=BLU, lw=2)
    ax.axhspan(m * m, k * k, color=VERDE, alpha=0.25)
    ax.plot([-k, -m], [0, 0], color=ARANCIO, lw=6, solid_capstyle="butt"); ax.plot([m, k], [0, 0], color=ARANCIO, lw=6, solid_capstyle="butt")
    for yy in (m * m, k * k):
        ax.axhline(yy, color=GRIGIO, lw=0.8, ls="--")
    ax.set_xlim(-k - 1, k + 1); ax.set_ylim(-0.6, k * k + 1.5)
    ax.text(k + 0.9, (m * m + k * k) / 2, "T = [%d, %d]" % (m * m, k * k), color=VERDE, ha="right", va="center", fontsize=10)
    ax.text(0, -0.45 if False else 0.15 * k * k / 6 + 0.1, "", fontsize=1)
    ax.set_xlabel("x"); ax.set_ylabel("y", rotation=0); ax.set_title("f(x) = x²: la controimmagine di T è in arancio", fontsize=10)
    return _salva(fig, nome)


def venn(insiemi, nome, universo=None, evidenzia=None):
    """insiemi: dict nome -> set (2 o 3). Le regioni mostrano gli elementi; evidenzia: espressione su sets, es. lambda r: r['A'] and not r['B']."""
    nomi = list(insiemi); n = len(nomi)
    fig, ax = plt.subplots(figsize=(4.6, 3.6)); ax.set_aspect("equal"); ax.axis("off")
    centri = {2: [(-0.6, 0), (0.6, 0)], 3: [(-0.6, 0.35), (0.6, 0.35), (0, -0.6)]}[n]
    R = 1.1
    if evidenzia:   # riempie con una griglia di punti le regioni selezionate
        gx, gy = np.meshgrid(np.linspace(-2.2, 2.2, 300), np.linspace(-2, 2, 300))
        masks = {nm: (gx - c[0]) ** 2 + (gy - c[1]) ** 2 <= R * R for nm, c in zip(nomi, centri)}
        sel = evidenzia(masks)
        ax.imshow(np.where(sel, 1.0, np.nan), extent=(-2.2, 2.2, -2, 2), origin="lower", cmap="Blues", vmin=0, vmax=2, alpha=0.6, zorder=0)
    cols = [BLU, ROSSO, VERDE]
    for (cx, cy), nm, col in zip(centri, nomi, cols):
        ax.add_patch(Circle((cx, cy), R, fill=False, ec=col, lw=2, zorder=2))
        ax.text(cx + (-0.95 if cx < 0 else (0.95 if cx > 0 else 0)), cy + (0.95 if n == 2 or cy > 0 else -1.0), nm, color=col, fontsize=13, ha="center", style="italic")
    # etichette degli elementi per regione
    elementi = sorted(set().union(*insiemi.values()))
    regioni = {}
    for e in elementi:
        chiave = tuple(nm for nm in nomi if e in insiemi[nm]); regioni.setdefault(chiave, []).append(e)
    def posizione(chiave):
        pts = [centri[nomi.index(nm)] for nm in chiave]
        if not pts:
            return (-1.9, -1.7)
        mx = sum(p[0] for p in pts) / len(pts); my = sum(p[1] for p in pts) / len(pts)
        if len(chiave) == 1:
            c = pts[0]; return (c[0] + (c[0] - sum(p[0] for p in centri) / n) * 0.55, c[1] + (c[1] - sum(p[1] for p in centri) / n) * 0.55)
        return (mx, my)
    for chiave, els in regioni.items():
        x, y = posizione(chiave); ax.text(x, y, ", ".join(str(e) for e in els), ha="center", va="center", fontsize=11, zorder=3)
    if universo is not None:
        ax.add_patch(Rectangle((-2.2, -2.0), 4.4, 4.0, fill=False, ec="black", lw=1, zorder=1))
        ax.text(2.1, 1.8, "U", ha="right", va="top", fontsize=12)
    ax.set_xlim(-2.3, 2.3); ax.set_ylim(-2.1, 2.1)
    return _salva(fig, nome)


def piano_complesso(punti, nome, mostra_modulo=False, mostra_arg=None, lim=None):
    """punti: dict etichetta -> complesso. mostra_arg: etichetta del punto di cui disegnare l'angolo."""
    zs = list(punti.values()); L = lim or math.ceil(max(max(abs(z.real), abs(z.imag)) for z in zs) + 1)
    fig, ax = plt.subplots(figsize=(4.2, 4.0)); ax.set_aspect("equal")
    ax.axhline(0, color="black", lw=0.9); ax.axvline(0, color="black", lw=0.9)
    ax.set_xlim(-L, L); ax.set_ylim(-L, L); ax.grid(True, color="#dddddd", lw=0.6)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.set_xlabel("Re"); ax.set_ylabel("Im", rotation=0)
    for et, z in punti.items():
        ax.annotate("", xy=(z.real, z.imag), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=BLU, lw=1.5))
        ax.plot(z.real, z.imag, "o", color=BLU, ms=4)
        ax.annotate(f"{et}", (z.real, z.imag), textcoords="offset points", xytext=(6, 6), fontsize=11, color=BLU)
        if mostra_modulo:
            ax.add_patch(Circle((0, 0), abs(z), fill=False, ec=GRIGIO, lw=0.8, ls="--"))
    if mostra_arg:
        z = punti[mostra_arg]; th = math.degrees(math.atan2(z.imag, z.real)); r = min(abs(z) * 0.4, L * 0.35)
        ax.add_patch(Arc((0, 0), 2 * r, 2 * r, theta1=0 if th >= 0 else th, theta2=th if th >= 0 else 0, color=ROSSO, lw=1.6))
        a = math.radians(th / 2); ax.text(1.25 * r * math.cos(a), 1.25 * r * math.sin(a), "θ", color=ROSSO, fontsize=12)
    return _salva(fig, nome)


def radici_unita(n, nome, centro_raggio=1.0, fase=0.0, etichette=True):
    """Le n radici n-esime di un numero di modulo centro_raggio^n e argomento n*fase: vertici di un n-agono regolare."""
    fig, ax = plt.subplots(figsize=(4.0, 4.0)); ax.set_aspect("equal")
    ax.axhline(0, color="black", lw=0.8); ax.axvline(0, color="black", lw=0.8)
    ax.add_patch(Circle((0, 0), centro_raggio, fill=False, ec=GRIGIO, lw=1, ls="--"))
    pts = [centro_raggio * np.exp(1j * (fase + 2 * math.pi * k / n)) for k in range(n)]
    xs = [p.real for p in pts] + [pts[0].real]; ys = [p.imag for p in pts] + [pts[0].imag]
    ax.plot(xs, ys, color=BLU, lw=1.5); ax.plot([p.real for p in pts], [p.imag for p in pts], "o", color=ROSSO, ms=6)
    if etichette:
        for k, p in enumerate(pts):
            ax.annotate(f"z{k}", (p.real, p.imag), textcoords="offset points", xytext=(8 if p.real >= 0 else -16, 6), fontsize=11)
    L = centro_raggio * 1.35; ax.set_xlim(-L, L); ax.set_ylim(-L, L)
    ax.set_xlabel("Re"); ax.set_ylabel("Im", rotation=0)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    return _salva(fig, nome)


def polinomio(coeff, xmin, xmax, nome, titolo=None):
    """coeff: coefficienti dal grado più alto, es. [1, 0, -1] per x^2 - 1. Segna le radici reali."""
    p = np.poly1d(coeff); x = np.linspace(xmin, xmax, 600); y = p(x)
    fig, ax = plt.subplots(figsize=(4.6, 3.4))
    ax.axhline(0, color="black", lw=0.8); ax.axvline(0, color="black", lw=0.8)
    ax.plot(x, y, color=BLU, lw=2)
    for r in p.roots:
        if abs(r.imag) < 1e-9:
            ax.plot(r.real, 0, "o", color=ROSSO, ms=6); ax.annotate(f"{r.real:g}", (r.real, 0), textcoords="offset points", xytext=(4, -14), color=ROSSO, fontsize=10)
    ax.set_xlim(xmin, xmax); ax.set_ylim(max(y.min(), -10 * abs(y).max()) - 0.5, y.max() + 0.5)
    ax.set_xlabel("x"); ax.set_ylabel("p(x)", rotation=0, labelpad=16)
    if titolo:
        ax.set_title(titolo, fontsize=11)
    return _salva(fig, nome)


# ======================================================================================
# Blocchi di costruzione generali (usati da figure_mate.py): disegni su un asse `ax`
# ======================================================================================
def _salva(fig, nome):  # versione con sottocartelle (nome può contenere "mate/…")
    p = OUT / f"{nome}.png"
    p.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(p, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return f"figure/{nome}.png"


def ovali_ax(ax, ovali, frecce=(), titolo=None, xlim=(0, 10), ylim=(0, 6.4), fs=12):
    """Ovali con elementi e frecce.
    ovali:  lista di dict(nome, elems, cx, cy=3.1, w=2.8, h=5.0, evid=set() sottoinsieme evidenziato, col=BLU, sub=nome del sottoinsieme)
    frecce: lista di dict(da=(i, elem), a=(j, elem), col=BLU, tratt=False, rad=0.0, lab=None)"""
    ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.axis("off")
    pos = {}
    for i, o in enumerate(ovali):
        cx, cy, w, h = o["cx"], o.get("cy", 3.1), o.get("w", 2.8), o.get("h", 5.0)
        ax.add_patch(Ellipse((cx, cy), w, h, fill=False, ec="black", lw=1.4))
        ax.text(cx, cy + h / 2 + 0.28, o["nome"], ha="center", va="center", fontsize=fs + 1, style="italic")
        els = list(o["elems"]); n = len(els)
        ys = np.linspace(cy + h * 0.30, cy - h * 0.30, n) if n > 1 else [cy]
        ev = o.get("evid", set()); col = o.get("col", ARANCIO)
        if ev:   # ellisse attorno agli elementi evidenziati
            yy = [y for e, y in zip(els, ys) if e in ev]
            ax.add_patch(Ellipse((cx, (min(yy) + max(yy)) / 2), w * 0.78, (max(yy) - min(yy)) + 0.95, fc=col, ec=col, alpha=0.18, lw=1.4))
            ax.add_patch(Ellipse((cx, (min(yy) + max(yy)) / 2), w * 0.78, (max(yy) - min(yy)) + 0.95, fill=False, ec=col, lw=1.4, ls="--"))
            if o.get("sub"):
                ax.text(cx + w * 0.5 + 0.1, (min(yy) + max(yy)) / 2, o["sub"], color=col, fontsize=fs, va="center", ha="left")
        for e, y in zip(els, ys):
            ax.plot(cx, y, "o", color="black", ms=4); ax.text(cx + 0.28, y, str(e), va="center", fontsize=fs)
            pos[(i, e)] = (cx, y)
    for fr in frecce:
        p0, p1 = pos[fr["da"]], pos[fr["a"]]
        ax.add_patch(FancyArrowPatch((p0[0] + 0.12, p0[1]), (p1[0] - 0.12, p1[1]), arrowstyle="-|>", mutation_scale=12, color=fr.get("col", BLU), lw=1.5,
                                     linestyle="--" if fr.get("tratt") else "-", connectionstyle=f"arc3,rad={fr.get('rad', 0.0)}", shrinkA=16, shrinkB=16))
        if fr.get("lab"):
            ax.text((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2 + 0.25, fr["lab"], color=fr.get("col", BLU), ha="center", fontsize=fs - 1, style="italic")
    if titolo:
        ax.set_title(titolo, fontsize=fs, pad=2)


def coppia_ovali(A, B, mappa, nomeA="A", nomeB="B", extra=None, **kw):
    """Costruisce (ovali, frecce) per una funzione/relazione A -> B; mappa: dict elem -> elem oppure lista di (a, b)."""
    coppie = list(mappa.items()) if isinstance(mappa, dict) else list(mappa)
    ovali = [dict(nome=nomeA, elems=A, cx=2.3), dict(nome=nomeB, elems=B, cx=7.7)]
    frecce = [dict(da=(0, a), a=(1, b), col=BLU) for a, b in coppie]
    return ovali, frecce


def pannelli(nome, disegni, ncols=None, larghezza=3.6, altezza=2.9, wspace=0.15):
    """disegni: lista di callable(ax). Restituisce il percorso del PNG."""
    n = len(disegni); ncols = ncols or n; nrows = math.ceil(n / ncols)
    fig, axs = plt.subplots(nrows, ncols, figsize=(larghezza * ncols, altezza * nrows)); axs = np.atleast_1d(axs).ravel()
    for ax, f in zip(axs, disegni):
        f(ax)
    for ax in axs[n:]:
        ax.axis("off")
    fig.subplots_adjust(wspace=wspace)
    return _salva(fig, nome)


def venn_ax(ax, insiemi, evidenzia=None, universo=False, titolo=None, mostra_elementi=True, fs=11, nomi_pos=None):
    """Diagramma di Venn su un asse. insiemi: dict nome -> set; evidenzia(masks) -> maschera booleana sulle regioni."""
    nomi = list(insiemi); n = len(nomi)
    ax.set_aspect("equal"); ax.axis("off")
    centri = {1: [(0, 0)], 2: [(-0.6, 0), (0.6, 0)], 3: [(-0.6, 0.35), (0.6, 0.35), (0, -0.6)]}[n]
    R = 1.0 if n == 1 else 1.1
    if evidenzia:
        gx, gy = np.meshgrid(np.linspace(-2.2, 2.2, 300), np.linspace(-2, 2, 300))
        masks = {nm: (gx - c[0]) ** 2 + (gy - c[1]) ** 2 <= R * R for nm, c in zip(nomi, centri)}
        ax.imshow(np.where(evidenzia(masks), 1.0, np.nan), extent=(-2.2, 2.2, -2, 2), origin="lower", cmap="Blues", vmin=0, vmax=2, alpha=0.6, zorder=0)
    cols = [BLU, ROSSO, VERDE]
    for (cx, cy), nm, col in zip(centri, nomi, cols):
        ax.add_patch(Circle((cx, cy), R, fill=False, ec=col, lw=2, zorder=2))
        dx = -0.95 if cx < 0 else (0.95 if cx > 0 else 0.0); dy = (0.95 if (n < 3 or cy > 0) else -1.0)
        ax.text(cx + dx, cy + dy, nm, color=col, fontsize=fs + 2, ha="center", style="italic")
    if mostra_elementi:
        regs = {}
        for e in sorted(set().union(*insiemi.values()), key=str):
            regs.setdefault(tuple(nm for nm in nomi if e in insiemi[nm]), []).append(e)
        for chiave, els in regs.items():
            if not chiave:
                x, y = -1.8, -1.6
            else:
                pts = [centri[nomi.index(nm)] for nm in chiave]
                mx, my = sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts)
                if len(chiave) == 1 and n > 1:
                    cxm = sum(p[0] for p in centri) / n; cym = sum(p[1] for p in centri) / n
                    mx, my = mx + (mx - cxm) * 0.55, my + (my - cym) * 0.55
                x, y = mx, my
            ax.text(x, y, ", ".join(str(e) for e in els), ha="center", va="center", fontsize=fs, zorder=3)
    if universo:
        ax.add_patch(Rectangle((-2.2, -2.0), 4.4, 4.0, fill=False, ec="black", lw=1, zorder=1)); ax.text(2.1, 1.8, "U", ha="right", va="top", fontsize=fs + 1)
    ax.set_xlim(-2.3, 2.3); ax.set_ylim(-2.1, 2.1)
    if titolo:
        ax.set_title(titolo, fontsize=fs + 1, pad=2)
