# 02B_assegnamento_memory_model

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
Memoria e Variabili
Modello della memoria per il linguaggio 
C, dalle variabili alle espressioni
1

<!-- pagina 2 -->
Dai bit ai tipi di dati strutturati
• Il software serve a rappresentare e manipolare la realtà.
• Ogni informazione del mondo (numeri, testi, immagini, 
decisioni) deve essere trasformata in dati per essere elaborata 
da una macchina.
• Ma i dati da soli non bastano: occorre stabilire come 
interpretarli
• Questo è il ruolo dei tipi: regole che danno signiﬁcato ai bit in 
memoria e ne delimitano l’uso.
Un tipo di dato è un ponte tra i bit e il senso che vogliamo dare 
ai dati codiﬁcati tramite quei bit. Senza i tipi, avremmo solo 
sequenze di bit indistinguibili.
2

<!-- pagina 3 -->
I tipi nel linguaggio C
Un tipo qualiﬁca una sequenza di bit secondo varie dimensioni:
• Nome: identiﬁcatore usato nel codice (int, ﬂoat, struct Persona)
• Dimensione in memoria: quanti byte occupa (int = tipicamente 4B, double = 
8B)
• Dominio di valori: insieme di valori validi (es. int = numeri interi compresi in 
un certo intervallo)
• Operazioni consentite: quali operatori o funzioni si possono applicare 
(somma su interi, sqrt su ﬂoat, ...)
• Rappresentazione interna: come i bit vengono codiﬁcati (complemento a 2 
per interi, IEEE 754 per ﬂoat, …) → ve ne occuperete in Architetture degli 
Elaboratori e in Fondamenti dell’Informatica.
• Compatibilità con altri tipi: regole di conversione implicite ed esplicite (cast)
3

<!-- pagina 4 -->
Le variabili in C
• Una variabile associa un nome e un tipo di dato a una porzione di 
memoria che contiene un valore.
• Permette al programmatore di lavorare con i dati attraverso nomi 
simbolici, senza dover manipolare direttamente indirizzi di memoria 
e rappresentazioni binarie.
• Nel modello EDVAC/Von Neumann le operazioni agiscono 
direttamente su valori memorizzati a determinati indirizzi. I linguaggi 
di alto livello introducono le variabili come astrazione di queste 
posizioni di memoria.
• Possiamo così esprimere le operazioni sui dati in modo più leggibile 
e indipendente dai dettagli ﬁsici della loro collocazione in memoria.
4

<!-- pagina 5 -->
Le variabili in C
Una variabile è deﬁnita da:
• Nome: identiﬁcatore scelto dal programmatore (contatore, altezza, media)
• Tipo: stabilisce il signiﬁcato dei bit (es. int → intero, ﬂoat → numero 
reale)
• Indirizzo: la posizione ﬁsica in memoria dove il dato è memorizzato. 
• Valore: il contenuto attuale, che può cambiare durante l’esecuzione.
5
valore: 60.54
indirizzo: 0x367F
tipo: float
nome: media
valore: 1
indirizzo: 0x904A
tipo: int
nome: contatore
int contatore = 1;
float media = 60.54;

<!-- pagina 6 -->
Le variabili in C
• Una volta dichiarata una variabile, il programmatore 
normalmente non speciﬁca il suo indirizzo di memoria: la 
collocazione concreta viene determinata automaticamente* dal 
compilatore e dal sistema di esecuzione.
• Il programmatore stabilisce invece il tipo di dato, quindi:
– quali valori la variabile può rappresentare;
– come tali valori sono codiﬁcati in memoria;
– quali operazioni possono essere applicate;
– come valori di tipi diversi possono interagire.
• Comprendere i tipi signiﬁca quindi collegare il livello astratto del 
C alla rappresentazione concreta dei dati nella memoria della 
macchina.
* La gestione della memoria in C è solo parzialmente automatica.
6

