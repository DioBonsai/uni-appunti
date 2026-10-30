# 32. Le Permutazioni: Definizione, Composizione e Inversa
## Un chiarimento sul binomio di Newton
La lezione si apre riprendendo la formula del binomio (cap. 31), perché a qualcuno non era chiaro come mai il coefficiente di a^{k}b^{n−k} sia un coefficiente binomiale (n su k) e quindi una **combinazione semplice**, e non una combinazione con ripetizione, dato che nell'insieme {a, b} gli elementi ripetuti sembrano essere proprio a e b.

Il modo per capirlo, come spiegato a lezione, è immaginare che ciascuno dei 10 fattori di (a + b)^{10} abbia un **interruttore a due posizioni**: la posizione «a» e la posizione «b». Per ottenere, per esempio, il termine a³b⁷ bisogna mettere **tre interruttori nella posizione a** (e quindi gli altri sette nella posizione b). Basta scegliere gli interruttori che vanno su a, perché i restanti vanno su b: la scelta non è «fra a e b», ma **di 3 posizioni tra le 10 possibili**, cioè un sottoinsieme di 3 elementi dell'insieme dei 10 interruttori. Si contano quindi i sottoinsiemi di k elementi di un insieme di n elementi: combinazioni semplici, con coefficiente (n su k).

**In parole povere:** non si scelgono «lettere a o b» con ripetizione: si scelgono quali dei dieci fattori contribuiscono con la a, e quel conteggio è proprio quello delle combinazioni semplici.

## Che cos'è una permutazione
Si comincia un nuovo argomento.

**Definizione.** Sia X un insieme non vuoto. Una **permutazione** su X è una **funzione biettiva** f : X → X.

**In parole povere:** una permutazione è un modo di «rimescolare» gli elementi di X, dove ognuno finisce in un posto e nessun posto resta vuoto o occupato due volte.

La definizione ha senso per qualunque insieme, ma interessa soltanto il caso in cui **X è finito**, con n elementi. Numerando gli elementi si può usare sempre l'insieme **I_{n} = {1, 2, …, n}**: una permutazione è dunque una funzione biettiva che manda ogni numero da 1 a n in un numero da 1 a n (eventualmente lo stesso).

L'insieme delle permutazioni di {1, …, n} si indica con **S_{n}**. È una notazione standard, valida in tutti i libri; la S sta per «simmetrico», per ragioni tradizionali, e l'indice n dice quanti oggetti si stanno permutando.

## Due osservazioni
**Prima osservazione: quante sono.** Dare una permutazione equivale a **riordinare** gli n elementi: sapere chi è il nuovo primo, il nuovo secondo e così via. I riordinamenti di un insieme con n elementi sono già stati contati: quindi **|S_{n}| = n!** (come già visto per i riordinamenti).

Gli esempi piccoli, fatti a lezione:
- **S₁** ha una sola permutazione, l'identità: con un solo elemento non c'è altro modo di scriverlo.
- **S₂** ne ha 2! = 2: l'identità e lo scambio, che manda 1 in 2 e 2 in 1.
- **S₃** ne ha 3! = 6: l'identità e altre 5. Tre sono **scambi** (ognuno scambia due elementi e ne lascia fisso uno): quello che scambia 1 e 2 lasciando fisso 3, quello che scambia 1 e 3 lasciando fisso 2 e quello che scambia 2 e 3 lasciando fisso 1. Le ultime due **non lasciano fisso niente**: una manda 1 in 2, 2 in 3 e 3 in 1, l'altra manda 1 in 3, 3 in 2 e 2 in 1. Sono sei in tutto e non ce ne sono altre.

Per n = 4 se ne avrebbero 24: non le si scrive tutte.

È utile, come si diceva a lezione, pensarle come **spostamenti fisici di oggetti**: l'1 viene spostato al posto del 2, il 2 al posto dell'1, il 3 resta dov'è.

**Seconda osservazione: si possono comporre.** Le permutazioni sono funzioni biettive con lo **stesso dominio e codominio**, quindi si possono comporre fra loro; e la composizione di funzioni biettive è ancora biettiva (fatto già visto sulle funzioni). Dunque **la composizione di due permutazioni è ancora una permutazione**: la composizione è un'operazione sull'insieme S_{n}.

L'immagine proposta a lezione è quella di un **mazzo di carte**: mescolare è una permutazione; rimescolare il mazzo una seconda volta ne è un'altra; il risultato finale è una nuova permutazione, la permutazione totale. Si vuole capire l'«algebra» di queste operazioni: quali permutazioni di base permettono di scrivere tutte le altre, che cosa succede ripetendo più volte la stessa, e così via.

## Le proprietà della composizione
Poiché le permutazioni sono funzioni:
1. l'**identità** appartiene a S_{n} ed è neutra per la composizione (comporre qualcosa con l'identità non lo cambia);
2. ogni permutazione ha un'**inversa** (essendo biettiva), che è ancora una permutazione (scambiando dominio e codominio la funzione resta biettiva);
3. la composizione è **associativa**.

