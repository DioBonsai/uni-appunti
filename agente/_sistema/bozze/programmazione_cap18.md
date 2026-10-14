# Capitolo 18: Intervalli, Cortocircuitazione e Semplificazione delle Condizioni
## Confronti su intervalli
Nei programmi spesso si deve verificare se un valore cade in un certo intervallo: un indice, una temperatura, un'età. In matematica la condizione si scrive in modo compatto, `min ≤ x ≤ max`. In C bisogna invece **spezzare il confronto in due condizioni** e combinarle con un AND: `min <= x && x <= max`, che è la forma più vicina alla notazione matematica.

Scrivere in C `min <= x <= max` non produce l'effetto sperato, e il pericolo è proprio che compila senza errori. Il confronto si valuta da sinistra a destra: prima `min <= x`, che dà 0 oppure 1, e poi quel risultato viene confrontato con max. Con min = 0, x = 20 e max = 10, per esempio, `0 <= 20` vale 1 e `1 <= 10` è vero, anche se 20 non sta nell'intervallo.

I quattro tipi di intervallo si traducono così:
- **chiuso** (inclusivo), x ∈ [min, max]: `min <= x && x <= max`;
- **semiaperto sinistro**, x ∈ [min, max): `min <= x && x < max`;
- **semiaperto destro**, x ∈ (min, max]: `min < x && x <= max`;
- **aperto** (esclusivo), x ∈ (min, max): `min < x && x < max`.

![I quattro tipi di intervallo e la loro espressione in C: il cerchio pieno include l'estremo, quello vuoto lo esclude.](figure/prog/ch18_intervalli.png|13)

Le denominazioni "sinistro" e "destro" sono quelle usate nel corso: contano le notazioni tra parentesi. Nel corso si userà molto questa notazione per verificare se un indice appartiene a un intervallo semiaperto sinistro.

## La cortocircuitazione
Quando si combinano più condizioni con AND oppure OR, il C interrompe la valutazione appena il risultato è già determinato (lo standard lo garantisce). Questo comportamento si chiama **cortocircuitazione** (in inglese *short-circuit evaluation*):
- con l'**AND**, se la prima condizione è falsa il risultato è sicuramente falso, e la seconda non viene valutata;
- con l'**OR**, se la prima condizione è vera il risultato è sicuramente vero, e la seconda non viene valutata.

La cortocircuitazione non è solo un risparmio di tempo, ma permette di scrivere condizioni che altrimenti sarebbero pericolose. Per verificare che il divisore sia diverso da zero e che la divisione dia un risultato maggiore di 5 si scrive:

```c
bool condizione = (divisore != 0) && ((numeratore / divisore) > 5);
```

Se il divisore è 0 la seconda parte non viene eseguita, e si evita l'errore a tempo di esecuzione della divisione per zero. Un altro esempio verifica che l'utente abbia inserito un numero e che sia pari:

```c
int valore;
bool scanPari = (scanf("%d", &valore) == 1) && (valore % 2 == 0);
```

Se scanf non riesce a leggere il valore (il suo risultato, come visto nel capitolo 10, non è 1), la parte a destra non viene valutata e non si guarda il contenuto di valore, che in quel caso non è affidabile.

Lo stesso schema si ritrova in un programma completo, che legge un numero e stampa tre risultati:

```c
#include <stdio.h>
#include <stdbool.h>
int main(void) {
    int numero;
    bool letto, positivo, dispari;
    printf("Inserisci un numero intero: ");
    letto = (scanf("%d", &numero) == 1);     // true se scanf ha letto correttamente
    positivo = letto && (numero > 0);         // input valido e maggiore di 0
    dispari  = letto && (numero % 2 != 0);    // input valido e non divisibile per 2
    // stampa i risultati (0 = falso, 1 = vero)
    printf("Input valido? %d\n", letto);
    printf("Numero positivo? %d\n", positivo);
    printf("Numero dispari? %d\n", dispari);
}
```

Se l'utente inserisce 7 il programma stampa 1 per tutte e tre le domande; se inserisce una lettera, `letto` vale 0 e di conseguenza anche le altre due condizioni valgono 0.

## Semplificare le espressioni complesse
Le espressioni booleane con molti AND e OR mescolati diventano difficili da leggere, facili da scrivere in modo sbagliato e complicate da modificare. Ecco un esempio:

```c
bool sconto = registrato && spesaTotale >= 100 ||
              (codiceNonScaduto && attivatoDallUtente);
```

Si procede spezzando l'espressione in sotto-condizioni con nomi chiari, usando variabili booleane intermedie e rendendo la condizione finale la combinazione semplice di pochi termini:

```c
bool clientePremium = registrato && (spesaTotale >= 100);
bool promoExtra     = codiceNonScaduto && attivatoDallUtente;
bool sconto         = clientePremium || promoExtra;
```

Le due versioni calcolano la stessa cosa, perché in C l'AND ha la precedenza sull'OR; ma la seconda si legge a colpo d'occhio e ogni condizione ha un nome che spiega a che cosa serve.

## L'operatore condizionale ternario
L'**operatore ternario** è un operatore condizionale compatto, che ha la forma `condizione ? valore_se_vero : valore_se_falso`. Si valuta la condizione: se è vera l'espressione vale il primo valore, se è falsa vale il secondo. È utile per piccole espressioni condizionali, ma solo se non pregiudica la semplicità del codice:

```c
int x = 5;
int y = (x % 2 == 0) ? 100 : 200;   // y = 200, perché x è dispari
```

Per condizioni più articolate è meglio usare i blocchi `if..else`, che sono l'argomento del prossimo capitolo.
