# 26. Dimensione e Basi Canoniche
## Tutte le basi hanno la stessa cardinalità
**Teorema.** Se uno spazio vettoriale V ha una base formata da n vettori, allora ogni altra base di V ha esattamente n vettori (due basi qualunque hanno la stessa **cardinalità**, cioè lo stesso numero di elementi: contano quanti vettori ci sono, non quali).

Il teorema non viene dimostrato; è fondamentale perché permette di dare una definizione rigorosa a un'idea intuitiva, quella di dimensione.

**Definizione.** Uno spazio vettoriale ha **dimensione finita** se ammette una base finita. In tal caso la **dimensione** di V, che si indica con dim V, è il numero di elementi di una sua base. Se V non ha una base finita si dice che ha dimensione infinita.

**In parole povere:** la dimensione è il numero di «direzioni indipendenti» dello spazio, cioè quanti vettori servono per descrivere ogni punto senza sprechi. Si usa una base qualunque: il teorema garantisce che il numero è sempre lo stesso.

Da qui in avanti si studiano quasi solo gli spazi di dimensione finita.

## Come si calcola una dimensione
Per calcolare la dimensione di uno spazio, si cerca una base: si prende un insieme di vettori candidati, si mostra che è davvero una base (generatori e indipendenti), e si contano i suoi elementi. Come sottolineato a lezione, conviene scegliere la base più semplice e naturale possibile. Gli esempi che seguono, come ha raccomandato il docente, non vanno trattati come semplici esempi da dimenticare: sono risultati fondamentali che servono in tutto il corso.

## La dimensione di 𝕂^{n}
Si consideri 𝕂^{n} = { (a₁, …, aₙ) | aᵢ ∈ 𝕂 }, i vettori colonna con n entrate. I candidati più semplici sono quelli con un solo 1 e tutti gli altri zeri:
e₁ = (1, 0, …, 0), e₂ = (0, 1, 0, …, 0), …, eₙ = (0, …, 0, 1).

1. **Generatori.** Ogni vettore (a₁, …, aₙ) si scrive come combinazione lineare di e₁, …, eₙ: (a₁, …, aₙ) = a₁e₁ + a₂e₂ + … + aₙeₙ, e i coefficienti sono proprio le entrate del vettore.
2. **Indipendenza.** Se 0 = a₁e₁ + … + aₙeₙ = (a₁, …, aₙ), allora a₁ = 0, a₂ = 0, …, aₙ = 0: l'unica combinazione nulla è quella banale.

Dunque {e₁, …, eₙ} è una base di 𝕂^{n}, detta **base canonica**, e quindi **dim 𝕂^{n} = n**.

**In parole povere:** la base canonica è la base più naturale: i vettori con un solo 1 e tutti 0, e in essa le coordinate di un vettore coincidono con le sue entrate (per i polinomi, con i suoi coefficienti). Come sottolineato a lezione, il nome «spazio euclideo n-dimensionale» dato a ℝ^{n} quando era stato introdotto non era solo un nome: adesso ℝ^{n} è davvero uno spazio vettoriale di dimensione n.

## La dimensione dei polinomi di grado al più d
Sia 𝕂[x]_{d} = { p(x) ∈ 𝕂[x] | deg p(x) ≤ d } = { a_{d}x^{d} + a_{d−1}x^{d−1} + … + a₁x + a₀ | aᵢ ∈ 𝕂 }. Formano una base i polinomi 1, x, x², …, x^{d}?
1. **Generatori.** Un polinomio qualunque p(x) = a_{d}x^{d} + … + a₁x + a₀ è già, così com'è, una combinazione lineare di 1, x, …, x^{d} con coefficienti a₀, a₁, …, a_{d}.
2. **Indipendenza.** Se la combinazione a₀·1 + a₁·x + … + a_{d}·x^{d} è il polinomio nullo, allora tutti i coefficienti sono nulli, perché due polinomi sono uguali quando hanno gli stessi coefficienti.

Quindi 1, x, …, x^{d} è una base (anche questa si chiama **base canonica**) e **dim 𝕂[x]_{d} = d + 1**, perché gli elementi sono quelli con esponente da 0 a d. Poiché 𝕂[x], l'insieme di tutti i polinomi, non ha una base finita, ha dimensione infinita.

## Quando basta controllare una sola condizione
**Proposizione.** Sia V uno spazio vettoriale con dim V = n e siano v₁, …, vₙ esattamente n vettori. Se sono linearmente indipendenti **oppure** sono un insieme di generatori, allora sono una base.

**In parole povere:** se si sa già che il numero di vettori è quello giusto, basta controllare una sola delle due proprietà: l'altra arriva gratis. Come sottolineato a lezione, la dimostrazione non si fa, ma il risultato è un trucco utile: per mostrare che n vettori sono indipendenti si può scegliere di mostrare che generano, quando è più facile.

## Un altro esempio: le matrici
L'insieme M(m, n, 𝕂) delle matrici m × n a coefficienti in 𝕂 è uno spazio vettoriale. Una base è una collezione di matrici. Le candidate naturali sono le matrici E_{ij}, una per ogni posizione (i, j) con 1 ≤ i ≤ m e 1 ≤ j ≤ n: E_{ij} ha un 1 al posto (i, j) e 0 altrove. Per esempio, per 2 × 2 le quattro matrici sono
( 1 0 ; 0 0 ), ( 0 1 ; 0 0 ), ( 0 0 ; 1 0 ), ( 0 0 ; 0 1 ).

Un ragionamento analogo ai precedenti mostra che ogni matrice si scrive in un solo modo come combinazione lineare delle E_{ij}, i cui coefficienti sono le sue entrate, e che l'unica combinazione nulla è quella con coefficienti tutti nulli. Le matrici E_{ij} sono tante quante le posizioni, cioè m·n; quindi **dim M(m, n, 𝕂) = m·n**. Come sottolineato a lezione, le matrici E_{ij} sono tante quante le scelte della posizione di un 1, e una matrice m × n ha esattamente m·n entrate; di qui il risultato.

## Esercizi
**Esercizio 7.14.** Dimostrare che (−1, 1) e (2, 1) formano una base di ℝ². Basta mostrare che sono due vettori indipendenti: non sono multipli (da (−1, 1) = a·(2, 1) seguirebbe −1 = 2a e 1 = a, impossibile), quindi sono indipendenti; e poiché dim ℝ² = 2, per la proposizione precedente due vettori indipendenti sono già una base.

**Esercizio 7.15.** Si considerino in ℝ³ i vettori v₁ = (1, 1, 2), v₂ = (−1, 1, −1), v₃ = (1, 5, 4), v₄ = (0, 1, 1). Si mostra che v₁, v₂, v₃ sono dipendenti e che v₁, v₂, v₄ sono indipendenti.
- **Dipendenza di v₁, v₂, v₃.** Si cerca v₃ = a·v₁ + b·v₂ confrontando le componenti: a − b = 1, a + b = 5, 2a − b = 4. Dalle prime due si ricava a = 3 e b = 2, e la terza è verificata (2·3 − 2 = 4). Quindi v₃ = 3v₁ + 2v₂, cioè 3v₁ + 2v₂ − v₃ = 0: i tre vettori sono dipendenti.
- **Indipendenza di v₁, v₂, v₄.** Da a·v₁ + b·v₂ + c·v₄ = 0 si ottiene a − b = 0, a + b + c = 0, 2a − b + c = 0. La prima dà b = a; sostituendo, le altre due diventano 2a + c = 0 e a + c = 0; sottraendo si trova a = 0, poi c = 0 e b = 0. L'unica soluzione è quella banale: i tre vettori sono indipendenti.