**La composizione non è commutativa**, in generale: cambiando l'ordine dei fattori, il risultato può cambiare. Per esempio, in S₃ si prendano S₁ = lo scambio che fissa 1 (2 ↔ 3) e S₂ = lo scambio che fissa 2 (1 ↔ 3). **S₂ ∘ S₁** (prima S₁ e poi S₂): 1 va in 1 e poi in 3; 2 va in 3 e poi in 1; 3 va in 2 e poi resta in 2; il risultato manda 1 → 3, 2 → 1, 3 → 2. **S₁ ∘ S₂** (prima S₂ e poi S₁): 1 va in 3 e poi in 2; 2 resta in 2 e poi va in 3; 3 va in 1 e poi resta in 1; il risultato manda 1 → 2, 2 → 3, 3 → 1. Sono due permutazioni diverse (le due che non fissano nulla).

Con due soli elementi la composizione è commutativa; dal terzo elemento in poi non più. Questa è la novità: in questa «algebra» **cambiare l'ordine dei fattori cambia il risultato**.

**In parole povere:** se si fanno due mescolate diverse, in generale l'ordine conta.

## Come si scrive una permutazione: la tabella a due righe
Per non descrivere ogni volta la funzione a parole si usa una **tabella a due righe**: nella prima riga i numeri 1, 2, …, n in ordine (è solo una convenzione psicologica: sarebbe uguale in qualunque ordine) e sotto ciascuno la sua immagine. Per esempio, con n = 7, la permutazione π della lezione è
- prima riga: 1 2 3 4 5 6 7;
- seconda riga: 3 4 6 1 2 5 7,
e significa π(1) = 3, π(2) = 4, π(3) = 6, π(4) = 1, π(5) = 2, π(6) = 5, π(7) = 7.

**Come si riconosce che una tabella è una permutazione?** La seconda riga deve contenere **tutti i numeri da 1 a n, ciascuno una sola volta**. Se invece, per esempio, compare due volte il 5, la funzione non è iniettiva e quindi non è una permutazione. Per esempio, con n = 5, la tabella con seconda riga 2 5 3 1 5 non è una permutazione: il 5 compare due volte, quindi la funzione non è iniettiva.

**L'inversa si legge subito.** Una funzione manda x in y, la sua inversa manda y in x: basta **scambiare le due righe** e poi riordinare le colonne perché la prima riga sia 1, 2, …, n. Per π: nella nuova tabella, sotto 1 si scrive il numero che nella tabella di π sta sopra all'1 della seconda riga, cioè 4; sotto 2 va 5; sotto 3 va 1; sotto 4 va 2; sotto 5 va 6; sotto 6 va 3; sotto 7 va 7. Quindi
**π^{-1}**: seconda riga 4 5 1 2 6 3 7.

## Come si compongono: il metodo a tre righe
Per **comporre** due permutazioni si procede in modo quasi meccanico, tenendo ben presente che sono funzioni: la composizione si legge **da destra verso sinistra**, cioè nella scrittura σ ∘ π si applica **prima π e poi σ** (come in tutte le composizioni di funzioni). Come osservato a lezione, è uno degli errori più frequenti.

**Esempio.** Si prenda, oltre a π, la permutazione σ con seconda riga 5 2 6 1 3 7 4 (n = 7). Per calcolare σ ∘ π:
1. si scrive la tabella di π (prima riga 1…7, seconda riga 3 4 6 1 2 5 7);
2. si aggiunge una **terza riga** con l'effetto di σ: **sotto ogni numero della seconda riga si scrive la sua immagine secondo σ** (e non si ricopia la seconda riga di σ così com'è: bisogna mantenere il legame fra elemento e immagine). Quindi sotto 3 va σ(3) = 6, sotto 4 va σ(4) = 1, sotto 6 va σ(6) = 7, sotto 1 va σ(1) = 5, sotto 2 va σ(2) = 2, sotto 5 va σ(5) = 3 e sotto 7 va σ(7) = 4;
3. la **seconda riga era solo un passaggio intermedio**: si cancella, e resta la tabella con la prima e la terza riga.

Risultato: **σ ∘ π** ha seconda riga 6 1 7 5 2 3 4, mentre **π ∘ σ** (prima σ e poi π) ha seconda riga 2 4 5 3 6 7 1: ancora una volta due risultati diversi.

Lo stesso metodo funziona con più permutazioni: si aggiunge una riga per ogni permutazione da applicare, e alla fine si tengono solo la prima e l'ultima.

**In parole povere:** comporre significa «seguire» ogni numero attraverso le permutazioni, una dopo l'altra, e scrivere dove finisce; non si scopre ancora nessun segreto delle permutazioni, è soltanto un modo rapido e meccanico di scrivere.

Nel capitolo seguente si guarda invece come si muovono i numeri, e si scopre che ogni permutazione si spezza in «giri» indipendenti: i cicli.
