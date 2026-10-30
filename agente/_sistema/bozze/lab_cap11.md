# Capitolo 11: Laboratorio 4: for e while, Sommatorie e Sequenze con Terminatore
## Quando usare for e while
Il laboratorio della lezione 4 è dedicato alle **iterazioni**. Due regole di scelta:
- si usa il **`for`** quando il numero di iterazioni è **noto fin dall'inizio**; i cicli `for` hanno tipicamente una di queste forme:

```c
for (int i = 0; i < n; i++) {
    // codice che usa ma non cambia i
}

for (int i = n - 1; i >= 0; i--) {
    // codice che usa ma non cambia i
}
```

- si usa il **`while`** quando la condizione di terminazione si determina **solo durante le iterazioni** stesse, oppure quando non serve inizializzare una variabile di iterazione:

```c
bool continua = true;
while (continua) {
    // ...
    if (condizione)
        continua = false;
}

int i = 0;
// ...
while (i < n) {
    // ...
    i = i + k;
}
```

(In parole povere: se si sa in anticipo quante volte ripetere, si conta con un `for`; se si deve ripetere «finché succede qualcosa» che si scopre strada facendo, serve un `while`.)

## Come cambia la variabile di controllo
Nella dichiarazione di un `for` conta capire come varia la variabile di controllo i:
- `for (int i = 1; i <= 100; ++i)`: i va da 1 a 100 inclusi, con incrementi di 1;
- `for (int i = 100; i >= 1; --i)`: i va da 100 a 1 inclusi, con decrementi di 1 (incrementi di −1);
- `for (int i = 7; i <= 77; i += 7)`: i va da 7 a 77 inclusi, con incrementi di 7;
- `for (int i = 20; i >= 2; i -= 7)`: i parte da 20 e scende di 7 alla volta: assume i valori 20, 13 e 6 (la slide dice «da 20 a 2 inclusi», ma il 2 non viene mai raggiunto: l'ultimo valore è 6);
- `for (size_t i = 0; i < 10; ++i)`: la variabile `unsigned` i varia nell'intervallo semiaperto [0, 10);
- `for (ptrdiff_t i = 100; i >= 0; --i)`: i varia nell'intervallo chiuso [100, 0] in ordine inverso; il tipo `ptrdiff_t` è compatibile con `size_t` ma **ha il segno**, ed è quindi necessario, con la condizione `i >= 0`, per scendere fino a 0 incluso (cap. 24; il tipo è definito in `<stddef.h>`).

## Esempio: la somma dei numeri pari da 2 a 100
Primo modo: si scorre tutta la sequenza da 0 a 100 e si accumulano solo i valori pari:

```c
// inizializza accumulatore della somma
int sum = 0;
// scorre tutti i numeri da 0 a 100
for (int number = 0; number <= 100; ++number) {
    // accumula in sum i valori pari
    if (number % 2 == 0)
        sum += number;
}
printf("La somma è %d\n", sum);
```

Secondo modo: si scorrono direttamente solo i numeri pari, con passo 2 (considerazione nostra: così le iterazioni sono 50 invece di 101):

```c
int sum = 0;
// scorre tutti i numeri pari da 2 a 100
for (int number = 2; number <= 100; number += 2) {
    sum += number;
}
printf("La somma è %d\n", sum);
```

La variabile `sum` è un **accumulatore** (cap. 20): parte da 0 e a ogni iterazione si somma il nuovo valore.

## Esercizi iterativi per iniziare
Si chiede un programma `iterazioni_n.c` con tre punti: (1) dato un intero positivo n letto con `scanf`, stampare tutti gli interi da 0 a n e poi da n a 0 (la domanda posta è quale ciclo sia più appropriato; considerazione nostra: un `for`, perché il numero di iterazioni è noto); (2) stampare tutti gli interi dispari da 0 a n; (3) stampare il **fattoriale** di n, cioè 1 · 2 · … · (n − 1) · n.

## Sequenze terminate da un valore speciale
Si supponga di leggere con `scanf` una sequenza di numeri per sommarli tutti, **finché non si legge lo 0**, che funge da terminatore della sequenza. Non si sa quanti numeri si leggeranno: si usa il ciclo `while`.

Prima versione, con una variabile sentinella (cap. 22):

```c
int sum = 0;
bool continua = true;
while (continua) {
    int number;
    // legge il prossimo numero della sequenza
    scanf("%d", &number);
    if (number == 0)
        continua = false;   // sequenza terminata
    else
        sum += number;
}
printf("La somma è %d\n", sum);
```

Seconda versione, più compatta, che usa il valore restituito da `scanf`:

```c
int sum = 0;
int number;
while (1 == scanf("%d", &number) && number != 0) {
    sum += number;
}
printf("La somma è %d\n", sum);
```

`scanf` legge i valori indicati dagli specificatori di conversione della stringa di formato e **restituisce il numero di variabili ricevute lette con successo**. Con la stringa `"%d"` restituisce 1 se e solo se ha letto un intero; in ogni altro caso (non è un numero, l'input è finito, …) non restituisce 1. Nel ciclo si usa inoltre la valutazione **cortocircuitata** (~lazy~) dell'`&&` (cap. 18): se `scanf` non ha letto nulla, la seconda condizione non viene nemmeno valutata.

(In parole povere: «cortocircuitata» vuol dire che il C si ferma appena il risultato è deciso, senza guardare il resto della condizione.)

(In parole povere: `1 == scanf("%d", &number)` vuol dire «ho davvero letto un numero?»; il ciclo prosegue finché la risposta è sì e il numero non è lo 0 che chiude la sequenza.)

## La media di una sequenza
Si chiede un programma `media_seq.c` che legga dall'input una sequenza di interi terminata dallo 0 (che si assume non appartenga alla sequenza) e, quando l'utente inserisce 0, stampi la **media** (come numero in virgola) di tutti i numeri letti. Per esempio, con l'input `4 8 10 2 0` l'output è 6. Servono due variabili di supporto: un **accumulatore** che somma i numeri letti e un **contatore** di quanti numeri sono stati letti (in parole povere: l'accumulatore è il «totale parziale» e il contatore è il «conto dei numeri»); alla fine del ciclo

media = accumulatore_somma / contatore.

Come aggiunta nostra: attenzione alla divisione fra interi (cap. 16): per ottenere una media in virgola mobile bisogna convertire uno dei due operandi.

Nel codice iniziale del laboratorio c'è una cartella `input_media_seq` con diverse sequenze di numeri, una per file. Il programma si può eseguire in due modi: **interattivo**, lanciando `media_seq` e digitando l'input a mano; oppure **non interattivo**, usando il contenuto di un file come input. Detto `input01.txt` il file con la sequenza, su Unix si scrive `./media_seq < input01.txt`, su Windows `media_seq.exe < input01.txt`.

Il capitolo successivo prosegue con i divisori, il triangolo di Floyd, i pattern, i quantificatori sulle sequenze, Fibonacci e il gioco dell'indovina il numero.
