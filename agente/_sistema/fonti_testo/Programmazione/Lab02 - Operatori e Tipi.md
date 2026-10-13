# Lab02 - Operatori e Tipi

<!-- pagina 1 -->
A.A. 2026/27
Canale B
Programmazione I
Laboratorio
DIPARTIMENTO DI 
INFORMATICA
CORSO DI LAUREA 
TRIENNALE
Operatori e Tipi
Lezione nº 2

<!-- pagina 2 -->
Aritmetica
Provare il programma aritmetica.c leggendo 
attentamente il codice prima di eseguirlo.
2
NOTA: per compilare usiamo il comando gcc:
●Unix:  
gcc -Wall aritmetica.c -o aritmetica
●Windows:  gcc -Wall aritmetica.c -o aritmetica.exe

<!-- pagina 3 -->
Operazioni su interi
Scrivere un semplice programma operazioni_su_interi.c che:
1. chieda all’utente di inserire due numeri interi, che 
chiamiamo n1 ed n2;
2. calcoli la somma di n1 ed n2
3. stampi a video il valore della variabile somma
4. stampi a video:
a. il prodotto di n1 con n2
b. la divisione intera di n1 / n2
c. la divisione reale di n1 / n2
d. il resto della divisione intera tra n1 ed n2
NOTA: Per chiedere all'utente i due interi n1 ed n2, usare la 
funzione scanf, come visto a lezione.
3

<!-- pagina 4 -->
Ordine di valutazione
Quali risultati otteniamo in C da queste espressioni:
1.int x = 7 + 3 * 6 / 2 - 1;
2.int x = 2 % 2 + 2 * 2 - 2 / 2;
3.int x = (3 * 9 * (3 + (9 * 3 / (3))));
4

<!-- pagina 5 -->
Ordine di valutazione
Quali risultati otteniamo in C da queste espressioni:
1.int x = 7 + 3 * 6 / 2 - 1;
2.int x = 2 % 2 + 2 * 2 - 2 / 2;
3.int x = (3 * 9 * (3 + (9 * 3 / (3))));
5
15
3
324

<!-- pagina 6 -->
Ordine di valutazione
Quali di queste espressioni corrisponde ad: y = ax3 + 7 ?
1.int y = a * x * x * x + 7;
2.int y = a * x * x * (x + 7); 
3.int y = (a * x) * x * (x + 7); 
4.int y = (a * x) * x * x + 7; 
5.int y = a * (x * x * x) + 7;
6.int y = a * x * (x * x + 7);
6

<!-- pagina 7 -->
Ordine di valutazione
Quali di queste espressioni corrisponde ad: y = ax3 + 7 ?
1.int y = a * x * x * x + 7;
2.int y = a * x * x * (x + 7); 
3.int y = (a * x) * x * (x + 7); 
4.int y = (a * x) * x * x + 7; 
5.int y = a * (x * x * x) + 7;
6.int y = a * x * (x * x + 7);
7

<!-- pagina 8 -->
Circonferenza
Aprire il programma circonferenza.c e completare la parte 
per calcolare la circonferenza. 
Si ricorda che:
• la circonferenza di un cerchio di raggio r è pari a 2πr
• l’area di un cerchio di raggio r è pari a πr2
8
NOTA: Su Linux potrebbe essere necessario compilare 
come
●gcc -Wall circonferenza.c -o circonferenza -lm
dove -lm indica di aggiungere le funzioni matematiche 
dell’header math.h

<!-- pagina 9 -->
Errori in C
Quali errori vedete in questo codice?
#include <stdio.h>
int main() {
int x, y;
printf("Inserisci due interi: ");
scanf("%d %d", &x, y)
z = x + y;
printf("La somma %d + %d vale ", x, y);
printf("%d\n", &z);
}
9

<!-- pagina 10 -->
Errori in C
Quali errori vedete in questo codice?
#include <stdio.h>
int main() {
int x, y;
printf("Inserisci due interi: ");
scanf("%d %d", &x, y)
z = x + y;
printf("La somma %d + %d vale ", x, y);
printf("%d\n", &z);
}
10

<!-- pagina 11 -->
Errori in C
11
Leggere il codice errori.c e (senza compilare) individuare quali errori 
sono presenti.  Riuscite a trovarli tutti e 8?

<!-- pagina 12 -->
Media di tre numeri
Leggere il codice del file media.c, e sperimentare input 
differenti seguendo gli esercizi proposti.
Rispondere alle domande indicate nei commenti del codice.
12

