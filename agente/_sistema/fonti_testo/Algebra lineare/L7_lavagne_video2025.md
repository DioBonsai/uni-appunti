# Algebra lineare, Lezione 7: Spazi vettoriali III (lavagne dalla registrazione Webex dell'8 ottobre 2025, prof. Radeschi)

Fonte: video della registrazione dell'anno scorso (MDAG2, «Lezione 7: Spazi Vettoriali III - Video della lezione»), file `audio/algebra_L7_2025.mp4` (91 min 25 s, completo), trascrizione `trascrizioni/algebra_L7_2025.txt`.
Contenuto letto da 46 fotogrammi (da 01:00 a 89:50; uno ogni 2,5 minuti, più alcuni intermedi). La lavagna è in 4 pannelli (alto/basso, sinistra/destra) che vengono riempiti, fatti scorrere e cancellati; qui il contenuto è in ordine di comparsa, con il tempo approssimativo (mm:ss) della prima apparizione. Dove una parte era coperta dal docente è segnato [coperto].

## Titolo e richiamo (01:00)
**LEZIONE 7: SPAZI VETTORIALI III**
**Previously:** V sp. vettoriale su 𝕂.
→ Span(v₁, …, vₙ) = { v ∈ V | v = a₁v₁ + … + aₙvₙ, per qualche a₁, …, aₙ ∈ 𝕂 }. La somma a₁v₁ + … + aₙvₙ è chiamata **COMBINAZIONI LINEARI di v₁, …, vₙ**.

## Esempio (a): tre vettori in ℝ² (03:30 – 13:30)
**Prendiamo V = ℝ²**, con un piano cartesiano disegnato (assi, v₁, v₂, v₃, poi w).
**(a)** v₁ = (1, 0)ᵗ, v₂ = (−1, 0)ᵗ, v₃ = (0, 1)ᵗ.
Span(v₁, v₂, v₃) = { a·(1,0)ᵗ + b·(−1,0)ᵗ + c·(0,1)ᵗ } = { (a − b, c)ᵗ | a, b, c ∈ ℝ } (il docente scrive sotto ogni addendo il vettore risultante: (a,0)ᵗ, (−b,0)ᵗ, (0,c)ᵗ).

Poi (da 13:30 circa, pannello in alto a destra):
- (5, 6)ᵗ = 5·v₁ + 0·v₂ + 6·v₃ = 0·v₁ − 5·v₂ + 6·v₃ (**due modi diversi** di scrivere lo stesso vettore)
- (x, y)ᵗ = x·v₁ + 0·v₂ + y·v₃
- **①** Span(v₁, v₂, v₃) = ℝ² («v₁, v₂, v₃ sono **generatori**»)
- **②** v₁, v₂, v₃ sono «**ridondanti**» («v₁, v₂, v₃ sono **linearmente dipendenti**»): v₂ = (−1, 0)ᵗ = (−1)·v₁ + 0·v₃ = −v₁ + 0·v₃ ⟷ **v₁ + v₂ + 0·v₃ = 0_V**.

## Esempio (b): un solo vettore (18:30 – 26:00)
**(b)** w = (1, 1)ᵗ.
Span(w) = { a·(1,1)ᵗ } = { (a, a)ᵗ } (la retta bisettrice).
- **①** Span(w) ≠ V.
- **②** ∃ a tale che a·w = (0,0)ᵗ? **Solo per a = 0.** → «{w} NON è ridondante» («w è **LINEARMENTE INDIPENDENTE**»).

## (c) Una base di ℝ² (26:00)
**(c)** I vettori {v₁, v₃} di (a) generano tutto ℝ², «senza ridondanze» («**basi**»).

## Definizioni: generatori, lineare indipendenza, base (27:00 – 33:30)
**Def.** V sp. vettoriale su 𝕂 e {v₁, …, vₙ} ⊆ V. Diciamo che v₁, …, vₙ è:
**①** un **INSIEME DI GENERATORI** se Span(v₁, …, vₙ) = V ⟷ ∀ v ∈ V si può scrivere come v = a₁v₁ + … + aₙvₙ per qualche a₁, …, aₙ ∈ 𝕂.
**②** **LINEARMENTE INDIPENDENTE (l.i.)** se l'unico modo di scrivere 0_V = a₁v₁ + … + aₙvₙ è con a₁ = 0 = a₂ = a₃ = … = aₙ (la combinazione lineare banale). **(altrimenti, {v₁, …, vₙ} è linearmente dipendente)**
**③** **BASE**, se è sia l.i. che insieme di generatori. (Scritta a 31:00; a 33:30 il docente richiama ℝ² e la retta di w.)

