"""Figura del capitolo 24 di Fondamenti: tavole di verità delle regole 3 e 4 (la riga del controesempio evidenziata).
PNG in _sistema/figure/fond/.  Uso: python figure_fond5.py
"""
import sys
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_math import BLU, ROSSO, VERDE, GRIGIO, plt, Rectangle, _salva


def _impl(a, b):
    return (not a) or b


def _tabella(ax, x0, y0, titolo, intest, righe, evid_riga, larghezze, col_prem, col_concl):
    ax.text(x0, y0 + 0.9, titolo, fontsize=10.5, fontweight="bold", color=BLU)
    cw = larghezze
    ch = 0.52
    x = x0
    for j, h in enumerate(intest):
        ax.add_patch(Rectangle((x, y0), cw[j], ch, fc="#E8EFFA", ec="#9aa7bd", lw=1))
        ax.text(x + cw[j] / 2, y0 + ch / 2, h, ha="center", va="center", fontsize=9.2)
        x += cw[j]
    for i, r in enumerate(righe):
        x = x0
        y = y0 - (i + 1) * ch
        for j, v in enumerate(r):
            if i == evid_riga:
                fc = "#FDE3DF"
            elif j in col_prem:
                fc = "white"
            else:
                fc = "white"
            ax.add_patch(Rectangle((x, y), cw[j], ch, fc=fc, ec="#9aa7bd", lw=1))
            col = "black"
            if i == evid_riga and j in (col_concl,):
                col = ROSSO
            ax.text(x + cw[j] / 2, y + ch / 2, "V" if v else "F", ha="center", va="center", fontsize=9.2, color=col,
                    fontweight="bold" if i == evid_riga else None)
            x += cw[j]


def regole_tavole():
    fig, ax = plt.subplots(figsize=(10.4, 5.0)); ax.axis("off"); ax.set_xlim(0, 15.6); ax.set_ylim(-5.5, 1.6)
    # regola 3: p→r, r→q ⊢ q
    r3 = []
    for p, r, q in product([True, False], repeat=3):
        r3.append((p, r, q, _impl(p, r), _impl(r, q), q))
    ev3 = next(i for i, x in enumerate(r3) if (not x[0]) and (not x[1]) and (not x[2]))
    _tabella(ax, 0.1, 0.0, "Regola 3:  p → r,  r → q  ⊢  q", ["p", "r", "q", "p → r", "r → q", "q"], r3, ev3, [0.8, 0.8, 0.8, 1.1, 1.1, 0.8], (3, 4), 5)
    # regola 4: ¬r→¬p, r ⊢ p
    r4 = []
    for p, r in product([True, False], repeat=2):
        r4.append((p, r, _impl(not r, not p), r, p))
    ev4 = next(i for i, x in enumerate(r4) if (not x[0]) and x[1])
    _tabella(ax, 7.9, 0.0, "Regola 4:  ¬r → ¬p,  r  ⊢  p", ["p", "r", "¬r → ¬p", "r", "p"], r4, ev4, [0.8, 0.8, 1.5, 0.8, 0.8], (2, 3), 4)
    ax.text(0.1, -5.15, "In rosso la riga del controesempio: le premesse sono vere e la conclusione è falsa.\nUna sola riga così basta a rendere la regola non valida.", fontsize=9.5, color=ROSSO)
    ax.text(7.9, -3.0, "Si guardano solo le righe con tutte le\npremesse vere (qui: p = V, r = V e p = F, r = V);\nnella seconda la conclusione p è falsa.", fontsize=9, color=GRIGIO)
    return _salva(fig, "fond/regole_tavole")


if __name__ == "__main__":
    print(regole_tavole())
