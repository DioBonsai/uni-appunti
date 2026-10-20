# Capitolo 20: Le Iterazioni e il Ciclo while
## Perché servono i cicli
Quando un programma deve ripetere un'operazione più volte, non ha senso copiare lo stesso codice decine di volte: serve un meccanismo di **ripetizione controllata**. Le **iterazioni**, o **cicli**, sono gli strumenti della programmazione strutturata (la terza struttura di controllo, dopo sequenza e selezione) che permettono di ripetere un blocco di istruzioni in modo controllato e leggibile.

(In parole povere: un ciclo è un "ripeti questo finché serve". Invece di scrivere dieci volte la stessa riga per stampare dieci numeri, la scrivi una volta sola e dici al computer quante volte, o fino a quando, deve rifarla.)

## Il ciclo while
Il **while** ripete un blocco di istruzioni **finché una condizione logica è vera**. La sintassi è:

```c
while (condizione) {
    // blocco di istruzioni da ripetere
}
```

Il funzionamento è questo: si valuta la condizione; se è vera il blocco viene eseguito e poi si torna a valutare la condizione; se è falsa il ciclo termina e si passa all'istruzione subito dopo il while. Ne seguono due casi limite: se la condizione è falsa fin dall'inizio il blocco **non viene eseguito mai**, e se la condizione rimane sempre vera il ciclo non finisce più (**ciclo infinito**).

(In parole povere: il while è come un buttafuori che, prima di ogni giro, chiede "la condizione è ancora vera?". Se sì, fa entrare per un altro giro; se no, il ciclo è finito. Se la risposta è "no" già alla prima domanda, non si entra nemmeno una volta.)

## La terna fondamentale: stampare i numeri da 0 a 9
Ogni ciclo si regge su tre elementi, la **terna fondamentale**: l'**inizializzazione** (il valore di partenza della variabile di controllo), la **condizione** (che decide se continuare) e l'**aggiornamento** (che fa avanzare la variabile di controllo verso la fine del ciclo). Per stampare i numeri da 0 a 9:

```c
#include <stdio.h>

int main(void) {
    int i = 0;

    while (i < 10) {
        printf("%d\n", i);
        i++;
    }
}
```

Il ciclo itera per i = 0, 1, 2, …, 9; quando i diventa 10 la condizione `i < 10` è falsa e il ciclo termina. Il diagramma di flusso mostra bene il ruolo di ciascun elemento: l'assegnamento iniziale `i ← 0` viene eseguito una sola volta, la condizione viene controllata prima di ogni giro, e `i ← i + 1` chiude il giro riportando il flusso al controllo.

![Diagramma di flusso del ciclo while che stampa i numeri da 0 a 9.](figure/prog/ch20_flow_while.png|8)

(In parole povere: la terna è la ricetta di ogni ciclo. Da dove parto? Fino a quando vado avanti? Come mi avvicino alla fine a ogni giro? Se dimentichi una di queste tre risposte, il ciclo non parte, non si ferma o non finisce mai.)

## Il conto alla rovescia
L'aggiornamento non è per forza un incremento: può essere un decremento, e la condizione può essere "invertita". La logica del ciclo dipende dal problema, non ha una forma fissa. Un conto alla rovescia da 5 a 1:

```c
#include <stdio.h>

int main(void) {
    int i = 5;

    while (i > 0) {
        printf("%d\n", i);
        i--;
    }
}
```

La terna è sempre la stessa: inizializzazione `i = 5`, condizione `i > 0`, aggiornamento `i--`.

## Sommatorie e variabili accumulatore
Il while non serve solo a ripetere istruzioni: spesso serve a **costruire progressivamente un risultato**. Per farlo si usa una **variabile accumulatore**, opportunamente inizializzata e modificata a ogni giro. Per esempio, la somma dei primi n numeri:

```c
int n = 5, i = 1, somma = 0;
while (i <= n) {
    somma = somma + i;
    i++;
}
printf("Somma = %d\n", somma);
```

Con n = 5 la somma passa da 0 a 1, 3, 6, 10 e infine 15, che è il valore stampato. L'accumulatore va inizializzato prima del ciclo (qui a 0, l'elemento neutro dell'addizione): se partisse da un valore qualsiasi, il risultato sarebbe falsato.

