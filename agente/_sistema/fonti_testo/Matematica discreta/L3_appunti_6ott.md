# Matematica discreta, lezione 3 (6 ottobre 2026): appunti a mano
(trascrizione dell'appunto manoscritto, prof. Mori; fonte: L3_appunti_6ott.pdf, 2 pagine)

## Partizioni
Insieme S. Una **partizione** di S è una collezione di sottoinsiemi tc: 1) ∪Aᵢ = S (ricoprimento); 2) ∀i, Aᵢ ≠ ∅; 3) ∀i ≠ j, Aᵢ ∩ Aⱼ = ∅.
ℤ = P ∪ D (numeri pari, numeri dispari). ℕ = {0,…,10} ∪ {10,…,20} ∪ {20,…,30} ∪ … → ricoprimento ma non partizione.

## Insieme quoziente
Se ho una partizione {Aᵢ} di S posso considerare l'insieme Q = {A₁, A₂, …}: si dice **insieme quoziente** (associato alla partizione).

## Confrontare 2 elementi di S
Sia S un insieme. Considero S × S = {(x,y) | x,y ∈ S} (coppie ordinate: (x,y) ≠ (y,x)). Dico che una **relazione** in S è un sottoinsieme R ⊆ S × S. Dico che x, y ∈ S sono in relazione se (x,y) ∈ R: xRy.
Es. 1) descrivere la relazione ≤ in ℤ: vuol dire considerare il sottoinsieme R = {(m,n) | m ≤ n} ⊆ ℤ × ℤ. (1,3) ∈ R; (2,−4) ∉ R.
Dirò che R soddisfa la proprietà:
- **RIFLESSIVA** ∀x ∈ S, xRx
- **SIMMETRICA** ∀x,y ∈ S, xRy ⟹ yRx
- **ANTISIMMETRICA** ∀x,y ∈ S, xRy ∧ yRx ⟹ x = y
- **TRANSITIVA** ∀x,y,z ∈ S, xRy ∧ yRz ⟹ xRz
Es.: mRn se m|n (m divide n): antisimmetrica in ℕ, non lo è in ℤ (es. −3|9, 2∤5).

**Def.** Sia S un insieme e R ⊆ S × S una relazione in S. Dirò che R è un'**equivalenza** se R è: riflessiva, simmetrica e transitiva.

## Classi di equivalenza
S insieme, R equivalenza in S. Prendo x ∈ S: Cₓ = {y ∈ S tc xRy} (≠ ∅, perché xRx) = **classe di equivalenza** di x. Facendo variare x otteniamo che S = ∪_{x∈S} Cₓ (ricoprimento). (Disegno "sbagliato": classi che si sovrappongono parzialmente.)
Siano x, y ∈ S e Cₓ, C_y le loro classi. Se Cₓ ∩ C_y = ∅ OK! Supponiamo Cₓ ∩ C_y ≠ ∅: sia z ∈ Cₓ ∩ C_y → xRz, yRz → (simmetria) zRy, (transitività) xRz ∧ zRy ⟹ xRy ⟹ C_y ⊆ Cₓ (e per simmetria Cₓ ⊆ C_y).
Quindi ho dimostrato che se x ≠ y ho solo due possibilità: Cₓ ∩ C_y = ∅ oppure Cₓ = C_y.
**Questo dice che le classi di equivalenza formano una partizione.**

## Viceversa
Data una partizione {Aᵢ} di S posso definire una relazione xRy se x, y ∈ allo stesso Aᵢ. **Esercizio:** dimostrare che questa è un'equivalenza.

## Funzioni
Grafico di una funzione f: ℝ → ℝ: punti (a, f(a)); G ⊆ ℝ × ℝ (una "curva" di coppie (a,b) per cui per ogni a esiste un solo b).
