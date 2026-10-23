# 28. Il Rango di una Matrice
## L'idea
Nei numeri c'è lo 0, che è speciale: qualunque numero moltiplicato per 0 dà 0, e lo 0 non ha inverso; tutti gli altri numeri sono invertibili. Anche per le matrici c'è la matrice nulla, quella con tutti gli zeri. Ci saranno poi matrici non nulle che sono «molto speciali» (come si vedrà, invertibili in qualche senso), e in mezzo tutto un mondo di matrici intermedie. Un modo per misurare quanto una matrice è lontana dall'essere la matrice nulla è il **rango**. Come sottolineato a lezione, il rango si può pensare come un numero che dice quanto siamo lontani dalla matrice nulla.

## La definizione
Sia A ∈ M(m, n, 𝕂), scritta come insieme delle sue colonne: A = ( A¹ | … | Aⁿ ), con A^{j} ∈ 𝕂^{m}.

**Definizione.** Il **rango** (per colonne) di A è il numero intero
rk(A) = dim Span( A¹, …, Aⁿ ),
cioè la dimensione dello spazio generato dalle colonne di A.

**In parole povere:** il rango dice quante «direzioni indipendenti» generano le colonne di una matrice: è la dimensione dello spazio che si può costruire combinando le sue colonne.

Per capirlo: le colonne sono vettori di 𝕂^{m}; lo Span di alcuni vettori è l'insieme di tutte le loro combinazioni lineari ed è uno spazio vettoriale; la dimensione di uno spazio vettoriale è il numero di elementi di una sua base, ed è un numero intero. Quel numero intero è il rango.

## Due fatti fondamentali
**Proposizione 1.** rk(A) è il **massimo numero di colonne linearmente indipendenti** di A.

**Proposizione 2.** rk(A) = rk(ᵗA).

Poiché la trasposta scambia righe e colonne, calcolare il rango di ᵗA vuol dire calcolare la dimensione dello Span delle righe di A. La proposizione 2 dice quindi che la dimensione dello Span delle colonne e quella dello Span delle righe sono uguali, e che il massimo numero di colonne indipendenti è uguale al massimo numero di righe indipendenti.

Un procedimento per calcolare il rango segue dalla proposizione 1: si guardano le colonne; se sono tutte indipendenti il rango è n; altrimenti ce n'è una che dipende dalle altre, la si toglie e si ripete la verifica finché le colonne rimaste sono indipendenti; il rango è allora il numero di colonne rimaste. Come sottolineato a lezione, in futuro si vedrà un algoritmo molto migliore per calcolare il rango.

## Conseguenze: un limite al rango
- Il rango di A è **al più n**, il numero di colonne: il massimo numero di colonne indipendenti non può superare il numero di colonne (proposizione 1).
- Per la proposizione 2, rk(A) = rk(ᵗA); ma ᵗA ha tante colonne quante sono le righe di A, quindi rk(ᵗA) ≤ m. Quindi **rk(A) ≤ m**.

Come sottolineato a lezione, il rango non può superare né il numero di colonne né il numero di righe: in una matrice con mille colonne e due righe il rango è al più 2. Sapere questo limite non dice però quanto vale il rango: per una matrice 1 000 000 × 1 000 000 il rango è al più un milione, ma una cosa è sapere un limite superiore e un'altra dire esattamente quanto vale.

## Esempi
**La matrice nulla.** Sia 0 ∈ M(m, n, 𝕂) la matrice con tutti zeri. Ogni colonna è il vettore nullo 0 di 𝕂^{m}, quindi il rango è dim Span(0, …, 0). Lo Span di vettori nulli è l'insieme delle combinazioni λ₁·0 + … + λ_{n}·0, che per la distributività si raccolgono in (λ₁ + … + λ_{n})·0 = 0: è lo spazio vettoriale che contiene solo lo zero. In questo spazio non c'è nessun vettore linearmente indipendente (il vettore nullo da solo è dipendente), e a lezione si conclude che il suo rango, cioè la sua dimensione, è 0. Quindi **rk(0) = 0**. Come sottolineato a lezione, la matrice nulla è l'unica matrice di rango 0, ed è in questo senso che il rango misura la lontananza dalla matrice nulla.

**La matrice di tutti uni.** Sia A = ( 1 1 ; 1 1 ; 1 1 ) ∈ M(3, 2). Per quanto visto, rk(A) ≤ min(3, 2) = 2. Calcoliamolo davvero: le due colonne sono uguali, (1, 1, 1) e (1, 1, 1); lo Span è l'insieme dei multipli di (1, 1, 1), che ha come base il solo (1, 1, 1): dimensione 1. Si arriva alla stessa conclusione con la proposizione 1: le due colonne sono una multipla dell'altra, quindi dipendenti; se ne toglie una e la colonna rimasta, essendo non nulla, è da sola indipendente; il massimo numero di colonne indipendenti è 1. Quindi **rk(A) = 1**. Come sottolineato a lezione, per la proposizione 2 si otterrebbe lo stesso numero usando le righe.

**La matrice identità.** La matrice identità I_{n} ∈ M(n) ha 1 sulla diagonale e 0 altrove. Le sue colonne sono i vettori e₁, e₂, …, e_{n} della base canonica di 𝕂^{n}, che sono in particolare dei generatori di 𝕂^{n}: il loro Span è tutto 𝕂^{n}, che ha dimensione n. Quindi **rk(I_{n}) = n**.

**In parole povere:** la matrice identità è quella con 1 sulla diagonale e 0 altrove, e ha rango massimo: nessuna delle sue colonne si può ricostruire con le altre.

## Quando sembra indipendente ma non lo è
Si consideri A = ( 3 1 2 ; 1 0 1 ) ∈ M(2, 3): ha tre colonne, (3, 1), (1, 0) e (2, 1), che sembrano molto diverse l'una dall'altra, quindi viene da pensare che siano indipendenti e che il rango sia 3. Ma il rango è al più 2, perché le colonne vivono in 𝕂², che ha dimensione 2, e vale esattamente 2: (1, 0) e (2, 1) non sono una multipla dell'altra, quindi sono indipendenti. Infatti la prima colonna è la somma delle altre due: (3, 1) = (1, 0) + (2, 1). Come sottolineato a lezione, il fatto che tre colonne non si assomiglino non vuol dire che siano linearmente indipendenti.

**Proposizione.** Sia V uno spazio vettoriale di dimensione n. Se v₁, …, v_{m} sono m vettori di V con m > n, allora sono **linearmente dipendenti**.

**In parole povere:** in uno spazio con n «direzioni» non si possono avere più di n vettori indipendenti.

Il motivo: se fossero indipendenti, li si potrebbe completare a una base di V con almeno m > n elementi (come detto a lezione, un insieme indipendente si può sempre arricchire fino a ottenere una base), e questo è impossibile perché ogni base di V ha esattamente n elementi (cap. 26).

Il capitolo seguente introduce il prodotto fra matrici.