(In parole povere: l'accumulatore è come il totale sullo scontrino della cassa, che a ogni articolo si aggiorna aggiungendo il prezzo nuovo. Prima di cominciare deve valere zero.)

## Leggere l'input con un valore di terminazione
Non sempre sappiamo in anticipo quante iterazioni servono, per esempio quando leggiamo dei dati da tastiera. In questi casi si fissa un **valore di terminazione** (o **valore sentinella**) che l'utente inserisce per dire "ho finito". Nell'esempio della media delle altezze il valore di terminazione è qualunque altezza negativa: ogni altezza valida (maggiore o uguale a 0) aggiorna la **somma** (variabile accumulatore) e il **conteggio** (variabile contatore), e al termine i due insieme permettono di calcolare la media:

```c
int somma = 0, count = 0, altezza = 0;

while (altezza >= 0) {
    printf("Inserisci altezza: ");
    scanf("%d", &altezza);

    if (altezza >= 0) {
        somma += altezza;
        count++;
    }
}
printf("Media = %f\n", somma / (float)count);
```

Nota: `altezza` parte da 0 solo perché la condizione `altezza >= 0` sia vera al primo controllo. L'`if` interno serve perché anche il valore sentinella viene letto con `scanf`, ma non deve essere contato fra le altezze. La divisione usa il cast a `float` per non fare una divisione fra interi (capitolo 16). Una cautela in più: se l'utente inserisce subito un valore negativo, `count` resta 0 e la media non è definita; questo caso non è gestito nel codice di esempio (aggiunta nostra): in quel caso la divisione darebbe un risultato non numerico.

(In parole povere: è il "dimmi i numeri uno alla volta e quando hai finito scrivi un numero negativo". La somma tiene il totale e il contatore tiene quanti ne hai dati: dividendo il primo per il secondo esce la media.)

## Terminare per una condizione di successo
Un ciclo può anche finire per una **condizione di successo** che dipende dal contesto, senza contatori né valori di terminazione. Per esempio, indovinare un PIN:

```c
int segreto = 12345, guess = -1;
while (guess != segreto) {
    printf("Indovina il pin segreto: ");
    scanf("%d", &guess);
}
printf("Bravo, hai indovinato!\n");
```

Il while è molto flessibile e generale: basta esprimere una opportuna condizione booleana e provvedere a inizializzare e aggiornare le variabili di controllo. Qui `guess` parte da −1 per essere certi che la prima condizione sia vera, e viene aggiornata dalla `scanf` a ogni giro.

## Un errore comune: il ciclo infinito
Se la condizione non diventa mai falsa si ha un **ciclo infinito**. Il caso tipico è dimenticare l'aggiornamento:

```c
int i = 0;
while (i < 10) {
    printf("%d\n", i);
    // manca i++;
}
```

Qui `i` resta sempre 0 e il programma stampa `0` all'infinito (si interrompe dal terminale con Ctrl+C).

(In parole povere: è come una canzone in ripetizione in cui nessuno preme mai "stop". Se dentro il giro non cambia niente che renda falsa la condizione, il ciclo non ha motivo di fermarsi.)

## La visibilità delle variabili nei blocchi
Ogni blocco `{ ... }` introduce un **ambito di visibilità** (in inglese ~scope~) locale: le variabili dichiarate al suo interno esistono solo durante l'esecuzione di quel blocco. Quando un ciclo viene eseguito, a **ogni iterazione** una nuova istanza delle variabili locali viene allocata sullo stack e poi deallocata alla fine del giro.

(In parole povere: le variabili dichiarate dentro le graffe sono come i fogli che usi in una stanza e butti via uscendo. Ogni volta che rientri nella stanza, cioè a ogni giro del ciclo, ne hai di nuovi, e fuori dalla stanza non puoi più leggerli.)

Si segue il programma seguente:

```c
#include <stdio.h>

int main(void) {
    int x = 1;                  // visibile in tutto main()

    while (x < 3) {
        int y = x * 2;          // y visibile solo dentro il blocco
        printf("x=%d, y=%d\n", x, y);
        x++;
    }
    printf("x finale=%d", x);
}
```

All'inizio esiste solo `x`, uguale a 1. La condizione `x < 3` è vera: si entra nel blocco e `y` viene allocata sullo stack, con valore `x * 2` = 2; si stampa `x=1 y=2` e `x` passa a 2. Alla chiusura della graffa `y` viene deallocata. La condizione `x < 3` è ancora vera: si rientra, `y` viene allocata di nuovo (e vale 4), si stampa `x=2 y=4`, `x` passa a 3 e `y` scompare ancora. Ora `x < 3` è falsa, il ciclo termina e il programma stampa `x finale=3`.

![Lo stato delle variabili x e y a ogni passo del ciclo: y esiste solo dentro il blocco (in rosso le celle che cambiano).](figure/prog/ch20_scope_stack.png|14)

La variabile `y` non è quindi accessibile dopo la fine del ciclo: scrivere `printf("%d", y);` dopo il while è un **errore** (la variabile non è più visibile). Se il suo valore servisse, si può dichiarare `y` fuori dal ciclo oppure copiarne il valore in una variabile visibile nel `main` prima che il blocco termini.

Il prossimo capitolo presenta il ciclo `for`, una forma più compatta del while quando le iterazioni sono note in anticipo, e i cicli annidati.
