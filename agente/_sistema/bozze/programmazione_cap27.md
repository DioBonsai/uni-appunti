# Capitolo 27: Le Funzioni in C: Definizione, Prototipo e Chiamata
## Perché servono le funzioni
Finora tutto il codice è stato scritto dentro `main()`. Per programmi semplici può bastare, ma appena il codice cresce diventa lungo, ripetitivo, difficile da capire e da mantenere. Scrivere programmi grandi richiede strumenti per **organizzare il codice**: come dice una frase di Gerald Weinberg (*The Psychology of Computer Programming*, 1971), «la chiave per scrivere programmi grandi è non scrivere mai programmi grandi».

Un esempio: si deve calcolare più volte il massimo fra due numeri.
- **Senza funzioni** ogni volta si copia il codice, con il rischio di errori, duplicazioni inutili e codice ripetitivo e noioso.
- **Con le funzioni** il codice per il massimo si separa una volta sola e si riutilizza ogni volta che serve.

**In parole povere:** una funzione è una «macchinetta» a cui si dà un nome: si scrive una volta cosa fa e poi la si può usare quante volte si vuole, senza ricopiarla.

## Che cos'è una funzione in C
Una **funzione** (talvolta chiamata anche metodo, procedura o ~subroutine~) è un **blocco di codice con un nome**, che può ricevere dati in ingresso (i **parametri**), eseguire istruzioni e restituire un risultato (il **valore di ritorno**). Le funzioni servono a organizzare il programma in parti indipendenti, riutilizzabili e più facili da leggere e mantenere. Il concetto ha un forte parallelo con quello matematico, ma non coincide completamente con esso.

(In parole povere: una funzione C è un pezzo di programma con un nome, che prende dei dati, fa qualcosa e può restituire un risultato.)

## Richiamo: la funzione in matematica
Siano A e B due insiemi di valori. Una funzione f : A → B associa a ogni elemento x ∈ A un unico elemento f(x) ∈ B, dove A è il **dominio**, B è il **codominio** e f(x) è il valore associato all'argomento x. Per esempio f : ℝ → ℝ, f(x) = x²: la scrittura f : ℝ → ℝ specifica dominio e codominio, mentre la **regola di corrispondenza** f(x) = x² dice come si determina il valore associato a ogni argomento. **Applicare** (o valutare) la funzione a un argomento dà f(3) = 9.

## La sintassi di una funzione in C
Gli elementi della funzione matematica si ritrovano nella sintassi del C:

```c
<tipo_ritorno> nomeFunzione(<lista_parametri>) {
    // corpo della funzione
    istruzioni;
    return valore;   // opzionale se tipo_ritorno è void
}
```

- `<tipo_ritorno>`: il tipo del valore che la funzione restituisce (`int`, `float`, …, oppure `void` se non restituisce alcun valore);
- `nomeFunzione`: l'identificatore con cui si chiama la funzione da altre parti del programma;
- `<lista_parametri>`: i parametri di ingresso, ciascuno con tipo e nome;
- il **corpo** (~function body~): le istruzioni da eseguire;
- `return`: il valore restituito a chi ha chiamato la funzione (obbligatorio se il tipo di ritorno non è `void`).

**In parole povere:** la prima riga della funzione, con il tipo di ritorno, il nome e i parametri, è la «carta d'identità»: dice cosa entra, cosa esce e come si chiama.

## Un primo esempio: square
Si definisce una funzione `square`, corrispondente a f(x) = x²:

```c
float square(float x);        // prototipo

float square(float x) {       // definizione
    return x * x;
}
```

Il **prototipo** (~function prototype~) dichiara il nome della funzione, il tipo dei parametri e il tipo del valore restituito: è l'analogo della specifica di dominio e codominio f : ℝ → ℝ. La **definizione** specifica il codice da eseguire e realizza la regola di corrispondenza f(x) = x². La **chiamata** applica la funzione a un argomento, come la valutazione y = f(x):

```c
float x2 = square(3.14f);
float y2 = square(y);
```

