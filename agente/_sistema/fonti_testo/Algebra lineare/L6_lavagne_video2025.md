# Algebra lineare, Lezione 6: Spazi vettoriali II (lavagne dalla registrazione Webex del 6 ottobre 2025, prof. Radeschi)

Fonte: video della registrazione dell'anno scorso (MDAG2). Contenuto letto da 42 fotogrammi (uno ogni 2,5 minuti, da 01:00 a 103:30). La lavagna è in 4 pannelli (alto-sinistra, alto-destra, basso-sinistra, basso-destra) che vengono riempiti, fatti scorrere e cancellati; qui è riportato in ordine di comparsa, con il tempo approssimativo (mm:ss) della prima apparizione. Dove una parte era coperta dal docente o cancellata è segnato [coperto] o [illeggibile].

## Titolo e richiamo (01:00)
**Lezione 6: Spazi vettoriali II**
**Previously:** spazi vettoriali su un campo 𝕂; es. 𝕂ⁿ, 𝕂 (= 𝕂¹), 𝕂[x].

## Matrici: definizione (03:30, completa a 06:00)
**Def.** Una **MATRICE** a m righe e n colonne (m × n) a coefficienti in 𝕂 è una tabella
A = ( a₁₁ a₁₂ … a₁ₙ ; a₂₁ a₂₂ … a₂ₙ ; … a_ij … ; a_m1 a_m2 … a_mn ).
Sulla lavagna: la riga che contiene a_ij è la **i-esima riga**, la colonna che lo contiene è la **j-esima colonna**. Gli a_ij si chiamano **coefficienti / entrate / termini** di A.

**Def.** M(m, n, 𝕂) = { matrici m × n a coefficienti in 𝕂 } (inizio a 06:00, completa a 08:30).

**Es.** (08:30)
- A = ( 2  π  1 ; √2  −1  0 ) ∈ M(2, 3, ℝ), con a₁,₂ = π;
- ( 3+i  π ; i  √2+1 ; 1  √5 ) ∈ M(3, 2, ℂ).

**Oss.** (scritta a 08:30, completata a 13:30) M(m, 1, 𝕂) = { (a₁₁, a₂₁, …, a_m1)ᵗ | a_i1 ∈ 𝕂 } = 𝕂ᵐ.

## Notazione per colonne e righe (11:00, righe a 13:30)
**NOTAZIONE.** A = ( a₁₁ … a₁ₙ ; ⋮ ; a_m1 … a_mn ) ∈ M(m, n, 𝕂).
- Chiameremo le **colonne** A¹, A², …, Aⁿ; per esempio A¹ = (a₁₁, a₂₁, …, a_m1)ᵗ.
- Chiameremo le **righe** A₁, …, A_m; per esempio A_i = (a_i1, a_i2, …, a_in).

## Operazioni tra matrici (16:00)
Esempi in M(3, 2, ℝ) (risultato a 18:30):
- ( 2 3 ; 1 1 ; 0 5 ) + ( −1 1 ; 0 1 ; 1 4 ) = ( 1 4 ; 1 2 ; 1 9 ). Le entrate di posto corrispondente si sommano (il docente cerchia 2, 3 e −1, 1 per mostrare la prima riga).
- −2 · ( 1 2 ; 3 4 ; 5 6 ) = ( −2 −4 ; −6 −8 ; −10 −12 ). Ogni entrata si moltiplica per lo scalare.

**Affermazione** (21:00): rispetto alle operazioni qui sopra (somma entrata per entrata e prodotto per scalare), lo spazio M(m, n, 𝕂) è uno spazio vettoriale su 𝕂.

**Oss.** (21:00, completata a 23:30) Il vettore nullo è la matrice con tutte le entrate 0: 0_{M(m,n,𝕂)} = ( 0 … 0 ; ⋮ ⋱ ⋮ ; 0 … 0 ) = 0 · ( a₁₁ … a₁ₙ ; ⋮ ; a_m1 … a_mn ).
Data A = ( a₁₁ … a₁ₙ ; ⋮ ; a_m1 … a_mn ), l'**opposto** −A di A è −A = (−1)·A = ( −a₁₁ … −a₁ₙ ; ⋮ ; −a_m1 … −a_mn ).