<!-- pagina 7 -->
Panoramica del type system del C
7
Tipi primitivi (built-in)
Tipi derivati
Funzioni
Typedef
Tipi qualiﬁcati
const  volatile  restrict
Numeri Interi (ℤ)
int, short, char, …
Numeri Naturali (ℕ)
unsigned int, 
unsigned short, …, 
bool
Numeri Reali (ℝ)
ﬂoat, double
Tipi incompleti
void
Puntatori
Array
Struct
Union
Enum

<!-- pagina 8 -->
Tipi primitivi del linguaggio C
Partiamo da un sottoinsieme dei tipi primitivi, utili per iniziare:
▶int: tipo delle variabili che rappresentano numeri interi (ℤ)
– Altri tipi interi: short int, long int, long long int
▶unsigned int: tipo che rappresenta numeri naturali (ℕ)
▶ﬂoat: tipo dei numeri reali (ℝ)
– Altri tipi reali: double, long double
▶char: tipo dei caratteri, occupa 1 byte (8 bit)
▶size_t: tipo intero unsigned delle dimensioni.
– deﬁnito in <stddef.h>
▶bool: tipo delle operazioni logiche. 0/1, false/true
– deﬁnito in <stdbool.h>
8

<!-- pagina 9 -->
I tipi numerici del C sono finiti
Le categorie ℕ, ℤ e ℝ indicano il dominio matematico di riferimento, ma 
non coincidono con i tipi del C.
• Gli insiemi ℕ, ℤ e ℝ sono inﬁniti.
• Un valore C è rappresentato usando una quantità ﬁnita di memoria, 
quindi ogni tipo può rappresentare solo un insieme ﬁnito di valori.
• int rappresenta solo un intervallo ﬁnito di numeri interi.
• unsigned int rappresenta solo un intervallo ﬁnito di numeri naturali.
• ﬂoat e double rappresentano un insieme ﬁnito di valori usati per 
approssimare i numeri reali.
I tipi numerici del C sono quindi modelli ﬁniti dei corrispondenti domini 
matematici. Questo introduce limiti di intervallo per gli interi e di 
precisione per i numeri ﬂoat/double.
9

<!-- pagina 10 -->
Dichiarazione di variabili
• Ogni variabile deve essere dichiarata con un tipo e un 
identiﬁcatore
int x;
• Questo riserva lo spazio necessario in base al tipo in 
un’area di memoria detta pila (stack)
• Dopo la dichiarazione, l’area di memoria riservata diventa 
accessibile usando il nome scelto
• L’identiﬁcatore è simbolico perché rappresenta un 
indirizzo della memoria, e non esiste nell’assembly
10

<!-- pagina 11 -->
Stampa dei valori
Vediamo una prima operazione che si può fare sulle variabili di un 
tipo primitivo: stamparne il valore a schermo.
11
1.
int x = 10;       // variabile intera
2.
float y = 3.14f;  // variabile reale (o in “virgola mobile”)
3.
// Stampa dei valori
4.
printf("La variabile x vale: %d\n", x);   // %d → intero (int)
5.
printf("La variabile y vale: %f\n", y);   // %f → float (decimale)
La funzione printf permette di stampare testo assieme ai valori 
delle variabili:   printf("testo e specificatori", lista_di_variabili);
• La stringa di formato contiene testo normale più speciﬁcatori di 
formato (es. %d, %f, %c …)
• Dopo la stringa, si passano come argomenti le variabili da stampare, 
nell’ordine corrispondente agli speciﬁcatori.

<!-- pagina 12 -->
Tassonomia dei tipi primitivi del C
12
Naturali (ℕ)
Interi (ℤ)
Reali (ℝ)
char
unsigned char
short
short int
unsigned short
unsigned short int
int
signed int
unsigned int
unsigned signed int
long
long int
unsigned long
unsigned long int
long long
long long int
unsigned long long
unsigned long long int
float
double
Numeri
Dimensioni
ptrdiff_t
size_t
Carattere
Byte
char
unsigned char
Logico
bool

