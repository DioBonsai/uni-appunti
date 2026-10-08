# Capitolo 9: Il Referenziamento e l'Indirizzo delle Variabili
## L'indirizzo di una variabile
Nel modello di Von Neumann ogni variabile è memorizzata nella memoria centrale e occupa una certa quantità di byte. Per identificarla, la CPU usa il suo **indirizzo di memoria**: un numero senza segno e univoco, analogo al numero civico di una casa. Per compattezza un indirizzo si visualizza di solito in formato esadecimale (ad esempio 0x7fffd0624e0c).

Il linguaggio C permette di ottenere questo indirizzo tramite l'**operatore di referenziamento** & (~ampersand~). L'espressione &x si legge "l'indirizzo della variabile x". L'operatore era già comparso nel capitolo 8, nella lettura con scanf: qui lo studiamo in dettaglio.

## Valore e indirizzo sono informazioni diverse
Ogni variabile ha due caratteristiche distinte: un valore e un indirizzo. Dato il codice:

```c
int main(void) {
    int x = 5;
}
```

Qui x è il **valore**, cioè il contenuto della cella di memoria (5), mentre &x è l'**indirizzo**, cioè la posizione della cella in memoria (nello schema del corso, 0x03FC). Le due espressioni non vanno confuse: indicano cose diverse.

## Perché è utile conoscere gli indirizzi
Poter nominare l'indirizzo di una variabile permette di scrivere istruzioni del tipo "moltiplica due numeri e memorizza il risultato in questa cella di memoria" oppure "leggi da tastiera un numero e memorizzalo nello spazio di memoria di una certa variabile". Ma c'è di più:
- è indispensabile per lavorare con i **puntatori**, cioè variabili il cui valore è un indirizzo di memoria;
- rende possibile gestire la memoria dinamica, le strutture dati complesse e la comunicazione efficiente tra funzioni.

Per cominciare ci limitiamo a un uso semplice: stampare gli indirizzi a video. (Come nelle slide, negli esempi si omette la riga #include <stdio.h>, necessaria per usare printf e scanf.)

## Stampare un indirizzo con %p
La funzione printf usa lo specificatore di conversione **%p** per mostrare un indirizzo, normalmente in forma esadecimale:

```c
int main(void) {
    int x = 5;
    int y = 2;
    int z = x + y;

    printf("La var x all'indirizzo %p vale %d \n", &x, x);
    printf("La var y all'indirizzo %p vale %d \n", &y, y);
    printf("La var z all'indirizzo %p vale %d \n", &z, z);
}
```

Un'esecuzione possibile produce:

```
La var x all'indirizzo 0x7fffd0624e0c vale 5
La var y all'indirizzo 0x7fffd0624e08 vale 2
La var z all'indirizzo 0x7fffd0624e04 vale 7
```

Si nota che le variabili dichiarate dopo hanno indirizzi più bassi, e che i tre interi da 4 byte occupano celle contigue: è coerente con il modello dello stack usato nel corso, che si sviluppa verso indirizzi decrescenti (capitolo 7).

## Il formato concreto degli indirizzi
Il valore concreto di un indirizzo dipende dalla piattaforma e dalla singola esecuzione del programma; di solito è un numero molto grande (i dettagli si vedono nel corso di Sistemi Operativi). Per questo il valore stampato **non deve mai essere incorporato nella logica del programma**.

Negli esempi del corso si usano indirizzi simbolici più corti, come 0x03FC, 0x03F8 e 0x03F4, per rendere leggibili gli schemi della memoria. Ciò che conta non è il valore numerico dell'indirizzo, ma il fatto che identifichi una posizione in memoria.
