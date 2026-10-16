# 24. Le Disposizioni: con Ripetizione e Semplici
## Scelte ordinate di alcuni elementi
Con gli ordinamenti si prendono **tutti** gli elementi di un insieme e li si mette in fila. Nella realtà spesso interessa scegliere solo alcuni elementi, sempre tenendo conto dell'ordine. Alle Olimpiadi, per esempio, vengono premiati i primi tre: nella finale dei 100 metri con 8 atleti si vuole sapere quante sono le possibili assegnazioni di oro, argento e bronzo, quindi si ordinano solo tre degli otto, mentre gli altri possono arrivare in qualunque ordine e non interessano. Un altro problema: un falegname ha prodotto 5 oggetti diversi e dispone di smalti di 4 colori, e vuole sapere in quanti modi può colorare gli oggetti.

Entrambe le situazioni sono **disposizioni**. Una **disposizione** di elementi di un insieme A è una scelta **ordinata** di elementi di A: l'ordine conta, perché il primo scelto e il secondo scelto hanno ruoli diversi (arrivare primo e secondo non è la stessa cosa che arrivare secondo e primo; e nei colori, colorare l'oggetto a di bianco e l'oggetto b di rosso è diverso dal contrario).

I due problemi però non sono uguali, e vanno trattati con formule diverse. Un atleta non può vincere due medaglie nella stessa gara, quindi non ci sono ripetizioni nella scelta. Invece il falegname può colorare tutti e cinque gli oggetti di bianco, e la scelta del colore può ripetersi. Per questo si distinguono le **disposizioni con ripetizione**, in cui lo stesso elemento si può scegliere più volte, e le **disposizioni semplici**, in cui no.

Come sottolineato a lezione, la parte più difficile è leggere il problema e capire di che tipo è; le formule sono semplici. I due indizi principali sono: se le scelte possono ripetersi oppure no, e se l'ordine conta oppure no.

## Disposizioni con ripetizione
Sia A un insieme con n elementi (nel problema dei colori, l'insieme dei 4 smalti) e si devono fare k scelte ordinate in A. Una **disposizione con ripetizione** di ordine k in A è quindi una successione di k elementi di A non necessariamente distinti. In termini di funzioni, si tratta di assegnare a ciascuno dei numeri 1, 2, …, k un elemento di A: una **funzione qualunque** da I_{k} = {1, …, k} in A, perché non c'è alcuna condizione (si può scegliere sempre lo stesso elemento).

Nell'albero, alla prima scelta ci sono n possibilità; alla seconda ce ne sono di nuovo n, perché l'elemento già scelto si può scegliere ancora; e così a ogni livello. Con n = 4 il primo livello ha 4 rami, il secondo 4 · 4 = 16, il terzo 4 · 4 · 4 = 64, e al livello k ci sono 4^{k} punti finali.

![L'albero delle disposizioni con ripetizione per n = 4: a ogni livello 4 scelte, quindi 4, 16, 64, …](figure/mate/ch24_albero_ripetizione.png|13)

**Proposizione.** Il numero delle disposizioni con ripetizione di k scelte tra n oggetti è n^{k}.

Si indica con D^{r}_{n,k}, dove la r sta per «ripetizione» (non è un esponente), e vale D^{r}_{n,k} = n^{k}. Per il falegname, con n = 4 colori e k = 5 oggetti, ci sono 4⁵ = 1024 colorazioni. Altri esempi: la prova scritta di 15 candidati con voti da 0 a 10 ha 11 voti possibili per candidato, quindi 11^{15} esiti complessivi; 7 oggetti con 4 smalti si possono colorare in 4⁷ modi.

Un chiarimento sul modello: le scelte si fanno **nell'insieme dei colori**, a ogni oggetto si associa un colore, ma non a ogni colore un oggetto (lo stesso colore può servire a più oggetti). Per questo la scelta è una funzione dall'insieme degli oggetti, numerati da 1 a k, nell'insieme dei colori, non il contrario. La numerazione ha senso perché gli oggetti sono **diversi tra loro**, quindi distinguibili: se invece fossero 5 sedie identiche, scegliere bianco per la prima e rosso per la seconda sarebbe la stessa cosa che il contrario, l'ordine non conterebbe più e il problema sarebbe un altro.

## Disposizioni semplici
Una **disposizione semplice** di ordine k in A è una successione di k elementi di A a due a due distinti, cioè una scelta ordinata senza ripetizioni. Equivale a una **funzione iniettiva** da I_{k} in A, perché due numeri diversi non possono avere lo stesso elemento.

Una conseguenza immediata: per il principio dei cassetti (o delle gabbie dei piccioni) non si possono associare in modo iniettivo più elementi di quanti ce ne siano nell'insieme di arrivo, quindi deve essere k ≤ n. Con k > n non esistono disposizioni semplici. Con k = n la disposizione semplice è un ordinamento di tutto A, e il numero è n!. Se k < n la funzione non è suriettiva (si usano solo alcuni elementi di A), ma questo non è richiesto.

Il conteggio procede come per gli ordinamenti, ma ci si ferma prima. Alla prima scelta ci sono n possibilità, alla seconda n − 1 (non si può ripetere l'elemento già scelto), alla terza n − 2, e così via. All'ultima scelta, la k-esima, ci sono n − (k − 1) = n − k + 1 possibilità: i fattori sono k in tutto e il primo non toglie niente, il secondo toglie 1, il terzo toglie 2, il k-esimo toglie k − 1.

![L'albero delle disposizioni semplici per n = 5 e k = 3: 5 scelte, poi 4, poi 3, in tutto 60.](figure/mate/ch24_albero_podio.png|13)

**Proposizione.** Per 1 ≤ k ≤ n, il numero delle disposizioni semplici di k elementi scelti tra n, indicato con D_{n,k}, è

D_{n,k} = n · (n − 1) · … · (n − k + 1).

Nell'albero con n = 5 e k = 3 si hanno 5 · 4 · 3 = 60 punti finali. Per la finale dei 100 metri con 8 atleti i podi possibili sono D_{8,3} = 8 · 7 · 6 = 336, e con 12 atleti D_{12,3} = 12 · 11 · 10 = 1320.

Esiste una scrittura più compatta con il fattoriale. Scrivendo n! = n · (n − 1) · … · (n − k + 1) · (n − k) · (n − k − 1) · … · 3 · 2 · 1, i fattori dopo (n − k + 1) formano (n − k)!. Quindi, dividendo n! per (n − k)!, restano solo i primi k fattori:

D_{n,k} = n! / (n − k)!.

Con k = n si ottiene n!/0! = n!, coerente con gli ordinamenti, ed è qui che la convenzione 0! = 1 è utile.

## Verso le combinazioni
Non sempre l'ordine conta. In una gelateria con 15 gusti, un cono grande contiene tre gusti: cioccolato, nocciola, pistacchio è lo stesso cono di pistacchio, cioccolato, nocciola. Sono scelte **non ordinate**, e il modello matematico non è una funzione ma un **sottoinsieme**: scegliere un cono equivale a scegliere un sottoinsieme di 3 gusti dai 15. Anche una vaschetta di pasticcini non dipende dall'ordine in cui li si mettono, ma lì lo stesso tipo di pasticcino si può prendere più volte: è un caso con ripetizione, che si tratterà a parte. Una **combinazione** di ordine k in un insieme A con n elementi è la scelta di un sottoinsieme S di A con k elementi, con k ≤ n. Quante siano si vedrà nella prossima lezione, insieme ai coefficienti binomiali.
