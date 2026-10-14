# Capitolo 16: Conversioni di Tipo: Implicite, Promozione ed Esplicite
## Perché servono le conversioni
Quando in un programma si usano variabili di tipi diversi (interi, reali, caratteri), queste non hanno la stessa rappresentazione né le stesse caratteristiche. Per poterle usare in una stessa espressione, i valori devono essere trasformati in un formato compatibile: questo processo si chiama **conversione di tipo**. In C esistono due modalità:
- le **conversioni implicite**, eseguite automaticamente dal compilatore;
- le **conversioni esplicite** (dette **cast**), richieste in modo volontario dal programmatore.

In entrambi i casi la conversione può comportare una perdita di informazione o di precisione, ed è proprio questo il punto su cui occorre stare attenti.

## Le conversioni implicite
Il C permette di combinare nella stessa espressione variabili di tipi diversi (per esempio int, float e double): il compilatore provvede da solo a uniformarli, con un meccanismo chiamato **implicit casting**. L'avvertenza importante è che queste conversioni possono causare perdite di precisione **senza generare errori o avvisi**. L'esempio tipico, già incontrato nel capitolo 6 con `int y = 8.89;`, è assegnare un valore float a una variabile int: la parte frazionaria viene eliminata in silenzio.

I casi principali sono questi:
- **int → float** e **int → double**: la conversione è implicita e di norma non perde dati (il float può perdere precisione solo per interi molto grandi). Con `int x = 5; float y = x;` si ottiene y = 5.0;
- **float → int** e **double → int**: la parte frazionaria va persa, senza errore. Con `float x = 3.7; int y = x;` y vale 3, e con `double x = 9.9; int y = x;` vale 9. Se il valore è fuori dall'intervallo degli interi il comportamento è indefinito;
- **double → float**: si perde precisione. Con `double a = 3.14159; float b = a;` b vale circa 3.14159, ma con meno cifre affidabili;
- **char → int**: il valore ASCII del carattere viene promosso a int. Con `char c = 'A'; int x = c;` x vale 65;
- **conversioni non compatibili**: il compilatore le segnala come errore, come `int x = 5; int *p = x;`, che assegna un intero a un puntatore.

## La promozione di tipo
Quando si scrivono espressioni aritmetiche con operandi di tipo diverso, occorre capire i tipi di ciascun operando, seguendo le regole di **promozione di tipo** applicate dal compilatore, e valutare se la combinazione può causare una perdita di precisione o un risultato inatteso. Il principio è che i tipi "più piccoli" vengono promossi a tipi più grandi (char → short → int → long, e float → double quando l'altro operando è un double), così da ridurre la perdita di informazione. Se i tipi differiscono, il compilatore converte l'operando al tipo più ampio o più preciso. Se uno dei due è intero e l'altro reale, la promozione è a reale. Per esempio:
- char + int viene promosso a int;
- int + double viene promosso a double.

## La divisione tra interi
La promozione spiega un errore molto frequente. Consideriamo questo programma:

```c
int main(void) {
    int x = 5, y = 2;
    float z = x / y;
    printf("La var x vale %d\n", x);
    printf("La var y vale %d\n", y);
    printf("La var z vale %f\n", z);
}
```

Si potrebbe pensare che z valga 2.5, perché z è un float. Invece l'espressione `x / y` ha due operandi interi, quindi la divisione è una **divisione tra interi** e dà 2: la parte frazionaria si perde già durante la divisione. Il valore 2 viene poi assegnato a z con una conversione implicita da int a float, e z vale 2.000000. L'ultima printf stampa quindi `La var z vale 2.000000`.

Il contrario accade con un'altra variante:

```c
int main(void) {
    float x = 5, y = 2;
    int z = x / y;
    printf("La var x vale %f\n", x);
    printf("La var y vale %f\n", y);
    printf("La var z vale %d\n", z);
}
```

Ora la divisione tra float non ha problemi e dà 2.5, ma questo valore viene assegnato a una variabile int: è un casting implicito da float a int con perdita della parte frazionaria, e z vale 2. La stampa è `La var z vale 2`.

![Tre divisioni con tipi diversi: dove si perde la parte frazionaria (le prime due sono quelle di questa sezione, la terza è con il cast della sezione seguente).](figure/prog/ch16_conversioni_divisione.png|12.5)

## Le conversioni esplicite (cast)
Per decidere noi se e quando convertire si usa il **cast esplicito**, che si scrive indicando il tipo desiderato tra parentesi davanti all'espressione:

```c
int x = 5;
float z = (float)x;   // x viene convertito in float
```

È importante quando si vuole controllare il tipo di una specifica operazione, per esempio nella divisione tra interi:

```c
int x = 5, y = 2;
float z = x / (float)y;   // y convertito a float: risultato 2.5
```

Qui y viene convertito esplicitamente a float; di conseguenza, per le regole di promozione, nella divisione anche il valore di x viene portato a float (la variabile x resta int) e la divisione è tra reali, quindi z vale 2.500000. Il cast evita la perdita della parte frazionaria che si avrebbe con la divisione intera `x / y`.

Il cast agisce **solo sull'espressione immediatamente alla sua destra**. In `int x = 10, y = 3; float z = x / (float)y;` viene convertita in float soltanto l'espressione y, mentre x resta di tipo int (nella divisione il suo valore viene poi promosso a float dalle regole viste sopra, e z vale 3.333333). Il cast cambia il tipo dell'espressione durante la valutazione, non il tipo delle variabili coinvolte: x e y rimangono interi.
