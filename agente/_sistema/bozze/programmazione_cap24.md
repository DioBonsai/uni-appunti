# Capitolo 24: La Scansione degli Array: Somma, Conteggio e Massimo
## Che cos'è una scansione
Chiamiamo **scansione** di un array (~array traversal~, ~linear scan~) un ciclo che itera su **tutti gli indici validi** dell'array. Poiché gli indici validi formano l'intervallo semiaperto [0, length), da 0 incluso a `length` escluso, la scansione in avanti è

```c
for (size_t i = 0; i < length; i++) { /* usa v[i] */ }
```

(In parole povere: la condizione è `i < length` e non `i <= length`, perché l'ultimo elemento ha indice `length - 1`: se arrivassimo a `length` leggeremmo una posizione che non esiste.)

## Scansione all'indietro
Il ciclo in ordine inverso si scrive di solito in due forme. La prima usa ancora `size_t`: l'indice `i` va da `length` fino a 1 e si accede a `v[i-1]`, così non scende mai sotto zero:

```c
for (size_t i = length; i > 0; i--) { /* usa v[i-1] */ }
```

La seconda usa `ptrdiff_t`, il tipo intero **con segno** per gli indici (definito in `<stddef.h>`):

```c
for (ptrdiff_t i = (ptrdiff_t)length - 1; i >= 0; i--) { /* usa v[i] */ }
```

Qui serve `ptrdiff_t` invece di `size_t` perché l'indice deve **scendere sotto lo zero** per far terminare il ciclo, e `size_t` è un tipo unsigned: non può mai diventare negativo, quindi la condizione `i >= 0` sarebbe sempre vera.

Un esempio completo con le due scansioni:

```c
#include <stdio.h>
#include <stddef.h>    // definisce size_t e ptrdiff_t

int main(void) {
    #define N 5
    int v[N] = {10, 20, 30, 40, 50};

    // Scansione in avanti: indici [0, N)
    printf("Scansione in avanti:\n");
    for (size_t i = 0; i < N; i++) {
        printf("v[%zu] = %d\n", i, v[i]);
    }

    // Scansione all'indietro: indici [N-1, 0]
    printf("\nScansione all'indietro:\n");
    for (ptrdiff_t i = N - 1; i >= 0; i--) {
        printf("v[%td] = %d\n", i, v[i]);
    }
}
```

Lo specificatore di conversione di `printf` per `ptrdiff_t` è `%td`.

## Somma e media
Per elaborare una sequenza di voti si scorre l'array accumulando la somma e poi si divide per il numero di elementi:

```c
#define N 5
int voti[N] = {18, 19, 24, 21, 30};
int somma = 0;
for (size_t i = 0; i < N; i++) {
    somma += voti[i];
}
printf("Media: %f\n", somma / (float)N);
```

Il cast `(float)N` serve perché la divisione fra due interi darebbe un risultato intero (cap. 16 sulle conversioni di tipo). In notazione matematica la media è (1/N)·Σ aᵢ, la somma degli aᵢ divisa per N, con indici da 1 oppure da 0 a seconda della convenzione usata: in C gli indici partono da 0.

## Contare i valori che superano una soglia
Combinando ciclo e condizione si contano gli elementi che soddisfano una proprietà. Per contare i giorni in cui la temperatura supera la soglia 22.0:

```c
#define N 8
double temperature[N] = {18.5, 21.1, 25.2, 28.2,
                         19.4, 22.0, 26.3, 21.8};
int conta = 0;
for (size_t i = 0; i < N; i++) {
    if (temperature[i] > 22.0) {
        conta++;
    }
}
printf("Giorni caldi: %d su %d\n", conta, N);
```

(In parole povere: si scorre tutto l'array con un contatore a zero, e ogni volta che un elemento soddisfa la condizione il contatore sale di uno.)

## Il massimo di un array non vuoto
Per trovare il massimo si parte dal primo elemento come candidato e si aggiorna ogni volta che se ne incontra uno più grande:

```c
#define N 6
int numeri[N] = {3, 7, 2, 9, 5, 1};
int max = numeri[0];
for (size_t i = 1; i < N; i++) {
    if (numeri[i] > max) {
        max = numeri[i];
    }
}
printf("Massimo: %d\n", max);
```

Il ragionamento si può descrivere con una proprietà che resta vera a ogni passo del ciclo (un **invariante**): all'inizio (con i = 1) `max` è il massimo nell'intervallo [0, 1), cioè il solo `numeri[0]`; a ogni iterazione `max` è il massimo nell'intervallo [0, i); alla fine, quando i vale `length`, `max` è il massimo di tutto l'intervallo [0, length).

Questo programma funziona solo per array **non vuoti**: legge `numeri[0]` senza controllare che esista. Se la lunghezza fosse zero (cosa possibile quando la lunghezza si legge a ~runtime~, come con i VLA del capitolo 25), `numeri[0]` sarebbe un accesso fuori dai limiti.

Il capitolo successivo collega gli array ai puntatori e presenta gli errori più comuni.
