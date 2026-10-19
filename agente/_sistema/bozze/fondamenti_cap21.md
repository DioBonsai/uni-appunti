# 21. Il Quantificatore Universale
## La definizione
Un enunciato della forma «per ogni x, P(x)» si dice **enunciato quantificato universalmente**. Il simbolo ∀ significa «per ogni» e si chiama **quantificatore universale**: l'enunciato si scrive ∀x P(x). Nel linguaggio naturale, in inglese, «for all», «for any» e «for every» sono sinonimi; il simbolo ∀ si può leggere in tutti questi modi. È «universale» perché tutti gli oggetti del discorso devono avere la proprietà.

**Definizione.** Sia P una funzione proposizionale con dominio D. L'enunciato ∀x P(x) è **vero** se P(x) è vera per ogni x ∈ D. È **falso** se P(x) è falsa per almeno un x ∈ D.

Come sottolineato a lezione, per decidere il valore di un quantificatore si assegnano alla funzione tutti i possibili valori del dominio e si controlla che siano tutti veri. Ne basta **uno falso** su infiniti perché il quantificatore sia falso: non è una questione di probabilità. Si lavora con due soli valori di verità, quindi non esistono gradazioni come «quasi sempre vero» (quelle appartengono a studi molto più avanzati).

![I tre casi: P(x) vera ovunque, vera in alcuni punti, falsa ovunque.](figure/fond/logica_quantificatori_dominio.png|13.5)

Un valore di x del dominio che rende P(x) falsa si chiama **controesempio** all'enunciato ∀x P(x).

## Il dominio cambia il valore di verità
Il dominio del discorso è essenziale, perché lo stesso enunciato può essere vero in un dominio e falso in un altro. Si consideri ∀x (x² ≥ 0).
- Con dominio ℝ è **vero**: per ogni numero reale il quadrato è positivo o nullo (se x > 0 il quadrato è positivo, se x = 0 è zero, se x < 0 il quadrato è positivo).
- Con dominio ℂ è **falso**: prendendo x = √(−1) = i si ha x² = −1, che non è ≥ 0 (e un controesempio basta).

Un secondo esempio, sempre con dominio ℝ: ∀x (x² − 1 > 0). È **falso**: per x = 1 la proposizione 1² − 1 > 0 è falsa, e 1 è un controesempio. Ci sono tantissimi valori che rendono vera la funzione (per esempio x = 10 dà 99 > 0 e x = 5 dà 24 > 0), ma il quantificatore universale è falso lo stesso, perché basta un'eccezione. In realtà tutti i valori da −1 a +1, zero compreso, sono controesempi: per un x con |x| ≤ 1 il quadrato è minore o uguale a 1, e x² − 1 non è positivo.

## Come si dimostra che ∀x P(x) è vero
Per provare che ∀x P(x) è vero bisogna, in sostanza, esaminare **ogni** valore di x del dominio e mostrare che P(x) è vera. Una tecnica è porre che x sia un elemento **arbitrario** del dominio D e procedere con il simbolo x: qualunque cosa si affermi su x deve valere per qualsiasi valore x possa avere in D, e il ragionamento deve concludere che P(x) è vera. Mostrare che P(x) è vera per un valore particolare **non** dimostra che ∀x P(x) sia vero.

Per specificare il dominio si scrive anche: per ogni x ∈ D, P(x).

**Esempio.** Si verifica che l'enunciato «per ogni numero reale x, se x > 1 allora x + 1 > 1» è vero. Sia x un reale qualunque. Allora vale x ≤ 1 oppure x > 1.
- Se x ≤ 1, l'implicazione «se x > 1 allora x + 1 > 1» è **vera per difetto**: l'ipotesi è falsa e, come visto nel capitolo 16, un'implicazione con ipotesi falsa è vera qualunque sia la tesi (nella maggior parte delle dimostrazioni questo caso si omette).
- Se x > 1, qualunque sia il valore di x si ha x + 1 > x; da x + 1 > x e x > 1 si conclude che x + 1 > 1, quindi la conclusione è vera e l'implicazione è vera.

In entrambi i casi l'implicazione è vera, quindi l'enunciato quantificato è vero.

Il lettore interessato alla «meccanizzazione» può notare che questa prova usa passaggi più piccoli: la compatibilità del maggiore con la somma (da x > 1 si ricava x + 1 > 1 + 1, aggiungendo 1 a entrambi i lati), il calcolo 1 + 1 > 1 e la **transitività** del maggiore (se a > b e b > c allora a > c). Un corso di matematica chiede di saper fare questi ragionamenti direttamente, senza spiegare i passaggi più piccoli, ma per una macchina tutto deve essere precisato.

Dimostrare che ∀x P(x) è **falso** è molto più semplice: basta trovare **un** controesempio.

## Un algoritmo per decidere ∀x P(x) su un dominio finito
Se il dominio è infinito non c'è un modo ovvio per decidere un quantificatore con la sola definizione: servirebbero infiniti controlli, e un elenco, per quanto lungo, di valori non li esaurisce (esistono metodi migliori, ma appartengono ad altri corsi, di verifica automatica e di intelligenza artificiale). Quando il dominio è **finito**, invece, si può scrivere un programma. Sia D = {d₁, …, d_{n}} (per esempio gli elementi di un vettore) e sia P una funzione proposizionale su D. Questo pseudocodice (non è un linguaggio particolare) decide ∀x P(x):

```
for i = 1 to n
    if (¬P(d_i))
        return false
return true
```

Il ciclo esamina uno a uno gli elementi del dominio. Se trova un d_{i} per cui P(d_{i}) è falsa, la condizione ¬P(d_{i}) dell'if è vera e il programma restituisce **false** (d_{i} è un controesempio) e termina. Se P(d_{i}) è vera per ogni d_{i}, la condizione dell'if è sempre falsa, il ciclo arriva alla fine e il programma restituisce **true**. Quindi se ∀x P(x) è vero il ciclo deve arrivare fino in fondo, controllando ogni elemento; se è falso, il ciclo si ferma appena trova un elemento che rende P(x) falsa.

**Trabocchetto d'esame.** Come sottolineato a lezione, è un tipo di programma che si chiede agli esami, e gli errori più comuni sono due.
- Scrivere un `else` con `return true` dentro il ciclo: se P(d₁) è vera non si può concludere che il quantificatore sia vero, perché dipende dagli altri valori che non sono stati controllati. L'if va lasciato senza else: quando P(d_{i}) è vera non c'è abbastanza informazione e il ciclo deve semplicemente passare all'elemento successivo.
- Mettere il `return true` dentro il ciclo o sotto l'if. Il `return true` finale deve stare **fuori dal ciclo**, allineato con il `for`: è l'istruzione che si esegue solo se il for finisce senza aver mai trovato un falso. Se fosse dentro, il programma prenderebbe il primo valore di P e lo darebbe per valore del quantificatore, cosa in generale falsa.

Cicli di questo tipo sono quelli che cercano un oggetto con una certa proprietà in una banca dati; in un programma reale si cerca anche l'indirizzo dell'oggetto, ma qui interessa solo il valore di verità.

In pratica un ∀ si controlla con un programma solo se il dominio è finito e molto piccolo (anche qualche miliardo, ma non di più): una tavola di verità, per esempio, è di solito un dominio troppo grande, quando il numero di proposizioni atomiche è elevato. Per questo spesso si usano ragionamenti, cioè deduzioni valide in tutti i casi, invece di esplorare tutti i casi.
