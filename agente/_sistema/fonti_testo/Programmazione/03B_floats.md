# 03B_floats

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
Numeri reali in C
Float, double, precisione, conversione

<!-- pagina 2 -->
Tipi dei numeri reali
• Nel calcolo scientiﬁco e in moltissime applicazioni pratiche 
(graﬁca, simulazioni, elaborazione di dati) è necessario lavorare 
con numeri reali, cioè valori che includono una parte intera e 
una frazionaria.
• Nel linguaggio C questi numeri sono rappresentati 
principalmente tramite i tipi 
– ﬂoat (tipicamente 32 bit)
– double (tipicamente 64 bit)
• Questi tipi differiscono per precisione e range dei valori 
rappresentabili.
• La loro codiﬁca segue lo standard IEEE 754, che vedrete nel 
corso di Fondamenti dell’Informatica
2

<!-- pagina 3 -->
Confronto tra float e double
3
Tipo
Dimensione 
(tipica)
Precisione 
approssimativa
Intervallo di valori 
rappresentabili
Uso consigliato
ﬂoat
32 bit (4 byte)
~7 cifre decimali
da ~10⁻³⁸ a ~10³⁸
Quando serve 
risparmiare memoria o 
per calcoli meno critici
double
64 bit (8 byte)
~15-16 cifre decimali
da ~10⁻³⁰⁸ a ~10³⁰⁸
Per calcoli scientiﬁci o 
applicazioni che 
richiedono alta precisione
• Operazioni aritmetiche:  addizione (+), sottrazione (-), 
moltiplicazione (*) e divisione (/). Non c'è✤ il modulo (%)
✤ C'è ma non come operatore, si trova in libreria e si chiama fmod. Non lo useremo.

<!-- pagina 4 -->
Formati di stampa per float e double
4
Speciﬁc
atore
Descrizione
Esempio 
(double z = 2.5;)
Quando usarlo
%f
Notazione decimale ﬁssa
2.500000 
(default 6 decimali)
Quando si vuole la 
rappresentazione “naturale” di 
un numero reale
%e
Notazione scientiﬁca 
(esponenziale)
2.500000e+00
Utile per numeri molto grandi o 
molto piccoli
%g
Formato adattivo: sceglie tra 
%f e %e quello più compatto, 
eliminando zeri inutili
2.5
Quando serve una stampa 
leggibile e compatta, senza 
preoccuparsi della notazione
• NOTA: per leggere i double con scanf, usare gli speciﬁcatori  
%lf %le e %lg invece di %f, %e e %g.

<!-- pagina 5 -->
Esempi di formattazione
5
https://www.gnu.org/software/libc/manual/html_node/Formatted-Output.html
• Stampa notazione naturale
printf("z vale %f\n", z);
⇒
z vale 2.500000
• Stampa troncata al terzo decimale
printf("z vale %.3f\n", z);
⇒
z vale 2.500
• Stampa notazione esponenziale troncata al terzo decimale
printf("z vale %.3e\n", z);
⇒
z vale 2.500e+00

<!-- pagina 6 -->
I tipi float e double
int main(void) {
    float x = 5, y = 2, z;
    z = x / y;
    printf("La var x vale %f\n", x);
    printf("La var y vale %f\n", y);
    printf("La var z vale %f\n", z);
}
$ ./math 
La var x vale 5.000000 
La var y vale 2.000000 
La var z vale 2.500000Il ptr pX all'ind 0xbd6ac520 
vale 0xbd6ac52c 
Area codice
Indirizzi di memoria crescenti
32 bit, 4 bytes
float x
5,000000
float y
2,000000
2,500000
float z

<!-- pagina 7 -->
I tipi float e double
$ ./math 
La var x vale 5.000000 
La var y vale 2.000000 
La var z vale 2.500000Il ptr pX all'ind 0xbd6ac520 
vale 0xbd6ac52c 
Area codice
Indirizzi di memoria crescenti
32 bit, 4 bytes
double x
5,000000
double y
2,000000
2,500000
double z
64 b, 8B
64 b, 8B
64 b, 8B
int main(void) {
    double x = 5, y = 2, z;
    z = x / y;
    printf("La var x vale %f\n", x);
    printf("La var y vale %f\n", y);
    printf("La var z vale %f\n", z);
}

<!-- pagina 8 -->
I tipi float e double
$ ./math 
La var x vale 5.000000 
La var y vale 2.000000 
La var z vale 2.500000Il ptr pX all'ind 0xbd6ac520 
vale 0xbd6ac52c 
Area codice
Indirizzi di memoria crescenti
32 bit, 4 bytes
float x
double z
32 b, 4B
64 b, 8B
5,000000
float y
2,000000
2,500000
32 b, 4B
int main(void) {
    float x = 5, y = 2;
    double z = x / y;
    printf("La var x vale %f\n", x);
    printf("La var y vale %f\n", y);
    printf("La var z vale %f\n", z);
}

