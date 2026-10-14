# Capitolo 19: Il Controllo di Flusso e il Costrutto if
## Dalla sequenza alle decisioni
Finora abbiamo scritto programmi in cui le istruzioni vengono eseguite prevalentemente una dopo l'altra. Per costruire algoritmi più articolati dobbiamo invece poter **controllare l'ordine** con cui le istruzioni vengono eseguite. La programmazione strutturata (capitolo 3) utilizza tre strutture di controllo fondamentali:
- la **sequenza**: esecuzione ordinata delle istruzioni;
- la **selezione**: scelta fra alternative, che si realizza con l'`if`;
- l'**iterazione**: ripetizione condizionata, con `while`, `for` e `do-while`.

In questo capitolo ci occupiamo della selezione, mentre l'iterazione verrà dopo.

## Tre strutture sono sufficienti
Negli anni Sessanta non era ancora chiaro quale fosse il giusto insieme di astrazioni per esprimere il flusso di controllo di un programma. Nel 1966 Corrado Böhm e Giuseppe Jacopini mostrarono che sequenza, selezione e iterazione sono **sufficienti per rappresentare qualsiasi funzione calcolabile**: è il **teorema di Böhm–Jacopini**. Questo risultato è alla base della programmazione strutturata e ha influenzato profondamente i linguaggi moderni: poche strutture di controllo elementari, componibili e annidabili, permettono di costruire algoritmi arbitrariamente complessi.

## Il controllo di flusso condizionato
Vediamo come rappresentare le scelte: se una condizione è vera si esegue un blocco di codice; se è falsa si fa qualcos'altro oppure si passa oltre. Questo meccanismo si chiama **controllo di flusso condizionato**. Un esempio quotidiano: se piove prendo l'ombrello, altrimenti esco senza (qui `piove` è una variabile booleana).

```c
if (piove) {
    printf("Prendi l'ombrello.\n");
}
else {
    printf("Esci senza.\n");
}
```

La condizione fra parentesi è un'espressione booleana, di quelle viste nei capitoli 17 e 18.

## Il costrutto if
L'**if** è il costrutto che permette al programma di scegliere che cosa fare in base a una condizione logica. La sintassi è:

```c
if (condizione) {
    // codice eseguito solo se la condizione è vera
}
```

Se la condizione è vera (1) il programma entra nel blocco; se è falsa (0) lo salta e continua dopo. Per esempio:

```c
int voto = 25;
if (voto >= 18) {
    printf("Esame superato!\n");
}
```

## Il costrutto if-else
L'**if-else** estende l'if permettendo di gestire due percorsi alternativi:

```c
if (condizione) {
    // blocco A: se la condizione è vera
}
else {
    // blocco B: se la condizione è falsa
}
```

Se la condizione è vera si entra nel blocco A, se è falsa nel blocco B. Un esempio:

```c
int batteria = 15;
if (batteria < 20) {
    printf("Batteria quasi scarica! Collega il caricatore.\n");
}
else {
    printf("Batteria sufficiente.\n");
}
```

Con batteria uguale a 15 la condizione `batteria < 20` è vera, e il programma stampa il primo messaggio.

## Il costrutto if-else if-else
L'**if-else if-else** è la generalizzazione dell'if-else a più alternative:

```c
if (condizione1) {
    // blocco 1
}
else if (condizione2) {
    // blocco 2
}
else {
    // blocco di default
}
```

Se la condizione1 è vera si entra nel blocco 1; altrimenti, se è vera la condizione2, si entra nel blocco 2; e così via. Se tutte le condizioni precedenti sono false si entra nel blocco di default. Le condizioni sono valutate nell'ordine in cui sono scritte e si esegue al più un solo blocco (esattamente uno se c'è l'else finale). Per esempio, un semaforo:

```c
char colore = 'G';   // R = Rosso, G = Giallo, V = Verde
if (colore == 'R') {
    printf("Fermati!\n");
}
else if (colore == 'G') {
    printf("Attenzione, rallenta.\n");
}
else if (colore == 'V') {
    printf("Puoi passare.\n");
}
else {
    printf("Colore non valido!\n");
}
```

Con colore uguale a 'G' il programma stampa `Attenzione, rallenta.`; il blocco finale gestisce tutti i colori non previsti.

![Il flusso di esecuzione di if, if-else e if-else if-else.](figure/prog/ch19_flusso_if.png|14)

Il prossimo capitolo raccoglie gli errori più comuni con questi costrutti, la visibilità delle variabili dentro i blocchi e alcuni schemi che si ripetono spesso.
