"""Tavole di verità della logica proposizionale (Fondamenti, capitoli 13-15) come immagini.
Genera in _sistema/figure/fond/: logica_connettivi.png, logica_formula.png, logica_demorgan.png
Uso: python figure_logica.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_math import BLU, ROSSO, VERDE, ARANCIO, GRIGIO, OUT, np, plt, Rectangle, _salva

V1, V0 = "#cfe8d5", "#f7e1de"   # 1 = vero (verde chiaro), 0 = falso (rosso chiaro)
EV = {"b": BLU, "v": VERDE, "r": ROSSO}


def tavola(ax, x0, gruppi, righe, colori_gruppo=None, evid=(), cw=1.0, rh=0.62, gap=0.35, sub_fs=7.5, hdr_fs=10.5):
    """Disegna una tavola a partire da x0. gruppi: [[(intestazione, sottotitolo), ...], ...]; righe: liste di 0/1 (tutte le colonne).
    evid: indici (globali) delle colonne da evidenziare con un bordo spesso. Restituisce x finale."""
    n = sum(len(g) for g in gruppi); x = x0; col = 0; ytop = 0
    for gi, g in enumerate(gruppi):
        for (h, s) in g:
            ax.text(x + cw / 2, ytop + 0.55, h, ha="center", va="center", fontsize=hdr_fs, fontweight="bold", color=colori_gruppo[gi] if colori_gruppo else "black")
            if s:
                ax.text(x + cw / 2, ytop + 0.2, s, ha="center", va="center", fontsize=sub_fs, color=GRIGIO)
            for r, riga in enumerate(righe):
                v = riga[col]; y = -(r + 1) * rh
                ax.add_patch(Rectangle((x, y), cw, rh, fc=V1 if v else V0, ec="white", lw=1.6))
                ax.text(x + cw / 2, y + rh / 2, str(v), ha="center", va="center", fontsize=12, fontweight="bold", color="#14532d" if v else "#7f1d1d")
            if col in evid:
                ax.add_patch(Rectangle((x, -len(righe) * rh), cw, len(righe) * rh, fc="none", ec=BLU, lw=2.6, zorder=5))
            x += cw; col += 1
        x += gap
    return x - gap


def nuova(w, h, xl, yl):
    fig, ax = plt.subplots(figsize=(w, h)); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(*xl); ax.set_ylim(*yl)
    return fig, ax


def connettivi():
    fig, ax = nuova(8.6, 3.0, (-0.2, 11.6), (-3.0, 1.2))
    righe = [(1, 1, 1, 1, 0, 1), (1, 0, 0, 1, 1, 0), (0, 1, 0, 1, 1, 0), (0, 0, 0, 0, 0, 1)]
    xe = tavola(ax, 0.0, [[("p", ""), ("q", "")], [("p ∧ q", "e"), ("p ∨ q", "o"), ("xor", "aut"), ("equiv", "uguali")]], righe, colori_gruppo=["black", BLU], cw=1.1)
    righe_not = [(1, 0), (0, 1)]
    tavola(ax, xe + 0.9, [[("p", ""), ("¬p", "non")]], righe_not, colori_gruppo=[BLU], cw=1.1)
    ax.text(5.8, -2.85, "1 = vero, 0 = falso (con l'ordine del libro: prima il vero)", ha="center", fontsize=8, color=GRIGIO)
    return _salva(fig, "fond/logica_connettivi")


def formula():
    fig, ax = nuova(6.4, 2.9, (-0.2, 8.4), (-3.0, 1.2))
    righe = [(1, 1, 1, 0, 0), (1, 0, 1, 0, 0), (0, 1, 1, 1, 1), (0, 0, 0, 1, 0)]
    tavola(ax, 0.0, [[("p", ""), ("q", "")], [("p ∨ q", ""), ("¬p", "")], [("(p ∨ q) ∧ ¬p", "")]], righe, colori_gruppo=["black", GRIGIO, BLU], cw=1.1, evid=(4,))
    ax.text(3.9, -2.85, "l'unico 1: p falso e q vero", ha="center", fontsize=8.5, color=BLU)
    return _salva(fig, "fond/logica_formula")


def demorgan():
    fig, ax = nuova(9.2, 2.9, (-0.2, 12.4), (-3.0, 1.2))
    righe = [(1, 1, 1, 0, 0, 0, 0), (1, 0, 1, 0, 0, 1, 0), (0, 1, 1, 0, 1, 0, 0), (0, 0, 0, 1, 1, 1, 1)]
    tavola(ax, 0.0, [[("p", ""), ("q", "")], [("p ∨ q", ""), ("¬(p ∨ q)", "")], [("¬p", ""), ("¬q", ""), ("¬p ∧ ¬q", "")]], righe, colori_gruppo=["black", BLU, BLU], cw=1.4, evid=(3, 6))
    ax.text(6.0, -2.85, "le due colonne in blu coincidono: ¬(p ∨ q) è equivalente a ¬p ∧ ¬q", ha="center", fontsize=8.5, color=BLU)
    return _salva(fig, "fond/logica_demorgan")


def implicazione():
    fig, ax = nuova(4.6, 3.0, (-0.2, 5.8), (-3.0, 1.2))
    righe = [(1, 1, 1), (1, 0, 0), (0, 1, 1), (0, 0, 1)]
    tavola(ax, 0.0, [[("p", "ipotesi"), ("q", "tesi")], [("p → q", "")]], righe, colori_gruppo=["black", BLU], cw=1.2)
    ax.text(2.9, -2.85, "falsa solo con ipotesi vera e tesi falsa", ha="center", fontsize=8.5, color=ROSSO)
    return _salva(fig, "fond/logica_implicazione")


def contrapposta():
    fig, ax = nuova(8.4, 3.0, (-0.2, 10.6), (-3.0, 1.2))
    righe = [(1, 1, 0, 0, 1, 1), (1, 0, 0, 1, 0, 0), (0, 1, 1, 0, 1, 1), (0, 0, 1, 1, 1, 1)]
    tavola(ax, 0.0, [[("p", ""), ("q", "")], [("¬p", ""), ("¬q", "")], [("p → q", ""), ("¬q → ¬p", "")]], righe, colori_gruppo=["black", GRIGIO, BLU], cw=1.4, evid=(4, 5))
    ax.text(5.4, -2.85, "le due colonne in blu coincidono: p → q ≡ ¬q → ¬p", ha="center", fontsize=8.5, color=BLU)
    return _salva(fig, "fond/logica_contrapposta")


def bicondizionale():
    fig, ax = nuova(10.0, 3.0, (-0.2, 12.9), (-3.0, 1.2))
    righe = [(1, 1, 1, 1, 1, 1), (1, 0, 0, 1, 0, 0), (0, 1, 1, 0, 0, 0), (0, 0, 1, 1, 1, 1)]
    tavola(ax, 0.0, [[("p", ""), ("q", "")], [("p → q", ""), ("q → p", "")], [("(p → q) ∧ (q → p)", ""), ("p ↔ q", "")]], righe, colori_gruppo=["black", GRIGIO, BLU], cw=1.95, evid=(4, 5))
    ax.text(6.1, -2.85, "le due colonne in blu coincidono: p ↔ q ≡ (p → q) ∧ (q → p)", ha="center", fontsize=8.5, color=BLU)
    return _salva(fig, "fond/logica_bicondizionale")


def implicazione_disgiunzione():
    fig, ax = nuova(6.8, 3.0, (-0.2, 8.6), (-3.0, 1.2))
    righe = [(1, 1, 1, 0, 1), (1, 0, 0, 0, 0), (0, 1, 1, 1, 1), (0, 0, 1, 1, 1)]
    tavola(ax, 0.0, [[("p", ""), ("q", "")], [("p → q", ""), ("¬p", ""), ("¬p ∨ q", "")]], righe, colori_gruppo=["black", BLU], cw=1.3, evid=(2, 4))
    ax.text(4.3, -2.85, "le colonne in blu coincidono: p → q ≡ ¬p ∨ q", ha="center", fontsize=8.5, color=BLU)
    return _salva(fig, "fond/logica_implicazione_disgiunzione")


if __name__ == "__main__":
    for f in (connettivi, formula, demorgan, implicazione, contrapposta, bicondizionale, implicazione_disgiunzione):
        print(f())