<!-- pagina 9 -->
La libreria math.h
• In C gli operatori (+, -, *, /, %) coprono solo le operazioni 
aritmetiche di base.
• Per funzioni più avanzate (radici, potenze, logaritmi, 
trigonometria, …) si utilizza la libreria math.h, da includere con 
#include <math.h>
• Questa libreria fornisce una serie di funzioni utili (sqrt(), pow(), 
sin(), cos(), …) e per diversi tipi (int, ﬂoat, double, …)
• Link: https://en.cppreference.com/w/c/header/math.html
• NOTA: in Unix l’uso della libreria math.h richiede di essere 
compilata con -lm (es.: gcc programma.c -lm)
9

<!-- pagina 10 -->
La libreria math
10
#include <stdio.h>
#include <math.h>
int main(void) {
    float num = 9.0, radice, quadrato;
    quadrato = pow(num, 2);
    radice = sqrt(num);
    printf("Il quadrato di %.0f è %.2f\n", num, quadrato);
    printf("La radice di %.0f è %.2f\n", num, radice);
}
$ ./math_2
Il quadrato di 9 è 81.00 
La radice di 9 è 3.00 vale 0xbd6ac52c

<!-- pagina 11 -->
Conversioni di tipo
Come cambiare il tipo delle variabili 
e come gestire precisione e perdita 
di informazione nei passaggi tra tipi
11

<!-- pagina 12 -->
Conversioni di tipo
• Quando in un programma usiamo variabili di tipi diversi (interi, 
reali, caratteri, ecc.), queste non hanno la stessa rappresentazione 
e le stesse caratteristiche
• Per poterle usare in una stessa espressione, i valori devono 
essere trasformati in un formato compatibile: questo processo si 
chiama conversione di tipo
• In C esistono due modalità principali:
– Conversioni implicite, eseguite automaticamente dal compilatore
– Conversioni esplicite (casting), richieste in modo volontario dal 
programmatore
• Le conversioni di tipo possono comportare una perdita di 
informazione o di precisione
12

<!-- pagina 13 -->
Conversioni di tipo implicite
• In C è possibile usare e combinare nella stessa espressione 
variabili di tipi diversi (es. int, ﬂoat, double)
• Il compilatore provvede automaticamente a uniformarli: 
questo meccanismo è detto implicit casting 
• Attenzione: le conversioni implicite possono causare perdite 
di precisione senza generare errori o avvisi.
• Esempio tipico: assegnare un valore ﬂoat a una variabile int 
elimina la parte frazionaria in silenzio.
13

<!-- pagina 14 -->
Conversioni implicite e conseguenze
14
Conversione
Implicito
Perdita di dati?
Errore?
Esempio in C
int → ﬂoat
Sì
No (tranne per interi molto 
grandi)
No
int x = 5; 
ﬂoat y = x; // y = 5.0f
ﬂoat → int
Sì
Sì (parte frazionaria persa)
No
ﬂoat x = 3.7; 
int y = x; // y = 3
int → double
Sì
No (range molto ampio)
No
int x = 42; 
double y = x; // y = 42.0
double → int
Sì
Sì (frazione persa; Undeﬁned 
behaviour se fuori range)
No
double x = 9.9; 
int y = x; // y = 9
ﬂoat ↔ double
Sì
Sì (da double a ﬂoat si perde 
precisione)
No
double a = 3.14159; 
ﬂoat b = a; // b ≈ 3.14159 
ma meno preciso
char → int
Sì
No (valore ASCII promosso a 
int)
No
char c = 'A'; 
int x = c; // x = 65
Conversioni non 
compatibili
No
—
Errore di 
compilazione
int x = 5; 
int *p = x; // ERRORE

<!-- pagina 15 -->
Conversioni di tipo implicite
• Quando si scrivono espressioni aritmetiche con variabili 
di tipo diverso, è importante interpretare correttamente il 
signiﬁcato dell’operazione
• Occorre quindi:
– Analizzare i tipi di ciascun operando nell’espressione, 
seguendo le regole di promozione di tipo
– Valutare se la combinazione dei tipi può causare una perdita 
di precisione o un risultato inatteso
• Vediamo le regole principali e qualche esempio speciﬁco
15

<!-- pagina 16 -->
Promozione di tipo
• Le regole di promozione di tipo sono applicate dal compilatore 
per uniformare gli operandi di ciascuna espressione, e poter 
calcolare un risultato coerente
• I tipi “più piccoli” vengono promossi a tipi più grandi:
– char → short → int → long
– ﬂoat → double
esempio: char + int → promozione ad int
• Se i tipi differiscono, il compilatore converte al tipo più 
ampio/preciso per ridurre la perdita di informazione
– tipo intero e tipo reale → promozione a reale
esempio:  int + double →promozione a double
16

