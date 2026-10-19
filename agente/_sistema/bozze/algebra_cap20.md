# 20. I Sottospazi Vettoriali
## Uno spazio dentro un altro spazio
Per parlare di **sottospazio** bisogna sapere qual è lo spazio più grande da cui si parte, esattamente come per parlare di sottoinsieme serve prima l'insieme. Sia dunque V uno spazio vettoriale su un campo 𝕂: per esempio ℝ³, i vettori tridimensionali che molti conoscono già.

**Definizione.** Un **sottospazio vettoriale** di V è un sottoinsieme W ⊆ V che soddisfa tre condizioni:
1. **0** ∈ W: il vettore nullo di V sta in W;
2. se w₁, w₂ ∈ W allora w₁ + w₂ ∈ W: W è chiuso rispetto alla somma;
3. se w ∈ W e λ ∈ 𝕂 allora λ·w ∈ W: W è chiuso rispetto al prodotto per scalare.

**In parole povere:** un sottospazio è un pezzo di uno spazio vettoriale che è «chiuso in sé»: se prendi due vettori del pezzo e li sommi, resti nel pezzo; se ne allunghi o accorci uno con uno scalare, resti nel pezzo; e dentro c'è sempre l'origine. Non puoi «cadere fuori» facendo le operazioni solite. Per esempio un piano per l'origine di ℝ³ è un sottospazio, mentre un piano che non passa per l'origine no.

La prima condizione ha un motivo preciso: ogni spazio vettoriale ha un elemento zero, quindi anche un sottospazio, che è a sua volta uno spazio, lo deve avere. E lo zero del sottospazio è lo zero dello spazio grande: l'origine è la stessa.

**Proposizione.** Se W è un sottospazio di V, allora W, con la somma e il prodotto per scalare di V, è a sua volta uno spazio vettoriale su 𝕂.

(Le proprietà della somma e del prodotto valgono in W perché valgono in V, e le condizioni 1-3 garantiscono che le operazioni non facciano uscire da W.) Ogni spazio V ha sempre almeno due sottospazi: il **sottospazio banale** W = {0}, che contiene solo il vettore nullo, e il **sottospazio totale** W = V. Per ogni sottospazio vale {0} ⊆ W ⊆ V.

**In parole povere:** il sottospazio banale è il pezzo più piccolo possibile, la sola origine; il sottospazio totale è il pezzo più grande, tutto lo spazio. Ogni altro sottospazio sta in mezzo.

## Un esempio che funziona e uno che non funziona in ℝ³
In V = ℝ³ si considerano due sottoinsiemi che hanno una definizione molto simile:
- W₁ = { (a, b, 0) | a, b ∈ ℝ }, i vettori con **ultima componente 0**;
- W₂ = { (a, b, 1) | a, b ∈ ℝ }, i vettori con **ultima componente 1**.

Entrambi sono sottoinsiemi di ℝ³, ma solo uno è un sottospazio. Si controllano le tre condizioni.

**W₁ è un sottospazio.**
1. Il vettore nullo (0, 0, 0) ha la forma (a, b, 0) con a = b = 0, quindi sta in W₁.
2. Se (a, b, 0) e (c, d, 0) sono in W₁, la loro somma è (a + c, b + d, 0 + 0) = (a + c, b + d, 0): l'ultima componente è ancora 0, quindi sta in W₁.
3. Se (a, b, 0) ∈ W₁ e λ ∈ ℝ, allora λ·(a, b, 0) = (λa, λb, 0) ha ancora ultima componente 0, quindi sta in W₁.

Geometricamente W₁ è il piano orizzontale per l'origine (il piano x-y).

**W₂ non è un sottospazio**, e non ne funziona nemmeno una condizione.
1. Il vettore nullo (0, 0, 0) ha ultima componente 0, non 1, quindi non sta in W₂.
2. La somma di (a, b, 1) e (c, d, 1) è (a + c, b + d, 2): l'ultima componente è 2, non 1, quindi esce da W₂.
3. Il multiplo λ·(a, b, 1) = (λa, λb, λ) ha ultima componente λ, che è 1 solo se λ = 1: per esempio il doppio di (1, 1, 1) è (2, 2, 2), che non sta in W₂.

![W₁ e W₂ in ℝ³ (visti di lato): il piano per l'origine è un sottospazio, il piano a quota 1 no.](figure/alg/sottospazi_piani.png|11)

Moralità: la definizione dei due insiemi è quasi identica, ma per uno funziona tutto e per l'altro niente. Quando si vogliono costruire sottospazi conviene imporre che qualcosa **sia zero** (lo zero ha la bella proprietà che 0 + 0 = 0 e λ·0 = 0), non che sia uguale a un numero diverso da zero. Infatti l'origine deve stare nel sottospazio, e imporre «uguale a 1» la esclude subito.

## Altri esempi nel piano
Sia V = ℝ². Tre sottoinsiemi si confrontano con le tre condizioni.
- W = { (x, x²) | x ∈ ℝ }, cioè la **parabola** y = x². **Non** è un sottospazio: (1, 1) ∈ W ma ½·(1, 1) = (½, ½) ∉ W, perché (½)² = ¼ ≠ ½. La terza condizione fallisce.
- W = { (x, 0) | x ≥ 0 }, una **semiretta** sull'asse x. **Non** è un sottospazio: (1, 0) ∈ W ma (−1)·(1, 0) = (−1, 0) ∉ W. Anche qui la terza condizione fallisce.
- W = { (x, x) | x ∈ ℝ }, la **retta** y = x. È un sottospazio: (0, 0) ∈ W; (a, a) + (b, b) = (a + b, a + b) ∈ W; λ·(a, a) = (λa, λa) ∈ W.

![Parabola e semiretta non sono sottospazi (il punto bianco esce dall'insieme), la retta y = x sì.](figure/alg/sottospazi_esempi_piano.png|13)

## I polinomi
Fissato d ∈ ℕ, l'insieme 𝕂_{d}[x] dei polinomi di grado **minore o uguale** a d è un sottospazio dello spazio 𝕂[x] di tutti i polinomi: lo zero è il polinomio nullo (che per convenzione appartiene a 𝕂_{d}[x]), la somma di due polinomi di grado al più d ha ancora grado al più d (il grado può diminuire nella somma, ma non aumentare), e anche un multiplo per uno scalare ha grado al più d.

L'insieme dei polinomi di grado **esattamente** 5, invece, non è un sottospazio di ℝ[x], con lo stesso fenomeno già visto nel capitolo 18, la somma che fa scendere il grado: x⁵ + x e −x⁵ + x² hanno grado 5, ma la loro somma x² + x ha grado 2, e anche il polinomio nullo non ha grado 5.

Il capitolo successivo vede i sottospazi più importanti dello spazio delle matrici quadrate.
