# Matematica discreta, lezione 2 (2 ottobre 2026): appunti a mano
(trascrizione dell'appunto manoscritto, prof. Mori; fonte: L2_appunti_2ott.pdf, 2 pagine)

## Insiemi
- Differenza: A \ B = { x ∈ A | x ∉ B }; B \ A.
- **Caso speciale** B ⊆ A: complementare di B in A: 𝒞_A(B) = { x ∈ A | x ∉ B } ⊆ A. 𝒞_A(∅) = A, 𝒞_A(A) = ∅. A = B ∪ 𝒞_A(B) (⇒ ovvio; ⊆: x ∈ A ⟹ x ∈ B ∨ x ∉ B ⟹ x ∈ B ∪ 𝒞_A(B)). B ∩ 𝒞_A(B) = ∅.
- A ⊇ S, T (S, T sottoinsiemi di A).

**Leggi di De Morgan** (il complementare scambia l'intersezione con l'unione):
1. 𝒞_A(S ∪ T) = 𝒞_A(S) ∩ 𝒞_A(T)
2. 𝒞_A(S ∩ T) = 𝒞_A(S) ∪ 𝒞_A(T)
Dimostrazione di (1), "⊆": x ∈ 𝒞_A(S ∪ T) ⟹ x ∈ A, x ∉ S ∪ T ⟹ x ∈ A, x ∉ S e x ∉ T ⟹ x ∈ 𝒞_A(S) e x ∈ 𝒞_A(T) ⟹ x ∈ 𝒞_A(S) ∩ 𝒞_A(T). Per "⊇" si ripercorre al contrario. **Provare a dimostrare la 2.**

## Insieme delle parti
A insieme; 𝒫(A) = { B | B ⊆ A }.
- 𝒫(∅) = {∅} ≠ ∅ (⚠ A = {{a}} vs A = {a}).
- 𝒫({a}) = {∅, {a}}: 2 elementi.
- 𝒫({a,b}) = {∅, {a}, {b}, {a,b}}: 4.
- 𝒫({a,b,c}) = {∅, {a}, {b}, {c}, {a,b}, {a,c}, {b,c}, {a,b,c}}: 8. Poi 16, 32, 64.
**Teorema**: sia A un insieme con |A| = n, allora |𝒫(A)| = 2ⁿ. (U = { n ∈ ℕ | se |A| = n allora |𝒫(A)| = 2ⁿ }.)

## I numeri naturali ℕ = {0, 1, 2, 3, …}
**Assiomi di Peano**
1. 0 è un numero naturale, 0 ∈ ℕ
2. ∀n ∈ ℕ ha un successore S(n) (0; 1 = S(0); 2 = S(1); …)
3. Se m ≠ n (∈ ℕ) allora S(m) ≠ S(n)
4. 0 non è successore di alcun n
5. **Principio di induzione**: sia U ⊆ ℕ tale che 0 ∈ U e ∀n ∈ U, S(n) ∈ U, allora U = ℕ.

Esempio: 1² + 2² + … + n² = (1/6)·n·(n+1)(2n+1). Sia U = { n ∈ ℕ | la formula è vera }. La formula per n = 1 è ok. Sia n ∈ U (⟹ n+1 ∈ U): 1² + … + n² + (n+1)² = (1/6)n(n+1)(2n+1) + (n+1)² = (n+1)((1/6)n(2n+1) + (n+1)) = … (continua).
Per la dimostrazione di |𝒫(A)| = 2ⁿ: A ∈ U (cioè n elementi), A = {a₁, a₂, …, aₙ} ∪ {aₙ₊₁}. B ⊆ A: distinguo 2 casi: aₙ₊₁ ∈ B oppure aₙ₊₁ ∉ B (∪{aₙ₊₁} / \{aₙ₊₁}).

## Def. Ricoprimento e partizione
Sia S un insieme. Un **ricoprimento** di S è una collezione di sottoinsiemi {Aᵢ} tali che S = ∪Aᵢ. Es.: ℕ = {0,…,1000} ∪ {100,…,10000} ∪ {n > 10000} → ricoprimento ma "non è una partizione".
Una **partizione** di S è un ricoprimento {Aᵢ} di S tale che: 1. ∅ ≠ Aᵢ ∀i; 2. se i ≠ j allora Aᵢ ∩ Aⱼ ≠ ∅ [sic nel quaderno: dev'essere = ∅ — refuso]. ℕ = P ∪ D (pari e dispari).
