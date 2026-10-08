# 02C_referenziamento_scanf_puntatori

<!-- pagina 1 -->
Programmazione I
Teoria
Elvio Amparore
A.A. 2026/27
Canale B
DIPARTIMENTO DI 
INFORMATICA
 
CORSO DI LAUREA 
TRIENNALE
Referenziamento, Input 
e Puntatori in C
Dall’indirizzo di memoria ai puntatori

<!-- pagina 2 -->
Il referenziamento
Ottenere l’indirizzo di memoria delle 
variabili
2

<!-- pagina 3 -->
Indirizzo di una variabile
• Abbiamo detto che nel modello di Von Neumann ogni 
variabile è memorizzata in memoria centrale, ed occupa 
una certa quantità di byte.
• Per identiﬁcarla, la CPU usa un indirizzo di memoria, un 
numero senza segno univoco analogo al numero civico di 
una casa.
– Solitamente un indirizzo di memoria viene visualizzato in 
formato esadecimale (es: 0x7fffd0624e0c) per compattezza.
• Il linguaggio C permette di ottenere questo indirizzo 
tramite l’operatore di referenziamento & (ampersand)
– Esempio: &x → “l’indirizzo della variabile x”.
3

<!-- pagina 4 -->
Indirizzo di una variabile
Area codice
5
x
int main(void) {
    int x = 5;
}
Ogni variabile ha valore e indirizzo:
• x è il valore, il contenuto della cella
• &x è l’indirizzo della variabile. la 
posizione in memoria della cella.
x e &x sono informazioni diverse.
0x03FC
valore: 5
indirizzo: 0x03FC
La variabile x ha:
4

<!-- pagina 5 -->
Perché è utile conoscere gli indirizzi?
• Permette di scrivere codice del tipo:
– “moltiplica due numeri e memorizza il risultato in questa cella di memoria”
– “leggi da tastiera un numero, e memorizzalo nello spazio di memoria di una 
certa variabile”
• È indispensabile per lavorare con i puntatori, cioè variabili il cui 
valore è un indirizzo di memoria.
• Rende possibile gestire memoria dinamica, strutture dati 
complesse e comunicazione efﬁciente tra funzioni.
• Partiamo con un uso semplice: possiamo stampare a video gli 
indirizzi di memoria usando printf con lo speciﬁcatore di 
conversione %p
5

<!-- pagina 6 -->
Indirizzo di una variabile
●printf usa lo speciﬁcatore di conversione %p per mostrare un indirizzo.
●L'indirizzo viene normalmente visualizzato in forma esadecimale.
●Il valore concreto dipende dall'esecuzione: non deve mai essere incorporato 
nella logica del programma.
int main(void) {
    int x = 5;
    int y = 2;
    int z = x + y;
  
    printf("La var x all'indirizzo %p vale %d \n",  &x,  x);
    printf("La var y all'indirizzo %p vale %d \n",  &y,  y);
    printf("La var z all'indirizzo %p vale %d \n",  &z,  z);
}
$ ./address 
La var x all'indirizzo 0x7fffd0624e0c vale 5 
La var y all'indirizzo 0x7fffd0624e08 vale 2 
La var z all'indirizzo 0x7fffd0624e04 vale 7
6
5
x @ 0x7fffd0624e0c
2
7
Indirizzi di memoria crescenti
y @ 0x7fffd0624e08
z @ 0x7fffd0624e04
Area codice

<!-- pagina 7 -->
Formato degli indirizzi
• Il valore concreto di un indirizzo dipende dalla piattaforma e 
dalla singola esecuzione del programma.
– Il valore concreto è tipicamente molto grande: vedrete i dettagli in 
Sistemi Operativi.
• Nei nostri esempi useremo indirizzi simbolici più corti, come 
0x03FC, per rendere leggibili le rappresentazioni della 
memoria.
• Non ci interessa tanto il valore numerico dell'indirizzo, ma il 
fatto che identiﬁchi una posizione in memoria.
7

<!-- pagina 8 -->
Input da tastiera
Interagire con l’utente, un primo 
utilizzo degli indirizzi
8

