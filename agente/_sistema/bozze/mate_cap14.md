# 14. Funzioni Suriettive, Iniettive e Biettive
## Suriettività
Una funzione f : A → B è **suriettiva** se la sua immagine totale è tutto il codominio, cioè se f(A) = B: ogni elemento di B è raggiungibile dalla funzione partendo da qualche elemento del dominio. Si può scrivere in modi equivalenti:
- ∀ b ∈ B, ∃ a ∈ A tale che f(a) = b;
- ∀ b ∈ B, f^{-1}(b) ≠ ∅: ogni elemento del codominio ha almeno una controimmagine.

## Iniettività
Una funzione f è **iniettiva** se elementi distinti del dominio hanno immagini distinte:

∀ a₁, a₂ ∈ A, a₁ ≠ a₂ ⟹ f(a₁) ≠ f(a₂).

In termini di controimmagini: ∀ b ∈ B, |f^{-1}(b)| ≤ 1, cioè nessun elemento del codominio viene raggiunto da due elementi diversi del dominio. Nel disegno con le frecce, f non è iniettiva quando due frecce partenti da punti diversi arrivano nello stesso punto.

Per dimostrare che f **non** è iniettiva basta mostrare che esistono due elementi diversi del dominio con la stessa immagine: negando la proposizione, il suo contrario è "esistono a₁ ≠ a₂ con f(a₁) = f(a₂)". Un controesempio basta.

## Biettività
f è **biettiva** (o corrispondenza biunivoca) se è sia iniettiva sia suriettiva, cioè ∀ b ∈ B, |f^{-1}(b)| = 1: ogni elemento del codominio ha esattamente una controimmagine. Equivalentemente, ∀ b ∈ B ∃! a ∈ A con f(a) = b.

## Il ruolo di dominio e codominio
Prendiamo f(x) = x². Come funzione ℝ → ℝ:
- non è iniettiva, perché f(−1) = f(1) = 1 pur essendo −1 ≠ 1;
- non è suriettiva, perché i numeri negativi non hanno controimmagine (per esempio f^{-1}(−4) = ∅) e quindi Im(f) = [0, +∞) ≠ ℝ.

Se cambiamo il codominio e consideriamo g : ℝ → [0, +∞), g(x) = x², la funzione **diventa suriettiva**: i numeri negativi non sono più nel codominio e ogni numero non negativo è un quadrato. Se restringiamo anche il dominio a [0, +∞), cioè q : [0, +∞) → [0, +∞), q(x) = x², diventa biettiva. L'espressione è sempre la stessa, ma abbiamo cambiato uno dei tre ingredienti: la funzione è diversa, e infatti ha una proprietà che l'altra non ha.

## Altri esempi
- h : ℤ → ℤ, h(n) = 2n + 1 è **iniettiva**: da 2n₁ + 1 = 2n₂ + 1 segue 2n₁ = 2n₂ e quindi n₁ = n₂. Non è suriettiva: l'immagine è l'insieme dei numeri dispari e i pari non hanno controimmagine in ℤ.
- k : ℝ → ℝ, k(x) = x³ è **biettiva**: ogni numero reale ha un'unica radice cubica reale.

**Come sottolineato a lezione:** prima di dire se una funzione è iniettiva o suriettiva bisogna leggere con cura dominio e codominio: la stessa espressione può essere suriettiva o no a seconda dell'insieme di arrivo, e iniettiva o no a seconda dell'insieme di partenza.

Con queste proprietà possiamo parlare di funzioni composte e di funzioni inverse.
