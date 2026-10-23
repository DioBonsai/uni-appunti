# Algebra lineare, Lezione 8: Matrici I (dispensa MDAG Parte II, Buzano e Radeschi, cap. 8, pagg. 36-40)

Fonte: pagine 36-40 di `fonti/Algebra lineare/dispense_MDAG.pdf`, lette dalle immagini delle pagine (le formule sono rese in testo). **Non esiste una registrazione 2025 su Moodle per questa lezione** (nel corso mancano i video delle lezioni 4, 8 e 9) **e non c'è un audio 2026** nelle cartelle dei file: per ora l'unica fonte della lezione 8 è questa dispensa. Le lavagne e l'audio vanno aggiunti se arriveranno (per esempio dalla lezione in classe).

## 8 Matrici I
Richiamo: per un campo 𝕂, M(m, n, 𝕂) è l'insieme delle matrici con m righe e n colonne a coefficienti in 𝕂. Per A = (a_ij), B = (b_ij) ∈ M(m, n, 𝕂) e λ ∈ 𝕂 sono definite
- **A + B** = (a_ij + b_ij),
- **λA** = (λ·a_ij).
Con queste operazioni M(m, n, 𝕂) è uno spazio vettoriale su 𝕂 di **dimensione mn** (Esercizio 7.13). In questa lezione si studiano altre operazioni sulle matrici.

## 8.A Trasposta di una matrice
**Definizione 8.1.** La **trasposta** di A ∈ M(m, n, 𝕂) è la matrice ᵗA ∈ M(n, m, 𝕂) definita scambiando righe e colonne: (ᵗA)_ij = A_ji.

**Esempio 8.2.** A = ( 2 1 ; −1 0 ; 5 7 ) ⟹ ᵗA = ( 2 −1 5 ; 1 0 7 ).

Proprietà:
- ᵗ(A + B) = ᵗA + ᵗB e ᵗ(λA) = λ(ᵗA);
- se A ∈ M(n), allora anche ᵗA ∈ M(n);
- A ∈ M(n) è **simmetrica** ⟺ ᵗA = A; A ∈ M(n) è **antisimmetrica** ⟺ ᵗA = −A.

## 8.B Rango di una matrice
Sia A una matrice m × n a coefficienti in 𝕂; con A¹, …, Aⁿ si indicano le colonne di A (ciascuna è un vettore di 𝕂ᵐ).

**Definizione 8.3.** Il **rango** di A (o rango per colonne di A) è la dimensione dello spazio Span(A¹, …, Aⁿ) ⊂ 𝕂ᵐ. Si indica con rk(A).

**Proposizione 8.4.** Il rango di A è il **massimo numero di colonne linearmente indipendenti** di A. (Segue da un'osservazione della Lezione 7.)

**Definizione 8.5.** Il **rango per righe** di A è la dimensione dello spazio generato dalle righe, Span(A₁, …, A_m) ⊂ 𝕂ⁿ. In altre parole è il rango della trasposta ᵗA.

**Proposizione 8.6.** Per ogni matrice A il rango per righe è uguale al rango per colonne. Vale quindi rk(ᵗA) = rk(A).

## 8.C Prodotto fra matrici
**Definizione 8.7.** Se A è una matrice m × n e B è una matrice n × p, il **prodotto AB** è la matrice m × p il cui elemento (AB)_ij è
(AB)_ij = Σ_{k=1}^{n} A_ik B_kj = A_i1 B_1j + ⋯ + A_in B_nj.
Si chiama **prodotto riga per colonna** perché (AB)_ij si ottiene facendo un opportuno prodotto fra la riga i-esima A_i di A e la colonna j-esima Bʲ di B (Figura 7: una riga di A e una colonna di B che «si incrociano» nella casella (i, j) del risultato).

**Esempio 8.8.** A = ( 1 2 ; −1 1 ; 0 3 ) (3 × 2), B = ( −1 2 0 1 ; 3 0 3 0 ) (2 × 4). Allora
AB = ( 5 2 6 1 ; 4 −2 3 −1 ; 9 0 9 0 ) (3 × 4).
Si può fare AB perché il numero di colonne di A (2) è uguale al numero di righe di B (2). Non si può fare BA, perché le colonne di B sono 4 e le righe di A sono 3.

**Esempio 8.9.** Se A è m × n e x è n × 1 (un vettore colonna x ∈ 𝕂ⁿ), allora Ax è m × 1, cioè un vettore colonna di 𝕂ᵐ. Per esempio ( 1 2 ; −1 1 ; 0 3 ) · ( 1 ; −1 ) = ( −1 ; −2 ; −3 ).

**Attenzione.** Se A e B sono due matrici n × n, sono definiti sia AB sia BA, ma in generale **non sono uguali**: il prodotto **non è commutativo**.

**Esempio 8.10.** A = ( 1 0 ; 0 0 ), B = ( 0 1 ; 0 0 ). Allora AB = ( 0 1 ; 0 0 ) = B e BA = ( 0 0 ; 0 0 ) = 0. Quindi AB ≠ BA.

**Proposizione 8.11.** Per ogni A, B, C per cui prodotti e somme hanno senso e per ogni λ ∈ 𝕂:
1. A(BC) = (AB)C (**associatività**);
2. A(B + C) = AB + AC e (A + B)C = AC + BC (**distributività**);
3. λ(AB) = (λA)B = A(λB).

## 8.D Traccia di una matrice quadrata
**Definizione 8.12.** La **traccia** di una matrice quadrata A ∈ M(n) è il numero tr A = A_11 + ⋯ + A_nn, cioè la somma dei numeri sulla diagonale principale.

**Proposizione 8.13.** Se A, B ∈ M(n), vale tr(AB) = tr(BA).
*Spiegazione.* tr(AB) = Σ_{i,j=1}^{n} A_ij B_ji = Σ_{j,i=1}^{n} B_ji A_ij = tr(BA).

## 8.E Esercizi
- **Esercizio 8.14.** Dimostrare che ᵗ(AB) = ᵗB ᵗA.
- **Esercizio 8.15.** A = ( 1 2 ; 3 4 ; 5 6 ), B = ( 1 2 3 ; 4 5 6 ). Calcolare AB e BA, e la traccia di AB e di BA.
- **Esercizio 8.16.** A = ( 1 2 3 ; 4 5 6 ; 7 8 9 ), B = ( 1 0 1 ; 0 1 0 ; 1 0 1 ), C = ( −1 0 0 ; 0 0 −1 ; 0 −1 0 ). Calcolare (AB)C, A(BC), (BA)C e C(BA).
