# Capitolo 22: Sentinelle, break, continue e il Ciclo do-while
## Il problema: quando fermarsi
In molti casi non possiamo sapere all'inizio quante volte un ciclo dovrà ripetersi. Serve quindi un meccanismo per decidere **quando fermarsi**. Si usano due concetti, che vanno spesso insieme.

Un **valore sentinella** è un valore speciale che segnala la fine delle iterazioni (per esempio, leggo da input il valore −1). Altri nomi con cui si trova: valore di terminazione, marcatore di fine input, codice di arresto, EOF (~end of file~).

Una **variabile sentinella** è una variabile booleana che controlla il proseguimento del ciclo. Altri nomi comuni: flag di controllo (~flag~ vuol dire "bandierina di segnalazione"), controllo di ciclo (~loop flag~), variabile di controllo di terminazione.

Spesso si usano insieme: il valore sentinella, letto da input, serve ad aggiornare la variabile sentinella che controlla la terminazione del ciclo.

(In parole povere: il valore sentinella è il "basta, ho finito" che l'utente scrive per fermare il programma; la variabile sentinella è la bandierina alzata dal programma quando decide di fermarsi. Spesso la prima serve ad abbassare o alzare la seconda.)

## Un esempio: il primo quadrato maggiore di 500
Per trovare il primo numero il cui quadrato è maggiore di 500 si può usare una variabile sentinella `trovato`:

```c
int n = 1;
bool trovato = false;       // variabile sentinella (serve <stdbool.h>, cap. 17)

while (!trovato) {
    int q = n * n;
    if (q > 500) {
        trovato = true;
    }
    else {
        n++;
    }
}
printf("%d x %d = %d\n", n, n, n*n);
```

Lo stesso problema si può risolvere più brevemente scrivendo direttamente nella condizione il caso in cui si deve continuare:

```c
int n = 1;
// n*n <= 500: finché vale, si continua
while (n * n <= 500) {
    n++;
}
printf("%d x %d = %d\n", n, n, n*n);
```

Il risultato è lo stesso: il primo n con n² > 500 è 23 (22² = 484, 23² = 529). La seconda versione è più breve; la prima rende esplicito il motivo per cui il ciclo si ferma, e per questo è più adatta quando le condizioni di uscita sono più di una o più complicate.

## La media delle altezze con una variabile sentinella
Nel capitolo 20 la media delle altezze usava il valore sentinella (un'altezza negativa) direttamente nella condizione del while. La versione con una variabile sentinella `continua` rende più chiaro il flusso:

```c
int somma = 0, count = 0;
bool continua = true;       // variabile sentinella

while (continua) {
    int altezza;
    printf("Inserisci altezza (negativa per terminare): ");
    scanf("%d", &altezza);

    if (altezza >= 0) {
        somma += altezza;
        count++;
    }
    else {                  // altezza è un valore sentinella (< 0)
        continua = false;   // aggiorna la sentinella: il ciclo finisce
    }
}
printf("Media = %f\n", somma / (float)count);
```

Il valore sentinella (altezza negativa) serve ad aggiornare la variabile sentinella `continua`, che a sua volta controlla la terminazione. Il giro in corso finisce e, alla successiva valutazione della condizione, `continua` è falsa e il ciclo termina.

## Il controllo esplicito del flusso: break e continue
Il linguaggio definisce due parole chiave per controllare in modo esplicito il flusso dentro un ciclo.

L'istruzione **break** interrompe immediatamente il ciclo corrente: il flusso riprende subito dopo il ciclo. L'istruzione **continue** salta il resto del blocco per l'iterazione corrente e passa subito alla successiva valutazione della condizione.

```c
for (int i = 0; i < 10; i++) {
    if (i == 5)
        break;              // stop al ciclo
    printf("%d ", i);
}
```

Questo primo ciclo stampa `0 1 2 3 4` e si ferma quando `i` vale 5.

```c
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0)
        continue;           // salta i pari
    printf("%d ", i);
}
```

Questo secondo ciclo stampa `1 3 5 7 9`: per i numeri pari il `continue` salta la `printf` e passa al giro successivo. Nel `for` l'aggiornamento `i++` viene eseguito comunque, ed è per questo che il ciclo non diventa infinito (nota nostra: in un `while` equivalente un `continue` salterebbe anche l'aggiornamento).

(In parole povere: `break` è l'uscita di emergenza che fa uscire dal ciclo subito; `continue` è il "salta questo giro" che passa direttamente al prossimo.)

Entrambe le istruzioni possono essere utili in casi particolari, ma peggiorano la leggibilità. Per questo **nel corso si eviterà di usarle**: è meglio esplicitare le condizioni di terminazione con le variabili sentinella.

## Il ciclo do-while
Il **do-while** è una variante del while in cui la valutazione della condizione è **posticipata**:

```c
do {
    // blocco di istruzioni da ripetere
} while (condizione);
```

Il blocco viene **sempre eseguito almeno una volta**, e poi si ripete finché la condizione è vera. Si noti il punto e virgola finale dopo la parentesi della condizione.

(In parole povere: nel while si controlla prima di entrare, nel do-while si entra e si controlla dopo. È come assaggiare il piatto prima di decidere se ne vuoi ancora.)

![A confronto while e do-while: il controllo della condizione è prima o dopo il blocco.](figure/prog/ch22_while_dowhile.png|12)

È utile per scenari specifici, come la **validazione dell'input**: chiedere un valore finché l'utente non ne inserisce uno valido. Si ricorda che `scanf` restituisce il numero di valori letti correttamente (capitolo 10):

```c
int x, retval;
do {
    printf("Inserisci un numero [1,10]: ");
    retval = scanf("%d", &x);
    // ripeti se input non valido o non compreso nell'intervallo [1,10]
} while (retval == 0 || !(1 <= x && x <= 10));

printf("Hai inserito %d\n", x);
```

Attenzione: nelle slide la condizione è scritta `!(1 <= x || x <= 10)`, con un `||` al posto di `&&`. Così com'è non controlla l'intervallo, perché `1 <= x || x <= 10` è vera per qualunque numero: per verificare l'appartenenza a [1, 10] servono **entrambe** le condizioni insieme, come nel codice qui sopra. (Per riconoscere l'errore basta provare con il valore 15: con `||` il ciclo si ferma, con `&&` chiede di nuovo.)

## Come scegliere il ciclo
Riassumendo i tre cicli visti nei capitoli 20-22, più le sentinelle:
- **for** quando si conosce già il numero di iterazioni o si percorre un intervallo con passo regolare;
- **while** quando le iterazioni non sono note, e il controllo è fatto prima di ogni giro (può non essere eseguito mai);
- **do-while** quando il blocco deve girare almeno una volta, tipicamente per la validazione dell'input;
- sentinelle (di valore o di variabile) per decidere quando fermarsi quando la durata dipende dai dati.
