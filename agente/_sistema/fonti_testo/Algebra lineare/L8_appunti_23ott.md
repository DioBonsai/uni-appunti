# Algebra lineare, lezione 8: Matrici I (23 ottobre 2026): appunti a mano di Emanuele
(Trascrizione delle 3 pagine di `fonti/Algebra lineare/23 Ottobre.pdf`; le formule sono rese in testo. Tra parentesi quadre le mie note di lettura. Gli evidenziatori gialli sono segnalati.)

## Pagina 1
**Lezione 8: Matrici, I**
**Prev.** M(m, n, 𝕂) = { A = (a_11 … a_1n ; … ; a_m1 … a_mn) | a_ij ∈ 𝕂 }. M(n) = M(n, n, 𝕂) → **matrici quadrate**.
A + B = (a_11 + b_11 … ; … ; a_m1 + b_m1 … a_mn + b_mn); per λ ∈ 𝕂: λ·A = (λ a_11 … λ a_1n ; … ; λ a_m1 … λ a_mn).

### Trasposta
A ∈ M(m, n) → ᵗA ∈ M(n, m). **La trasposta è la matrice tc (tale che) (ᵗA)_ij = A_ji.**
es. A = ( 3 0 ; 2 5 ; 1 6 ) → ᵗA = ( 3 2 1 ; 0 5 6 ). [Evidenziati in giallo: l'elemento 2 di A (riga 2, colonna 1) e l'elemento 2 di ᵗA (riga 1, colonna 2); a lato: «→ a_{2,1} = a_{1,2}» come illustrazione dello scambio degli indici.]

**Proprietà**
1. ᵗ(ᵗA) = A.
2. ᵗ(A + B) = ᵗA + ᵗB.
3. ᵗ(λA) = λ · ᵗA.
4. A ∈ M(n) ⟹ ᵗA ∈ M(n), e A = ᵗA sse A è **simmetrica**. [Scritto «sse V è simmetrica»: probabile refuso per A.]

### Notazione
Data A ∈ M(m, n, 𝕂), chiamiamo A¹, …, Aⁿ ∈ 𝕂ᵐ le colonne; scriviamo A = (A¹ | A² | … | Aⁿ).
Similmente A_1, …, A_m ∈ 𝕂ⁿ sono le righe di A, e scriviamo A come la colonna di blocchi (A_1 ; A_2 ; … ; A_m).

### Rango
A ∈ M(m, n, 𝕂), A = (A¹ | … | Aⁿ).
**RANGO (per colonne)** di A è **rk(A) = dimensione Span(A¹, …, Aⁿ)**.
**Prop.**
1. rk(A) è il massimo numero di colonne linearmente indipendenti.
2. rk(A) = rk(ᵗA).
→ **Conseguenze:** rk(A) ≤ n; rk(A) = rk(ᵗA) ≤ m.
**es.** 0 ∈ M(m, n, 𝕂) (matrice nulla): rk(0) = dim Span(0¹ | … | 0ⁿ) con 0ʲ = (0 ; … ; 0) = 0_{𝕂ᵐ}, quindi = dim Span(0, …, 0) = 0, perché Span(0_{𝕂ᵐ}, …, 0_{𝕂ᵐ}) = { λ_1 0, …, λ_n 0 } = {0}. [Nel foglio gli spazi sono scritti 𝕂ⁿ; per le colonne di una matrice m × n sarebbe 𝕂ᵐ.]

## Pagina 2
**es. 2** A = ( 1 1 ; 1 1 ; 1 1 ) ∈ M(3, 2) → rk(A) ≤ min(3, 2) = 2; rk(A) = dim Span( (1,1,1), (1,1,1) ) = 1.
**es. 3** I_n ∈ M(n), I_n = matrice identità (1 sulla diagonale, 0 altrove); (I_n)¹ = (1, 0, …, 0) = e_1 ∈ 𝕂ⁿ. rk(I_n) = dim Span(e_1, …, e_n) = dim 𝕂ⁿ = n, perché e_1, …, e_n sono generatori di 𝕂ⁿ.
**Esempio con righe e colonne.** A = ( 3 1 2 ; 1 0 1 ), rk(A) = 2. ᵗA = ( 3 1 ; 1 0 ; 2 1 ). [Freccia dalla prima colonna: (3 ; 1) = (1 ; 0) + (2 ; 1): la prima colonna è somma delle altre due, quindi le colonne sono dipendenti, e due sono indipendenti.]
**Prop.** V spazio vettoriale di dimensione n → se m > n, allora m vettori v_1, …, v_m di V sono **linearmente dipendenti** [evidenziata in giallo la parola «dipendenti»].

### Prodotti tra matrici
**Def.** A ∈ M(m, n, 𝕂), B ∈ M(n, p, 𝕂). Il prodotto AB ∈ M(m, p, 𝕂) è la matrice con
(A·B)_ij = a_i1 b_1j + a_i2 b_2j + … + a_in b_nj = Σ_{k=1}^{n} a_ik b_kj, per 1 ≤ i ≤ m e 1 ≤ j ≤ p.
**es.** A = ( 3 1 1 ; 2 0 5 ) ∈ M(2, **3**), B = ( 1 2 ; −1 0 ) ∈ M(**2**, 2): **A·B non esiste (3 ≠ 2)**.
C = ( 2 −1 ; 1 1 ; 0 1 ) [nel foglio una volta l'ultima riga è (0 0), ma nel calcolo si usa (0 1)]: A·C ∈ M(2, 2):
A·C = ( 3 1 1 ; 2 0 5 ) · ( 2 −1 ; 1 1 ; 0 1 ) = ( 6 + 1 + 0 , −3 + 1 + 1 ; 4 + 0 + 0 , −2 + 0 + 5 ) = ( 7 −1 ; 4 3 ). [Il «6+10» e il «17» del foglio sono 6 + 1 + 0 = 7.]

**Proprietà**
1. A ∈ M(m, n), B ∈ M(n, p), C ∈ M(p, q) → A·(B·C) = (A·B)·C — **ASSOCIATIVA**.
2. A ∈ M(m, n), B, C ∈ M(n, p) → A·(B + C) = A·B + A·C — **DISTRIBUTIVA**.
3. A ∈ M(m, n), B ∈ M(n, p), λ ∈ 𝕂 → λ(A·B) = (λA)·B = A·(λB).
4. ᵗ(A·B) = ᵗB · ᵗA.

**Osservazione:** A·B ≠ B·A.
- es. 1: A = ( 2 1 ; 1 2 ), B = ( 3 ; −1 ): A·B = ( 5 ; 1 ); **B·A NON si può fare**.
- es. 2: A = ( 1 ; 2 ) (2 × 1), B = ( 0, 3 ) (1 × 2): A·B = ( 0 3 ; 0 6 ) (2 × 2); B·A = ( 6 ) (1 × 1). [Disegnati i due prodotti riga per colonna con le frecce.]

## Pagina 3
### Traccia
**Def.** A ∈ M(n), **traccia** di A: tr(A) = a_11 + a_22 + … + a_nn = Σ_{k=1}^{n} a_kk.
**es.** tr( 3 0 1 ; 2 1 0 ) → non è quadrata → **NON BEN DEFINITA**.
tr( 3 0 1 ; −1 −2 −3 ; 4 0 5 ) = 3 − 2 + 5 (= 6) [diagonale evidenziata in giallo].
**Proprietà:** se A, B ∈ M(n) → A·B ∈ M(n) e B·A ∈ M(n) ⟹ **tr(AB) = tr(BA)**.
[La pagina finisce qui; l'ultimo foglio è vuoto.]
