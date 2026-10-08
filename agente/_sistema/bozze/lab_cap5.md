# Capitolo 5: Leggere e Scrivere con il Terminale
## I primi programmi
Scriviamo ora i programmi con un editor di testo semplice, ma adatto alla programmazione, ed eseguiamo manualmente i passi che servono per la compilazione, come visto nel capitolo 4.

Per compilare ed eseguire un programma si usano i comandi del capitolo 4, ad esempio `gcc -Wall -Werror scrivi_intero.c -o scrivi_intero` (su Windows con `-o scrivi_intero.exe`) e poi `./scrivi_intero` in Unix oppure `scrivi_intero` in Windows.

## Leggere un intero e stamparlo
Il primo programma, **scrivi_intero.c**, chiede un numero intero all'utente, lo legge con scanf e lo mostra a video con printf:

```c
#include <stdio.h>
int main(void) {
    int number;
    printf("Scrivi un numero intero: ");
    // leggi il numero inserito
    scanf("%d", &number);
    // mostra il numero a video
    printf("Hai scritto: %d\n", number);
    return 0;
}
```

La variabile number è un intero; scanf riceve l'indirizzo &number della variabile in cui scrivere il valore letto (come visto nei capitoli 8 e 10 del riassunto di teoria), mentre printf usa lo specificatore %d per stampare un intero.

## La tabella delle moltiplicazioni
Il secondo programma, **tabella_moltiplicazioni.c**, legge un intero n e stampa i suoi primi 10 multipli:

```c
#include <stdio.h>
int main(void) {
    int n;
    printf("Scrivi un numero intero: ");
    scanf("%d", &n);
    // stampa i primi 10 multipli di n
    for (int i = 1; i <= 10; ++i) {
        printf("%d * %d = %d \n", n, i, n * i);
    }
    return 0;
}
```

L'istruzione `for` ripete il blocco tra parentesi graffe: la variabile i parte da 1; la condizione i <= 10 si controlla prima di ogni giro e, alla fine di ogni giro, i aumenta di 1 (`++i`); ogni volta la printf stampa una riga della tabella.

## Gli esercizi proposti
Per prendere confidenza con il linguaggio, il laboratorio propone questi esercizi:
- stampare due righe usando due chiamate a printf;
- stampare due righe usando una singola chiamata a printf;
- chiedere due numeri e poi stamparli a video;
- stampare la somma di due numeri;
- dichiarare tre numeri interi x, y e z, inizializzati con i valori 5, 8 e 11, e stampare il loro prodotto con printf;
- leggere gli errori di compilazione.

L'ultimo punto è importante quanto gli altri: imparare a leggere i messaggi del compilatore, soprattutto con le opzioni -Wall -Werror che useremo all'esame, è parte dell'imparare a programmare.
