"""Generatore di esercizi di Matematica discreta nello stile degli esami UniTo.
Ogni risposta e' calcolata e verificata con SymPy/Python (nessun valore "a memoria").

Uso:
    python genera_esercizi.py quiz [--n 10] [--seed 1]      # quiz a 5 risposte
    python genera_esercizi.py problema [--seed 1]            # problema permutazioni con punti a/b/c
    python genera_esercizi.py test                           # autotest: riproduce soluzioni degli esami veri

Scrive due file in _sistema/esami/generati/: `<nome>.md` (testo da mostrare) e `<nome>.json`
(risposte e spiegazioni: NON mostrarlo finche' lo studente non ha risposto).
"""
import argparse
import json
import math
import random
import sys
from datetime import datetime
from pathlib import Path

from sympy import binomial, factorial, totient
from sympy.combinatorics import Permutation

OUT = Path(__file__).resolve().parent.parent / "esami" / "generati"


# ---------------------------------------------------------------- permutazioni
def prod_cicli(cycles, n):
    """Prodotto di cicli come nei testi UniTo: il ciclo piu' a destra agisce per primo.
    In SymPy p*q significa 'prima p, poi q', quindi si scorre la lista da destra a sinistra."""
    res = Permutation(list(range(n)))
    for cyc in reversed(cycles):
        res = res * Permutation([[x - 1 for x in cyc]], size=n)
    return res


def n_stesso_tipo(tipo, n):
    """Numero di permutazioni di S_n con il tipo dato (i punti fissi sono cicli di lunghezza 1)."""
    full = list(tipo) + [1] * (n - sum(tipo))
    return int(factorial(n) / math.prod((l ** full.count(l)) * math.factorial(full.count(l)) for l in set(full)))


def cycles_text(p: Permutation) -> str:
    cs = [c for c in p.full_cyclic_form if len(c) > 1]
    return "".join("(" + " ".join(str(x + 1) for x in c) + ")" for c in cs) or "id"


def perm_type(p: Permutation):
    return tuple(sorted((len(c) for c in p.full_cyclic_form if len(c) > 1), reverse=True))


def parity(p: Permutation) -> str:
    return "pari" if p.is_even else "dispari"


# ---------------------------------------------------------------- quiz
def opts(rnd, correct, wrong_pool, k=5):
    wrong = [w for w in dict.fromkeys(wrong_pool) if w != correct]
    rnd.shuffle(wrong)
    choices = wrong[: k - 1] + [correct]
    rnd.shuffle(choices)
    return choices, choices.index(correct) + 1


def q_generatore(rnd):
    N_pool = [n for n in range(20, 90)]
    k = rnd.choice([6, 8, 10, 12, 14, 15, 18])
    good = [n for n in N_pool if math.gcd(k, n) == 1]
    bad = [n for n in N_pool if math.gcd(k, n) != 1]
    correct = rnd.choice(bad)
    wrong = rnd.sample(good, 4)
    ch, ans = opts(rnd, f"N = {correct}", [f"N = {w}" for w in wrong])
    return dict(t="Z_N-additivo, generatori",
                testo=f"Per quale dei seguenti valori del modulo N la classe [{k}]_N NON è un generatore del gruppo additivo (Z_N, +)?",
                scelte=ch, risposta=ans,
                spiegazione=f"[{k}]_N genera Z_N se e solo se MCD({k}, N) = 1. Per N = {correct} si ha MCD = {math.gcd(k, correct)} ≠ 1.")


def q_phi(rnd):
    n = rnd.choice([n for n in range(30, 130) if n % 2 == 0 or n % 3 == 0])
    c = int(totient(n))
    wrong = {c + d for d in (-6, -4, -2, 2, 4, 6, 8, n - c)} - {c, 0}
    ch, ans = opts(rnd, str(c), [str(w) for w in wrong if w > 0])
    return dict(t="Z_N-moltiplicativo",
                testo=f"Il numero degli elementi del gruppo moltiplicativo (Z_{n}^*, ·) è:",
                scelte=ch, risposta=ans,
                spiegazione=f"|Z_N^*| = φ(N) = numero di classi con MCD(a, N) = 1. Qui φ({n}) = {c}.")


def q_conteggio(rnd):
    n = rnd.randint(8, 14)
    k = rnd.randint(2, 4)
    c = int(binomial(n, k))
    pool = [f"C({n},{k}) = {c}", f"{n}!/{n - k}!", f"{n}^{k}", f"{k}!·{n - k}!", f"C({n + 1},{k})", f"{n}!/{k}!"]
    ch, ans = opts(rnd, f"C({n},{k}) = {c}", pool)
    return dict(t="combinatoria, coefficienti-binomiali",
                testo=f"Le {n} caselle di una riga devono essere colorate di rosso o di blu in modo che ci siano esattamente {k} caselle rosse. Quanti sono i modi di farlo?",
                scelte=ch, risposta=ans,
                spiegazione=f"Basta scegliere quali {k} caselle sono rosse (l'ordine non conta): C({n},{k}) = {c}.")