## Prototipo, definizione e chiamata
Sono tre cose distinte.
- **Prototipo** (opzionale): dice al compilatore che la funzione esiste e quali sono il suo nome, il tipo di ritorno e i tipi dei parametri; **non contiene il codice**.
- **Definizione** (~function definition~ o ~implementation~): contiene il codice con le istruzioni da eseguire e deve rispettare il prototipo (tipi e numero dei parametri, tipo di ritorno).
- **Chiamata** (~function call~ o ~invocation~): usa la funzione in un'espressione o in un'istruzione e passa **valori effettivi** ai parametri formali.

**In parole povere:** il prototipo è l'annuncio («esiste una funzione fatta così»), la definizione è la ricetta completa, la chiamata è l'uso.

Un programma completo che le contiene tutte e tre:

```c
#include <stdio.h>

// PROTOTIPO (dichiarazione)
float square(float x);

int main(void) {
    float a = 3.14f;
    float risultato = square(a);   // CHIAMATA alla funzione
    printf("%f al quadrato = %f\n", a, risultato);
}

// DEFINIZIONE (implementazione)
float square(float x) {
    return x * x;   // RETURN: restituisce un float al chiamante
}
```

## Funzioni matematiche e funzioni C
La nozione di funzione in C riprende molti elementi di quella matematica:
- il **dominio** A trova una corrispondenza nei valori ammessi per il parametro, rappresentati in C dal tipo degli argomenti;
- il **codominio** B trova una corrispondenza nei valori che la funzione può restituire, determinati dal tipo di ritorno;
- la **regola di corrispondenza** f(x) è realizzata dalle istruzioni nel corpo della funzione;
- la **valutazione** y = f(a) corrisponde alla chiamata di funzione: `B y = f(a);`.

Una funzione C può quindi realizzare una funzione matematica come procedimento di calcolo. Ma **non è equivalente**:
- una funzione matematica è una definizione, una relazione tra valori; associa a ogni elemento del dominio un unico risultato nel codominio; non implica esecuzione né stato: a parità di argomento il risultato è lo stesso;
- una funzione C descrive un comportamento computazionale eseguito su una macchina; può calcolare e restituire un valore oppure non restituirne alcuno (`void`); può leggere o modificare lo stato del programma, producendo **effetti collaterali**; può quindi produrre comportamenti diversi anche con gli stessi argomenti.

**In parole povere:** in matematica la stessa x dà sempre lo stesso f(x); una funzione C, invece, è un'azione che il computer esegue, e può per esempio leggere un valore da tastiera o stampare qualcosa, quindi non è detto che a parità di argomenti faccia sempre la stessa cosa.

## Le quattro forme di funzione
Combinando presenza o assenza di parametri e di valore di ritorno si hanno quattro casi:

```c
int max(int a, int b) {            // con ritorno e con parametri
    return (a > b) ? a : b;
}

int leggiNumero(void) {            // con ritorno, senza parametri
    int x;
    scanf("%d", &x);
    return x;
}

void stampaQuadrato(float x) {     // senza ritorno (void), con parametri
    printf("%f\n", x * x);
}

void saluto(void) {                // senza ritorno e senza parametri
    printf("Ciao!\n");
}
```

- funzioni **con valore di ritorno e con parametri**: ricevono dati e restituiscono un risultato;
- con valore di ritorno ma **senza parametri**: non ricevono input, ma calcolano e restituiscono qualcosa;
- **senza valore di ritorno** (`void`) ma con parametri: eseguono un'azione ma non restituiscono un valore;
- senza ritorno e senza parametri: azioni generali, per esempio messaggi di servizio.

## Dove stanno le funzioni in memoria
Dopo la compilazione le funzioni sono memorizzate nella **sezione codice** del programma. In C il **nome della funzione** rappresenta l'indirizzo della sua prima istruzione: è, di fatto, un puntatore al codice (un **puntatore a funzione**). Stampando gli indirizzi di `main` e di `square` con `printf("%p", …)` si vedono due indirizzi diversi nell'area codice (nell'esempio 0x0010 e 0x004B). Come nell'esempio, il nome della funzione viene passato direttamente a `%p`; in C rigoroso `%p` richiederebbe un `void *`, ma qui interessa solo l'idea che il nome indichi un indirizzo.

Il capitolo successivo approfondisce come si passano i parametri e che cosa succede ai valori.