## Proposizione: dipendenza lineare e combinazioni (35:00 – 41:00)
**Prop.** {v₁, …, vₙ} è linearmente dipendente ⟺ c'è un vᵢ che è combinazione lineare degli altri.
**IN PARTICOLARE:**
- {v₁, v₂, 0_V} è dipendente: 0_V = 0·v₁ + 0·v₂ − 1·0_V … cioè 0·v₁ + 0·v₂ − 1·0_V = 0_V (coefficiente −1 ≠ 0 sul vettore nullo).
- {v₁, v₂ = 2v₁, v₃} è dipendente → v₂ = 2v₁ + 0·v₃.
- {v₁, v₂} LIN. DIPENDENTE ⟺ v₁ = a·v₂ (uno è multiplo dell'altro).

**Oss.** (da 41:00)
- {v₁} è lin. dip. ⟺ 0_V = a·v₁ con a ≠ 0 ⟺ v₁ = 0_V.
- Quindi **{v₁} è lin. indip. ⟺ v₁ ≠ 0_V**.

**Prop.** (a 46:00)
- {v₁, …, vₙ} l.i. ⟹ **ogni sottoinsieme è l.i.**
- {v₁, …, vₙ} generatori ⟹ **ogni insieme contenente {v₁, …, vₙ} è di generatori**.

## Esempio: (2,1) e (0,1) sono l.i.? (48:00 – 52:00)
**Es.** v₁ = (2, 1)ᵗ, v₂ = (0, 1)ᵗ: è l.i.?
(0, 0)ᵗ = a·(2, 1)ᵗ + b·(0, 1)ᵗ (+ c·(…) coperto dalla mano del docente in un fotogramma: è un terzo vettore aggiunto per far vedere il caso).
Se a = b = 0 è l'unica soluzione ⇒ l.i., sennò dipendente.
(0, 0)ᵗ = (2a, a + b)ᵗ ⟶ { 2a = 0 ; a + b = 0 } ⟶ a = 0 ⟶ b = 0 ⇒ **L.I.**

## Coordinate rispetto a una base (54:00 – 60:00)
**Prop.** V sp. vett. su 𝕂 e {v₁, …, vₙ} base; allora ∀ v ∈ V si può esprimere come v = a₁v₁ + … + aₙvₙ dove a₁, …, aₙ sono **UNICI**.
Gli aᵢ sono le **COORDINATE di v nella base {v₁, …, vₙ}**.

## Teorema e dimensione (59:00 – 66:00)
**TEOREMA.** Ogni due basi di uno spazio vettoriale hanno la stessa cardinalità.
**Def.** Uno spazio vettoriale ha **DIMENSIONE FINITA** se ammette una base finita.
Se V ha dimensione finita, la **dimensione** di V, dim V, è il numero di elementi di una base.

## Esempi importanti (66:00 – 82:00)
**ESEMPI IMPORTANTI:** 𝕂ⁿ = { (a₁, …, aₙ)ᵗ | aᵢ ∈ 𝕂 }. **Calcoliamo dim 𝕂ⁿ.**
e₁ = (1, 0, …, 0)ᵗ, e₂ = (0, 1, 0, …, 0)ᵗ, …, eₙ = (0, …, 0, 1)ᵗ: è una base?
**Oss.** (3, 2)ᵗ ∈ ℝ²: (3, 2)ᵗ = 3·(1, 0)ᵗ + 2·(0, 1)ᵗ = 3e₁ + 2e₂ (= (3, 0)ᵗ + (0, 2)ᵗ).
**In generale**, (a₁, …, aₙ)ᵗ = a₁e₁ + a₂e₂ + … + aₙeₙ.
**In particolare:**
- **①** ∀ (a₁, …, aₙ)ᵗ è comb. lineare di e₁, …, eₙ → **generatori**.
- **②** (0, …, 0)ᵗ = a₁e₁ + … + aₙeₙ = (a₁, …, aₙ)ᵗ ⟹ { 0 = a₁ ; 0 = a₂ ; … ; 0 = aₙ } → e₁, …, eₙ sono l.i.
- ⟹ {e₁, …, eₙ} sono una base di 𝕂ⁿ (**BASE CANONICA**) ⟹ **dim 𝕂ⁿ = n**.

**𝕂[x]_d = { p(x) ∈ 𝕂[x] | deg p(x) ≤ d } = { p(x) = a_d x^d + a_{d−1} x^{d−1} + … + a₁x + a₀ | a_i ∈ 𝕂 }** (scritto a 75:00).
1, x, x², …, x^d formano una base?
**Oss.** p(x) = a_d x^d + … + a₁x + a₀ = a₀·(1) + a₁·(x) + a₂·(x²) + … + a_d·(x^d).
⟹ **①** ∀ p(x) ∈ 𝕂[x]_d è comb. lin. di 1, x, …, x^d → generatori.
⟹ **②** 0·x^d + … + 0·x + 0 = a₀(1) + … + a_d(x^d) = a_d x^d + … + a₁x + a₀ ⟹ { 0 = a_d ; … ; 0 = a₁ ; 0 = a₀ } ⟹ 1, …, x^d sono l.i.
⟹ **1, x, …, x^d è una base (BASE CANONICA)** ⟹ **dim 𝕂[x]_d = d + 1**.

## Proposizione: n vettori in uno spazio di dimensione n (83:00 – 86:00)
**Prop.** Sia V sp. vett. di dim V = n, e siano v₁, …, vₙ un insieme **l.i., o di generatori**. Allora v₁, …, vₙ è una base.

## Matrici come spazio vettoriale (86:00 – 91:00)
**M(m, n, 𝕂) = { matrici (a_ij) m × n | a_ij ∈ 𝕂 }.**
**Candidati per una base:** E_ij = matrice m × n con **1 al posto (i, j)** (riga i, colonna j) e 0 altrove (a 87:30 scritta E₁₁ = (1 0 … 0 ; 0 … ; 0 …)).
La lezione si ferma qui: il docente sta introducendo le E_ij come candidati per una base di M(m, n, 𝕂) (il calcolo di dim M(m, n, 𝕂) = m·n non è completato nel video).

## Note sulla trascrizione audio
La trascrizione (`algebra_L7_2025.txt`) è del modello Whisper «small» in modalità veloce: il lessico matematico può essere storpiato; fidarsi della lavagna per le formule. La prima copia scaricata era troncata a 30 min (spostata in `trascrizioni/small_scartate/`).