def q_base2(rnd):
    n = rnd.randint(40, 250)
    b = bin(n)[2:]
    wrong = {bin(n + d)[2:] for d in (-9, -5, -3, 3, 6, 11)}
    ch, ans = opts(rnd, b, list(wrong))
    return dict(t="base-2",
                testo=f"Quale delle seguenti è la scrittura di {n} in base 2?",
                scelte=ch, risposta=ans,
                spiegazione=f"Divisioni successive per 2 e resti letti al contrario: {n} = ({b})_2.")


def q_periodo(rnd):
    n = rnd.randint(7, 10)
    while True:
        lens = sorted(rnd.sample(range(2, 6), rnd.choice([2, 2, 3])), reverse=True)
        if sum(lens) <= n:
            break
    elems = rnd.sample(range(1, n + 1), sum(lens))
    cyc, i = [], 0
    for l in lens:
        cyc.append(elems[i:i + l]); i += l
    text = "".join("(" + " ".join(map(str, c)) + ")" for c in cyc)
    p = Permutation([[x - 1 for x in c] for c in cyc], size=n)
    per = p.order()
    wrong = {per + d for d in (-2, -1, 1, 2, 3, sum(lens))} - {per, 0}
    ch, ans = opts(rnd, str(per), [str(w) for w in wrong])
    return dict(t="permutazioni, cicli-tipo-periodo",
                testo=f"In S_{n} la permutazione σ = {text} (cicli disgiunti) ha periodo:",
                scelte=ch, risposta=ans,
                spiegazione=f"Il periodo è il minimo comune multiplo delle lunghezze dei cicli {tuple(lens)}: {per}.")


def q_parita(rnd):
    n = rnd.randint(7, 10)
    while True:
        lens = sorted(rnd.sample(range(2, 6), rnd.choice([2, 3])), reverse=True)
        if sum(lens) <= n:
            break
    elems = rnd.sample(range(1, n + 1), sum(lens))
    cyc, i = [], 0
    for l in lens:
        cyc.append(elems[i:i + l]); i += l
    text = "".join("(" + " ".join(map(str, c)) + ")" for c in cyc)
    p = Permutation([[x - 1 for x in c] for c in cyc], size=n)
    corr = parity(p)
    ch = ["pari", "dispari", "né pari né dispari", "dipende dalla scelta dei numeri", "è l'identità"]
    return dict(t="parita",
                testo=f"In S_{n} la permutazione σ = {text} (cicli disgiunti) è:",
                scelte=ch, risposta=ch.index(corr) + 1,
                spiegazione=f"Un ciclo di lunghezza l è pari se l è dispari. Lunghezze {tuple(lens)} → {sum(1 for l in lens if l % 2 == 0)} cicli pari di lunghezza pari → σ è {corr}.")


def q_inverso(rnd):
    N = rnd.choice([n for n in range(15, 60)])
    a = rnd.choice([x for x in range(2, N) if math.gcd(x, N) == 1])
    inv = pow(a, -1, N)
    wrong = {(inv + d) % N for d in (1, 2, 3, -1, -2, 5)} - {inv, 0}
    ch, ans = opts(rnd, f"[{inv}]", [f"[{w}]" for w in wrong])
    return dict(t="Z_N-moltiplicativo, MCD-euclide",
                testo=f"Qual è l'inverso della classe [{a}] nel gruppo moltiplicativo (Z_{N}^*, ·)?",
                scelte=ch, risposta=ans,
                spiegazione=f"Si cerca x con {a}·x ≡ 1 (mod {N}) (algoritmo di Euclide esteso): x = {inv}, infatti {a}·{inv} = {a * inv} = {(a * inv) // N}·{N} + 1.")


def q_parti(rnd):
    n = rnd.randint(4, 9)
    c = 2 ** n
    ch, ans = opts(rnd, str(c), [str(x) for x in (n * n, 2 * n, math.factorial(n), n + 2, 2 ** (n - 1), 2 ** n - 1, 2 ** (n + 1))])
    return dict(t="insiemi, induzione",
                testo=f"Quanti sottoinsiemi ha (in totale, compresi ∅ e A stesso) un insieme A con {n} elementi?",
                scelte=ch, risposta=ans,
                spiegazione=f"|P(A)| = 2^n = 2^{n} = {c}.")


QUIZ_TYPES = [q_generatore, q_phi, q_conteggio, q_base2, q_periodo, q_parita, q_inverso, q_parti]


def make_quiz(n, seed):
    rnd = random.Random(seed)
    fns = [QUIZ_TYPES[i % len(QUIZ_TYPES)] for i in range(n)]
    rnd.shuffle(fns)
    return [dict(f(rnd), n=i + 1) for i, f in enumerate(fns)]