<!-- pagina 13 -->
Dimensione delle variabili
Il C non deﬁnisce in modo rigido la dimensione in bits/bytes dei tipi 
primitivi (per portabilità su architetture molto diverse), ma deﬁnisce 
relazioni di ordine tra le dimensioni:
sizeof(char) ≤ sizeof(short) ≤ sizeof(int) ≤ sizeof(long) ≤ sizeof(long long)
sizeof(ﬂoat) ≤ sizeof(double)
Il risultato dell’operatore sizeof ha tipo size_t.
Consideriamo alcune conﬁgurazioni tipiche delle dimensioni dei tipi sulle 
piattaforme a 32 e 64 bit, che useremo come riferimento (slide successiva)
13

<!-- pagina 14 -->
Tabella dei tipi e specificatori di conversione
14
Tipo
Uso
CPU 32 bit
CPU 64 bit
specificatori di 
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
Dimensioni e speciﬁcatori dei tipi elementari con segno:

<!-- pagina 15 -->
Tabella dei tipi e specificatori di conversione
15
Tipo
Uso
CPU 32 bit
CPU 64 bit
specificatori di 
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
Dimensioni e speciﬁcatori dei tipi elementari senza segno:
NOTA: non serve imparare a memoria queste tabelle!!

<!-- pagina 16 -->
Identificatori delle variabili
• Il nome della variabile deve seguire regole precise:
– Deve essere univoco all’interno del suo ambito (scope)
– Deve iniziare con una lettera o underscore (spesso si 
preferisce la lettera minuscola)
– Non può contenere spazi o simboli speciali
– Può contenere lettere, numeri (non iniziali) e underscore
• Esempio:    int laMiaPrimaVariabile;
16

<!-- pagina 17 -->
Identificatori delle variabili
• Useremo delle convenzioni per gli identiﬁcatori delle variabili:
– preferire il solo minuscolo, oppure per nomi composti da più parole si 
può usare la convenzione camelCase:
sommaTot,  media7giorni,  elementoTrovato.
– usare nomi signiﬁcativi, che ne descrivano il ruolo:
• Buoni esempi:   somma,  media,  massimoTrovato
• Solo se è chiaro dal contesto:  s,  m,  flag 
• Cattivi esempi:  pippo,  pluto,  nonSoCheNomeDare
• La scelta del nome di una variabile non è un dettaglio secondario, ma un 
elemento importante della prassi della programmazione
• Serve a rendere il codice leggibile e comprensibile: descrive chiaramente 
il signiﬁcato del dato, riduce gli errori e facilita il ragionamento
17

<!-- pagina 18 -->
Visibilità e durata delle variabili
• Una variabile può essere usata dove è visibile (in scope):
– Locale/Automatica (default): dichiarata dentro una funzione o un blocco di 
codice { ... }, è accessibile solo lì
– Globale: dichiarata fuori da ogni funzione, è visibile in tutto il ﬁle (e, se 
extern, anche in altri ﬁle).
– Statica: variabile persistente ma visibilità nel blocco in cui compare.
• Una variabile esiste in memoria in funzione della sua durata (lifetime):
– Le variabili locali/automatiche sono allocate sullo stack
– Le variabili globali/statiche esistono per tutta la durata del programma
– Le variabili dinamiche sono allocate nello heap (vedremo più avanti) con 
funzioni come malloc(), e persistono ﬁnché non vengono liberate 
manualmente.
• Per utilizzare il linguaggio C serve comprendere come la memoria è 
gestita (allocata e deallocata). Studieremo l’evoluzione della memoria 
dati del programma usando un modello della memoria
18

<!-- pagina 19 -->
Un primo modello di memoria
• Al caricamento (loading) del programma 
dalla memoria secondaria, viene allocata 
un’area di memoria per codice e dati del 
programma
Area codice
Words di 32 bit
Indirizzi di memoria crescenti
Area dati
Area di memoria 
riservata al 
programma
19

