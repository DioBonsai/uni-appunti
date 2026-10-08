# Capitolo 11: I Puntatori
## Il puntatore come tipo di dati
Un **puntatore** è una variabile che memorizza l'indirizzo di memoria di un'altra variabile, detta ~variabile puntata~. Il valore contenuto in un puntatore è quindi un indirizzo, anziché direttamente il dato puntato. Se per esempio la variabile int x = 5 ha indirizzo &x pari a 0x03FC, ci serve un posto dove memorizzare 0x03FC: quel posto è una variabile puntatore.

In C, per ciascun tipo di dati T esiste il corrispondente **tipo puntatore** T\* ("T star"): le variabili di tipo T* servono a memorizzare gli indirizzi delle variabili di tipo T. Per esempio:
- int è il tipo delle variabili intere;
- int* è il tipo delle variabili puntatore che possono contenere indirizzi di variabili int;
- float* è il tipo dei puntatori a float.

```c
int x = 5;
int* pX;
```

Qui x è una variabile di tipo int e pX è una variabile "puntatore agli interi", di tipo int*. Per convenzione si usa spesso il prefisso p nei nomi dei puntatori. Attenzione: dopo la sola dichiarazione, pX **non contiene ancora un indirizzo valido** da usare.

## L'operatore di referenziamento e l'assegnamento a un puntatore
L'operatore & (~address-of~), applicato a una variabile, ne restituisce l'indirizzo con tipo "puntatore al tipo della variabile". Possiamo allora inizializzare il puntatore:

```c
int x = 5;
int* pX = &x;   // pX riceve l'indirizzo di x
```

Le tre espressioni si interpretano così:
- x è una variabile intera, di valore 5;
- &x è un'espressione che vale l'indirizzo di x, di tipo int* (se x è int, allora &x è int*);
- pX è un puntatore a intero che memorizza l'indirizzo di x.

L'operatore & va applicato a qualcosa che identifica una posizione di memoria: non si può applicare a un semplice valore né al risultato temporaneo di un calcolo. Sono quindi errori:

```c
&5        // ERRORE
&(x + 1)  // ERRORE
```

## Un puntatore è una variabile come le altre
Nello schema della memoria la variabile x contiene il valore 5 all'indirizzo 0x03FC, mentre la variabile pX contiene 0x03FC, cioè l'indirizzo di x, e si trova a sua volta a un indirizzo proprio (nell'esempio 0x03F8). Un puntatore contiene un indirizzo, ma essendo una variabile occupa memoria e ha anche un suo indirizzo. L'assegnamento pX = &x è corretto perché &x e pX hanno lo stesso tipo, int*.

Per vederlo si possono stampare sia l'indirizzo del puntatore (&pX) sia il suo valore (pX):

```c
int main(void) {
    int x = 5;
    int* pX;
    pX = &x;
    printf("Il ptr pX all'ind %p vale %p \n", &pX, pX);
}
```

Con gli indirizzi simbolici dello schema, l'output sarebbe "Il ptr pX all'ind 0x03F8 vale 0x03FC".

## Due errori tipici
- **Usare &x prima di aver dichiarato x**: il compilatore segnala un errore ("'x' undeclared"), perché al momento di int* pX = &x la variabile x non esiste ancora.
- **Tipi incompatibili**: se x è un float, &x ha tipo float* e non è compatibile con una variabile int*; il compilatore avverte con un warning ("initialization of 'int *' from incompatible pointer type 'float *'"). Nei compilatori più recenti (ad esempio GCC 14) questo caso è invece un errore di compilazione.

## Come si scrive la dichiarazione
Finora abbiamo scritto int* pX, ma è in uso frequente anche la convenzione int *pX. Il simbolo * ha anche un altro significato nelle operazioni sui puntatori, il dereferenziamento, che vediamo nel prossimo capitolo.

## scanf riletta con i puntatori
La documentazione di scanf richiede che ogni conversione riceva un **puntatore al tipo appropriato**: per %d serve un int*. Con int x, l'espressione &x ha proprio tipo int*, ed è per questo che scanf("%d", &x) funziona: scanf può scrivere in quella cella il valore letto. Ma allora al posto di &x si può passare direttamente un puntatore che contiene lo stesso indirizzo:

```c
int main(void) {
    int x;
    int* pX = &x;
    printf("Inserisci un intero: ");
    scanf("%d", pX);
    printf("La var x all'ind %p vale %d \n", pX, x);
}
```

L'assegnamento pX = &x è lecito anche se x non è ancora inizializzata (si usa l'indirizzo, non il valore). Dopo che l'utente ha digitato 5, la cella di x contiene 5, e la printf mostra l'indirizzo contenuto in pX e il valore di x.
