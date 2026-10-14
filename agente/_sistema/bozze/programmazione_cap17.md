# Capitolo 17: Espressioni Booleane e Operatori Logici
## Perché servono le condizioni
Un programma non si limita a fare calcoli: deve anche prendere decisioni. Le **condizioni** permettono di dire al computer "se succede questo, allora fai quello", e le **espressioni booleane** sono il linguaggio con cui le scriviamo. Con le espressioni booleane traduciamo domande come "il numero di somme ripetute richieste è stato raggiunto?" (il contatore dell'algoritmo di moltiplicazione del capitolo 2), "l'input da tastiera è corretto?" oppure "lo studente ha superato l'esame?". Sono il ponte tra i dati numerici e le scelte logiche: senza di esse un programma sarebbe soltanto una lunga sequenza rigida di calcoli.

## Operatori relazionali e logici in C
Per scrivere le condizioni il C mette a disposizione operatori relazionali, che confrontano due valori, e operatori logici, che combinano condizioni. Accanto a ciascuno si indica la notazione matematica corrispondente:
- **==** (uguaglianza, x = y in matematica): `x == y` vale 1 se i due valori sono uguali, altrimenti 0;
- **!=** (diversità, x ≠ y): `x != y` vale 1 se sono diversi, altrimenti 0;
- **>** e **<** (maggiore e minore): `x > y` e `x < y` valgono 1 se la relazione è vera, altrimenti 0;
- **>=** e **<=** (maggiore o uguale, minore o uguale, x ≥ y e x ≤ y): valgono 1 se la relazione è vera, altrimenti 0;
- **&&** (AND, congiunzione, b ∧ c): `x > 0 && y > 0` vale 1 se entrambe le condizioni sono vere;
- **||** (OR, disgiunzione, b ∨ c): `x == 0 || y == 0` vale 1 se almeno una delle due è vera;
- **!** (NOT, negazione, ¬b): `!(x > 0)` inverte il valore logico della condizione.

Il risultato di ogni espressione di questo tipo è quindi un numero, 1 per vero e 0 per falso. Gli operatori relazionali si usano spesso fra numeri: `contatore != n` verifica se le ripetizioni sono completate, `pinInserito == pinCorretto` confronta due codici, `temperatura <= limiteMax` controlla un limite e `voto >= 18` verifica la sufficienza all'esame.

C'è un errore da non commettere mai: **==** è l'uguaglianza, mentre **=** è l'assegnamento (capitolo 8). Scrivere `x = y` dentro una condizione non confronta due valori: copia y in x, e l'espressione vale il valore copiato (se ne vedrà la conseguenza nel capitolo 20).

## Il tipo bool
Le condizioni, nella logica di Boole, possono assumere solo due valori: **true** (vero) e **false** (falso). La logica di Boole, o algebra booleana, è il sistema matematico basato su questi due valori e sugli operatori fondamentali AND, OR e NOT, alla base dei circuiti digitali (le porte logiche di Fondamenti dell'Informatica) e della programmazione.

Storicamente il C non aveva un tipo booleano fra i tipi primitivi, e si usavano gli interi con questa interpretazione: **0 è falso, un valore diverso da 0 è vero**. Nel C moderno (dal C99) esiste l'header `<stdbool.h>`, che introduce:
- il tipo **bool**, simile a int ma che chiarisce che la variabile è booleana;
- le costanti **true** e **false**.

Nel corso si userà il C moderno dove possibile. Nello schema della memoria una variabile booleana si rappresenta come un singolo bit, 0 oppure 1. Nel programma seguente ci sono due int, x e y, e un bool b inizializzato a false: nello schema b occupa un solo bit, che vale 0.

```c
#include <stdio.h>
#include <stdbool.h>
int main(void) {
    int x = 1;
    bool b = false;
    int y = 2;
}
```

Una variabile booleana può memorizzare il risultato della valutazione di una condizione. Nel programma seguente `superato` vale 1 perché 25 è maggiore o uguale a 18:

```c
#include <stdio.h>
#include <stdbool.h>
int main(void) {
    int votoScritto = 25;
    int sogliaSuff = 18;
    bool superato = votoScritto >= sogliaSuff;
    printf("Lo studente supera l'esame? %d\n", superato);
}
```

L'output è `Lo studente supera l'esame? 1`. Per il tipo bool **non esiste uno specificatore di formato dedicato**: si usa %d, come per gli interi, e quindi viene stampato 0 oppure 1.

## Combinare più condizioni
Nei programmi spesso non basta verificare una sola condizione: occorre stabilire il rapporto logico fra più condizioni contemporaneamente. Le condizioni si combinano con tre operatori:
- la **congiunzione** `condizione1 && condizione2`, vera se entrambe le condizioni sono vere;
- la **disgiunzione** `condizione1 || condizione2`, vera se almeno una è vera;
- la **negazione** `!condizione`, che dà l'opposto del valore della condizione.

Alcuni esempi tradotti in C:

```c
bool login = (numTentativi < 3) && !accountBloccato;       // il login è possibile se i tentativi sono meno di 3 e l'account non è bloccato
bool riscaldamento = (temperatura < 18) && termostatoOn;    // il riscaldamento si accende se fa freddo e il termostato è attivo
bool sconto = (eta < 12) || tesserato;                      // lo sconto spetta ai minori di 12 anni oppure ai tesserati
bool ventolaAccesa = (temperatura >= 28) || modoManuale;    // la ventola si accende se fa caldo oppure è in modo manuale
```

## Le tavole di verità
Gli operatori si definiscono con le loro tavole di verità, le stesse viste in Fondamenti dell'Informatica per i connettivi logici. L'operatore **AND** restituisce vero (1) solo se entrambe le condizioni sono vere, e falso (0) in tutti gli altri casi. L'operatore **OR** restituisce vero se almeno una delle due condizioni è vera, ed è falso solo se entrambe sono false. L'operatore **NOT** restituisce l'opposto della condizione: vera diventa falsa e falsa diventa vera.

![Le tavole di verità di AND, OR e NOT.](figure/prog/ch17_tavole_booleane.png|13)

Nel prossimo capitolo si vede come usare questi operatori per confrontare un valore con un intervallo, come il C valuta le condizioni e come semplificare le espressioni complesse.