## Sottospazi vettoriali: definizione (26:00, completa a 28:30)
**SOTTOSPAZI VETTORIALI.** Sia V uno spazio vettoriale su 𝕂.
**Def.** Un **SOTTOSPAZIO VETTORIALE** di V è un **SOTTOINSIEME** W ⊆ V tale che:
- ① ∀ w₁, w₂ ∈ W: w₁ +_V w₂ ∈ W;
- ② ∀ w₁ ∈ W, ∀ a ∈ 𝕂: a·w₁ ∈ W;
- ③ 0_V ∈ W.

## Proposizione (31:00, completa a 33:20)
**Prop.** Sia V uno spazio vettoriale su 𝕂 e W ⊆ V un sottospazio vettoriale. Allora W è anch'esso uno spazio vettoriale su 𝕂, rispetto alle operazioni di somma e prodotto per scalare in V.
(Non c'è dimostrazione sulla lavagna nei fotogrammi.)

## Non esempio 1: la parabola (36:00, completo a 41:00)
**NON ESEMPIO.** V = ℝ², W = { (x, x²)ᵗ | x ∈ ℝ } ⊆ ℝ². W è un sottospazio?
- Disegno: assi cartesiani con la parabola y = x² e, nel ramo destro, il punto w = (1, 1)ᵗ.
- Si verifica ②: w = (1, 1)ᵗ ∈ W, a = ½ ∈ ℝ. a·w ∈ W? ½·w ∈ W?
- ½·w = (½, ½)ᵗ ∉ W perché (½)² = ¼ ≠ ½.
- Nel disegno compaiono i punti v = (1, 1)ᵗ e ½·v sulla retta per l'origine, fuori dalla parabola.

## Non esempio 2: semiretta (43:30, completo a 48:30)
**Non esempio 2.** V = ℝ², W = { (x, 0)ᵗ | x ≥ 0 }. W è un sottospazio?
- ③ ✓, ① ✓.
- ② ? (1, 0)ᵗ ∈ W, ma −1·(1, 0)ᵗ = (−1, 0)ᵗ ∉ W. Quindi ② fallisce.

## Esempio: la retta y = x (46:00 inizio, completo a 51:00)
**ESEMPIO.** V = ℝ², W = { (x, x)ᵗ | x ∈ ℝ } = { (x, y)ᵗ ∈ ℝ² | x = y }.
- ① (a, a)ᵗ, (b, b)ᵗ ∈ W; (a, a)ᵗ + (b, b)ᵗ = (a+b, a+b)ᵗ ∈ W ✓.
- ② λ·(a, a)ᵗ ∈ W? (λ ∈ ℝ): λ·(a, a)ᵗ = (λa, λa)ᵗ ∈ W ✓.
- ③ 0_V = (0, 0)ᵗ ∈ W ✓.

## Riepilogo grafico dei tre esempi (53:30, completo a 56:00)
Nel pannello in basso a sinistra il docente disegna un solo piano cartesiano con i tre esempi: **W₁** la parabola (x, x²), **W₂** la semiretta sull'asse x (x ≥ 0), **W₃** la retta y = x. Il disegno viene poi cancellato (58:30). Solo W₃ è un sottospazio.

## Definizione e proposizione riscritte (61:00)
**Def.** V sp. vettoriale su 𝕂. W ⊆ V è **SOTTOSPAZIO** se:
- ① ∀ w₁, w₂ ∈ W: w₁ + w₂ ∈ W;
- ② ∀ w ∈ W, ∀ λ ∈ 𝕂: λ·w ∈ W;
- ③ 0_V ∈ W.
**Prop.** SOTTOSPAZI VETTORIALI sono essi stessi spazi vettoriali. (Riscrittura sintetica del punto precedente.)

## Esempi notevoli di sottospazi (66:00)
**ESEMPI NOTEVOLI DI SOTTOSPAZI**
① V spazio vettoriale ammette:
  - ① sottospazio **BANALE** W = {0_V} ⊆ V;
  - ② sottospazio **TOTALE** W = V.
② V = 𝕂[x], fissiamo un d ∈ ℕ. W = 𝕂[x]_d = { p(x) ∈ 𝕂[x] | deg p(x) ≤ d } è un sottospazio vettoriale di 𝕂[x] (completato a 68:30 e 71:00).

## Domanda: polinomi di grado esatto 5 (73:30, risposta a 76:00)
**Domanda.** W = { p(x) ∈ ℝ[x] | deg p(x) = 5 } ⊆ ℝ[x] è sottospazio vettoriale?
**NO.** Ad es. p(x) = x⁵ + x e q(x) = −x⁵ + x² sono in W, però p(x) + q(x) = x² + x ∉ W.

## Sottospazi di matrici (76:00)
**Def.** M(n, n, 𝕂) è detto **spazio delle matrici quadrate**; si scrive M(n, 𝕂) = M(n).

**Prop.** I seguenti sottoinsiemi di M(n) sono sottospazi (78:30 inizio, completo a 91:00):
- ① **U(n)** = { ( a₁₁ … a₁ₙ ; 0 ⋱ ⋮ ; 0 0 aₙₙ ) } = { (a_ij) ∈ M(n) | a_ij = 0 ∀ i > j } = **matrici triangolari superiori** (81:00). Es. ( 1 2 3 ; 0 4 5 ; 0 0 6 ). Nel disegno una diagonale tracciata dall'alto a sinistra al basso a destra separa la parte nulla.
- ② **L(n)** = { (a_ij) | a_ij = 0 ∀ j > i } = **matrici triangolari inferiori** (81:00-86:00). Es. ( 1 0 0 ; 2 4 0 ; 3 5 6 ).
- ③ **D(n)** = { ( a₁₁ 0 ; ⋱ ; 0 aₙₙ ) } = { (a_ij) | a_ij = 0 ∀ i ≠ j } = **matrici diagonali** (83:30). Es. ( 1 0 0 ; 0 2 0 ; 0 0 3 ) = diag(1, 2, 3).
- ④ **S(n)** = { (a_ij) | a_ij = a_ji ∀ i, j } = **matrici simmetriche** (86:00). Es. ( 1 2 3 ; 2 4 5 ; 3 5 6 ), con le entrate simmetriche rispetto alla diagonale cerchiate (88:30).
- ⑤ **A(n)** = { (a_ij) | a_ij = −a_ji ∀ i, j } = **matrici antisimmetriche** (88:30). Es. ( 0 1 2 ; −1 0 3 ; −2 −3 0 ). Osservazione scritta nel riquadro: a_ii = −a_ii (cioè le entrate sulla diagonale sono nulle; il passaggio finale a_ii = 0 non è visibile nei fotogrammi) (91:00).
(Per le dimostrazioni non c'è traccia nei fotogrammi: il docente commenta a voce.)

**Def.** (93:30) La **DIAGONALE PRINCIPALE** di una matrice quadrata è quella che contiene gli a_ii.

## Lo span (96:00)
**LO SPAN.** Sia V uno spazio vettoriale su 𝕂 e siano v₁, …, vₙ ∈ V.
{ a₁v₁ + a₂v₂ + … + aₙvₙ | a₁, …, aₙ ∈ 𝕂 } = Span(v₁, …, vₙ) è detto **spazio generato da** v₁, …, vₙ.
**Prop.** Span(v₁, …, vₙ) è un sottospazio vettoriale (98:30). (Dimostrazione non visibile.)

## Esempio di span in ℝ³ (101:00, completo a 103:30)
**Es.** V = ℝ³, v₁ = (1, 0, 0)ᵗ, v₂ = (0, 1, 0)ᵗ [le componenti sono lette dai disegni, in parte poco nitide].
- a·v₁ + b·v₂ = (a, 0, 0)ᵗ + (0, b, 0)ᵗ = (a, b, 0)ᵗ.
- Span(v₁, v₂) = { a·v₁ + b·v₂ } = { (a, b, 0)ᵗ | a, b ∈ ℝ }.
- Disegno: assi x, y, z con v₁ lungo x e v₂ lungo y; il piano generato da v₁, v₂ (il piano xy) è disegnato come un parallelogramma, indicato da una freccia dalla scritta Span(v₁, v₂).