<!-- pagina 20 -->
Un primo modello di memoria
• Al caricamento (loading) del programma 
dalla memoria secondaria, viene allocata 
un’area di memoria per codice e dati del 
programma
• La dimensione dell’area codice è ﬁssa
Area codice
Words di 32 bit
Indirizzi di memoria crescenti
Area dati
Area di memoria 
riservata al 
codice
20

<!-- pagina 21 -->
Un primo modello di memoria
●Al caricamento (loading) del programma 
dalla memoria secondaria, viene allocata 
un’area di memoria per codice e dati del 
programma
●La dimensione dell’area codice è ﬁssa
●L’area dati è ﬂessibile ma assumiamo 
abbia una dimensione massima
●Le variabili sono allocate nell'area riservata 
ai dati una dopo l’altra in ordine di 
dichiarazione
Area codice
Words di 32 bit
Indirizzi di memoria crescenti
Area dati
Area di memoria 
riservata ai dati
21

<!-- pagina 22 -->
Un primo modello di memoria
●Il Program Counter (PC) parte nell’area 
codice, all’indirizzo di inizio del main
●Il Frame Pointer (FP) è l’indirizzo base da 
cui iniziare ad allocare le variabili del 
programma (partendo dal main)
●Lo Stack Pointer (SP) indica l’indirizzo a cui 
allocare la prossima variabile
●All’inizio, FP e SP coincidono
Area codice
Frame Pointer e 
Stack pointer di 
main()
Indirizzi di memoria crescenti
Area dati
▶int main (void) {
     int x;
 }
32 bit, 4 bytes
22
FP
SP
PC

<!-- pagina 23 -->
Un primo modello di memoria
●Chiamiamo stack (pila) la parte “alta” 
dell’area dati.
●Nel nostro modello rappresentiamo lo stack 
nella parte alta dell’area dati e assumiamo 
che cresca verso indirizzi più bassi.
○NOTA: è una convenzione di 
rappresentazione: la direzione di crescita 
dello stack dipende dall’architettura e dal 
sistema.
Area codice
Indirizzi di memoria crescenti
Area dati
?
x
32 bit, 4 bytes
 int main (void) {
▶    int x;
 }
23
FP
SP

<!-- pagina 24 -->
Un primo modello di memoria
●Con questa convenzione, dopo la dichiarazione 
di x, SP viene decrementato della dimensione 
necessaria alla variabile (ad es. assumiamo 4 
byte per il tipo int).
●L’allocazione di una variabile occupa memoria 
sullo stack.
○Se lo spazio disponibile per lo stack si 
esaurisce, si può ottenere un errore runtime 
di tipo stack overﬂow.
Area codice
Indirizzi di memoria crescenti
Area dati
?
x
32 bit, 4 bytes
 int main (void) {
▶    int x;
 }
24
FP
SP

<!-- pagina 25 -->
Un primo modello di memoria
●Dichiarare una variabile locale senza 
inizializzarla riserva lo spazio di memoria, 
ma non le assegna un valore: il suo valore 
iniziale è indeterminato.
●Ne indicheremo il contenuto con «?».
Area codice
Indirizzi di memoria crescenti
Area dati
?
32 bit, 4 bytes
 int main (void) {
▶    int x;
 }
25
x
FP
SP

<!-- pagina 26 -->
Un primo modello di memoria
●Per ogni variabile dichiarata, viene allocata una 
quantità di memoria corrispondente al tipo
●L’allocazione avviene in ordine di dichiarazione
Area codice
?
?
y
?
z
Indirizzi di memoria crescenti
32 bit, 4 bytes
12 bytes allocati 
per 3 variabili di 
tipo int da
4 bytes l’una
int main(void) {
    int x;
    int y;
    int z;
}
26
x
FP
SP

<!-- pagina 27 -->
●Dichiarata una variabile, è possibile scrivere un valore in 
tale area di memoria assegnandogli un valore con 
l’operatore «=»
int x;
x = 10;
●Dichiarazione e assegnamento possono essere eseguiti 
sulla sulla stessa linea, per semplicità (deﬁnizione)
int x = 10;
Vediamo una seconda operazione che si può fare sulle variabili di 
un tipo primitivo: assegnargli un valore (assignment).
27
Assegnare valori

