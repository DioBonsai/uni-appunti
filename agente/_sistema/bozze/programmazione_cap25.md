# Capitolo 25: Array e Puntatori, VLA ed Errori Comuni
## Array e puntatori sono oggetti diversi
Un array e un puntatore sono oggetti diversi. Tuttavia, nella maggior parte delle espressioni, il **nome di un array viene convertito automaticamente in un puntatore al suo primo elemento**. Si consideri `int v[5] = {10, 20, 30, 40, 50};`:
- `v` viene convertito in un valore di tipo `int*` che punta a `v[0]`;
- `&v[i]` è l'indirizzo dell'elemento di indice i;
- `*(v + i)` è uguale a `v[i]`: è un dereferenziamento con offset.

```c
printf("%p\n", (void*)v);        // indirizzo del primo elemento (%p vuole un void*)
printf("%p\n", (void*)&v[0]);    // stesso indirizzo
printf("%d\n", v[2]);     // 30
printf("%d\n", *(v+2));   // 30 (equivalente)
scanf("%d", &v[2]);       // legge da input e modifica v[2]
size_t array_sz = sizeof(v);  // dimensione dell'intero array
```

L'array resta un oggetto di tipo `int[5]`: è l'espressione `v` che, quando il contesto lo richiede, viene convertita in `int*`. Questo si vede nell'ultima riga: `sizeof(v)` dà la dimensione dell'intero array, non quella di un puntatore.

(In parole povere: il nome dell'array, quando lo si usa in un'espressione, diventa «l'indirizzo del primo elemento»; ma l'array in sé è sempre l'intera fila di elementi.)

## Indicizzazione e aritmetica dei puntatori
In C l'operatore di indicizzazione `[]` è definito come sintassi equivalente a un'operazione sugli indirizzi:

v[i] ≡ \*(v + i)

Incrementare un puntatore di i elementi fa avanzare l'indirizzo di i · `sizeof(tipo_elemento)` byte: `v + i` vale indirizzo_base + i · `sizeof(tipo_elemento)` byte. In pratica `v` è convertito nel puntatore al primo elemento (`&v[0]`), `v + i` è il puntatore all'elemento `v[i]` e `*(v + i)` è il valore dell'elemento `v[i]`.

(In parole povere: scrivere `v[i]` e scrivere «parti dall'inizio di v e spostati di i elementi» è la stessa cosa.)

Si usa quasi sempre la notazione `v[i]`, ma è utile capire che si tratta di un'operazione sugli indirizzi, parte della cosiddetta aritmetica dei puntatori.

## Variable Length Array (VLA)
Un limite degli array statici è che la dimensione deve essere stabilita alla compilazione: non può dipendere, per esempio, da un valore letto in input. Per i casi in cui la dimensione è nota solo a ~runtime~ il C, a partire dallo standard C99, ha introdotto i **Variable Length Array** (VLA): array allocati nello stack, ma con dimensione scelta al momento dell'esecuzione. La dichiarazione è l'unica cosa diversa rispetto agli array statici:

```c
size_t len;
scanf("%zu", &len);
int v[len];    // lunghezza len decisa a runtime
```

(In parole povere: un VLA è un array la cui lunghezza è decisa mentre il programma gira, per esempio chiedendola all'utente; una volta creato, però, la lunghezza non cambia.)

Un esempio completo:

```c
#include <stdio.h>

int main(void) {
    size_t n;
    printf("Quante persone? ");
    scanf("%zu", &n);

    int altezze[n];  // dimensione VLA indicata dall'utente

    // Caricamento da input
    for (size_t i = 0; i < n; i++) {
        printf("Inserisci altezza persona %zu (in cm): ", i + 1);
        scanf("%d", &altezze[i]);
    }

    // Stampa tabella
    printf("\nTabella delle altezze:\n");
    for (size_t i = 0; i < n; i++) {
        printf("Persona %zu: %d cm\n", i + 1, altezze[i]);
    }
}
```

## Errore: assegnare un array
In C gli array **non sono variabili assegnabili**: il loro nome rappresenta un indirizzo costante, non un valore.

```c
int a[3] = {1, 2, 3};
int b[3];
b = a;    // ERRORE: non si può assegnare un intero array
```

Per copiare un array bisogna scrivere un ciclo che copia gli elementi uno a uno:

```c
for (size_t i = 0; i < 3; i++)
    b[i] = a[i];
```

In generale gli array in C non si comportano come le variabili scalari: **non si copiano, non si confrontano e non si assegnano direttamente**.

## Errore: accesso fuori dai limiti
```c
int v[5] = {10, 20, 30, 40, 50};
printf("%d\n", v[5]);    // ERRORE: indice 5 fuori dall'intervallo [0, 5)
```

Il C **non controlla i limiti** degli array. Un accesso fuori dai limiti produce **comportamento indefinito**: il linguaggio non dà alcuna garanzia sul risultato; il programma può, per esempio, produrre risultati errati, corrompere la memoria o terminare. La buona pratica è scrivere codice che si assicuri che gli indici siano validi, cioè nell'intervallo semiaperto [0, length).

(In parole povere: se si chiede una posizione che non esiste, il C non avvisa e non si ferma: legge o scrive quello che trova lì, e il risultato può essere imprevedibile.)

Il capitolo successivo introduce il testo, che in C è un caso speciale di array: l'array di caratteri.