<!-- pagina 13 -->
Tabella dei tipi e specificatori di conversione
13
Tipo
Uso
CPU 32 bit
CPU 64 bit
specificatori 
di 
conversione
Dimensione
[Byte / bit]
Intervallo
Dimensione
[Byte / bit]
Intervallo
char
ASCII
1 / 8
-128, 127
1 / 8
-128, 127
%c
short
short int
numeri 
interi
2 / 16
-215, +215-1
2 / 16
-215, +215-1
%hd
int
signed int
4 / 32
-231, +231-1
4 / 32
-231, +231-1
%d
long
long int
4 / 32
8 / 64
-231, +231-1
-263, +263-1
8 / 64
-263, +263-1
%ld
long long
long long int
8 / 64
-263, +263-1
8 / 64
-263, +263-1
%lld
ptrdiff_t
4 / 32
-231, +231-1
8 / 64
-263, +263-1
%t
float
numeri reali
(con virgola)
4 / 32
10-38, 10+38
4 / 32
10-38, 10+38
%f
double
8 / 64
10-308, 10+308
8 / 64
10-308, 10+308
%lf
Dimensioni e specificatori dei tipi elementari con segno:
NOTA: queste sono dimensioni indicative, poichè sono dipendenti 
dallo specifico sistema in uso (come ad esempio per long int).

<!-- pagina 14 -->
Tabella dei tipi e specificatori di conversione
14
Tipo
Uso
CPU 32 bit
CPU 64 bit
specificatori 
di 
conversione
Dimensione
[Byte / bit]
Intervallo
Dimensione
[Byte / bit]
Intervallo
unsigned char
bytes
1 / 8
0, 255
1 / 8
0, 255
%hhu
unsigned short
unsigned short int
numeri 
naturali
2 / 16
0, +216-1
2 / 16
0, +216-1
%hu
unsigned int
unsigned signed int
4 / 32
0, +232-1
4 / 32
0, +232-1
%u
unsigned long
unsigned long int
4 / 32
8 / 64
0, +232-1
0, +264-1
8 / 64
0, +264-1
%lu
unsigned long long
unsigned long long int
8 / 64
0, +264-1
8 / 64
0, +264-1
%llu
size_t
4 / 32
0, +232-1
8 / 64
0, +264-1
%zu
float
numeri reali
(con virgola)
4 / 32
10-38, 10+38
4 / 32
10-38, 10+38
%f
double
8 / 64
10-308, 10+308
8 / 64
10-308, 10+308
%lf
Dimensioni e specificatori dei tipi elementari senza segno:
NOTA: non serve imparare a memoria queste tabelle!!

<!-- pagina 15 -->
Dimensioni dei tipi
Leggere, compilare e provare il programma dim_tipi.c
Quale caratteristica hanno le dimensioni dei tipi puntatore?
Perché?
15

<!-- pagina 16 -->
Documentazione
Potete accedere ad una versione offline della 
documentazione del linguaggio e della libreria del C.
1. Accedere a https://en.cppreference.com/w/c
2. Andare su “Offline version” (in basso), poi scaricare la 
versione più recente (Unofficial Release)
3. Aprire la pagina html-book/reference/en/c.html
4. Cercare nella sezione degli Headers la documentazione 
di <stdio.h>, e poi leggere la documentazione completa 
di printf
NOTA: la documentazione di riferimento è molto più 
elaborata di quello visto finora, ma vi serve per capire come 
cercare le informazioni che vi servono.
16

<!-- pagina 17 -->
Mercato
Scrivere un file mercato.c per calcolare il prezzo di quanto 
acquistiamo al supermercato:
•
3 pacchi di orecchiette (prezzo di un pacco di orecchiette euro 1.50)
•
1 kg e 1⁄2 di pomodori (prezzo al kg dei pomodori: euro 2.50)
Scrivere la funzione main in modo che calcoli e visualizzi a video la 
spesa totale. Suggerimenti:
•
Modellare il problema utilizzando delle variabili 
opportunamente dichiarate con tipi adeguati.
•
Utilizzare una variabile anche per rappresentare il totale.
•
Indentare e commentare opportunamente il programma.
Infine, modificare il programma per far inserire le quantità degli 
articoli alimentari dall'utente da tastiera (anziché fissare nel codice 
del programma i valori delle variabili).
17

<!-- pagina 18 -->
Scambio di variabili
Leggere, compilare e provare il programma scambio.c 
(simile a quello che avete visto a lezione)
Scrivere un programma scambio4.c che prende 4 variabili 
intere v1, v2, v3 e v4 (opportunamente inizializzate con dei 
valori iniziali a scelta), e le scambia in modo tale che:
• v1 prende il valore di v2
• v2 prende il valore di v3
• v3 prende il valore di v4
• v4 prende il valore di v1
Stampare i valori delle quattro variabili prima e dopo lo 
scambio.
18
