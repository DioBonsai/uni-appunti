# Capitolo 23: Gli Array Statici: Dati Sequenziali, Indici e Memoria
## Dalle variabili singole alle collezioni
Finora abbiamo lavorato con **variabili scalari**: una variabile contiene un solo valore (un voto, un'altezza, un carattere). Molti problemi reali richiedono invece di gestire intere collezioni di dati **omogenei**, cioè tutti dello stesso tipo: i voti di una classe, una serie temporale di temperature o di prezzi, i caratteri di un testo.

La soluzione sono i **dati sequenziali** (o vettoriali): contenitori che raccolgono più valori dello stesso tipo in modo ordinato e permettono di raggiungerli tramite un **indice**.

(In parole povere: invece di avere cinque scatole separate con cinque nomi diversi, abbiamo una fila di cinque scatole numerate con un solo nome: per prendere quella che ci serve diciamo il nome della fila e il numero della scatola.)

## Che cos'è un array
Un **array** è una sequenza di valori dello stesso tipo, detti **elementi**, memorizzati in posizioni **contigue** di memoria. Le caratteristiche sono:
- tutti gli elementi hanno lo stesso tipo;
- ogni elemento si raggiunge tramite un indice;
- il numero di elementi è detto **lunghezza** (~length~) ed è fissato (noto);
- gli indici validi partono da **0** e arrivano a `length - 1`: appartengono quindi all'intervallo semiaperto [0, length), che include lo 0 ed esclude `length`.

(In parole povere: in un array di 5 elementi le posizioni valide sono 0, 1, 2, 3 e 4. Non esiste la posizione 5, anche se sembra "la quinta": si parte a contare da zero.)

Per rappresentare lunghezze e indici di array si usa normalmente `size_t`, il tipo intero senza segno (~unsigned~) che lo standard dedica alle dimensioni. È definito in `<stddef.h>`.

(In parole povere: `size_t` è il tipo «numero di elementi / posizione», un intero che non può essere negativo: adatto a contare e a indicare le posizioni di un array.)

Un **array statico** è un array la cui dimensione è fissata quando il programma viene compilato.

## Array statici: dichiarazione e accesso
Cominciamo dagli **array statici**: la loro dimensione è nota alla compilazione e vengono allocati sullo stack. La dichiarazione ha la forma `tipo nome[dimensione];` e l'accesso a un elemento si scrive `nome[indice]`.

```c
int numeri[4];             // array statico di 4 interi nello stack
numeri[0] = 10;            // primo elemento
numeri[1] = 20;            // secondo elemento
printf("%d\n", numeri[0]); // stampa 10
```

Gli elementi `numeri[2]` e `numeri[3]` non sono stati inizializzati: come per le variabili locali, in un array locale dichiarato senza inizializzatore gli elementi hanno **valore indeterminato**.

![Un array di 4 interi: elementi in celle contigue, indirizzi crescenti.](figure/prog/array_memoria.png|13)

## Come è fatto in memoria
Gli elementi di un array sono memorizzati in **celle contigue** e ogni cella ha la stessa dimensione (un `int` occupa tipicamente 4 byte). L'elemento di indice 0 si trova al primo indirizzo e gli altri seguono nell'ordine: se `numeri[0]` sta all'indirizzo 0x1000, allora `numeri[1]` sta a 0x1004, `numeri[2]` a 0x1008 e `numeri[3]` a 0x100C.

Dal punto di vista matematico un array si può vedere come un vettore numeri = (a₀, a₁, a₂, a₃), dove ogni elemento aᵢ è identificato dal suo indice i. Attenzione a una differenza di convenzione: in matematica gli indici di solito partono da 1, **in C partono sempre da 0**.

## Inizializzazione
Il C permette di definire un array statico inizializzato con una lista di valori noti (le tre righe che seguono sono alternative, non vanno scritte insieme nello stesso programma):

```c
int voti[5] = {18, 19, 24, 21, 30};
int voti[] = {18, 19, 24, 21, 30};   // equivalente: il compilatore conta i valori
int zeri[5] = {0};                   // tutti gli elementi a zero
```

(In parole povere: se si scrive la lista si può anche omettere la lunghezza, perché il compilatore la deduce contando gli elementi; con `{0}` si riempie tutto l'array di zeri.)

## Dimensioni fisse con #define
Per definire le dimensioni, che per gli array statici sono fisse, si usa una costante del preprocessore: `#define COSTANTE_LUNGHEZZA numero`. Un uso tipico è memorizzare serie di dati, scorrere gli elementi con un ciclo (`for`, `while`) ed elaborarli: statistica, calcoli, ordinamento.

```c
#define N 5
int voti[N] = {18, 24, 28, 30, 19};

for (size_t i = 0; i < N; i++) {
    printf("Voto %zu: %d\n", i, voti[i]);
}
```

La variabile di controllo `i` è di tipo `size_t`, perché è l'indice di accesso all'array; il suo specificatore di conversione per `printf` è `%zu`.

Nel capitolo successivo si approfondisce la **scansione** di un array e si vedono gli algoritmi più comuni: somma, media, conteggio e massimo.
