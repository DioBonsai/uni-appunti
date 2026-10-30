# Capitolo 28: Parametri, Passaggio per Valore, Return ed Errori Comuni
## Più parametri e un solo valore di ritorno
Una funzione può avere **più parametri**, separati da virgola, ciascuno con il suo tipo e il suo nome:

```c
float potenza(float base, int exp);
float risultato = potenza(10, 3);   // base = 10, exp = 3
```

La chiamata passa i valori **in ordine**: il primo argomento al primo parametro, il secondo al secondo, e così via.

In C una funzione può restituire **al massimo un valore** con `return`. Se serve restituirne più di uno ci sono due possibilità: usare **puntatori** e parametri di uscita, oppure costruire strutture dati (le `struct`, che in questo corso non si vedono).

## Prototipi con soli tipi
Nei prototipi i nomi dei parametri sono **facoltativi**: `float potenza(float, int);` è un prototipo valido. È utile per brevità, ma per chiarezza è sempre meglio indicare i nomi.

## Le regole per il return
Si distinguono due casi.
1. **Funzioni con ritorno** (`int`, `float`, …): ogni percorso di esecuzione di una funzione non `void` deve arrivare a un `return <espressione>` appropriato. Una buona pratica è un solo `return` alla fine.
2. **Funzioni `void`**: possono omettere il `return`; facoltativamente si può esplicitare il punto di uscita con `return;`.

**In parole povere:** una funzione che promette di restituire un numero deve farlo in qualunque modo il programma ci arrivi; una funzione `void` invece può finire anche «da sola», quando termina il corpo.

## Parametro formale e argomento
Due parole spesso confuse:
- il **parametro formale** è la variabile definita nella dichiarazione o definizione della funzione; è come una **variabile locale** alla funzione che contiene il valore passato all'inizio della chiamata;
- l'**argomento** (o **parametro attuale**) è il valore passato alla funzione al momento della chiamata, e viene **copiato** nel parametro formale corrispondente.

```c
int square(int x) {   // x è un parametro formale
    return x * x;
}

int y = square(5);    // 5 è un argomento
int z = square(y);    // y è un argomento
```

**In parole povere:** il parametro formale è il «segnaposto» scritto nella definizione; l'argomento è il valore vero che si mette al suo posto quando si chiama la funzione.

## Il passaggio per valore
In C l'argomento viene sempre passato **per valore** (~by value~): alla funzione viene passata una **copia** del valore, assegnata al parametro formale corrispondente. La funzione può quindi modificare solo una copia locale, e **non può influenzare le variabili di chi l'ha chiamata**:

```c
void incr(int x) { x++; }   // non modifica il chiamante
```

Dopo `incr(a)`, la variabile `a` del chiamante non è cambiata: è cambiata solo la copia `x`. Tuttavia si può passare (sempre per valore) un **puntatore**: attraverso il puntatore la funzione può fare un accesso indiretto alla variabile del chiamante e modificarla. Questo schema si vedrà più avanti nel dettaglio.

**In parole povere:** passare per valore vuol dire che la funzione lavora su una fotocopia del dato: puoi scarabocchiarla quanto vuoi, l'originale resta com'era; solo dandole l'indirizzo dell'originale (un puntatore) può cambiarlo.

## Riepilogo dei termini

- **Parametro formale**: sta nella definizione della funzione; per esempio in `int square(int x)` x è formale.
- **Argomento (parametro attuale)**: sta nella chiamata; in `square(5)` il 5 è attuale.
- **Passaggio per valore**: è il meccanismo predefinito in C; `incr(x)` non modifica x.
- **Passaggio di un indirizzo**: si fa con i puntatori; `incrPtr(&x)` modifica x nel chiamante.
- **Chiamata di funzione**: è nel codice del chiamante, come `y = square(5);`.

## Errori comuni
**1. Dimenticare il return in una funzione non void.**

```c
int square(int x) {
    x * x;   // ERRORE: manca return
}
```

Il compilatore di solito segnala un ~warning~: una funzione non `void` deve restituire il valore previsto.

**2. Tipi incoerenti fra prototipo e definizione.**

```c
// Prototipo
float square(float x);
// Definizione
int square(int x) {   // ERRORE: tipi diversi dal prototipo
    return x * x;
}
```

**3. Numero o ordine errato dei parametri.**

```c
int max(int a, int b);
int main(void) {
    int m = max(10);        // ERRORE: manca un argomento
    int n = max(10, 3.5);   // conversione implicita: 3.5 diventa 3
}
```

Nel secondo caso non c'è errore di compilazione, ma una conversione implicita (cap. 16): il valore 3.5 viene troncato a 3, perché il parametro è un `int`.

**4. Funzioni troppo «pesanti».** Una funzione `gestisciTutto(void)` che fa input, calcoli, stampa e scrittura su file è meglio spezzarla in più funzioni semplici: una funzione per ogni compito (e una funzione molto lunga è anche più difficile da leggere e da testare, cap. 29).

**Chiarezza nei nomi.** Con `int f(int a, int b, int c);` non si capisce che cosa faccia f né che cosa significhino a, b e c; è meglio `int calcolaPrezzo(int quantita, int sconto, int iva);`.

Il capitolo successivo mostra come si usano le funzioni per scomporre un programma.