<!-- pagina 9 -->
Input da tastiera
• Spesso un programma non deve solo mostrare risultati, ma anche 
ricevere dati dall’utente.
• In linguaggio C questa operazione si effettua con la funzione scanf(), 
che permette di leggere valori digitati da tastiera e memorizzarli 
direttamente in variabili.
• Esempio: per leggere un numero intero in una variabile x già 
dichiarata:
scanf("%d", &x);
• Passando l’indirizzo &x di x consiente a scanf() di conoscere 
l’indirizzo di memoria in cui scrivere il dato letto in input
• La funzione scanf completa quando l’utente inserisce l’input e 
preme ENTER
9

<!-- pagina 10 -->
Input da tastiera
int main(void) {
    int x, y, z;
▶   printf("Inserisci x: ");
    scanf("%d", &x);
    printf("Inserisci y: ");
    scanf("%d", &y);
    z = x + y;
    printf("%d + %d = %d\n", x, y, z);
}
$ ./scanf_ex1 
Inserisci x: 
Area codice
?
?
?
Indirizzi di memoria crescenti
int x @0x03FC
int y @0x03F8
int z @0x03F4
10

<!-- pagina 11 -->
int main(void) {
    int x, y, z;
    printf("Inserisci x: ");
▶   scanf("%d", &x);
    printf("Inserisci y: ");
    scanf("%d", &y);
    z = x + y;
    printf("%d + %d = %d\n", x, y, z);
}
Input da tastiera
$ ./scanf_ex1 
Inserisci x: 5
Area codice
5
?
?
Indirizzi di memoria crescenti
int x @0x03FC
int y @0x03F8
int z @0x03F4
11

<!-- pagina 12 -->
int main(void) {
    int x, y, z;
    printf("Inserisci x: ");
    scanf("%d", &x);
    printf("Inserisci y: ");
▶   scanf("%d", &y);
    z = x + y;
    printf("%d + %d = %d\n", x, y, z);
}
Input da tastiera
$ ./scanf_ex1 
Inserisci x: 5
Inserisci y:
Area codice
5
2
?
Indirizzi di memoria crescenti
int x @0x03FC
int y @0x03F8
int z @0x03F4
12

<!-- pagina 13 -->
int main(void) {
    int x, y, z;
    printf("Inserisci x: ");
    scanf("%d", &x);
    printf("Inserisci y: ");
    scanf("%d", &y);
    z = x + y;
▶   printf("%d + %d = %d\n", x, y, z);
}
Input da tastiera
$ ./scanf_ex1 
Inserisci x: 5
Inserisci y: 2
5 + 2 = 7
Area codice
5
2
7
Indirizzi di memoria crescenti
int x @0x03FC
int y @0x03F8
int z @0x03F4
13

<!-- pagina 14 -->
Input da tastiera
int main(void) {
    int x, y, z;
    printf("Inserisci due interi : ");
▶   scanf("%d%d", &x, &y);
    z = x + y;
    printf("%d + %d = %d\n", x, y, z);
}
$ ./scanf_ex2
Inserisci due interi:
Area codice
?
?
Indirizzi di memoria crescenti
int x @0x03FC
int y @0x03F8
int z @0x03F4
?
14

<!-- pagina 15 -->
Input da tastiera
int main(void) {
    int x, y, z;
    printf("Inserisci due interi : ");
▶   scanf("%d%d", &x, &y);
    z = x + y;
    printf("%d + %d = %d\n", x, y, z);
}
$ ./scanf_ex2
Inserisci due interi: 5 2
Area codice
?
?
Indirizzi di memoria crescenti
I due numeri possono essere separati da uno 
o più caratteri di spaziatura.
int x @0x03FC
int y @0x03F8
int z @0x03F4
?
15

<!-- pagina 16 -->
Input da tastiera
int main(void) {
    int x, y, z;
    printf("Inserisci due interi : ");
▶   scanf("%d%d", &x, &y);
    z = x + y;
    printf("%d + %d = %d\n", x, y, z);
}
$ ./scanf_ex2
Inserisci due interi: 5 2
Area codice
5
2
Indirizzi di memoria crescenti
int x @0x03FC
int y @0x03F8
int z @0x03F4
?
16

<!-- pagina 17 -->
Input da tastiera
int main(void) {
    int x, y, z;
    printf("Inserisci due interi : ");
    scanf("%d%d", &x, &y);
    z = x + y;
▶   printf("%d + %d = %d\n", x, y, z);
}
$ ./scanf_ex2
Inserisci due interi: 5 2
5 + 2 = 7
Area codice
5
2
Indirizzi di memoria crescenti
int x @0x03FC
int y @0x03F8
int z @0x03F4
?
17