# ---------------------------------------------------------------- problema
def make_problem(seed):
    rnd = random.Random(seed)
    n = 9
    while True:
        lens = sorted(rnd.sample(range(2, 6), 2), reverse=True)
        if sum(lens) <= n:
            break
    elems = rnd.sample(range(1, n + 1), sum(lens))
    c1, c2 = elems[:lens[0]], elems[lens[0]:]
    sigma = Permutation([[x - 1 for x in c1], [x - 1 for x in c2]], size=n)
    tipo = perm_type(sigma)
    per = sigma.order()
    k = rnd.choice([m for m in range(2, 6) if m < per] or [2])
    sk = sigma ** k
    stesso_tipo = n_stesso_tipo(tipo, n)
    testo = (f"In S_{n} si consideri la permutazione σ = {cycles_text(sigma)}.\n"
             f"a) (Punti 4) Calcolare il tipo, il periodo e la parità di σ, e scrivere σ^{k} come prodotto di cicli disgiunti.\n"
             f"b) (Punti 3) Calcolare quante sono le permutazioni di S_{n} che hanno lo stesso tipo di σ (non è necessario calcolare i fattoriali).\n"
             f"c) (Punti 4) Sia H = ⟨σ⟩ il sottogruppo ciclico generato da σ. Quanti elementi ha H? H contiene σ^{k}?")
    sol = {
        "a": f"σ = {cycles_text(sigma)} ha tipo {tipo}, periodo mcm{tipo} = {per}, è {parity(sigma)}. σ^{k} = {cycles_text(sk)}.",
        "b": f"Le permutazioni di S_{n} con lo stesso tipo (cicli di lunghezza {tipo}, {n - sum(tipo)} punti fissi) sono {n}!/Π(l^m·m!) = {stesso_tipo}.",
        "c": f"|H| = periodo di σ = {per}; sì, σ^{k} ∈ H perché è una potenza di σ.",
    }
    return dict(testo=testo, soluzione=sol)


# ---------------------------------------------------------------- autotest sugli esami veri
def selftest():
    ok = True
    # Esame 13/1/2026, problema 1: σ = (1 2)(5 9 4)(4 2 7)(9 5 6 2 3) → (1 2 3 4)(5 6 7), tipo (4,3), periodo 12, 15120 permutazioni
    sigma = prod_cicli([[1, 2], [5, 9, 4], [4, 2, 7], [9, 5, 6, 2, 3]], 9)
    got = cycles_text(sigma)
    print("Esame 13/1/2026: σ =", got, "| atteso (1 2 3 4)(5 6 7)")
    ok &= got == "(1 2 3 4)(5 6 7)"
    tipo = perm_type(sigma)
    n_tipo = n_stesso_tipo(tipo, 9)
    print("tipo", tipo, "(atteso (4, 3)) | periodo", sigma.order(), "(atteso 12) | stesso tipo", n_tipo, "(atteso 15120)")
    ok &= tipo == (4, 3) and sigma.order() == 12 and n_tipo == 15120
    # Esame 14/1/2025, problema 1: σ = (1 3)(2 4 3)(3 5 1) → (1 2 4)(3 5), tipo (3,2), periodo 6, dispari
    s2 = prod_cicli([[1, 3], [2, 4, 3], [3, 5, 1]], 6)
    print("Esame 14/1/2025: σ =", cycles_text(s2), "| atteso (1 2 4)(3 5), periodo 6, dispari ->", s2.order(), parity(s2))
    ok &= cycles_text(s2) == "(1 2 4)(3 5)" and s2.order() == 6 and parity(s2) == "dispari"
    print("AUTOTEST", "OK" if ok else "FALLITO")
    return ok


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["quiz", "problema", "test"])
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--seed", type=int, default=int(datetime.now().strftime("%H%M%S")))
    a = ap.parse_args()
    if a.cmd == "test":
        sys.exit(0 if selftest() else 1)
    OUT.mkdir(parents=True, exist_ok=True)
    name = f"{a.cmd}_{datetime.now().strftime('%Y%m%d_%H%M%S')}_s{a.seed}"
    if a.cmd == "quiz":
        qs = make_quiz(a.n, a.seed)
        md = [f"# Quiz di Matematica discreta (seed {a.seed})\n"]
        for q in qs:
            md.append(f"**Domanda {q['n']}.** {q['testo']}")
            md += [f"{i}. {s}" for i, s in enumerate(q["scelte"], 1)]
            md.append("")
        (OUT / f"{name}.md").write_text("\n".join(md), encoding="utf-8")
        (OUT / f"{name}.json").write_text(json.dumps(qs, ensure_ascii=False, indent=1), encoding="utf-8")
    else:
        pr = make_problem(a.seed)
        (OUT / f"{name}.md").write_text(f"# Problema (seed {a.seed})\n\n{pr['testo']}\n", encoding="utf-8")
        (OUT / f"{name}.json").write_text(json.dumps(pr, ensure_ascii=False, indent=1), encoding="utf-8")
    print(OUT / f"{name}.md")


if __name__ == "__main__":
    main()
