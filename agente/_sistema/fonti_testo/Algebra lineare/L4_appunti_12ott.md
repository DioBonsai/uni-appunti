# Appunti a mano, 12 ottobre (Algebra lineare, lezione 4: Polinomi) — trascrizione

## p.1
**Polinomi.**
Def: un **monomio** è un'espressione algebrica con una parte numerica (il coefficiente) ed una parte letterale (variabili) usando le operazioni +, −, · nella parte letterale.
es. monomi: 4x, −2xy², √5·x⁴. Non monomi: sin(x), x/y, √x.
Il **grado** di un monomio è la somma degli esponenti delle variabili.
Def: un **polinomio** è la somma di monomi. Il grado del polinomio è il massimo grado dei suoi monomi.
es. 4x − 2xy² + √5·x⁴ → polinomio di grado 4.
In questo caso ci interessano principalmente polinomi con **una** variabile x. Scriviamo P(x) per il polinomio. Possiamo sempre scrivere P(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + … + a₁x + a₀ con aₙ ≠ 0 (tranne per P(x) ≡ 0). Un tale P(x) ha grado n.
Def: ℝ[x] è l'insieme di tutti i polinomi con variabile x e coefficienti in ℝ. Simile ℂ[x]. ℝₖ[x] è l'insieme di tutti i p(x) ∈ ℝ[x] con grado ≤ k.
Notiamo: se p(x), q(x) ∈ ℝₖ[x] ⟹ p(x) + q(x) ∈ [ℝₖ[x], incompleto].

**Divisione con resto fra polinomi.**
Se p(x), d(x) sono due polinomi allora esistono (e sono unici) due polinomi q(x) (quoziente) e r(x) (resto) tali che p(x) = d(x)·q(x) + r(x) con grado r(x) < grado d(x). (p = dividendo, d = divisore.)
es. p(x) = x⁴ − 2x³ + 2x² + x − 1, d(x) = x² − 1. Divisione in colonna: (x⁴ − 2x³ + 2x² + x − 1) : (x² − 1) = x² … resto: −x + 2.
Se il resto è 0 diciamo che d(x) divide p(x) e scriviamo d(x) | p(x).

**Radici di un polinomio.**
Se p(x) è un polinomio e a è un numero (in ℝ o in ℂ) denotiamo con p(a) il numero che otteniamo sostituendo x con a.
Def: a è una radice di p(x) ⟺ p(a) = 0.
**Proposizione.** a è una radice di p(x) ⟺ (x − a) | p(x) (⟺ p(x) = (x − a)q(x)).

## p.2
Dim: facciamo la divisione con resto: esistono q(x) e r(x) tali che p(x) = (x − a)q(x) + r(x). Sappiamo che grado r(x) < grado (x − a) = 1, quindi grado r = 0 (r = r₀ costante).
a è radice di p ⟺ p(a) = 0 ⟺ r₀ = 0 ⟺ (x − a) | p(x).

Def: la **molteplicità** di una radice a è il massimo numero k ∈ ℕ tale che (x − a)ᵏ | p(x) (k ≥ 1).
es. p(x) = x³ − 1 ∈ ℝ₃[x]; a = 1 è una radice di p(x) [perché p(1) = 1³ − 1 = 0]; (x − 1) | p(x) (per la prop.).
[Foto esempio] x³ − 1 = (x − 1)(x² + x + 1), dove q(x) = x² + x + 1. a = 1 non è radice di q(x) [perché q(1) = 1 + 1 + 1 = 3 ≠ 0], allora (x − 1) ∤ q(x) ⟹ la molteplicità è 1.
es. 2: p(x) = x³ − 2x² + x; a = 1 è una radice [perché p(1) = 1³ − 2·1² + 1 = 0]; (x − 1) | p(x). [altri esempi: non svolti negli appunti]

**Prop.** Un polinomio di grado n ≥ 1 ha al massimo n radici contate con molteplicità.
Dim: induzione sul grado n ∈ ℕ: 1) vale per n = 1; 2) se vale per un n ∈ ℕ allora vale anche per n + 1.
- n = 1: se p(x) è un polinomio di grado 1, allora p(x) = ax + b (per qualche a, b); ax + b = 0 ⟺ ax = −b ⟺ x = −b/a è la radice.
- Assumere che la proposizione valga per qualche n ∈ ℕ e dimostriamo che vale anche per n + 1. Sia p(x) un polinomio di grado n + 1.
  - possibilità 1: p non ha radici ⟺ la prop. vale.
  - possibilità 2: p(x) ha almeno una radice a ⟺ p(x) = (x − a)q(x), con q(x) di grado n (q(x) ha al massimo n radici).

es. (foto 12:43~): Δ = b² − 4ac.
- se Δ > 0: p(x) ha 2 radici x₁,₂ = (−b ± √Δ)/(2a);
- se Δ = 0: p(x) ha 1 radice con molteplicità 2: x = −b/(2a);
- se Δ < 0: p(x) non ha radici reali.
Lavorando con ℂ: ±√Δ sono i due numeri complessi che soddisfano z² = Δ ⟹ p(x) ha sempre 2 radici complesse!

**Teorema fondamentale dell'algebra.** Un polinomio p(x) di grado n ≥ 1 ha sempre esattamente n radici complesse.
es. p(x) = x² + 1 ha radici ± i.
