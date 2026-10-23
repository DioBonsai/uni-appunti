# 30. Proprietà del Prodotto, Non Commutatività e Traccia
## Le proprietà del prodotto
Nelle proprietà seguenti le dimensioni delle matrici sono scelte in modo che tutte le operazioni abbiano senso: le somme richiedono matrici della stessa dimensione, i prodotti richiedono che le colonne della prima siano quante le righe della seconda. Come sottolineato a lezione, tutta l'attenzione sulle dimensioni serve solo a far sì che le uguaglianze che si scrivono abbiano senso.
1. **Associativa.** Se A ∈ M(m, n), B ∈ M(n, p) e C ∈ M(p, q), allora A·(B·C) = (A·B)·C: è la stessa matrice sia che si moltiplichi prima B per C e poi per A, sia che si moltiplichi prima A per B e poi per C.
2. **Distributiva.** Se A ∈ M(m, n) e B, C ∈ M(n, p), allora A·(B + C) = A·B + A·C (e analogamente (A + B)·C = A·C + B·C). Le matrici AB e AC non sono la stessa matrice, ma hanno le stesse dimensioni, e si possono quindi sommare.
3. **Con uno scalare.** Se A ∈ M(m, n), B ∈ M(n, p) e λ ∈ 𝕂, allora λ(A·B) = (λA)·B = A·(λB).
4. **Con la trasposta.** ᵗ(A·B) = ᵗB · ᵗA: la trasposta di un prodotto è il prodotto delle trasposte **in ordine inverso**.

**In parole povere:** il prodotto fra matrici si può raggruppare e distribuire come quello fra numeri, ma l'ordine dei fattori conta, e la trasposta lo inverte.

**Dimostrazione della proprietà 4.** L'entrata (i, j) di ᵗ(AB) è l'entrata (j, i) di AB, cioè Σ_{k} A_{jk}B_{ki}. L'entrata (i, j) di ᵗB·ᵗA è Σ_{k} (ᵗB)_{ik}(ᵗA)_{kj} = Σ_{k} B_{ki}A_{jk}, che è la stessa somma con i fattori scritti in ordine diverso. ∎

## Il prodotto non è commutativo
Al contrario di tutte le altre moltiplicazioni viste finora, il prodotto fra matrici **non è commutativo**: AB e BA in generale non sono la stessa matrice. Può addirittura accadere che AB si possa fare e BA no.

**Esempio 1.** A = ( 2 1 ; 1 2 ) ∈ M(2, 2) e B = ( 3 ; −1 ) ∈ M(2, 1). Allora AB ha 2 righe e 1 colonna e vale ( 2·3 + 1·(−1) ; 1·3 + 2·(−1) ) = ( 5 ; 1 ). Invece **BA non si può fare**: B ha una sola colonna, mentre A ha due righe.

**Esempio 2.** A = ( 1 ; 2 ) ∈ M(2, 1) e B = ( 0 3 ) ∈ M(1, 2). Questa volta si possono fare entrambi i prodotti, ma hanno dimensioni diverse: AB è una matrice 2 × 2 e vale ( 0 3 ; 0 6 ), mentre BA è una matrice 1 × 1 e vale ( 0·1 + 3·2 ) = ( 6 ). Come sottolineato a lezione, ci sono anche casi in cui AB e BA hanno le stesse dimensioni e sono comunque diverse.

**Esempio 3.** A = ( 1 0 ; 0 0 ) e B = ( 0 1 ; 0 0 ). Allora AB = ( 0 1 ; 0 0 ) = B e BA = ( 0 0 ; 0 0 ) = 0: due matrici 2 × 2 con AB ≠ BA.

## La traccia
**Definizione.** Sia A ∈ M(n) una matrice **quadrata**. La **traccia** di A è la somma delle entrate lungo la diagonale principale:
tr(A) = A_{11} + A_{22} + … + A_{nn} = Σ_{k=1}^{n} A_{kk}.

**In parole povere:** la traccia si ottiene sommando i numeri sulla diagonale che va dall'alto a sinistra al basso a destra.

La traccia ha senso solo sulle matrici quadrate: per esempio per A = ( 3 0 1 ; 2 1 0 ), che non è quadrata, la traccia **non è ben definita**. Per A = ( 3 0 1 ; −1 −2 −3 ; 4 0 5 ), la diagonale principale contiene 3, −2 e 5, quindi tr(A) = 3 − 2 + 5 = 6. Come sottolineato a lezione, la diagonale principale è quella che parte dall'alto a sinistra: l'altra diagonale ha un uso diverso, che si vedrà.

**Proposizione.** Se A, B ∈ M(n), allora **tr(AB) = tr(BA)**.

Se A e B sono entrambe n × n, si possono fare sia AB sia BA, e sono entrambe matrici n × n; come visto, non sono in generale uguali, ma **hanno sempre la stessa traccia**.

**Dimostrazione.** tr(AB) = Σ_{i=1}^{n} (AB)_{ii} = Σ_{i=1}^{n} Σ_{k=1}^{n} A_{ik}B_{ki} = Σ_{k=1}^{n} Σ_{i=1}^{n} B_{ki}A_{ik} = Σ_{k=1}^{n} (BA)_{kk} = tr(BA). Si sono scambiati l'ordine delle due somme e l'ordine dei fattori nel prodotto fra due numeri, che è commutativo. ∎

## Un esercizio di verifica
Siano A = ( 1 2 ; 3 4 ; 5 6 ) ∈ M(3, 2) e B = ( 1 2 3 ; 4 5 6 ) ∈ M(2, 3). Si possono fare sia AB sia BA, ma hanno dimensioni diverse (3 × 3 e 2 × 2):
- AB = ( 1·1+2·4 , 1·2+2·5 , 1·3+2·6 ; 3·1+4·4 , 3·2+4·5 , 3·3+4·6 ; 5·1+6·4 , 5·2+6·5 , 5·3+6·6 ) = ( 9 12 15 ; 19 26 33 ; 29 40 51 );
- BA = ( 1·1+2·3+3·5 , 1·2+2·4+3·6 ; 4·1+5·3+6·5 , 4·2+5·4+6·6 ) = ( 22 28 ; 49 64 ).

Le due matrici sono molto diverse, ma tr(AB) = 9 + 26 + 51 = 86 e tr(BA) = 22 + 64 = 86. Qui A e B non sono quadrate, ma AB e BA sì: la proposizione è stata enunciata per matrici quadrate dello stesso ordine, ma lo stesso calcolo della dimostrazione (scambiare le due somme) funziona anche in questo caso, e l'uguaglianza delle tracce si conferma.
