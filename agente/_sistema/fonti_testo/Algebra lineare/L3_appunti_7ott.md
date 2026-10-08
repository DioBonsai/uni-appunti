# Algebra lineare, lezione 3 (7 ottobre 2026): appunti a mano (iPad)
(trascrizione dell'appunto manoscritto; fonte: L3_appunti_7ott.pdf, 2 pagine)

## Coordinate polari
P(a,b) coordinate cartesiane. r = lunghezza di OP; θ (theta) = angolo tra asse x e OP; (r, θ) = coordinate polari.
Dati (r, θ): a = r·cos(θ), b = r·sen(θ) (★) → (a, b).
Cosa sono seno e coseno? Circonferenza di raggio 1: punto P, seno(θ) = ordinata, coseno(θ) = ascissa.
r = |z| modulo (norma) di z; θ = Arg(z) argomento di z.
Usando (★): z = r·cos(θ) + i·r·sen(θ) = r·(cos(θ) + i·sen(θ)) = **r·e^{iθ}**.

**Prop.** e^{i(θ₁+θ₂)} = e^{iθ₁}·e^{iθ₂}.
Dim.: e^{iθ₁}·e^{iθ₂} = (cos θ₁ + i sen θ₁)(cos θ₂ + i sen θ₂) = cos θ₁ cos θ₂ + i cos θ₁ sen θ₂ + i sen θ₁ cos θ₂ − sen θ₁ sen θ₂ = (cos θ₁ cos θ₂ − sen θ₁ sen θ₂) + i(cos θ₁ sen θ₂ + sen θ₁ cos θ₂) = cos(θ₁+θ₂) + i sen(θ₁+θ₂) = e^{i(θ₁+θ₂)}.
Se z ∈ ℂ ha coordinate polari (r, θ) allora z = r·e^{iθ}: **rappresentazione polare** di z.

Es. 1. Trovare rapp. polare di −5 ∈ ℂ: r = 5, θ = π → −5 = 5·e^{iπ}. Similmente −1 = e^{iπ} (e^{iπ} = cos π + i sen π = −1) → e^{iπ} + 1 = 0.
Es. 2. Scrivere z = 2·e^{iπ/4} in forma cartesiana = 2(cos π/4 + i sen π/4) = 2(1/√2 + i·1/√2) = 2/√2 + i·2/√2 = √2 + i√2.

## Moltiplicazione
z₁ = r₁e^{iθ₁}, z₂ = r₂e^{iθ₂}: z₁·z₂ = r₁e^{iθ₁}·r₂e^{iθ₂} = (r₁r₂)e^{i(θ₁+θ₂)}
⇒ |z₁z₂| = r₁·r₂ = |z₁|·|z₂|; ⇒ Arg(z₁z₂) = θ₁ + θ₂ = Arg(z₁) + Arg(z₂).
**Significato geometrico**: moltiplicare z₁·z₂ equivale a ruotare z₁ dell'angolo θ₂ e riscalarne la lunghezza del fattore r₂.
Es.: (1+i)·(1+i) = (√2·e^{iπ/4})² = 2e^{iπ/2} = 2i.

## Inverso
z = r·e^{iθ} → z⁻¹ = z̄/|z|² = r·e^{−iθ}/r² = (1/r)·e^{−iθ}; z̄ = r·e^{−iθ}.

## Potenze
z = r·e^{iθ}: zⁿ = (r·e^{iθ})ⁿ = rⁿ·e^{iθ}···e^{iθ} (n volte) = rⁿ·e^{inθ}
⇒ |zⁿ| = rⁿ = |z|ⁿ; Arg(zⁿ) = n·θ = n·Arg(z).
es. (1+i)²⁰⁰⁰ = (√2·e^{iπ/4})²⁰⁰⁰ = (√2)²⁰⁰⁰·e^{i·2000π/4} = 2¹⁰⁰⁰·e^{i·500π}.

⚠ In coordinate polari (r₁,θ₁) = P = (r₂,θ₂): r₁ = r₂ → θ₁ = θ₂ + k·2π.
Se z = r₁e^{iθ₁} = r₂e^{iθ₂} allora r₁ = r₂ = |z| e θ₂ = θ₁ + 2kπ, k ∈ ℤ.

## Radici
Dato z ∈ ℂ, diciamo che w ∈ ℂ è UNA radice n-esima di z se **wⁿ = z**. Si ottengono esattamente n radici distinte per k = 0, 1, …, n−1.
Dato z = r·e^{iθ}, quanto valgono le radici n-esime? Dobbiamo trovare w = r'·e^{iθ'} t.c. wⁿ = z: (r')ⁿ·e^{inθ'} = wⁿ = z = r·e^{iθ}.
(r')ⁿ = r → r' = ⁿ√r. n·θ' = θ + 2πk, k ∈ ℤ → θ' = θ/n + (2π/n)·k = θ'_k ⇒ **w_k = ⁿ√r · e^{i(θ/n + 2πk/n)}**.
Es. Calcolare le radici terze (n=3) di z = 8: w₀ = 2e^{i·0} = 2; w₁ = 2e^{i·2π/3} = −1 + i√3; w₂ = 2e^{i·4π/3} = −1 − i√3. (disegno: w₀ = 2 sull'asse reale, 8 più a destra)