<!-- pagina 28 -->
●L’assegnamento di valore deve riﬂettere il tipo della 
variabile
int x = -8;
●Alcuni valori danno overﬂow non rilevabili dal compilatore
int x = 2 147 483 649;
●Alcune espressioni potrebbero essere interpretate 
diversamente da come inteso dal programmatore a seconda 
del tipo
  int x = 8.89;
$ ./overflow 
x vale -2147483647
$ ./float2int 
x vale 8
28
Assegnare valori

<!-- pagina 29 -->
Assegnamento in C
• La forma generale di un assegnamento è:
variabile = espressione;
• Lato sinistro (lvalue) 
variabile: indica l’area di memoria in cui salvare il risultato 
• Lato destro (rvalue)
espressione: un valore o una formula da calcolare
• Passaggi logici:
– L’espressione a destra viene valutata (evaluated)
– Se la valutazione ha successo, produce un valore
– Questo valore viene copiato nell’area di memoria associata al nome 
della variabile
29

<!-- pagina 30 -->
Espressioni aritmetiche in C (su interi)
• Per ora ci concentriamo solo su espressioni algebriche con 
variabili intere
• Il linguaggio delle espressioni aritmetiche elementari è:
– Somma: 
valoreA + valoreB 
– Sottrazione: 
valoreA - valoreB
– Moltiplicazione: 
valoreA * valoreB
– Divisione intera (solo parte intera): valoreA / valoreB 
– Modulo (resto della divisione): 
valoreA % valoreB 
– Parentesi tonde:  raggruppamento delle operazioni
• Esempi
    int incasso = biglietti * prezzoBiglietto;
    int utile = incasso - costoSala;
30

<!-- pagina 31 -->
Precedenza degli operatori aritmetici
• Le regole di precedenza stabiliscono quale operatore viene 
valutato per primo quando in un’espressione sono presenti più 
operatori.
• Gli operatori *, /, % hanno la precedenza più alta tra quelli 
aritmetici
• Subito dopo, in ordine decrescente, troviamo + e -
• A parità di precedenza, le operazioni vengono valutate da sinistra 
a destra
• L’operatore di assegnamento = viene eseguito solo alla ﬁne
• Le parentesi tonde () hanno precedenza assoluta:
– permettono di forzare l’ordine di valutazione
– possono essere annidate su più livelli
31

<!-- pagina 32 -->
Divisione intera e modulo in C
• La divisione intera (/) restituisce solo la parte intera del 
quoziente, mentre la parte decimale viene scartata (non 
arrotondata)
int a = 13, b = 3;
int quot = a / b;    // quot = 4
• Il modulo (%) restituisce il resto della divisione intera
int r = a % b;   // r = 1 perchè 13 = 3*4 + 1
• Il modulo è molto utile per controllare la parità di un 
numero
– se num % 2 vale 0 allora num è pari
– se num % 2 vale 1 allora num è dispari
32

<!-- pagina 33 -->
Espressioni algebriche
int main(void) {
    int x;
    int y;
▶   int z;
    x = 5;
    y = 2;
    z = x + y;
    printf("Le var x, y  e z valgono %d, %d, %d\n", 
            x, y, z);
}
Area codice
?
?
?
Indirizzi di memoria crescenti
32 bit, 4 bytes
$ ./treVariabili 
33
y
z
x
FP
SP

<!-- pagina 34 -->
int main(void) {
    int x;
    int y;
    int z;
    x = 5;
▶   y = 2;
    z = x + y;
    printf("Le var x, y  e z valgono %d, %d, %d\n", 
            x, y, z);
}
Espressioni algebriche
Area codice
5
2
?
Indirizzi di memoria crescenti
32 bit, 4 bytes
$ ./treVariabili 
Assegnamento di 
un valore numerico
34
y
z
x
FP
SP

