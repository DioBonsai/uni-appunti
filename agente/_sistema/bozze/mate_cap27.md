# 27. Problemi con più Scelte: Quando si Moltiplica e Quando si Somma
## Un problema non si risolve con una formula sola
Con le combinazioni semplici si sa contare una singola scelta di k elementi fra n. I problemi veri però sono spesso più articolati: usano le combinazioni come tecnica di base, ma richiedono di suddividere la scelta in **più passi**. In questo capitolo ci sono tre problemi, e il loro confronto mostra un punto importante: a volte i numeri dei vari passi si **moltiplicano**, altre volte si **sommano**.

Come sottolineato a lezione, di questi problemi **non interessa tanto il numero finale, ma il procedimento**: se si arriva a scrivere l'espressione giusta, il calcolo con la calcolatrice è secondario. Per i calcoli conviene comunque semplificare prima e usare la calcolatrice solo alla fine.

## La scuola di ballo: due gruppi separati
In una scuola di ballo ci sono 10 studenti maschi e 12 studentesse. Per una coreografia i maestri scelgono 4 uomini e 4 donne. Quante sono le scelte possibili?

Un modo sbagliato di risolvere il problema è dire che ci sono 22 studenti e se ne devono scegliere 8, quindi C_{22,8}. È sbagliato perché fra i 22 non se ne devono scegliere 8 qualsiasi: la scelta è vincolata, perché 4 vanno presi da un gruppo e 4 dall'altro. Come sottolineato a lezione, la strategia giusta è dividere la scelta in due passi, uno dopo l'altro, e disegnare l'albero delle possibilità.

Si scelgono prima gli uomini: 4 su 10, cioè (10 su 4) modi. Poi si scelgono le donne: qualunque sia la scelta degli uomini, le donne sono un gruppo separato, e quindi in ogni caso ci sono (12 su 4) possibilità. L'ordine dei due passi non cambia il risultato (prima gli uomini e poi le donne, o il contrario, danno gli stessi gruppi finali). I punti finali dell'albero, cioè tutte le situazioni possibili, si ottengono **moltiplicando** i due numeri, per il metodo delle scelte successive (capitolo 22):

(10 su 4) · (12 su 4) = 210 · 495 = 103 950.

![L'albero delle scelte per la scuola di ballo: 210 rami per gli uomini, e da ciascuno sempre 495 rami per le donne.](figure/mate/ch27_albero_ballo.png|13)

Il calcolo, con le semplificazioni: (10 su 4) = 10!/(4! · 6!) = (10 · 9 · 8 · 7)/(4 · 3 · 2 · 1) = 210, e (12 su 4) = 12!/(4! · 8!) = (12 · 11 · 10 · 9)/(4 · 3 · 2 · 1) = 495.

(In parole povere: quando due scelte sono indipendenti, cioè quello che scegli nella seconda non dipende da quello che hai scelto nella prima, il numero totale di possibilità è il prodotto dei due numeri. Ogni scelta degli uomini si può abbinare con ogni scelta delle donne.)

## La squadra di calcio: quattro scelte indipendenti
Una squadra di calcio ha una rosa di 3 portieri, 8 difensori, 7 centrocampisti e 4 attaccanti, in totale 22 giocatori. L'allenatore decide di schierare 1 portiere, 4 difensori, 4 centrocampisti e 2 attaccanti, cioè 11 giocatori con il modulo 4-4-2. Quante squadre diverse può schierare?

È lo stesso tipo di problema della scuola di ballo, ma con quattro scelte invece di due, e quindi un albero più alto. Il modo in cui si scelgono i difensori non influisce su quello dei centrocampisti o degli attaccanti: a ogni passo il numero di possibilità è sempre quello. I numeri da calcolare sono:
- portiere: (3 su 1) = 3;
- difensori: (8 su 4) = 8!/(4! · 4!) = (8 · 7 · 6 · 5)/(4 · 3 · 2 · 1) = 70;
- centrocampisti: (7 su 4) = 7!/(4! · 3!) = (7 · 6 · 5)/(3 · 2 · 1) = 35;
- attaccanti: (4 su 2) = 4!/(2! · 2!) = (4 · 3)/2 = 6.

Dato che ogni passo ha sempre lo stesso numero di scelte, si **moltiplica**: 3 · 70 · 35 · 6 = 44 100 squadre possibili. Il docente ha osservato che, se si cominciasse a dire che un certo attaccante ha litigato con un certo difensore e non devono giocare insieme, il numero di scelte di uno dei passi dipenderebbe da quelle precedenti e l'albero e l'analisi si complicherebbero.

## La gelateria: quando il secondo passo dipende dal primo
Una gelateria ha 15 gusti ed è possibile acquistare coni piccoli (1 gusto), medi (2 gusti diversi) o grandi (3 gusti diversi). Quanti coni diversi si possono comprare in totale?

Si divide il problema in due passi: prima si dice alla cassa la dimensione del cono (tre possibilità), poi si scelgono i gusti. Si disegna l'albero. Ogni scelta di gusti è una combinazione semplice, perché non conta l'ordine e non si ripete un gusto:
- cono piccolo: (15 su 1) = 15 possibilità;
- cono medio: (15 su 2) = 15!/(2! · 13!) = (15 · 14)/2 = 105 possibilità;
- cono grande: (15 su 3) = 15!/(3! · 12!) = (15 · 14 · 13)/(3 · 2 · 1) = 455 possibilità.

Questo albero è diverso da quelli visti finora. Nei casi precedenti, da qualunque ramo del primo livello si partisse, il numero di scelte del secondo livello era sempre lo stesso, e per questo i numeri si moltiplicavano. Qui invece **il numero delle scelte al secondo livello dipende dal ramo**: sono 15 per il piccolo, 105 per il medio e 455 per il grande. I punti finali dell'albero sono quindi la **somma** dei punti finali di ciascun ramo:

15 + 105 + 455 = 575 coni.

![L'albero della gelateria: ogni tipo di cono ha un numero diverso di scelte di gusti, e i punti finali si sommano.](figure/mate/ch27_albero_gelato.png|13)

(In parole povere: il tipo di cono divide il problema in casi alternativi, "o prendi il cono piccolo, o il medio, o il grande", e ogni caso ha un numero diverso di scelte di gusti. I casi non si abbinano fra loro come nella scuola di ballo: si sommano i loro conteggi.)

## Quando si moltiplica e quando si somma
Come sottolineato a lezione, è una cosa da tenere molto presente quando si analizzano questi problemi:
- se a ogni passo il numero delle scelte è **sempre lo stesso**, qualunque sia il percorso fatto fin lì, si **moltiplicano** i numeri dei vari passi (scuola di ballo, squadra di calcio);
- se invece il numero delle scelte di un passo **dipende da dove si è arrivati** al passo precedente, l'espressione è più complicata e coinvolge delle **somme** (gelateria), una per ciascun ramo.

Quando un problema si complica in questo modo il numero di casi esplode e non è possibile elencare tutte le possibilità. Il metodo è quindi prima di tutto capire che cosa chiede il problema, poi capire se è una questione di ordine oppure no, poi suddividere in pezzi più piccoli da risolvere uno alla volta e infine rimetterli insieme, moltiplicando o sommando a seconda dei casi.

Nel prossimo capitolo manca ancora un tipo di scelta, quella non ordinata in cui lo stesso elemento si può prendere più volte: le combinazioni con ripetizione.
