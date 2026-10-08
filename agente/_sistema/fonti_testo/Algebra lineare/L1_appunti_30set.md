# Algebra lineare, lezione 1 (30 settembre 2026): appunti a mano di Emanuele
(trascrizione dell'appunto manoscritto; fonte: L1_appunti_30set.pdf)

## Oggetti fondamentali
- **Vettore**: elemento di uno spazio vettoriale. Spazio vettoriale: insieme in cui 2 elementi possono essere sommati e moltiplicati per un numero.
- **Mappa lineare**: funzioni tra spazi vettoriali.
- L'algebra lineare è fondamentale in informatica: la manipolazione dell'input per ottenere l'output è composta probabilmente da mappe lineari.

## Segnali
Segnale sporco → (ripulito, tramite una mappa lineare) → segnale pulito.

## Insiemi numerici
- ℕ = numeri naturali = {0, 1, 2, …}
- ℤ = numeri interi = ℕ ∪ {−1, −2, …}
- ℚ = numeri razionali = { a/b | a, b ∈ ℤ, b ≠ 0 }
- ℝ = numeri reali: classi di equivalenza di successioni di Cauchy di numeri razionali.
- Rappresentazione sulla retta reale: √2 ∉ ℚ (diagonale del quadrato di lato 1).
- Esempio: π = 3,1 (a₁), 3,14 (a₂), 3,141 (a₃), 3,1415 (a₄), … sono successioni di Cauchy (successioni di numeri che si avvicinano sempre di più). Sono possibili più successioni per arrivare al numero finale → sono allora definite *equivalenti*.
- Esempi di potenze: 2³ = 2·2·2 = 8; 2⁻³ = 1/2³ = 1/8; 2^(3/5) = ⁵√(2³); 2^π = 2^3,1, 2^3,14, 2^3,141, …

## Operazioni in ℝ
a, b ∈ ℝ: a + b somma, a · b prodotto.
**Definizione**: un insieme dotato di operazioni + e · che soddisfano le 9 proprietà è detto **campo**.

## Proprietà di + e ·
1. (+) commutativa: ∀a,b ∈ ℝ, a+b = b+a
2. (+) associativa: (a+b)+c = a+(b+c)
3. (+) ∃ 0 ∈ ℝ tale che ∀a, a+0 = a
4. (+) ∀a ∃ −a tale che a+(−a) = 0
5. (·) commutativa: a·b = b·a
6. (·) associativa: (a·b)·c = a·(b·c)
7. (·) ∃ 1 ∈ ℝ tale che ∀a, a·1 = a
8. (·) ∀a ≠ 0 ∃ a⁻¹ tale che a·a⁻¹ = 1
9. (+ e ·) distributiva: a·(b+c) = a·b + a·c