<!-- pagina 18 -->
Limiti e comportamento di scanf
• La gestione dell’input è un punto critico: l’utente può sempre inserire valori 
sbagliati o incompleti.
• La funzione scanf() prova a interpretare l’input in base al formato speciﬁcato 
(es. "%d%d" per due interi).
• Se l’utente sbaglia (per esempio inserendo un carattere invece di un 
numero), scanf() smette di leggere (cioè si ferma non appena incontra un 
dato incompatibile) e restituisce il numero di valori letti con successo, che 
può essere minore di quelli attesi.
Esempio:
int x, y;
int n = scanf("%d%d", &x, &y);
• se n vale 2 → entrambi i valori letti correttamente
• se n vale 1 → solo il primo valore valido
• se n vale 0 → nessun valore letto, variabili non aggiornate
18

<!-- pagina 19 -->
Input da tastiera
19
int main(void) {
 int x;
 printf("Inserisci un intero: ");
 int n = scanf("%d", &x);
 printf("Valori letti correttamente: %d\n", n);
 printf("x vale %d \n", x);
}
$ ./scanf_ex3 
Inserisci un intero: 1234
Valori letti correttamente: 1
x vale 1234
Numero
intero

<!-- pagina 20 -->
Input da tastiera
20
$ ./scanf_ex3 
Inserisci un intero: 1234.56
Valori letti correttamente: 1
x vale 1234
Atteso numero intero (%d): l’input viene letto fino a “1234”, 
mentre “.56” rimane non consumato nell’input
viene stampato il 
valore intero letto
int main(void) {
 int x;
 printf("Inserisci un intero: ");
 int n = scanf("%d", &x);
 printf("Valori letti correttamente: %d\n", n);
 printf("x vale %d \n", x);
}

<!-- pagina 21 -->
int main(void) {
 int x;
 printf("Inserisci un intero: ");
 int n = scanf("%d", &x);
 printf("Valori letti correttamente: %d\n", n);
 printf("x vale %d \n", x);
}
Input da tastiera
21
$ ./scanf_ex3 
Inserisci un intero: A
Valori letti correttamente: 0
x vale ?????
Input non conforme: la lettera “A” non può essere 
interpretata come numero decimale
Variabile x
non aggiornata
Il programma tenta di leggere il valore non 
inizializzato di x per passarlo a printf: il 
comportamento è indefinito.

<!-- pagina 22 -->
int main(void) {
 int x;
 printf("Inserisci un intero: ");
 int n = scanf("%d", &x);
 printf("Letti con successo %d interi\n", n);
 printf("x vale %d \n", x);
}
Input da tastiera
22
●NOTA: è lecito ottenere &x anche se x non è ancora inizializzata: stiamo 
usando l'indirizzo di x, non leggendo il suo valore.
●Se però x non viene inizializzata (in questo caso da scanf) allora non 
possiamo assumere nulla sul valore di x.
dichiarazione 
variabile
valore 
variabile
indirizzo 
variabile
valore inizializzato 
variabile
≠
≠
≠

<!-- pagina 23 -->
int main(void) {
 int x = -1;
 printf("Inserisci un intero: ");
 int n = scanf("%d", &x);
 printf("Letti con successo %d interi\n", n);
 printf("x vale %d \n", x);
}
Input da tastiera
23
$ ./scanf_ex3 
Inserisci un intero: A
Letti con successo 0 interi
x vale -1
Variabile x
non aggiornata
Se l’input non può essere interpretato secondo 
la speciﬁca di conversione, la variabile 
corrispondente non viene modiﬁcata.
NOTA: Se scanf non aggiorna una variabile 
non inizializzata, il suo valore resta 
indeterminato

<!-- pagina 24 -->
I puntatori
Variabili che memorizzano indirizzi di 
memoria
24

<!-- pagina 25 -->
I puntatori come tipo di dati
• Un puntatore è una variabile che 
memorizza l’indirizzo di memoria di 
un’altra variabile (detta variabile 
puntata).
• Il valore memorizzato in una variabile 
puntatore è un indirizzo di memoria, 
anziché direttamente il dato puntato.
25
Area codice
5
x
0x03FC
La variabile int x = 5 ha 
indirizzo &x pari a 
0x03FC
Dove possiamo 
memorizzare 0x03FC ?

