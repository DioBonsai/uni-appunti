# Capitolo 21: Il Ciclo for e i Cicli Annidati
## Il ciclo for
In molti casi sappiamo già quante iterazioni servono. Per questi casi il C offre il **for**, una variante sintattica più compatta e leggibile del while:

```c
for (inizializzazione; condizione; aggiornamento) {
    // blocco di istruzioni da ripetere
}
```

Il funzionamento è questo: l'**inizializzazione** viene eseguita una sola volta, prima del ciclo, e le variabili che dichiara sono visibili solo dentro il for; la **condizione** viene valutata prima di ogni iterazione; l'**aggiornamento** viene eseguito dopo ogni iterazione. Il for è un caso particolare del while, ma più ordinato: gli elementi di controllo sono scritti uno accanto all'altro, e questo riduce gli errori.

(In parole povere: il for mette in una sola riga la terna del capitolo precedente: da dove parto, fino a quando continuo, come avanzo. Tutto quello che serve a governare il ciclo sta nell'intestazione, e il corpo contiene solo il lavoro vero e proprio.)

## L'equivalenza fra for e while
Il for è un modo compatto di scrivere un while insieme alla sua terna di controllo. I due frammenti seguenti sono equivalenti:

```c
for (inizializzazione; condizione; aggiornamento) {
    // blocco di istruzioni da ripetere
}
```

```c
{
    inizializzazione;
    while (condizione) {
        // blocco di istruzioni da ripetere
        aggiornamento;
    }
}
```

Le graffe esterne nella versione con il while servono a limitare la visibilità: come nel for, la variabile inizializzata non esiste fuori dal ciclo.

## Percorrere un intervallo di valori
Il for è il modo naturale per percorrere un **intervallo di valori numerici**, descritto da tre cose: un valore iniziale (per esempio 0), una condizione di appartenenza all'intervallo (per esempio `x < 10`) e un passo (+1, +2, −1, …).

(In parole povere: un intervallo si dà come un percorso a piedi: punto di partenza, fino a dove si cammina e di quanti passi alla volta. Il for ti chiede esattamente queste tre informazioni.)

Alcuni esempi:

```c
// numeri nell'intervallo semiaperto [0, 10): inizio 0, condizione < 10, passo +1
for (int i = 0; i < 10; i++) {
    printf("%d\n", i);
}

// numeri pari nell'intervallo chiuso [0, 40]: inizio 0, condizione <= 40, passo +2
for (int i = 0; i <= 40; i += 2) {
    ...
}

// numeri in [0, n] in ordine decrescente: inizio n, condizione >= 0, passo -1
int n = 10;
for (int i = n; i >= 0; i--) {
    ...
}
```

Due applicazioni tipiche sono la somma fino a N (intervallo [1, N]) e la tabellina del 5 (intervallo [1, 10]):

```c
// con N già definito
int somma = 0;
for (int i = 1; i <= N; i++) {
    somma += i;
}

for (int i = 1; i <= 10; i++) {
    printf("%d x 5 = %d\n", i, i*5);
}
```

Si noti come la scelta fra `<` e `<=` decide se l'estremo destro è escluso o incluso: è lo stesso discorso degli intervalli visti nel capitolo 18.

## I cicli annidati
Gli elementi della programmazione strutturata sono componibili: un ciclo può contenere, nel suo blocco, un altro ciclo, detto **ciclo annidato**. Un esempio è la stampa di una griglia di numeri:

```c
for (int r = 0; r < 3; r++) {
    for (int c = 0; c < 3; c++) {
        printf("(%d,%d) ", r, c);
    }
    printf("\n");
}
```

Il ciclo esterno gestisce le righe `r`, quello interno le colonne `c`. A ogni valore di `r` il ciclo interno ricomincia da capo e percorre tutte le colonne, poi `printf("\n")` va a capo. Il risultato è una griglia di 3 righe e 3 colonne, con 3 × 3 = 9 coppie stampate:

```
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
```

![L'ordine con cui il ciclo annidato visita le 9 coppie (r, c): il ciclo interno gira più in fretta.](figure/prog/ch21_griglia.png|9)

(In parole povere: è come l'orologio, dove la lancetta dei minuti fa un giro completo per ogni passo di quella delle ore. Il ciclo interno gira "veloce" e quello esterno "lento".)

Valgono anche qui le regole di visibilità: ogni blocco introduce un ambito locale, quindi le variabili di un ciclo sono visibili all'interno del proprio blocco, e anche dentro i blocchi annidati. Nell'esempio `r` è visibile sia nel ciclo esterno sia in quello interno, mentre `c` è visibile solo nel ciclo interno.

## Errori comuni nei cicli for
Gli errori tipici sono questi:
- **condizione sempre vera**: `for (int i = 0; i >= 0; i++) { ... }` non si ferma mai (infinito);
- **aggiornamento mancante**: `for (int i = 0; i < 10; ) { ... }` lascia `i` invariata, e il ciclo è infinito;
- **off-by-one**: `for (int i = 0; i <= 10; i++)` esegue 11 iterazioni invece di 10, perché si include anche l'estremo destro;
- **uso improprio della variabile di controllo**: con `i = i + 2;` dentro il corpo si altera a mano il contatore, e il ciclo non scorre più come previsto;
- **scope della variabile contatore**: dopo `for (int i = 0; i < 5; i++) { ... }` scrivere `printf("%d", i);` è un errore, perché `i` non esiste fuori dal for.

(In parole povere: l'errore "off-by-one" è lo sbaglio del paletto e dello spazio fra paletti: se ti servono 10 passi e parti da 0, ti fermi a 9; se arrivi fino a 10 ne fai 11.)

## Quando usare for e quando while
La scelta dipende dalla natura del problema:
- il **for** va bene quando le iterazioni sono note a priori, per gli intervalli numerici con passo costante e quando il contatore è gestito in modo naturale e regolare;
- il **while** va bene quando le iterazioni sono ignote in anticipo, quando la condizione dipende da un input o da eventi esterni e quando l'aggiornamento non è numerico o è irregolare.

Il prossimo capitolo riguarda i problemi in cui non si sa quanto durerà il ciclo: le sentinelle, i comandi `break` e `continue` e il ciclo `do-while`.
