# 27. La Trasposta di una Matrice e le Notazioni per Righe e Colonne
## Dove siamo e dove si va
Finora le matrici sono servite come esempio di spazio vettoriale: l'insieme M(m, n, 𝕂) delle matrici con m righe e n colonne a coefficienti in 𝕂, con la somma entrata per entrata e il prodotto per uno scalare. Le matrici quadrate, cioè con tante righe quanto colonne, formano l'insieme M(n) = M(n, n, 𝕂). Come sottolineato a lezione, in realtà alle matrici si associano tante altre proprietà e numeri che danno informazioni su di esse, e si possono fare altre operazioni tra matrici. Le matrici sono una rappresentazione concreta di un concetto che verrà più avanti, quello di **applicazione lineare**, che sarà il modo in cui gli spazi vettoriali comunicano fra loro. Oggi si studiano la trasposta, il rango, il prodotto fra matrici e la traccia.

## La trasposta
**Definizione.** Sia A ∈ M(m, n, 𝕂), con m righe e n colonne. La **trasposta** di A è la matrice ᵗA ∈ M(n, m, 𝕂) (si legge «A trasposta» e si scrive con una t minuscola in alto a sinistra) che ha n righe e m colonne, cioè righe e colonne scambiate, ed è definita da
(ᵗA)_{ij} = A_{ji}
(le entrate di una matrice si indicano indifferentemente con A_{ij} o con a_{ij}: sono la stessa cosa).

**In parole povere:** la trasposta si ottiene facendo diventare colonne le righe e righe le colonne: la prima riga di A diventa la prima colonna di ᵗA, la seconda riga diventa la seconda colonna, e così via. È come ribaltare la tabella lungo la diagonale.

Per esempio, se A = ( 3 0 ; 2 5 ; 1 6 ), una matrice con tre righe e due colonne, la trasposta ha due righe e tre colonne: la prima riga di ᵗA ha le entrate in cui i vale 1, cioè la prima colonna di A, quindi (3, 2, 1); la seconda riga di ᵗA è la seconda colonna di A, quindi (0, 5, 6). In simboli ᵗA = ( 3 2 1 ; 0 5 6 ). Come controllo: l'entrata in riga 2 e colonna 1 di A, che vale 2, è uguale all'entrata in riga 1 e colonna 2 di ᵗA, perché A_{21} = (ᵗA)_{12}.

![La trasposta scambia righe e colonne: l'elemento 2 di A (riga 2, colonna 1) finisce nella riga 1, colonna 2 di ᵗA.](figure/alg/trasposta_esempio.png|11)

## Proprietà della trasposta
1. **ᵗ(ᵗA) = A.** Scambiando righe e colonne e poi di nuovo righe e colonne si torna alla matrice di partenza.
2. **ᵗ(A + B) = ᵗA + ᵗB.** La trasposta di una somma è la somma delle trasposte.
3. **ᵗ(λA) = λ · ᵗA**, per ogni scalare λ ∈ 𝕂. Come sottolineato a lezione, le proprietà 2 e 3 dicono che la trasposta si comporta bene rispetto alla somma e al prodotto per uno scalare.
4. Se A è una matrice quadrata, cioè A ∈ M(n), anche ᵗA ∈ M(n). Inoltre **A = ᵗA se e solo se A è simmetrica**; e, come nel cap. 21, A è **antisimmetrica** se e solo se ᵗA = −A.

**In parole povere:** una matrice è simmetrica quando coincide con la sua trasposta, cioè quando è uguale a sé stessa «ribaltata» lungo la diagonale.

## Notazione per colonne e per righe
Sia A ∈ M(m, n, 𝕂). Ciascuna colonna di A è un vettore colonna con m entrate, cioè un vettore di 𝕂^{m}. Le colonne si indicano con **apici**: A¹, A², …, Aⁿ. Si può allora pensare A come l'insieme delle sue colonne e scrivere
A = ( A¹ | A² | … | Aⁿ ).

Allo stesso modo le **righe** si indicano con **pedici**: A_{1}, A_{2}, …, A_{m}; ciascuna riga è un vettore riga con n entrate (un elemento di 𝕂^{n}) e A si può scrivere come la colonna formata dalle sue righe A_{1}, A_{2}, …, A_{m}, una sotto l'altra. Attenzione ai pedici: **un solo pedice** (A_{i}) indica una riga intera, **due pedici** (A_{ij}) indicano una singola entrata. Come sottolineato a lezione, la notazione per righe si userà poco: quella per colonne servirà spesso, per esempio nel capitolo seguente, dove si studia il rango.

**In parole povere:** A¹, A², … sono i «mattoni verticali» di A (le colonne) e A_{1}, A_{2}, … i «mattoni orizzontali» (le righe); l'apice non è una potenza, è solo un'etichetta di posizione.

Il capitolo successivo introduce il rango, un numero che si associa a ogni matrice.