<!-- pagina 26 -->
I puntatori come tipo di dati
• In C, per ciascun tipo di dati T, esiste il corrispondente tipo 
puntatore T* (“T star”)
– Variabili di tipo T* servono a memorizzare gli indirizzi di 
memoria delle variabili di tipo T
• Esempio:
– int: tipo delle variabili intere
– int*: tipo delle variabili puntatore che possono contenere indirizzi di 
variabili di tipo int
– ﬂoat*: puntatore a ﬂoat
26
int x = 5;
int* pX;
●
x e una variabile di tipo int.
●
pX e una variabile “puntatore agli interi”, quindi di tipo int*.
●
Per convenzione useremo spesso il preﬁsso p nei nomi dei puntatori.
●
Dopo la sola dichiarazione, pX non contiene ancora un indirizzo valido 
da usare.

<!-- pagina 27 -->
Operatore di referenziamento
• L’operatore &, detto operatore di referenziamento (address-of operator), 
applicato a una variabile ne restituisce l’indirizzo di memoria, con tipo 
puntatore al tipo della variabile stessa.
int x = 5;
int* pX = &x;   // pX riceve l’indirizzo di x
che interpretiamo come
– x 
variabile intera, valore = 5
– &x
espressione che vale l’indirizzo di x, tipo = int*
– pX 
puntatore a intero, che memorizza l’indirizzo di x
Se x è int, allora &x è int*
• L'operatore & deve essere applicato a qualcosa che identiﬁca una posizione 
di memoria; non può essere applicato a un semplice valore o al risultato 
temporaneo di un calcolo.
&5        // ERRORE
&(x + 1)  // ERRORE
27

<!-- pagina 28 -->
I puntatori come tipo di dati
• La variabile x contiene il valore 5.
• La variabile pX contiene 0x03FC, cioè 
l'indirizzo di x.
28
Area codice
5
x
0x03FC
0x03FC
pX
0x03F8
int x = 5;
int* pX = &x;
• pX e una variabile a tutti gli effetti: anch'essa occupa memoria e 
possiede un proprio indirizzo.
• Se &x ha tipo int*, e anche pX ha tipo int*,  allora 
l'assegnamento è compatibile: pX riceve l'indirizzo di x.
NOTA: un puntatore contiene un indirizzo, ma essendo esso stesso 
una variabile ha a sua volta anche un proprio indirizzo.

<!-- pagina 29 -->
I puntatori
29
$ ./address 
l'ind 0xbd6ac520 vale 0xbd6ac52c 
Area codice
5
Indirizzi di memoria crescenti
int x @ 0x03FC
int main(void) {
▶   int x = 5;
    int* pX;
    pX = &x;
    printf("Il ptr pX all'ind %p vale %p \n",
           &pX, pX);
}

<!-- pagina 30 -->
I puntatori
30
int main(void) {
    int x = 5;
▶   int* pX;
    pX = &x;
    printf("Il ptr pX all'ind %p vale %p \n",
           &pX, pX);
}
$ ./address 
l'ind 0xbd6ac520 vale 0xbd6ac52c 
Area codice
5
Indirizzi di memoria crescenti
?
int* pX @ 0x03F8
int x @ 0x03FC

<!-- pagina 31 -->
I puntatori
31
$ ./address 
 tr pX all'ind 0xbd6ac520 vale 0xbd6ac52c 
Area codice
5
Indirizzi di memoria crescenti
0x03FC
Ora pX contiene
l’indirizzo di x
int main(void) {
    int x = 5;
    int* pX;
▶   pX = &x;
    printf("Il ptr pX all'ind %p vale %p \n",
           &pX, pX);
}
int* pX @ 0x03F8
int x @ 0x03FC

<!-- pagina 32 -->
int main(void) {
    int x = 5;
    int* pX;
    pX = &x;
▶   printf("Il ptr pX all'ind %p vale %p \n",
           &pX, pX);
}
I puntatori
32
$ ./address 
Il ptr pX all'ind 0x03F8 vale 0x03FC 
Area codice
5
Indirizzi di memoria crescenti
0x03FC
int* pX @ 0x03F8
int x @ 0x03FC

<!-- pagina 33 -->
I puntatori
33
int main(void) {
    int x;
▶   int* pX = &x;
    printf("Inserisci un intero: ");
    scanf("%d", pX);
    printf("La var x all'ind %p vale %d \n",
           pX, x);
}
$ ./ptr_scanf
 
