# Capitolo 12: Dereferenziamento, Alias e Puntatore Nullo
## L'operatore di dereferenziamento *
L'operatore unario **asterisco (\*)** (~dereference~ o ~indirect access~) permette di accedere alla variabile puntata attraverso l'indirizzo memorizzato nel puntatore. Dereferenziare un puntatore significa usare l'indirizzo che contiene per accedere indirettamente alla variabile puntata. Per esempio:

```c
int y = 5;
int* pY = &y;
printf("%d", *pY);
```

Qui *pY accede alla stessa cella di memoria di y, perché pY ne contiene l'indirizzo. Il tipo segue una regola semplice: se un puntatore p ha tipo T*, allora l'espressione *p ha tipo T. Negli esempi di questo capitolo si alternano le scritture int* pX e int *pX, equivalenti.

## Leggere e modificare tramite il puntatore
Con int x = 5; e int* pX = &x; si può accedere alla variabile puntata in due modi:
- **in lettura**: printf("%d\n", *pX) stampa 5, il valore della variabile puntata, come x;
- **in modifica**: *pX = 10; assegna un nuovo valore alla variabile puntata; dopo l'istruzione x vale 10.

```c
int x = 5;
int *pX = &x;
printf("x = %d\n", x);      // stampa 5
printf("*pX = %d\n", *pX);  // stampa ancora 5
*pX = 10;                   // modifica x tramite pX
printf("x = %d\n", x);      // stampa 10
```

x e *pX accedono alla **stessa cella**, quindi leggono lo stesso valore: scrivere in *pX modifica x.

## Riferimenti multipli e aliasing
Due puntatori possono contenere lo stesso indirizzo:

```c
int x = 5;
int* pX = &x;
int* pXbis = pX;
*pXbis = 1234;
printf("x = %d\n", x);          // 1234
printf("*pX = %d\n", *pX);      // 1234
printf("*pXbis = %d\n", *pXbis);// 1234
```

La scrittura su *pXbis avviene nella cella di x: x, *pX e *pXbis indicano la stessa variabile (*pX e *pXbis sono alias di x). pX e pXbis sono due variabili puntatore diverse, ma contengono lo stesso indirizzo. Di conseguenza le tre istruzioni scanf("%d", &x), scanf("%d", pX) e scanf("%d", pXbis) sono equivalenti: indicano sempre la stessa cella.

Questo fenomeno si chiama **aliasing**. Quando si dichiara una variabile in C, essa è accessibile tramite un solo nome simbolico (x). Con i puntatori più "etichette" possono invece fare riferimento allo stesso dato: sia il nome diretto della variabile, sia uno o più puntatori che ne contengono l'indirizzo. Modificando la variabile attraverso uno degli alias, anche gli altri "vedono" il nuovo valore, perché accedono allo stesso indirizzo.

## Puntatori non inizializzati e puntatore nullo
Si può dereferenziare un puntatore **solo se contiene un indirizzo valido**. Dopo la sola dichiarazione, un puntatore ha un valore indeterminato, come ogni variabile automatica non inizializzata, e quel valore non può essere usato come indirizzo: dereferenziarlo è un errore a tempo di esecuzione (comportamento indefinito).

```c
int* pX;   // non inizializzato
*pX = 10;  // ERRORE
```

Per dare a un puntatore un valore esplicito che significa "non punta a niente" si usa **NULL**, valore di puntatore che indica che quel puntatore non fa riferimento ad alcuna variabile. Si usa come valore di inizializzazione o come valore sentinella:

```c
int main(void) {
    int *p = NULL; // inizializzazione sicura
    *p = 10;       // ERRORE: p non contiene un indirizzo accessibile
}
```

NULL consente di inizializzare esplicitamente un puntatore, evitando un valore indeterminato, e di riconoscere esplicitamente il caso "non punta ad alcuna variabile". Attenzione: dereferenziare un puntatore NULL produce un comportamento indefinito (in genere un errore che termina il programma).

## La dimensione di un puntatore
Un puntatore occupa memoria come ogni variabile, ma la sua dimensione dipende dalla **piattaforma** e non dalla dimensione del tipo puntato. Su una tipica CPU a 64 bit un puntatore occupa 8 byte, su una tipica CPU a 32 bit 4 byte:

```c
int x;
int* pX;
printf("sizeof(x) %zu B\n", sizeof(x));   // 4 B
printf("sizeof(pX) %zu B\n", sizeof(pX));  // 8 B su piattaforma a 64 bit
```

## & e * sono operazioni complementari
Se int a = 7; e int* pA = &a;, allora l'indirizzo di a, il valore di pA, &*pA e *&pA coincidono, mentre a e *pA valgono entrambi 7: gli operatori & e * si "annullano" a vicenda.

## I diversi usi del simbolo *
Il simbolo * (~star~) si usa in C con quattro significati:
1. operatore di **moltiplicazione**: int x = a * b;
2. **dichiarazione** di una variabile di tipo puntatore: int* pX = &x;
3. **dereferenziamento** di un puntatore: int x = *pX;
4. **puntatore a puntatore** (non trattato nel corso): int\*\* ppX = &pX; pX = \*ppX; \*\*ppX = 10;

Distinguere il contesto in cui compare l'asterisco è il modo per non confondere questi usi. I puntatori sono la base per gestire la memoria dinamica, le strutture dati complesse e la comunicazione efficiente tra funzioni.
