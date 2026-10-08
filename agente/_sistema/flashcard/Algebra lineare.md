## Campo
D: Quando un insieme con due operazioni (+ e ·) si dice campo?
R: Quando soddisfa le 9 proprietà: per la somma commutativa, associativa, elemento neutro 0, opposto; per il prodotto commutativa, associativa, elemento neutro 1, inverso (per a ≠ 0); più la distributiva a·(b+c) = a·b + a·c.

## Campo
D: Quali tra ℕ, ℤ, ℚ, ℝ, ℂ sono campi? Perché gli altri no?
R: ℚ, ℝ, ℂ sono campi.
- ℕ non lo è: mancano opposti e inversi.
- ℤ non lo è: ci sono gli opposti ma mancano gli inversi (1/2 ∉ ℤ).

## Numeri reali
D: Come si definisce formalmente un numero reale?
R: Come classe di equivalenza di successioni di Cauchy di numeri razionali (successioni che si avvicinano sempre di più). Due successioni sono equivalenti se rappresentano lo stesso numero finale.

## Numeri reali
D: Perché √2 ∉ ℚ è importante?
R: Mostra che i razionali lasciano "buchi" sulla retta numerica (la diagonale del quadrato di lato 1 misura √2). I reali servono a tappare questi buchi.

## Numeri complessi
D: Che cos'è un numero complesso e qual è l'unica regola nuova per calcolare?
R: z = a + bi con a, b ∈ ℝ. L'unica regola nuova è i² = −1.

## Numeri complessi
D: Come si calcolano somma e prodotto di (a + bi) e (c + di)?
R: - Somma: (a+c) + (b+d)i
- Prodotto: (ac − bd) + (ad + bc)i (si sviluppa e si sostituisce i² = −1)

## Numeri complessi
D: In z = 2 + 3i quanto valgono Re(z) e Im(z)? Qual è l'errore comune?
R: Re(z) = 2 e Im(z) = 3. L'errore è scrivere Im(z) = 3i: la parte immaginaria è un numero reale e non contiene i.

## Numeri complessi
D: ℂ è un insieme ordinato? Perché?
R: No. In un campo ordinato il quadrato di un elemento non nullo deve essere positivo, ma i² = −1: si avrebbe una contraddizione. Si possono confrontare solo uguaglianza e diversità.

## Coniugato e modulo
D: Definisci coniugato e modulo di z = a + bi, e dì quando z coincide col suo coniugato.
R: - Coniugato: z̄ = a − bi (riflessione rispetto all'asse reale).
- Modulo: |z| = √(a² + b²) ≥ 0.
- z = z̄ se e solo se Im(z) = 0, cioè z ∈ ℝ.

## Coniugato e modulo
D: Quanto vale z · z̄?
R: z · z̄ = a² + b² = |z|², sempre un reale non negativo.

## Inverso
D: Come si calcola l'inverso di z ≠ 0? Esempio con z = 2 + 5i.
R: z⁻¹ = z̄ / |z|². Per z = 2 + 5i: |z|² = 4 + 25 = 29, quindi z⁻¹ = (2 − 5i)/29 = 2/29 − (5/29)i.

## Piano complesso
D: Come si interpretano geometricamente somma, coniugio e modulo nel piano di Argand-Gauss?
R: - Somma: regola del parallelogramma.
- Coniugio: riflessione rispetto all'asse reale.
- Modulo: distanza dall'origine (Pitagora).

## Forma polare
D: Come si passa da coordinate polari (r, θ) alle cartesiane e viceversa?
R: a = r cos θ, b = r sen θ. Viceversa r = √(a² + b²), cos θ = a/r, sen θ = b/r. Attenzione al quadrante quando si usa arctan(b/a): se a < 0 si aggiunge π.

## Forma polare
D: Che cosa significa e^{iθ} e come si scrive z in forma polare?
R: e^{iθ} = cos θ + i sen θ. Ogni z ≠ 0 si scrive z = r e^{iθ}, con r = |z| e θ = Arg(z). I punti e^{iθ} sono quelli della circonferenza unitaria.

## Forma polare
D: Quanto valgono e^{iπ} e e^{2πi}? Qual è l'identità di Eulero?
R: e^{iπ} = −1, e^{2πi} = 1. Identità di Eulero: e^{iπ} + 1 = 0.

## Forma polare
D: Quando due scritture r₁e^{iθ₁} e r₂e^{iθ₂} rappresentano lo stesso numero?
R: Se e solo se r₁ = r₂ e θ₂ = θ₁ + 2kπ per qualche k ∈ ℤ (l'argomento è definito a meno di giri completi).

## Prodotto in forma polare
D: Come si moltiplicano due numeri complessi in forma polare e qual è il significato geometrico?
R: z₁z₂ = r₁r₂ e^{i(θ₁+θ₂)}: i moduli si moltiplicano e gli argomenti si sommano. Geometricamente è una rotazione di θ₂ combinata con un riscalamento di fattore r₂.

## Inverso e coniugio polari
D: Come si scrivono coniugato e inverso di z = r e^{iθ}?
R: z̄ = r e^{−iθ}; z⁻¹ = (1/r) e^{−iθ} (modulo inverso, argomento opposto).

## Potenze
D: Quanto vale zⁿ per z = r e^{iθ}? Calcola (1 + i)²⁰⁰⁰.
R: zⁿ = rⁿ e^{inθ} (formula di De Moivre). Poiché 1 + i = √2 e^{iπ/4}: (1+i)²⁰⁰⁰ = 2¹⁰⁰⁰ e^{i·500π} = 2¹⁰⁰⁰.

## Radici n-esime
D: Quante sono le radici n-esime di z₀ ≠ 0 e come si calcolano?
R: Sono esattamente n e distinte: w_k = ⁿ√r₀ · e^{i(θ₀/n + 2kπ/n)} per k = 0, 1, …, n−1. Stanno sui vertici di un poligono regolare di n lati centrato nell'origine.

## Radici n-esime
D: Calcola le radici terze di 8.
R: r₀ = 8, θ₀ = 0 → modulo 2, angoli 0, 2π/3, 4π/3.
- w₀ = 2
- w₁ = −1 + i√3
- w₂ = −1 − i√3