Area codice
?
Indirizzi di memoria crescenti
0x03FC
Assegnamento pX =&x
prima di aver inizializzato x
int* pX @ 0x03F8
int x @ 0x03FC

<!-- pagina 34 -->
int main(void) {
    int x;
    int* pX = &x;
    printf("Inserisci un intero: ");
▶   scanf("%d", pX);
    printf("La var x all'ind %p vale %d \n",
           pX, x);
}
I puntatori
34
$ ./ptr_scanf
Inserisci un intero:  5
Area codice
? 5
Indirizzi di memoria crescenti
0x03FC
int* pX @ 0x03F8
int x @ 0x03FC

<!-- pagina 35 -->
I puntatori
35
$ ./ptr_scanf
Inserisci un intero:  5
La var x all'ind 0x03FC vale 5
Area codice
5
Indirizzi di memoria crescenti
0x03FC
int main(void) {
    int x;
    int* pX = &x;
    printf("Inserisci un intero: ");
    scanf("%d", pX);
▶   printf("La var x all'ind %p vale %d \n",
           pX, x);
}
int* pX @ 0x03F8
int x @ 0x03FC

<!-- pagina 36 -->
I puntatori
36
int main(void) {
    int* pX = &x;
    int x;
    x = 5;
    printf("Il ptr pX all'ind %p vale %p \n",
           &pX, pX);
}
$ gcc -o pointer_ex1 pointer_ex1.c 
pointer_ex1.c: In function ‘main’:
pointer_ex1.c: error: ‘x’ undeclared (first use in this function)
   int* pX = &x;
              ^
Area codice
Indirizzi di memoria crescenti
???
Assegnamento pX =&x
prima di aver dichiarato x
int x @ 0x03FC

<!-- pagina 37 -->
I puntatori
37
int main(void) {
    float x = 5.0;
    int* pX = &x;
}
$ gcc pointer_ex2 -o pointer_ex2
pointer_ex2.c: In function ‘main’:
pointer_ex2.c:5:12: warning: initialization of ‘int *’ from incompatible pointer type ‘float *’
   int* pX = &x;
            ^
Area codice
Indirizzi di memoria crescenti
5.000000
Incompatibilità fra tipo 
variabile puntata x e 
puntatore pX
?
int* pX @ 0x03F8
int x @ 0x03FC
●&x ha tipo ﬂoat*; non è compatibile con una variabile int*.

<!-- pagina 38 -->
Dichiarazione delle variabili puntatore
• Abbiamo dichiarato i puntatori come
int* pX
ma un’altra convenzione in uso frequente è la seguente
int *pX
• Il simbolo * è utilizzato anche per un’altra operazione sui 
puntatori, il dereferenziamento.
38

<!-- pagina 39 -->
L’operatore di dereferenziamento *
• L’operatore unario di dereferenziamento * (dereference oppure 
indirect access) permette di accedere alla variabile puntata 
attraverso l'indirizzo memorizzato nel puntatore.
• Esempio: 
int y = 5;
int* pY = &y;
printf("%d", *pY);
In questo esempio, *pY accede alla stessa cella di memoria 
della variabile y, avendone memorizzato l’indirizzo.
• Dereferenziare un puntatore signiﬁca usare l’indirizzo che 
contiene per accedere indirettamente alla variabile puntata.
39

<!-- pagina 40 -->
Tipo e uso del dereferenziamento
• Se un puntatore p ha tipo T*, allora l’espressione *p ha tipo T
p ha tipo T*
⇒
*p ha tipo T
• *p permette quindi di accedere alla variabile che si trova 
all’indirizzo memorizzato in p.
int x = 5;
int* pX = &x;
40
Accesso in lettura
printf("%d\n", *pX);
●*pX legge il valore della variabile 
puntata. 
●*pX ha quindi valore 5, come x.
Accesso in modiﬁca
*pX = 10;
●L’assegnamento modiﬁca il valore 
della variabile puntata.
●Dopo l’istruzione, x vale 10.

<!-- pagina 41 -->
Dereferenziamento
• x e *pX accedono alla stessa cella, quindi leggono lo stesso 
valore.
41
Area codice
5
x
0x03FC
0x03FC
pX
0x03F8
x = 5
*pX = 5
1.
  int x = 5;
2.
  int *pX = &x;
3.
4.
  printf("x =%d\n", x);      // stampa 5
