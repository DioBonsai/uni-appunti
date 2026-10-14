# Capitolo 15: La Libreria math.h e la Lettura della Documentazione
## Oltre le operazioni di base
Gli operatori del C (+, -, *, / e, per gli interi, %) coprono solo le operazioni aritmetiche di base. Per le funzioni matematiche più avanzate, come radici, potenze, logaritmi e funzioni trigonometriche, si usa la libreria **math.h**, da includere con:

```c
#include <math.h>
```

La libreria fornisce una serie di funzioni utili, tra cui **sqrt()** (radice quadrata), **pow()** (potenza), **sin()** e **cos()**, disponibili in versioni per float, double e long double (con i suffissi f e l; un argomento int viene convertito automaticamente a double). L'elenco completo è consultabile nella documentazione online della libreria (per esempio su cppreference.com, alla pagina dedicata all'header math.h).

C'è un'avvertenza pratica per chi lavora in ambiente Unix: l'uso di math.h richiede di indicare al compilatore anche la libreria matematica, con l'opzione **-lm** da aggiungere alla fine del comando, per esempio `gcc programma.c -lm`. Senza questa opzione la fase di collegamento può fallire sulle funzioni di math.h (tipicamente con un errore di "undefined reference").

## Un esempio: quadrato e radice
Il programma seguente calcola il quadrato e la radice quadrata di un numero reale e li stampa con due decimali:

```c
#include <stdio.h>
#include <math.h>

int main(void) {
    float num = 9.0, radice, quadrato;
    quadrato = pow(num, 2);
    radice = sqrt(num);
    printf("Il quadrato di %.0f è %.2f\n", num, quadrato);
    printf("La radice di %.0f è %.2f\n", num, radice);
}
```

Qui `pow(num, 2)` calcola 9 elevato alla seconda, cioè 81, e `sqrt(num)` calcola la radice quadrata di 9, cioè 3. L'output è:

```
Il quadrato di 9 è 81.00
La radice di 9 è 3.00
```

Nella printf, `%.0f` stampa num senza decimali (9), mentre `%.2f` stampa i due risultati con due decimali (capitolo 14). Le funzioni di math.h lavorano in genere con valori double; qui il risultato viene assegnato a variabili float, con una conversione di tipo implicita di cui si parlerà nel capitolo 16.

## Imparare a leggere la documentazione
Come sottolineato a lezione, è utile imparare a leggere la documentazione: la libreria standard contiene molte più funzioni di quelle che servono di volta in volta, ma ognuna ha una descrizione rigorosa, a cui si ricorre quando si vuole capire che cosa fa una funzione specifica.

Prendiamo come esempio il calcolo della radice quadrata. La funzione si chiama **sqrt**, abbreviazione di *square root*. Aprendo la sua pagina nella documentazione (per esempio quella di cppreference per sqrt) si legge in sostanza:
- **dichiarazione**: la funzione è definita nell'header math.h e ne esistono tre varianti, una per ciascun tipo: `double sqrt(double arg)`, `float sqrtf(float arg)` e `long double sqrtl(long double arg)` (le ultime due introdotte con lo standard C99). Negli esempi useremo `sqrt`;
- **parametro**: `arg` è il valore in virgola mobile di cui calcolare la radice;
- **valore restituito**: la radice quadrata di arg;
- **errori**: se arg è minore di zero la radice non è definita nei reali (errore di dominio) e viene restituito un valore definito dall'implementazione (di solito NaN, *not a number*, dove supportato).

Le pagine di cppreference sono organizzate in questo modo, con le stesse sezioni per ogni funzione, e una volta capito come leggere quella di sqrt si può fare lo stesso con le altre.

Il prossimo capitolo torna sulle conversioni di tipo, che qui sono comparse in modo implicito.