<!-- pagina 35 -->
int main(void) {
    int x;
    int y;
    int z;
    x = 5;
    y = 2;
▶   z = x + y;
    printf("Le var x, y  e z valgono %d, %d, %d\n", 
            x, y, z);
}
Espressioni algebriche
Area codice
5
2
7
Indirizzi di memoria crescenti
$ ./treVariabili 
32 bit, 4 bytes
Assegnamento 
del risultato di 
espressione 
algebrica
LOAD, R0, @x
LOAD, R1, @y
ADD, R0, R1
STORE, R0, @z
35
y
z
x
FP
SP

<!-- pagina 36 -->
int main(void) {
    int x;
    int y;
    int z;
    x = 5;
    y = 2;
    z = x + y;
▶   printf("Le var x, y  e z valgono %d, %d, %d\n", 
            x, y, z);
}
Espressioni algebriche
Area codice
5
2
7
Indirizzi di memoria crescenti
32 bit, 4 bytes
Stampa a 
schermo
tre variabili
parametri
separati da
virgola
$ ./treVariabili 
Le var x, y  e z valgono 5, 2, 7
36
y
z
x
FP
SP

<!-- pagina 37 -->
Altri esempi con printf
37
●Permette la stampa di variabili usando gli 
speciﬁcatori di formato (o “di conversione”) 
●Per gli int lo speciﬁcatore é %d
●Segue un parametro per ciascun speciﬁcatore
printf("x vale %d, y vale %d\n", x, y);
●Il primo speciﬁcatore %d dice di stampare il primo 
parametro x come intero decimale
●Il secondo speciﬁcatore %d dice di stampare il 
secondo parametro y
$ ./printf_2 
x  vale 5, y vale 2
Area codice
5
x
2
y

<!-- pagina 38 -->
●Stampa con minimo numero di cifre intere richieste
printf("x vale %d\n", x);
●Stampa su, per es., 6 cifre intere con padding a sinistra
printf("x vale %6d\n", x);
●Stampa su, per es., 6 cifre intere con zeroing a sinistra
printf("x vale %06d\n", x);
Altri esempi con printf
38
$ ./printf_4 
x vale 7
$ ./printf_5 
x vale              7
$ ./printf_5 
x vale 000007
https://www.gnu.org/software/libc/manual/html_node/Formatted-Output.html

<!-- pagina 39 -->
Assegnamento: riassunto e sintassi
• Inizializzazione alla dichiarazione 
(Valore assegnato subito alla 
creazione della variabile)
int x = 10;
float y = 3.14;
• Assegnamento successivo 
(prima si dichiara, poi si assegna)
int x;
x = 10;
39
●Assegnamento da input
(tramite funzioni come scanf)
int n;
scanf("%d", &n);
●Assegnamento multiplo
(possibile assegnare un valore a 
più variabili in un’unica istruzione)
int a, b, c;
a = b = c = 0;

<!-- pagina 40 -->
Operatori di assegnamento composti
Il C consente di combinare un’operazione algebrica con un 
assegnamento, tramite gli operatori di assegnamento composti
40
Operatore
Espansione
Esempio in C
+=
x = x + y
x = 5; 
x += 3; // x = 8
-=
x = x - y
x = 5; 
x -= 2; // x = 3
*=
x = x * y
x = 5; 
x *= 4; // x = 20
/=
x = x / y
x = 20; 
x /= 5; // x = 4
%=
x = x % y
x = 20; 
x %= 6; // x = 2

<!-- pagina 41 -->
Operatori di incremento e decremento
• Sintassi compatta per aumentare o diminuire una variabile 
intera di una unità.
• Incremento
x++; // equivalente a:  x = x + 1
• Decremento
x--; // equivalente a:  x = x - 1
• Li useremo come istruzioni di incremento/decremento 
(questi operatori sono anche espressioni di pre/post incremento e 
decremento, ma non tratteremo questo caso)
41
