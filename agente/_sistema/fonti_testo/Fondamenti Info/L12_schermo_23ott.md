# Fondamenti, Lezione 12 (venerdì 23 ottobre 2026, prof. Berardi): contenuto visibile nel video

Fonte: registrazione Webex `audio/fondamenti_L12_23ott.mp4` (98 min; audio e video completi), trascrizione `trascrizioni/fondamenti_L12_23ott.txt`.
⚠ **Non c'è una lavagna.** Per i **primi ~49 minuti** il video mostra solo la webcam in aula, con lo schermo proiettato sullo sfondo, sfocato e in gran parte illeggibile (si distinguono a tratti le pagine del libro: sezione **1.6 Nested Quantifiers**, pagina 50). Da circa **49 minuti** il docente **condivide lo schermo** (documento Word `20261022--Lezione-11-Fondamenti` e pagine del libro nel browser) e si legge bene. Contenuto letto da 39 fotogrammi (uno ogni 2,5 minuti) più 50 fotogrammi aggiuntivi (uno al minuto) dal minuto 49 in poi.

## Prima parte (0-49 min): webcam e libro (frammenti leggibili)
- Si leggono, sulla pagina del libro proiettata (p. 50, sez. 1.6): «(x > 0) ∧ (y > 0) → (x + y) > 0 … written symbolically as ∀x∀y P(x, y)», «for every x and for every y …» (**quantificatori consecutivi dello stesso tipo**).
- **Example 1.6.1:** «Restate ∀m∃n(m < n) in words. The domain of discourse is the set Z⁺ × Z⁺» (frase del libro, parzialmente coperta).
- «**Everybody loves somebody**; symbolically, letting L(x, y) be the statement “x loves y”, ∀x∃y L(x, y). In words, for every person x, there exists a person y such that x loves y.»
- A 18:30 (810-1110 s) su un foglio proiettato si legge **∃y∀x L(x, y)** (la formula con i quantificatori scambiati: «c'è una persona amata da tutti»).
- A 21:00 (1260 s): «… dominio finito D = {d₁, …, dₙ}» (introduzione dell'algoritmo per i quantificatori annidati).

## Seconda parte (dal minuto ~49): schermo condiviso
### Il pseudocodice per ∀x∃y P(x, y) su un dominio finito (49:00 – 69:00)
Il libro (Example 1.6.8, p. 51): «Suppose that P is a propositional function with domain of discourse {d₁, …, dₙ} × {d₁, …, dₙ}. The following pseudocode determines whether ∀x∃y P(x, y) is true or false».
**Primo tentativo del docente (sbagliato):**
```
for i = 1 to i = n
  for j = 1 to j = n
    if (P(d_i, d_j) = false) then return false;
// Se il nested for non ha dato false
return true;
```
Poi la versione con `if (P(d_i, d_j) = true) then return true;` seguita da **«//NO!!»**: il blocco è barrato come errato.
**Problema:** decidere ∀x∃y.P(x, y) nel caso x, y abbiano un dominio finito D = {d₁, …, dₙ}.
Si scompone: **∀x∃y.P(x, y) = ∀x.Q(x)**, dove **Q(x) = ∃y.P(x, y)**.
**Decidiamo prima Q(x):**
```
ex(x) {
  for y = 1 to n
    if (P(x, y) = true)
      return true;
  return false;
}
```
**Poi il ∀:**
```
for x = 1 to n
  if (ex(x) = false)
    return false;
return true;
```

### Spiegazione dal libro (69:00 – 72:00)
«If for each dᵢ, there exists dⱼ such that P(dᵢ, dⱼ) is true, then for each i, P(dᵢ, dⱼ) is true for some j. Thus, exists_dj(i) returns true for every i. Since ¬exists_dj(i) is always false, the first for loop eventually terminates and true is returned to indicate that ∀x∃y P(x, y) is true. If for some dᵢ, P(dᵢ, dⱼ) is false for every j, then, for this i, P(dᵢ, dⱼ) is false for every j. In this case, the for loop in …» (testo continuo del libro).

### Esempi del libro (68:00 – 80:00)
- **Definizione (p. 51):** l'enunciato ∀x∃y P(x, y), con dominio X × Y, è vero se, per **ogni** x ∈ X, esiste **almeno un** y ∈ Y per cui P(x, y) è vero; è falso se c'è **almeno un** x ∈ X tale che P(x, y) è falso per **ogni** y ∈ Y.
- **Example 1.6.6** (esempio introduttivo) e **1.6.9:** ∃x∀y(x ≤ y), dominio Z⁺ × Z⁺: **vero**, perché esiste almeno un intero positivo x (x = 1) per cui x ≤ y per ogni intero positivo y: «in words, there is a **smallest** positive integer (namely 1)».
- **Example 1.6.10:** ∃x∀y(x ≥ y), dominio Z⁺ × Z⁺: **falso**, perché per ogni intero positivo x c'è almeno un intero positivo y, cioè y = x + 1, per cui x ≥ y è falso: «there is **no greatest** positive integer».
- **Example 1.6.11:** ∃x∃y((x > 1) ∧ (y > 1) ∧ (xy = 6)), dominio Z⁺ × Z⁺: **vero**, perché c'è almeno un intero x > 1 (x = 2) e almeno un intero y > 1 (y = 3) con xy = 6.
- **Example 1.6.12:** ∃x∃y((x > 1) ∧ (y > 1) ∧ (xy = 7)), dominio Z⁺ × Z⁺: **falso** (7 è primo).
- **Negazione (Example 1.6.13):** «The generalized De Morgan's laws for logic (Theorem 1.5.14) can be used to negate a proposition containing nested quantifiers.» ¬(∀x∃y P(x, y)) ≡ ∃x ¬(∃y P(x, y)) ≡ **∃x∀y ¬P(x, y)**. «Notice how in the negation, ∀ and ∃ are interchanged.»

### Negare un enunciato con quantificatori annidati (85:00 – 95:00)
Nel documento Word:
- **∀x∃y(x > y) = non esiste un minimo.**
- **¬∀x∃y(x > y) = ∃x.¬(∃y(x > y)) = ∃x∀y.¬(x > y) = ∃x∀y.(x ≤ y) = …** (e, in margine, l'equivalenza **x ≤ y ⟷ (x < y) ∨ (x = y)**; una casella «Carattere» di Word mostra la barratura del testo «non»). Il risultato è: **esiste un minimo.**
- **Domanda: ∃x∀y.(xy < 1) è vera? Dominio ℝ × ℝ:** vera per x = 0.
- **Dominio ℝ∖{0} × ℝ∖{0}** (poi corretto in **ℝ⁺ × ℝ⁺**): falsa; «in questo caso vale l'opposto»:
  **¬∃x∀y(xy < 1) = (de' Morgan) ∀x∃y(xy ≥ 1), vera scegliendo y = 1/x**; «dimostriamo che ∀x∃y(xy = 1)».
