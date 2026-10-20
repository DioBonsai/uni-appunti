"""Figure dei capitoli sui cicli (Programmazione cap. 20-22) e del Laboratorio 3 (cap. 10).
Genera i PNG in _sistema/figure/prog/ e figure/lab/.  Uso: python figure_cicli.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_info import vuoto, box, freccia, fl_box, stati_variabili, CH, BLU, ROSSO, VERDE, GRIGIO, plt, _salva
from matplotlib.patches import Polygon


def linea(ax, xs, ys, col="#333", lw=1.5):
    ax.plot(xs, ys, color=col, lw=lw, zorder=1)


def flow_while():
    """while (i < 10) { print(i); i++; } come diagramma di flusso."""
    fig, ax = vuoto(4.8, 5.6, (-3.2, 3.4), (-6.6, 1.0))
    fl_box(ax, 0, 0.4, 1.6, 0.6, "inizio", "term")
    fl_box(ax, 0, -1.0, 2.0, 0.7, "i ← 0")
    fl_box(ax, 0, -2.7, 2.2, 1.2, "i < 10 ?", "dec")
    fl_box(ax, 0, -4.2, 2.0, 0.7, "print(i)")
    fl_box(ax, 0, -5.4, 2.0, 0.7, "i ← i + 1")
    fl_box(ax, 2.6, -2.7, 1.4, 0.6, "fine", "term")
    freccia(ax, (0, 0.1), (0, -0.65)); freccia(ax, (0, -1.35), (0, -2.1)); freccia(ax, (0, -3.3), (0, -3.85)); freccia(ax, (0, -4.55), (0, -5.05))
    linea(ax, [-1.0, -2.0, -2.0], [-5.4, -5.4, -2.7]); freccia(ax, (-2.0, -2.7), (-1.15, -2.7))
    freccia(ax, (1.1, -2.7), (1.9, -2.7))
    ax.text(0.12, -3.45, "sì", color=VERDE, fontsize=10); ax.text(1.2, -2.45, "no", color=ROSSO, fontsize=10)
    ax.text(-3.1, -1.0, "inizializzazione", fontsize=8.5, color=BLU, ha="left", va="center")
    ax.text(-3.1, -3.3, "condizione", fontsize=8.5, color=BLU, ha="left", va="center")
    ax.text(-3.1, -6.1, "aggiornamento", fontsize=8.5, color=BLU, ha="left", va="center")
    return _salva(fig, "prog/ch20_flow_while")


def scope_stack():
    nomi = ["x", "y"]
    cols = [("inizio", [1, "—"]), ("1° giro: entra", [1, 2]), ("x++", [2, 2]), ("esce", [2, "—"]),
            ("2° giro: entra", [2, 4]), ("x++", [3, 4]), ("esce: fine", [3, "—"])]
    return stati_variabili("prog/ch20_scope_stack", "while (x < 3) { int y = x * 2; ... x++; }  (in rosso le celle che cambiano)", nomi, cols, 9.4)


def griglia():
    fig, ax = vuoto(4.6, 4.4, (-1.6, 6.2), (-4.0, 1.6))
    n = 1
    for r in range(3):
        for c in range(3):
            box(ax, c * 1.9 + 0.0, -r * 1.5, 1.7, 1.2, f"({r},{c})", fs=11, fc="#fbeed3" if r % 2 == 0 else CH, style="square,pad=0")
            ax.text(c * 1.9 + 0.12, -r * 1.5 + 1.08, str(n), fontsize=8.5, color=ROSSO, ha="left", va="top", fontweight="bold")
            n += 1
    for r in range(3):
        ax.text(-0.25, -r * 1.5 + 0.6, f"r = {r}", ha="right", va="center", fontsize=10, color=BLU)
    for c in range(3):
        ax.text(c * 1.9 + 0.85, 1.55, f"c = {c}", ha="center", va="bottom", fontsize=10, color=BLU)
    ax.text(2.7, -3.5, "i numeri rossi mostrano l'ordine di stampa", ha="center", fontsize=9, color=GRIGIO)
    return _salva(fig, "prog/ch21_griglia")


def while_dowhile():
    fig, axs = plt.subplots(1, 2, figsize=(8.0, 3.8)); [a.set_aspect("equal") or a.axis("off") for a in axs]
    ax = axs[0]; ax.set_xlim(-2.6, 3.0); ax.set_ylim(-4.6, 1.0); ax.set_title("while: prima si controlla", fontsize=11)
    fl_box(ax, 0, 0, 2.2, 1.2, "condizione?", "dec", 9); fl_box(ax, 0, -2.2, 1.8, 0.8, "blocco")
    freccia(ax, (0, -0.6), (0, -1.8)); ax.text(0.15, -1.2, "sì", color=VERDE, fontsize=10)
    linea(ax, [-0.9, -1.9, -1.9], [-2.2, -2.2, 0]); freccia(ax, (-1.9, 0), (-1.12, 0))
    freccia(ax, (1.1, 0), (2.4, 0)); ax.text(1.35, 0.15, "no", color=ROSSO, fontsize=10); ax.text(2.45, 0, "fine", fontsize=9, va="center")
    ax = axs[1]; ax.set_xlim(-2.6, 3.0); ax.set_ylim(-4.6, 1.0); ax.set_title("do-while: prima si esegue", fontsize=11)
    fl_box(ax, 0, 0, 1.8, 0.8, "blocco"); fl_box(ax, 0, -2.2, 2.2, 1.2, "condizione?", "dec", 9)
    freccia(ax, (0, -0.4), (0, -1.6))
    linea(ax, [-1.1, -1.9, -1.9], [-2.2, -2.2, 0]); freccia(ax, (-1.9, 0), (-0.92, 0)); ax.text(-1.8, -2.0, "sì", color=VERDE, fontsize=10)
    freccia(ax, (1.1, -2.2), (2.4, -2.2)); ax.text(1.35, -2.05, "no", color=ROSSO, fontsize=10); ax.text(2.45, -2.2, "fine", fontsize=9, va="center")
    fig.subplots_adjust(wspace=0.05)
    return _salva(fig, "prog/ch22_while_dowhile")


def flow_equazione():
    """Flusso di risoluzione di ax^2 + bx + c = 0 (schema delle slide del Lab03)."""
    fig, ax = vuoto(8.2, 5.4, (-4.2, 8.6), (-7.0, 1.4))
    fl_box(ax, 0, 0, 2.0, 1.1, "a = 0 ?", "dec")
    fl_box(ax, -1.6, -2.1, 2.0, 1.1, "b = 0 ?", "dec")
    fl_box(ax, -2.8, -4.4, 2.0, 1.1, "c = 0 ?", "dec")
    box(ax, 1.4, -0.45, 3.9, 0.9, "", fc="#f6c6c0", style="round,pad=0.02,rounding_size=0.1")
    ax.text(3.35, 0, "δ = b² − 4ac     W = 2a\nW₁ = −b / W     W₂ = √|δ| / W", ha="center", va="center", fontsize=9)
    ax.text(-1.2, -3.1, "x₁ = −c / b", fontsize=9.5, ha="left")
    ax.text(-3.3, -6.0, "indeterminata", fontsize=9.5, ha="center", color=BLU)
    ax.text(-0.3, -6.0, "impossibile", fontsize=9.5, ha="center", color=BLU)
    fl_box(ax, 3.35, -2.0, 2.0, 1.1, "δ = 0 ?", "dec")
    ax.text(2.2, -3.45, va="top", s="una radice:\nx₁ = W₁", fontsize=9.5, ha="center", color=BLU)
    fl_box(ax, 5.8, -3.8, 2.0, 1.1, "δ < 0 ?", "dec")
    ax.text(4.6, -5.3, va="top", s="radici complesse\nconiugate", fontsize=9.5, ha="center", color=BLU)
    ax.text(7.4, -5.3, va="top", s="radici reali\nx₁ = W₁ + W₂\nx₂ = W₁ − W₂", fontsize=9.5, ha="center", color=BLU)
    freccia(ax, (-1.9, 0), (-1.05, 0))
    freccia(ax, (1.05, 0), (1.4, 0), ROSSO); ax.text(1.12, 0.12, "no", color=ROSSO, fontsize=9)
    freccia(ax, (-0.5, -0.5), (-1.3, -1.5), VERDE); ax.text(-1.2, -0.8, "sì", color=VERDE, fontsize=9)
    freccia(ax, (-1.1, -2.5), (-1.0, -2.9), ROSSO)
    freccia(ax, (-2.2, -2.6), (-2.6, -3.8), VERDE)
    freccia(ax, (-3.2, -4.8), (-3.2, -5.6), VERDE); ax.text(-3.0, -5.3, "sì", color=VERDE, fontsize=9)
    freccia(ax, (-2.4, -4.8), (-0.5, -5.6), ROSSO); ax.text(-1.7, -5.0, "no", color=ROSSO, fontsize=9)
    freccia(ax, (3.35, -0.5), (3.35, -1.4))
    freccia(ax, (2.9, -2.4), (2.4, -3.0), VERDE); ax.text(2.4, -2.7, "sì", color=VERDE, fontsize=9)
    freccia(ax, (3.9, -2.4), (5.3, -3.3), ROSSO); ax.text(4.8, -2.7, "no", color=ROSSO, fontsize=9)
    freccia(ax, (5.3, -4.2), (4.7, -4.95), VERDE); ax.text(4.9, -4.5, "sì", color=VERDE, fontsize=9)
    freccia(ax, (6.4, -4.2), (7.3, -4.95), ROSSO); ax.text(7.0, -4.5, "no", color=ROSSO, fontsize=9)
    return _salva(fig, "lab/ch10_flow_equazione")


def tutte():
    for f in (flow_while, scope_stack, griglia, while_dowhile, flow_equazione):
        print(f.__name__, "->", f())


if __name__ == "__main__":
    tutte()
