# Matematica discreta, lezione 10 (22 ottobre 2026): appunti a mano di Emanuele
(Trascrizione della pagina unica di `fonti/Matematica discreta/22 Ottobre.pdf`, scansione di 1 pagina; le formule sono rese in testo. Tra parentesi quadre le mie note di lettura.)

## Coefficienti binomiali
C(n, k) = n! / ( k! (n − k)! ), con n ≥ 0 e 0 ≤ k ≤ n.

## Proprietà
**1)** C(n, 0) = C(n, n) = 1.
- C(n, 0) = n! / ( 0! · (n − 0)! ) = 1, perché 0! = 1 e n! si semplifica con (n − 0)!.
- C(n, 1) = n! / ( 1! · (n − 1)! ) = n · (n − 1)! / ( 1 · (n − 1)! ) = n.

**2) Simmetria: C(n, k) = C(n, n − k).**
Dimostrazione algebrica: C(n, n − k) = n! / ( (n − k)! · (n − (n − k))! ) = n! / ( (n − k)! · k! ), che è uguale a C(n, k).
Dimostrazione con una funzione. A insieme con |A| = n. A_k = { S ⊆ A | |S| = k } e A_{n−k} = { T ⊆ A | |T| = n − k }. Disegno: un cerchio A diviso in S e S' (il complementare).
F: A_k → A_{n−k}, **F(S) = C_A(S)** (complementare di S in A).
Si cerca la funzione inversa di F: G: A_{n−k} → A_k, **G(T) = C_A(T)**.
- G ∘ F (S) = G(C_A(S)) = C_A(C_A(S)) = S;
- F ∘ G (T) = F(C_A(T)) = C_A(C_A(T)) = T.
Quindi G = F⁻¹ e **F è biettiva**; ne segue |A_k| = |A_{n−k}|, cioè C(n, k) = C(n, n − k).

## Formula di Stiefel
Per n ≥ 1 e 1 ≤ k ≤ n:  **C(n − 1, k − 1) + C(n − 1, k) = C(n, k).**

Dimostrazione algebrica:
(n − 1)! / ( (k − 1)! (n − k)! ) + (n − 1)! / ( k! (n − 1 − k)! )
= [ k · (n − 1)! + (n − k) · (n − 1)! ] / ( k! (n − k)! )
= (k + n − k) · (n − 1)! / ( k! (n − k)! )
= n! / ( k! (n − k)! ) = C(n, k).
[Nello scritto a mano l'ultimo passaggio è letto così: il numeratore diventa (k + n − k)(k − 1)!, forse un refuso per (n − 1)!.]

Dimostrazione combinatoria. |A| = n; si fissa un elemento x ∈ A e si pone **B = C_A({x}) = A ∖ {x}**, con |B| = n − 1. Disegno: cerchio A con dentro S (contenente x) e T (non contenente x).
I sottoinsiemi di A sono di 2 tipi:
1. **x ∈ S**;
2. **x ∉ T**.
{Sottoinsiemi di A} = {1° tipo} ∪ {2° tipo}.
I sottoinsiemi di A con k elementi sono C(n, k).
- **1° tipo** (x ∈ S): |S ∩ B| = k − 1 (gli altri k − 1 elementi si scelgono tra i rimanenti n − 1; [la pagina si ferma qui: il conteggio completo è C(n − 1, k − 1)]).
- **2° tipo** (x ∉ T): [non scritto; per completezza sono k elementi scelti dagli n − 1 elementi di B, cioè C(n − 1, k)].