<!-- pagina 17 -->
Conversioni di tipo implicite
$ ./math 
xbd6ac520 vale 0xbd6ac52c 
Area codice
32 bit, 4 bytes
int x 
5
int y 
2
?
float z 
Perdita parte frazionaria
durante la divisione
fra interi
/
2
int main(void) {
    int x = 5, y = 2;
    float z = x / y;
    printf("La var x vale %d\n", x);
    printf("La var y vale %d\n", y);
    printf("La var z vale %f\n", z);
}

<!-- pagina 18 -->
Conversioni di tipo implicite
$ ./math 
d6ac520 vale 0xbd6ac52c 
Area codice
32 bit, 4 bytes
5
2
2,000000
Perdita parte frazionaria
già avvenuta
all’assegnazione
/
2
int x 
int y 
float z 
int main(void) {
    int x = 5, y = 2;
    float z = x / y;
    printf("La var x vale %d\n", x);
    printf("La var y vale %d\n", y);
    printf("La var z vale %f\n", z);
}

<!-- pagina 19 -->
Conversioni di tipo implicite
$ ./math 
La var x vale 5
La var y vale 2 
La var z vale 2.000000all'ind 0xbd6ac520 xbd6ac52c 
Area codice
32 bit, 4 bytes
5
2
2,000000
int x 
int y 
float z 
int main(void) {
    int x = 5, y = 2;
    float z = x / y;
    printf("La var x vale %d\n", x);
    printf("La var y vale %d\n", y);
    printf("La var z vale %f\n", z);
}

<!-- pagina 20 -->
Conversioni di tipo implicite
$ ./math 
d6ac520 vale 0xbd6ac52c 
Area codice
32 bit, 4 bytes
5,000000
2,000000
2
Divisione fra float
nessun problema
2,50000
/
float x
float y
int z
int main(void) {
    float x = 5, y = 2;
    int z = x / y;
    printf("La var x vale %f\n", x);
    printf("La var y vale %f\n", y);
    printf("La var z vale %d\n", z);
}

<!-- pagina 21 -->
Conversioni di tipo implicite
$ ./math 
20 vale 0xbd6ac52c 
Area codice
32 bit, 4 bytes
5,000000
2,000000
2
Casting implicito float -> int
durante l’assegnazione
con perdita parte frazionaria
2,50000
/
float x
float y
int z
int main(void) {
    float x = 5, y = 2;
    int z = x / y;
    printf("La var x vale %f\n", x);
    printf("La var y vale %f\n", y);
    printf("La var z vale %d\n", z);
}

<!-- pagina 22 -->
Conversioni di tipo implicite
$ ./math 
La var x vale 5.000000 
La var y vale 2.000000 
La var z vale 2all'ind 0xbd6ac520 vale 0xbd6ac52c 
Area codice
32 bit, 4 bytes
5,000000
2,000000
2
2,50000
/
float x
float y
int z
Parte frazionaria
persa
int main(void) {
    float x = 5, y = 2;
    int z = x / y;
    printf("La var x vale %f\n", x);
    printf("La var y vale %f\n", y);
    printf("La var z vale %d\n", z);
}

<!-- pagina 23 -->
Conversioni di tipo esplicite
• È possibile speciﬁcare in modo esplicito se e quando si vuole una 
conversione di tipo (explicit cast)
int x = 5;
float z = (float)x;   // x viene convertito in ﬂoat
• Importante quando si vuole controllare il tipo di una speciﬁca 
operazione, ad esempio, nella divisione tra interi:
int x = 5, y = 2;
float z = x / (float)y; // y convertito a ﬂoat → risultato 2.5
• In questo modo si evita la perdita della parte frazionaria che si 
avrebbe con la divisione intera x / y
23

<!-- pagina 24 -->
Conversioni di tipo esplicite
int main(void) {
    int x = 5, y = 2;
    float z = x / (float)y;
    printf("La var x vale %d\n", x);
    printf("La var y vale %d\n", y);
    printf("La var z vale %f\n", z);
}
$ ./math 
La var x vale 5.000000 
La var y vale 2.000000 
La var z vale 2.500000d6ac520 vale 0xbd6ac52c 
Area codice
32 bit, 4 bytes
int x 
5
int y 
2
2.50000
float z 
/
2.500000
Casting di y a float
preserva la
parte frazionaria

<!-- pagina 25 -->
Conversioni di tipo esplicite
• L’operazione di conversione di tipo agisce solo 
sull’espressione immediatamente alla sua destra.
int x = 10, y = 3;
float z = x / (float)y;
• Solo l'espressione y viene convertita in ﬂoat, mentre x 
rimane di tipo int. 
• La conversione cambia solo il tipo dell’espressione 
durante una valutazione, non cambia i tipi delle variabili 
coinvolte (es: x e y rimangono interi)
25
