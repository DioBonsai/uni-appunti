# Capitolo 10: L'Input da Tastiera con scanf()
## Perché scanf ha bisogno dell'indirizzo
Un programma non deve solo mostrare risultati, ma spesso anche ricevere dati dall'utente. In C questo si fa con la funzione **scanf()** (le basi sono nel capitolo 8, qui ne approfondiamo il funzionamento), che legge i valori digitati da tastiera e li memorizza direttamente in variabili. Per leggere un intero in una variabile x già dichiarata si scrive:

```c
scanf("%d", &x);
```

Passando l'indirizzo &x, si permette a scanf() di sapere in quale cella di memoria scrivere il dato letto. La funzione termina quando l'utente ha inserito l'input e preme INVIO.

## Un esempio passo per passo
Nel programma seguente le tre variabili occupano, nello schema del corso, gli indirizzi 0x03FC (x), 0x03F8 (y) e 0x03F4 (z):

```c
int main(void) {
    int x, y, z;
    printf("Inserisci x: ");
    scanf("%d", &x);
    printf("Inserisci y: ");
    scanf("%d", &y);
    z = x + y;
    printf("%d + %d = %d\n", x, y, z);
}
```

Ecco come cambia la memoria durante l'esecuzione:
- all'inizio x, y e z hanno un valore indeterminato (nello schema, "?");
- se l'utente digita 5, la prima scanf scrive 5 nella cella di x;
- se poi digita 2, la seconda scanf scrive 2 nella cella di y;
- l'assegnamento calcola z = 7 e l'ultima printf stampa "5 + 2 = 7".

## Leggere più valori con una sola chiamata
Con una sola scanf si possono leggere più valori, indicando più specificatori e più indirizzi:

```c
scanf("%d%d", &x, &y);
```

L'utente può separare i due numeri con uno o più caratteri di spaziatura (ad esempio "5 2").

## Il valore di ritorno e i limiti di scanf
La gestione dell'input è un punto critico: l'utente può sempre inserire valori sbagliati o incompleti. La funzione scanf() prova a interpretare l'input in base al formato specificato e, se incontra un dato incompatibile (per esempio un carattere al posto di un numero), **smette di leggere** e restituisce il numero di valori letti con successo, che può essere minore di quelli attesi. Per esempio, dopo

```c
int x, y;
int n = scanf("%d%d", &x, &y);
```

- se n vale 2, entrambi i valori sono stati letti correttamente;
- se n vale 1, solo il primo valore era valido;
- se n vale 0, nessun valore è stato letto e le variabili non sono state aggiornate.

Vediamo il comportamento con un programma che legge un solo intero e stampa quanti valori ha letto:

```c
int main(void) {
    int x;
    printf("Inserisci un intero: ");
    int n = scanf("%d", &x);
    printf("Valori letti correttamente: %d\n", n);
    printf("x vale %d \n", x);
}
```

- con input 1234, scanf legge 1234 e restituisce 1;
- con input 1234.56, il formato %d si aspetta un intero: viene letto "1234" e ".56" rimane non consumato nell'input; n vale 1 e x vale 1234;
- con input A, la lettera non si può interpretare come numero decimale: n vale 0 e **x non viene aggiornata**. Poiché x non era stata inizializzata, la printf tenta di leggere un valore indeterminato e il comportamento del programma è indefinito.

## Dichiarare, avere un valore, avere un indirizzo, essere inizializzata
L'ultimo esempio mette in luce quattro nozioni da tenere distinte: la **dichiarazione** di una variabile, il suo **valore**, il suo **indirizzo** e il fatto che il valore sia stato **inizializzato**. In particolare è lecito ottenere &x anche se x non è ancora inizializzata: stiamo usando l'indirizzo di x e non leggendo il suo valore. Ma se x non viene inizializzata (in questo caso da scanf), non si può assumere nulla sul suo valore.

Se invece x era stata inizializzata, per esempio con int x = -1, e l'input non è interpretabile secondo la specifica di conversione, la variabile non viene modificata e conserva il suo valore (nell'esempio, resta -1). Se scanf non aggiorna una variabile non inizializzata, il suo valore resta indeterminato.

**Buona pratica**: conviene sempre controllare il valore restituito da scanf prima di usare le variabili lette. Per capire fino in fondo perché scanf richiede un indirizzo servono i puntatori, che vediamo nel prossimo capitolo.
