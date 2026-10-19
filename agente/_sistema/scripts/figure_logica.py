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


def regole_inferenza():
    regole = [
        (["p → q", "p"], "q", "modus ponens"),
        (["p → q", "¬q"], "¬p", "modus tollens"),
        (["p"], "p ∨ q", "addizione"),
        (["p ∧ q"], "p", "semplificazione"),
        (["p", "q"], "p ∧ q", "congiunzione"),
        (["p → q", "q → r"], "p → r", "sillogismo ipotetico"),
        (["p ∨ q", "¬p"], "q", "sillogismo disgiuntivo"),
    ]
    fig, ax = plt.subplots(figsize=(9.0, 6.0)); ax.axis("off"); ax.set_xlim(0, 9.0); ax.set_ylim(0, 6.0)
    pos = [(0.25, 4.0), (3.2, 4.0), (6.15, 4.0), (0.25, 2.1), (3.2, 2.1), (6.15, 2.1), (0.25, 0.2)]
    for (prem, concl, nome), (x, y) in zip(regole, pos):
        ax.add_patch(Rectangle((x, y), 2.7, 1.75, fc="#F3F6FB", ec=BLU, lw=1.4))
        n = len(prem)
        for i, t in enumerate(prem):
            ax.text(x + 0.3, y + 1.45 - i * 0.38, t, fontsize=13, va="center")
        yl = y + 1.45 - n * 0.38 + 0.12
        ax.plot([x + 0.25, x + 1.6], [yl, yl], color="black", lw=1.2)
        ax.text(x + 0.3, yl - 0.27, "∴ " + concl, fontsize=13, va="center")
        ax.text(x + 1.35, y + 0.12, nome, fontsize=9.5, ha="center", va="bottom", color=BLU, style="italic")
    ax.text(6.15, 0.95, "ogni regola è un argomento valido:\nse le ipotesi sono vere, lo è la conclusione", fontsize=9.5, color=GRIGIO, va="center")
    return _salva(fig, "fond/logica_regole_inferenza")


def argomenti_tavole():
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.3))
    for ax in axs:
        ax.set_aspect("equal"); ax.axis("off")
    # modus ponens: ipotesi p -> q e p, conclusione q
    ax = axs[0]; ax.set_xlim(-0.2, 6.2); ax.set_ylim(-3.2, 1.5)
    righe = [(1, 1, 1, 1, 1), (1, 0, 0, 1, 0), (0, 1, 1, 0, 1), (0, 0, 1, 0, 0)]
    tavola(ax, 0.0, [[("p", ""), ("q", "")], [("p → q", "ipotesi"), ("p", "ipotesi")], [("q", "conclusione")]], righe, colori_gruppo=["black", BLU, ROSSO], cw=1.0, gap=0.3)
    ax.add_patch(Rectangle((-0.05, -0.62), 6.0, 0.62, fc="none", ec=VERDE, lw=2.4, zorder=6))
    ax.text(3.0, -3.0, "modus ponens: con le due ipotesi vere (prima riga) anche q è vera", ha="center", fontsize=8.3, color=VERDE)
    # affermare il conseguente: ipotesi p -> q e q, conclusione p
    ax = axs[1]; ax.set_xlim(-0.2, 6.2); ax.set_ylim(-3.2, 1.5)
    righe = [(1, 1, 1, 1, 1), (1, 0, 0, 0, 1), (0, 1, 1, 1, 0), (0, 0, 1, 0, 0)]
    tavola(ax, 0.0, [[("p", ""), ("q", "")], [("p → q", "ipotesi"), ("q", "ipotesi")], [("p", "conclusione")]], righe, colori_gruppo=["black", BLU, ROSSO], cw=1.0, gap=0.3)
    ax.add_patch(Rectangle((-0.05, -1.86), 6.0, 0.62, fc="none", ec=ROSSO, lw=2.4, zorder=6))
    ax.text(3.0, -3.0, "ipotesi vere e conclusione falsa (terza riga): argomento non valido", ha="center", fontsize=8.3, color=ROSSO)
    fig.subplots_adjust(wspace=0.08)
    return _salva(fig, "fond/logica_argomenti_tavole")