5.
▶ printf("*pX = %d\n", *pX); // stampa ancora 5
6.
  *pX = 10;                  // modifica x tramite pX
7.
  printf("x = %d\n", x);     // stampa 10 (x vale 10)

<!-- pagina 42 -->
Dereferenziamento
• Scrivere in *pX modiﬁca x, perché è la stessa cella di memoria.
42
Area codice
5 10
x
0x03FC
0x03FC
pX
0x03F8
x = 5
*pX = 5
x  =10
1.
  int x = 5;
2.
  int *pX = &x;
3.
4.
  printf("x =%d\n", x);      // stampa 5
5.
  printf("*pX = %d\n", *pX); // stampa ancora 5
6.
  *pX = 10;                  // modifica x tramite pX
7.
▶ printf("x = %d\n", x);     // stampa 10 (x vale 10)

<!-- pagina 43 -->
Rileggiamo scanf
• La documentazione di scanf richiede che ogni 
conversione riceva un puntatore al tipo appropriato.
• Per %d serve un int*
int x;
scanf("%d", &x);   // &x ha tipo int*
• &x, con x di tipo int, produce proprio un valore di tipo int* 
nel quale scanf può scrivere il valore che legge da input.
43

<!-- pagina 44 -->
Scanf usando i puntatori
44
int main(void) {
    int x = 5;
▶   int* pX = &x;
    printf("Inserisci nuovo valore di x: ");
    scanf("%d", pX);
    printf("La var x vale %d \n", x);
}
Area codice
Indirizzi di memoria crescenti
$./pointer_ex5
?
0x03FC
int* pX @ 0x03F8
int x @ 0x03FC

<!-- pagina 45 -->
int main(void) {
    int x = 5;
    int* pX = &x;
    printf("Inserisci nuovo valore di x: ");
▶   scanf("%d", pX);
    printf("La var x vale %d \n", x);
}
Scanf usando i puntatori
45
Area codice
Indirizzi di memoria crescenti
$./pointer_ex5
Inserisci nuovo valore di x: 1234
? 1234
0x03FC
int* pX @ 0x03F8
int x @ 0x03FC

<!-- pagina 46 -->
Scanf usando i puntatori
46
Area codice
Indirizzi di memoria crescenti
$./pointer_ex5
Inserisci nuovo valore di x: 1234
La var x vale 1234
? 1234
0x03FC
int main(void) {
    int x = 5;
    int* pX = &x;
    printf("Inserisci nuovo valore di x: ");
    scanf("%d", pX);
▶   printf("La var x vale %d \n", x);
}
int* pX @ 0x03F8
int x @ 0x03FC

<!-- pagina 47 -->
Considerazioni sui puntatori
Aliasing, riferimenti multipli, 
dimensioni, NULL
47

<!-- pagina 48 -->
Riferimenti multipli
48
  int x = 5;
  int* pX = &x;
  int* pXbis = pX;
▶ *pXbis = 1234;
  printf("x = %d\n", x);
  printf("*pX = %d\n", *pX);
  printf("*pXbis = %d\n", *pXbis);
    
La scrittura su *pXbis avviene nella cella di x
Area codice
5 1234
x
0x03FC
0x03FC
pX
0x03F8
0x03FC
pXbis
0x03F0

<!-- pagina 49 -->
Riferimenti multipli
49
  int x = 5;
  int* pX = &x;
  int* pXbis = pX;
  *pXbis = 1234;
  printf("x = %d\n", x);
  printf("*pX = %d\n", *pX);
▶ printf("*pXbis = %d\n", *pXbis);
    
x, *pX e *pXbis indicano la stessa variabile (sono alias).
IMPORTANTE: possiamo dereferenziare un puntatore solo se 
contiene un indirizzo valido.
Area codice
5 1234
x
0x03FC
0x03FC
pX
0x03F8
0x03FC
pXbis
0x03F0
x = 1234
*pX = 1234
*pXbis = 1234

<!-- pagina 50 -->
Alias della stessa variabile
50
In questo codice:
    int x = 5;
    int* pX = &x;
    int* pXbis = pX;
    ...
queste tre istruzioni:
    scanf("%d", &x);
    scanf("%d", pX);
    scanf("%d", pXbis);
sono equivalenti: indicano sempre la stessa cella.
Abbiamo quindi diversi modi di accedere ad una variabile: questi 
modi diversi si dicono alias. *pX e *pXbis sono alias di x.
Area codice
5
x
0x03FC
0x03FC
pX
0x03F8
0x03FC
pXbis
0x03F0
pX e pXbis sono due variabili puntatore 
diverse, ma contengono lo stesso indirizzo.

