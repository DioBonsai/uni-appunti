# Algebra lineare, Lezione 5: Spazi vettoriali I (lavagne dalla registrazione Webex del 1 ottobre 2025, prof. Radeschi)

Fonte: video `algebra_L5_2025.mp4` (101,9 min, registrazione dell'anno scorso presente su Moodle MDAG2). Contenuto letto dai fotogrammi (uno ogni 2 minuti). Le lavagne sono in 4 pannelli (alto-sinistra, alto-destra, basso-sinistra, basso-destra) che vengono riempiti e fatti scorrere; qui è riportato in ordine di comparsa. Dove una parte era coperta dal docente è segnato [coperto].

## Titolo e definizione di spazio euclideo
**Lezione 5: Spazi vettoriali, I**

**Def.** Lo spazio Euclideo n-dimensionale è
ℝⁿ = ℝ × ℝ × … × ℝ (n copie) = { (x₁, …, xₙ)ᵗ (vettore colonna) | x₁, …, xₙ ∈ ℝ }.

Dato v ∈ ℝⁿ lo chiameremo **VETTORE**.
**Def.** Dato v = (x₁, …, xₙ)ᵗ, chiameremo xᵢ = **i-esima COMPONENTE (COORDINATA)** di v.

## Esempi geometrici
**Es.** ℝ² = { (x, y)ᵗ | x, y ∈ ℝ }: piano cartesiano con assi x e y, un punto P di coordinate a (sull'asse x) e b (sull'asse y), la freccia dall'origine a P; P ⟷ v = (a, b)ᵗ.
ℝ³ = { (x, y, z)ᵗ | x, y, z ∈ ℝ }: tre assi x, y, z, punto P con coordinate a, b, c; P ⟷ v = (a, b, c)ᵗ.

**Un vettore in ℝⁿ può essere rappresentato come** v = (x₁, …, xₙ)ᵗ:
- il punto di coordinate (x₁, …, xₙ);
- una freccia dall'origine al punto di coordinate (x₁, …, xₙ).
Es.: in ℝ² il vettore (3, 2)ᵗ (punto nel piano); in ℝ³ il vettore (3, 4, 2)ᵗ con il punto P disegnato su tre assi.

## Operazioni su ℝⁿ
**SOMMA DI VETTORI**: v = (x₁, …, xₙ)ᵗ, w = (y₁, …, yₙ)ᵗ → v + w = (x₁ + y₁, …, xₙ + yₙ)ᵗ. Esempio nel piano: w = (1, 2)ᵗ, v = (3, 1)ᵗ, v + w = (4, 3)ᵗ, con la regola del parallelogramma disegnata.
**MOLTIPLICAZIONE PER ℝ**: v = (x₁, …, xₙ)ᵗ, a ∈ ℝ → a·v = (a x₁, …, a xₙ)ᵗ. Esempio: v = (3, 1)ᵗ, a = 2, 2v = (6, 2)ᵗ: la freccia raddoppia di lunghezza.

## Scalari e proprietà di ℝⁿ
**Def.** UNO SCALARE è un numero (o meglio, l'elemento di un campo).

**Prop.** In ℝⁿ somma e moltiplicazione hanno le seguenti proprietà:
1. ∀ u, v, w ∈ ℝⁿ: (u + v) + w = u + (v + w).
2. ∃ 0_ℝⁿ ∈ ℝⁿ t.c. ∀ v ∈ ℝⁿ: 0_ℝⁿ + v = v + 0_ℝⁿ = v; qui 0_ℝⁿ = (0, …, 0)ᵗ.
3. ∀ v ∈ ℝⁿ ∃ u ∈ ℝⁿ t.c. v + u = u + v = 0_ℝⁿ; se v = (x₁, …, xₙ)ᵗ allora u = (−x₁, …, −xₙ)ᵗ = −v.
4. ∀ u, v ∈ ℝⁿ: u + v = v + u.
5. ∀ a, b ∈ ℝ, ∀ v ∈ ℝⁿ: a·(b·v) = (ab)·v.
6. ∀ a, b ∈ ℝ, ∀ v ∈ ℝⁿ: (a + b)·v = a·v + b·v (nota sulla lavagna: la somma a + b è "somma in ℝ", il + a destra è somma di vettori; la moltiplicazione a·v è "molt. in ℝ" per le componenti).
7. ∀ a ∈ ℝ, ∀ v, w ∈ ℝⁿ: a·(v + w) = a·v + a·w.
8. 1·v = v, ∀ v ∈ ℝⁿ.

## Gruppi
**Def.** Un **gruppo** è un insieme G dotato di un'operazione ⋆ : G × G → G, (a, b) ↦ a ⋆ b [che soddisfi le proprietà ①②③ dette sopra].
- G con ⋆ : G × G → G che soddisfi ①②③ è un **GRUPPO**.
- G gruppo è **ABELIANO** (= COMMUTATIVO) se ④ vale.

## Spazio vettoriale
**Def.** Fissiamo un campo 𝕂. Uno **SPAZIO VETTORIALE su 𝕂** è un insieme V, con operazioni
+ : V × V → V, (v, w) ↦ v + w, e · : 𝕂 × V → V, (a, v) ↦ a·v,
tale che siano soddisfatte:
- Prop ①–④ ⟹ (V, +) è un gruppo abeliano;
- Prop ⑤–⑧, dove gli scalari sono elementi di 𝕂.

## Esempi
- **Es.** ℝⁿ, con (x₁, …, xₙ)ᵗ + (y₁, …, yₙ)ᵗ = (x₁ + y₁, …, xₙ + yₙ)ᵗ e a·(x₁, …, xₙ)ᵗ = (a x₁, …, a xₙ)ᵗ con a ∈ ℝ, è uno spazio vettoriale su ℝ.
- ℝ[x] = { p(x) = aₙxⁿ + … + a₁x + a₀ }, con (aₙxⁿ + … + a₀) + (bₙxⁿ + … + b₀) = (aₙ + bₙ)xⁿ + … + (a₁ + b₁)x + (a₀ + b₀) e c·(aₙxⁿ + … + a₀) = c aₙxⁿ + … + c a₁x + c a₀ (con c ∈ ℝ) (segnato con ⊛): è uno spazio vettoriale su ℝ.
- 𝕂 campo ⟹ 𝕂ⁿ = { (x₁, …, xₙ)ᵗ | x₁, …, xₙ ∈ 𝕂 }, con le operazioni v + w, a·v come in ℝ (a ∈ 𝕂), è uno spazio vettoriale su 𝕂.
- 𝕂[x] = { p(x) = aₙxⁿ + … + a₁x + a₀ | a₀, …, aₙ ∈ 𝕂 }, rispetto a + e · come in ⊛ (con c ∈ 𝕂), è uno spazio vettoriale su 𝕂.

## Osservazioni
**Oss.** Se V è uno spazio vettoriale, allora 0_V = 0·v. Se v ∈ V, l'opposto di v è dato da (−1)·v = −v.
Esempi: V = ℝ[x]: 0_V = 0xⁿ + … + 0x + 0 = 0·(x + 1) = 0x + 0 = 0. V = 𝕂ⁿ: 0_V = 0·(x₁, …, xₙ)ᵗ = (0·x₁, …, 0·xₙ)ᵗ = (0, …, 0)ᵗ. Similmente, p(x) = aₙxⁿ + … + a₁x + a₀ ⟹ −p(x) = (−1)·p(x) = −aₙxⁿ − … − a₀.

**Oss.** 𝕂¹ = { (x) | x ∈ 𝕂 } = 𝕂 ⟹ ogni campo 𝕂 è uno spazio vettoriale su 𝕂 stesso.
Ad esempio, ℂ è uno spazio vettoriale su ℂ; se si considera ℂ con le operazioni di somma e moltiplicazione per **numeri reali**, ℂ è uno spazio vettoriale su ℝ.

## Esempio con funzioni
**Es.** In V = { f : ℝ → ℝ } definisco:
- (f + g)(x) = f(x) + g(x) (ad es. eˣ + sin x);
- per a ∈ ℝ: (a·f)(x) = a·f(x) (ad es. 3e^{x²});
- (V, +, ·) è uno spazio vettoriale su ℝ.
Il docente disegna anche un grafico della somma di due funzioni (parabola x² + cos x…) e valuta a mano alcuni punti.

## Parte finale (domande di uno studente, ~minuti 92-100)
Sulla lavagna in basso a destra: z = a + ib con a, b ∈ ℝ; si discute 1 = z + z̄ = a + ib + a − ib = 2a [da confermare: la scrittura è parziale]; i ≠ ... ; "1 ≠ 0 MAI"; a² + b²; un disegno del piano complesso con una circonferenza; sin(2) = ... (esempio numerico di funzioni). Sono risposte a domande di uno studente, non argomenti nuovi.