def quantificatori_dominio():
    fig, ax = plt.subplots(figsize=(9.4, 4.0)); ax.axis("off"); ax.set_xlim(0, 12.2); ax.set_ylim(-0.4, 5.2)
    ax.text(3.3, 4.75, "valori di P(x) nel dominio", ha="center", fontsize=10.5, color=GRIGIO)
    ax.text(8.4, 4.75, "∀x P(x)", ha="center", fontsize=12, fontweight="bold", color=BLU)
    ax.text(10.9, 4.75, "∃x P(x)", ha="center", fontsize=12, fontweight="bold", color=ROSSO)
    casi = [([1, 1, 1, 1, 1, 1], "vero", "vero"), ([1, 1, 0, 1, 1, 0], "falso", "vero"), ([0, 0, 0, 0, 0, 0], "falso", "falso")]
    etich = ["tutti veri", "alcuni veri, alcuni falsi", "tutti falsi"]
    for r, ((vals, a, e), lab) in enumerate(zip(casi, etich)):
        y = 3.5 - r * 1.55
        for i, v in enumerate(vals):
            ax.add_patch(Rectangle((0.5 + i * 0.95, y), 0.85, 0.85, fc=V1 if v else V0, ec="white", lw=1.6))
            ax.text(0.5 + i * 0.95 + 0.425, y + 0.425, str(v), ha="center", va="center", fontsize=12, fontweight="bold", color="#14532d" if v else "#7f1d1d")
        ax.text(0.5, y - 0.22, lab, fontsize=8.8, color=GRIGIO, va="top")
        for xc, res in ((8.4, a), (10.9, e)):
            ok = res == "vero"
            ax.add_patch(Rectangle((xc - 0.6, y + 0.05), 1.2, 0.75, fc=V1 if ok else V0, ec="white", lw=1.6))
            ax.text(xc, y + 0.425, res, ha="center", va="center", fontsize=11, fontweight="bold", color="#14532d" if ok else "#7f1d1d")
    ax.text(6.1, -0.3, "∀ basta un falso per essere falso; ∃ basta un vero per essere vero", ha="center", fontsize=9, color=GRIGIO)
    return _salva(fig, "fond/logica_quantificatori_dominio")


def regole_quantificatori():
    righe = [("∀x P(x)", "∴ P(d)  se d ∈ D", "istanziazione universale"),
             ("P(d)  per ogni d ∈ D", "∴ ∀x P(x)", "generalizzazione universale"),
             ("∃x P(x)", "∴ P(d)  per qualche d ∈ D", "istanziazione esistenziale"),
             ("P(d)  per qualche d ∈ D", "∴ ∃x P(x)", "generalizzazione esistenziale")]
    fig, ax = plt.subplots(figsize=(8.6, 4.0)); ax.axis("off"); ax.set_xlim(0, 8.6); ax.set_ylim(-0.5, 3.6)
    ax.text(2.2, 3.3, "regola", ha="center", fontsize=11, fontweight="bold", color=BLU)
    ax.text(6.4, 3.3, "nome", ha="center", fontsize=11, fontweight="bold", color=BLU)
    for i, (pre, con, nome) in enumerate(righe):
        y = 2.5 - i * 0.82
        ax.add_patch(Rectangle((0.1, y - 0.3), 8.4, 0.74, fc="#F3F6FB" if i % 2 == 0 else "white", ec="#cdd8ee", lw=1))
        ax.text(0.35, y + 0.2, pre, fontsize=11.5, va="center")
        ax.plot([0.3, 3.3], [y + 0.0, y + 0.0], color="black", lw=1)
        ax.text(0.35, y - 0.17, con, fontsize=11.5, va="center")
        ax.text(6.4, y + 0.04, nome, fontsize=11, ha="center", va="center", style="italic", color=BLU)
    return _salva(fig, "fond/logica_regole_quantificatori")


if __name__ == "__main__":
    for f in (connettivi, formula, demorgan, implicazione, contrapposta, bicondizionale, implicazione_disgiunzione, regole_inferenza, argomenti_tavole, quantificatori_dominio, regole_quantificatori):
        print(f())
