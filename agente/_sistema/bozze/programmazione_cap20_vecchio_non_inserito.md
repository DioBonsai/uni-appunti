# Capitolo 20: Errori Comuni, Visibilità nei Blocchi e Schemi con if
## Gli errori più comuni
Molti errori nei programmi nascono da piccoli errori sintattici o logici negli if. Conviene conoscere quelli più frequenti.

**Usare = invece di ==.** Scrivere `if (a = 5) { ... }` è un errore logico: `=` è un assegnamento, non un confronto. Il programma compila, ma non verifica se a vale 5: assegna 5 ad a, e la condizione vale quindi 5, cioè è sempre vera.

**Dimenticare le graffe.** In C è consentito omettere le parentesi graffe se dopo l'if c'è una sola istruzione, ma questo può generare errori poco visibili:

```c
if (x > 0)
    printf("Positivo\n");
    printf("Errore!\n");   // eseguito sempre
```

La seconda printf non dipende dall'if, anche se l'indentazione lo suggerisce, e viene eseguita comunque. Per chiarezza è meglio usare sempre le graffe, anche con una sola istruzione, salvo casi davvero ovvi.

**Ordine sbagliato delle condizioni.** Nell'if-else if le condizioni si controllano nell'ordine in cui sono scritte, e si esce al primo blocco la cui condizione è vera:

```c
if (num % 2 == 0) {
    printf("Pari non nullo\n");
}
else if (num == 0) {
    printf("Zero\n");   // mai raggiunto
}
```

Lo zero è pari, quindi entra già nel primo blocco e il secondo non viene mai raggiunto. Si corregge controllando prima i casi più specifici:

```c
if (num == 0) {
    printf("Zero\n");
}
else if (num % 2 == 0) {
    printf("Pari non nullo\n");
}
```

**Condizioni ridondanti o mai vere.** In questo esempio i due blocchi finali non vengono mai eseguiti, perché ogni valore maggiore di 20 o di 50 è anche maggiore di 10 ed entra già nel primo blocco:

```c
if (x > 10) {
    ...
}
else if (x > 20) {
    ...   // mai eseguito!
}
else if (x > 50) {
    ...   // mai eseguito!
}
```

Infine, è buona norma gestire sempre tutti i casi possibili del flusso, con un **else** finale, così il programma non lascia situazioni non previste.

## Suggerimenti e buona prassi
Abituarsi a pensare ai casi limite evita brutte sorprese. Oltre a usare sempre le graffe e a ordinare le condizioni dal caso più specifico al più generale, come visto sopra, conviene mantenere le condizioni semplici e leggibili, spezzando quelle complesse con variabili booleane intermedie (capitolo 18):

```c
// difficile da leggere
if (a > 10 && b < 5 || c == 7 && !(d % 2)) { ... }

// meglio
bool condA = (a > 10 && b < 5);
bool condB = (c == 7 && d % 2 == 0);
if (condA || condB) { ... }
```

## Esempio: stampare due numeri in ordine
Un esempio che usa l'if: si chiedono all'utente due interi x e y e si stampano dal minore (o uguale) al maggiore. Negli esempi del docente la funzione main compare come `void main()`; qui usiamo la forma standard `int main(void)` e, come nei capitoli precedenti, omettiamo gli `#include`. Una prima soluzione stampa i due numeri in ordine diverso nei due rami:

```c
int main(void) {
    int x, y;
    printf("Inserisci x:");
    scanf("%d", &x);
    printf("Inserisci y:");
    scanf("%d", &y);
    if (y < x) {
        printf("%d %d", y, x);
    }
    else {   // y >= x
        printf("%d %d", x, y);
    }
}
```

Una seconda soluzione fa invece uno **scambio condizionato**: se y è minore di x scambia i due valori, usando la variabile temporanea del capitolo 13, e poi stampa sempre x e y nello stesso ordine:

```c
int main(void) {
    int x, y;
    printf("Inserisci x:");
    scanf("%d", &x);
    printf("Inserisci y:");
    scanf("%d", &y);
    if (y < x) {
        // scambio condizionato
        int temp = x;
        x = y;
        y = temp;
    }
    printf("%d %d", x, y);
}
```

## Visibilità nei blocchi condizionati
Nello scambio condizionato la variabile `temp` è dichiarata **dentro il blocco** dell'if. Seguiamo l'esecuzione con x = 10 e y = 5, quando la condizione `y < x` è vera:
- all'inizio sullo stack ci sono solo x e y, con i valori inseriti;
- entrando nel blocco, la dichiarazione di temp la rende visibile e la inizializza a 10;
- `x = y;` copia 5 in x e `y = temp;` copia 10 in y: i valori sono scambiati;
- all'uscita dal blocco, temp esce dalla visibilità: viene rimossa dallo stack e non è più accessibile.

Il programma stampa `5 10`. Come nel capitolo 7, la **visibilità** (scope) di una variabile è quindi limitata al blocco in cui è dichiarata, e la sua durata (lifetime) finisce quando il blocco termina.

![Lo scambio condizionato: temp esiste solo dentro il blocco dell'if (in rosso le celle che cambiano).](figure/prog/ch20_scambio_condizionato.png|13)

## Annidamenti non necessari
Conviene evitare gli annidamenti multipli di if quando non servono, perché rendono il codice meno chiaro. Questo programma calcola il biglietto in base all'età, usando un if dentro un else:

```c
int eta;
printf("Inserisci la tua età: ");
scanf("%d", &eta);
if (eta < 6) {
    printf("Biglietto gratuito\n");
}
else {
    if (eta < 18) {
        printf("Biglietto ridotto\n");
    }
    else {
        printf("Biglietto intero\n");
    }
}
```

Lo stesso comportamento si ottiene, in modo più leggibile, con un if-else if-else senza annidamenti:

```c
if (eta < 6) {
    printf("Biglietto gratuito\n");
}
else if (eta < 18) {
    printf("Biglietto ridotto\n");
}
else {
    printf("Biglietto intero\n");
}
```

## Schemi ricorrenti elementari
Alcuni usi dell'if si ripetono continuamente nei programmi.

**Massimo di due variabili.** Si confrontano a e b e si assegna a max il valore maggiore:

```c
int a, b, max;
scanf("%d%d", &a, &b);
// determina il massimo tra a e b
if (a > b) {
    max = a;
}
else {
    max = b;
}
// qui max contiene il massimo tra a e b
```

**Validazione dell'input.** Prima di usare i dati letti, si controlla che scanf li abbia letti correttamente, usando il suo valore di ritorno (capitolo 10):

```c
int valore;
if (scanf("%d", &valore) == 1) {
    printf("Hai inserito: %d\n", valore);
}
else {
    printf("Input non valido\n");
}
```

**Protezione da operazioni illegali.** Per esempio, si evita la divisione per zero controllando il divisore:

```c
if (divisore != 0) {
    printf("Risultato: %d\n", dividendo / divisore);
}
else {
    printf("Errore: divisione per zero!\n");
}
```

**Controllo che un valore stia in un intervallo.** Si combinano la lettura riuscita e il confronto sull'intervallo (capitolo 18); grazie alla cortocircuitazione, se la lettura è fallita la temperatura non viene nemmeno confrontata:

```c
float temperatura;
bool inputOk = scanf("%f", &temperatura) == 1;
// 0 <= temperatura <= 100
if (inputOk && 0 <= temperatura && temperatura <= 100) {
    printf("Temperatura entro i limiti\n");
}
else {
    printf("Temperatura fuori intervallo o lettura errata\n");
}
```