<!-- pagina 51 -->
Aliasing delle variabili
• Quando dichiariamo una variabile in C, essa è accessibile tramite un solo 
nome simbolico (ad esempio x).
• Utilizzando i puntatori, è possibile che più variabili puntatore facciano 
riferimento allo stesso indirizzo di memoria, cioè alla stessa variabile
• In questo caso, esistono più modi diversi per accedere e modiﬁcare la 
stessa cella di memoria:
– sia tramite il nome diretto della variabile (x)
– sia tramite uno o più puntatori che ne contengono l’indirizzo (pX, 
pXbis, …)
• Questo fenomeno prende il nome di aliasing:
– più “etichette” (alias) fanno riferimento allo stesso dato in memoria
– modiﬁcando la variabile attraverso uno degli alias, anche gli altri 
“vedranno” il nuovo valore, perché accedono allo stesso indirizzo
51

<!-- pagina 52 -->
int* pX;   // non inizializzato
  
  *pX = 10;  // ERRORE
    
• Dopo la dichiarazione, pX contiene un valore indeterminato, 
come ogni variabile automatica non inizializzata.
• Nel caso di un puntatore, quel valore non può essere usato 
come indirizzo da dereferenziare.
• Una variabile puntatore può contenere un valore che non 
rappresenta un indirizzo valido, cioè utilizzabile. 
IMPORTANTE: possiamo dereferenziare un puntatore solo se 
contiene un indirizzo valido.
Puntatori non inizializzati
52

<!-- pagina 53 -->
Il puntatore nullo
• NULL è un valore di puntatore che indica esplicitamente che quel 
puntatore non fa riferimento ad alcuna variabile.
• È usato come valore di inizializzazione o come valore sentinella per 
indicare che un puntatore non sta puntando a nulla.
int main(void) {
    int *p = NULL; // inizializzazione sicura
    *p = 10; // ERRORE: p non contiene un indirizzo di memoria 
             //         a cui si può accedere per indirezione
}
• Consente di inizializzare esplicitamente un puntatore, evitando che abbia 
un valore indeterminato.
• Permette di rappresentare e riconoscere esplicitamente il caso “non punta 
ad alcuna variabile”.
• Il dereferenziamento di un puntatore NULL produce un comportamento 
indeﬁnito (in genere un errore che termina il programma)
53

<!-- pagina 54 -->
Dimensione dei puntatori
54
int main(void) {
  int x;
  int* pX;
  printf("sizeof(x) %zu B\n", sizeof(x));
  printf("sizeof(pX) %zu B\n", sizeof(pX));
}
Esempio di output su piattaforma a 64-bit:
sizeof(x) 4 B
sizeof(pX) 8 B
• La dimensione di T* dipende dalla piattaforma, non dalla 
dimensione di T.
– Su una tipica CPU a 64 bit, un puntatore occupa 8 byte.
– Su una tipica CPU a 32 bit, un puntatore occupa 4 byte.

<!-- pagina 55 -->
Complementarietà di & e *
#include <stdio.h>
int main(void) {
    int a = 7;
    int* pA = &a;    // pA contiene l’indirizzo di a
    printf("Indirizzo di a: %p\nValore di pA: %p\n\n", &a, pA);
    printf("Valore di a: %d\nValore di *pA: %d\n\n", a, *pA);
    printf("Dimostrazione: * e & sono operazioni complementari\n");
    printf("&*pA = %p\n*&pA = %p\n", &*pA, *&pA);
}
55
Indirizzo di a: 0x16dc6b05c
Valore di pA: 0x16dc6b05c
Valore di a: 7
Valore di *pA: 7
Dimostrazione: * e & sono operazioni complementari
&*pA = 0x16dc6b05c
*&pA = 0x16dc6b05c

<!-- pagina 56 -->
Operatore *
Il simbolo «*» (star) viene utilizzato in C per diversi scopi
1. Indicare l’operatore di moltiplicazione
int x = a * b;
2. Dichiarare una variabile di tipo puntatore
int* pX = &x;
3. Dereferenziare un puntatore
int x = *pX;
4. Puntatore a puntatore (non vediamo)
int** ppX = &pX;   pX = *ppX;   **ppX = 10;
56
