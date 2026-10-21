# 05A_array_stringhe

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
Array e stringhe
Rappresentazione dei dati sequenziali, 
array statici, VLA e stringhe
1

<!-- pagina 2 -->
Dati sequenziali in C
• Per ora abbiamo lavorato con variabili scalari: 
una variabile = un valore
(es. un voto, un’altezza, un carattere)
• Ma molti problemi reali richiedono collezioni di dati omogenei*:
– tutti i voti di una classe
– serie temporali (temperature, prezzi, altimetriche, …)
– caratteri di un testo
• Soluzione: dati sequenziali (o vettoriali). 
Contenitori che permettono di gestire più valori omogenei in modo 
ordinato, accessibili tramite indici.
Passiamo da una variabile che contiene un singolo valore a contenitori 
che raccolgono più valori dello stesso tipo
2
*dati omogenei = dati dello stesso tipo.

<!-- pagina 3 -->
Array: definizione e caratteristiche
• Un array è una sequenza di valori dello stesso tipo, detti 
elementi, memorizzati in posizioni contigue di memoria
• Caratteristiche degli array:
– Tutti gli elementi hanno lo stesso tipo
– Ogni elemento è accessibile tramite indice
– Il numero di elementi, detto lunghezza (length), é deﬁnito
– Gli indici validi partono da 0 e arrivano a length - 1
⇒ gli indici validi appartengono ad un intervallo semiaperto
indice  ∈  [0, length)
– Per rappresentare1 lunghezze e indici di array usiamo normalmente 
size_t, il tipo intero unsigned standard dedicato alle dimensioni.
Il tipo size_t è deﬁnito in <stddef.h>.
3
1 The C standard says size_t represents an unsigned integral type and is recommended for any variable 
    representing an array’s size or subscripts. (pag. 247, Deitel)

<!-- pagina 4 -->
Array statici: sintassi
• Partiamo dagli array statici (dimensione nota alla compilazione, 
allocati sullo stack)
• Dichiarazione
tipo nome[dimensione];
• Accesso elementi:   
nome[indice]
• Esempio: array di 4 interi
4
1.
// array statico di 4 interi nello stack
2.
int numeri[4];
3.
numeri[0] = 10; // primo elemento
4.
numeri[1] = 20; // secondo elemento
5.
printf("%d\n", numeri[0]); // stampa 10
Codice
numeri[3] = ??
numeri[2] = ??
numeri[1] = 20
numeri[0] = 10
int numeri[4]
Indirizzi di memoria crescenti
word size

<!-- pagina 5 -->
Memoria e modello matematico degli array
• Rappresentazione in memoria
– Gli elementi di un array sono memorizzati in celle contigue
– Ogni cella ha la stessa dimensione (es. int = tipicamente 4 byte)
– L’elemento di indice 0 è al primo indirizzo; gli altri seguono in ordine
Esempio (array di 4 interi):
┌───────────────┬───────────────┬───────────────┬───────────────┐
│ numeri[0]     │ numeri[1]     │ numeri[2]     │ numeri[3]     │
│ 0x1000        │ 0x1004        │ 0x1008        │ 0x100C        │
└───────────────┴───────────────┴───────────────┴───────────────┘
• Rappresentazione matematica
– Un array può essere visto come un vettore:
numeri = (a₀, a₁, a₂, a₃)
– Ogni elemento del vettore aᵢ è identiﬁcato dal suo indice i
– NOTA: convenzionalmente gli indici in matematica iniziano da 1, in C 
iniziano sempre da 0
5

<!-- pagina 6 -->
Array statici: dichiarazione
• Il linguaggio C permette di deﬁnire array statici 
inizializzati con una lista di valori noti
int voti[5] = {18, 19, 24, 21, 30};
• Equivalente a
int voti[] = {18, 19, 24, 21, 30};
• Per inizializzare un array a zero
int voti[5] = {0};
6
Codice
30
int voti[4]@0x3FC
21
19
24
18
int voti[3]@0x3F8
int voti[2]@0x3F4
int voti[1]@0x3F0
int voti[0]@0x3EC
●Come per le variabili locali, gli elementi di un array locale dichiarato senza 
inizializzatore hanno valore indeterminato.
●Array con valori iniziali indeterminati:
int voti[5];  // elementi con valore indeterminato
Indirizzi di memoria crescenti
word size

<!-- pagina 7 -->
Array statici: un esempio
Uso tipico: memorizzare serie di dati, scorrere gli elementi tramite cicli (for, 
while), elaborare dati (statistica, calcoli, ordinamento).
Per deﬁnire le dimensioni (ﬁsse) degli array statici usiamo
#define COSTANTE_LUNGHEZZA numero
Esempio: stampa di una sequenza
7
1.
#define N 5
2.
int voti[N] = {18, 24, 28, 30, 19};
3.
4.
for (size_t i = 0; i < N; i++) {
5.
    printf("Voto %zu: %d\n", i, voti[i]);
6.
}
NOTA: la variabile di controllo i é di tipo size_t, in quanto è l’indice di accesso 
all’array. Lo speciﬁcatore di conversione per size_t è %zu.

<!-- pagina 8 -->
Array statici: esempi
Memorizzazione ed elaborazione sequenze (voti):
8
1.
#define N 5
2.
int voti[N] = {18, 19, 24, 21, 30};
3.
int somma = 0;
4.
for (size_t i = 0; i < N; i++) {
5.
    somma += voti[i];
6.
}
7.
printf("Media: %f\n", somma / (float)N);
Notazione matematica:
(assumendo indici che partono da 1)
(assumendo indici che partono da 0)

<!-- pagina 9 -->
Scansione di un array
• Chiamiamo scansione di un array (array traversal, linear scan) 
un ciclo che itera su tutti gli indici validi dell’array
• Poiché il dominio degli indici validi é l’intervallo semiaperto 
[0, length), cioé da 0 incluso a length escluso, otteniamo 
for (size_t i = 0; i < length; i++) { usa v[i] }
9
• Il ciclo in ordine inverso si scrive usualmente in due forme:
for (size_t i = length; i > 0; i--) { usa v[i-1] }
• oppure si può usare ptrdiff_t, il tipo per indici signed
for (ptrdiff_t i = (ptrdiff_t)length - 1; i >= 0; i--) { usa v[i] }
In questo caso serve ptrdiff_t invece di size_t perché l’indice deve 
scendere sotto lo zero per terminare il ciclo (size_t è unsigned)

<!-- pagina 10 -->
Scansione di un array - esempio
10
1.
#include <stdio.h>
2.
#include <stddef.h>    // definisce size_t e ptrdiff_t
3.
4.
int main(void) {
5.
    #define N 5
6.
    int v[N] = {10, 20, 30, 40, 50};
7.
8.
    // Scansione in avanti: indici [0, N)
9.
    printf("Scansione in avanti:\n");
10.
    for (size_t i = 0; i < N; i++) {
11.
        printf("v[%zu] = %d\n", i, v[i]);
12.
    }
13.
14.
    // Scansione all’indietro: indici [N-1, 0]
15.
    printf("\nScansione all’indietro:\n");
16.
    for (ptrdiff_t i = N - 1; i >= 0; i--) {
17.
        printf("v[%td] = %d\n", i, v[i]);
18.
    }
19.
}

<!-- pagina 11 -->
Array statici: esempi
Contare quanti valori superano una soglia (ciclo + condizione)
11
1.
#define N 8
2.
double temperature[N] = {18.5, 21.1, 25.2, 28.2, 
3.
                         19.4, 22.0, 26.3, 21.8};
4.
int conta = 0;
5.
for (size_t i = 0; i < N; i++) {
6.
    if (temperature[i] > 22.0) {
7.
        conta++;
8.
    }
9.
}
10.
printf("Giorni caldi: %d su %d\n", conta, N);
Notazione matematica:

<!-- pagina 12 -->
Array statici: esempi
Massimo in un array non vuoto
12
1.
#define N 6
2.
int numeri[N] = {3, 7, 2, 9, 5, 1};
3.
int max = numeri[0];
4.
for (size_t i = 1; i < N; i++) {
5.
    if (numeri[i] > max) {
6.
        max = numeri[i];
7.
    }
8.
}
9.
printf("Massimo: %d\n", max);
• Inizio (i=1):
max = massimo nell’intervallo [0, 1)
• Iterazione i:
max = massimo nell’intervallo [0, i)
• Fine (i==length):
max = massimo nell’intervallo [0, length)
Quale problema ha 
questo programma?
Notazione matematica:

<!-- pagina 13 -->
Conversione automatica array/puntatori
• Un array e un puntatore sono oggetti diversi.
• Tuttavia, nella maggior parte delle espressioni il nome di un array viene 
automaticamente convertito in un puntatore al suo primo elemento.
• Consideriamo:  int v[5] = {10, 20, 30, 40, 50};
–
v 
→ v viene convertito in un valore di tipo int* che punta a v[0] 
–
&v[i] 
→ indirizzo dell’elemento i
–
*(v + i) == v[i]
→ dereferenziazione con offset
printf("%p\n", v);       // indirizzo del primo elemento
printf("%p\n", &v[0]);   // stesso indirizzo
printf("%d\n", v[2]);    // 30
printf("%d\n", *(v+2));  // 30 (equivalente)
scanf("%d", &v[2]);      // leggi da input e modifica v[2]
size_t array_sz = sizeof(v); // dimensione dell’intero array
L’array rimane un oggetto di tipo int[5]; è l’espressione v che, quando richiesto 
dal contesto, viene convertita in int*.
13

<!-- pagina 14 -->
Indicizzazione e aritmetica dei puntatori
14
●In C, l’operatore di indicizzazione [] è deﬁnito come sintassi equivalente a:
v[i]   ≡   *(v + i)
cioè permette di accedere/modiﬁcare gli elementi dell’array come nella 
dereferenziazione di un puntatore.
• Dettaglio: Incrementare un puntatore di i elementi fa avanzare l'indirizzo di (i * 
sizeof(tipo_elemento)) byte.
v + i   =   indirizzo_base + i * sizeof(tipo_elemento) bytes
●In pratica:
○v 
è convertito nel puntatore al primo elemento (&v[0])
○v + i 
puntatore all'elemento v[i]
○*(v + i) 
valore dell’elemento v[i]
Useremo quasi sempre la notazione v[i], ma è utile comprendere che essa è 
un’operazione sugli indirizzi, parte dell’aritmetica dei puntatori

<!-- pagina 15 -->
Variable Length Array (VLA)
• Un limite degli array statici é che la dimensione deve essere stabilita 
a compilazione, e non può ad esempio dipendere da un valore letto 
in input
• Per gestire casi in cui la dimensione è nota solo a runtime, il C (a 
partire dallo standard C99) introduce i Variable Length Array (VLA)
• I VLA sono array allocati nello stack, ma con dimensione scelta al 
momento dell’esecuzione
• La dichiarazione è l’unica cosa diversa rispetto agli array statici
15
1.
size_t len;
2.
scanf("%zu", &len);
3.
int v[len];   // lunghezza len decisa a runtime

<!-- pagina 16 -->
Esempio con VLA
16
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    size_t n;
5.
    printf("Quante persone? ");
6.
    scanf("%zu", &n);
7.
8.
    int altezze[n];  // dimensione VLA indicata dall’utente
9.
10.
    // Caricamento da input
11.
    for (size_t i = 0; i < n; i++) {
12.
        printf("Inserisci altezza persona %zu (in cm): ", i + 1);
13.
        scanf("%d", &altezze[i]);
14.
    }
15.
16.
    // Stampa tabella
17.
    printf("\nTabella delle altezze:\n");
18.
    for (size_t i = 0; i < n; i++) {
19.
        printf("Persona %zu: %d cm\n", i + 1, altezze[i]);
20.
    }
21.
}

<!-- pagina 17 -->
Errori comuni
In C gli array non sono variabili assegnabili. Il loro nome rappresenta un 
indirizzo costante, non un valore
1.
int a[3] = {1, 2, 3};
2.
int b[3];
3.
b = a;    // ERRORE: non si può assegnare un intero array
Per copiare un array, si deve scrivere un ciclo che copia gli elementi. 
In generale: gli array in C non si comportano come variabili scalari: non si 
copiano, non si confrontano, e non si assegnano direttamente
1.
for (size_t i = 0; i < 3; i++)
2.
    b[i] = a[i];
17

<!-- pagina 18 -->
Errori comuni
Errore tipico: accesso fuori dai limiti
1.
int v[5] = {10, 20, 30, 40, 50};
2.
printf("%d\n", v[5]); // ERRORE: Indice 5 fuori intervallo [0..5)
• Il C non controlla i limiti degli array
• Un accesso fuori dai limiti produce comportamento indeﬁnito: il 
linguaggio non offre alcuna garanzia sul risultato; il programma può, 
ad esempio, produrre risultati errati, corrompere la memoria o 
terminare.
• Buona pratica: scrivere codice che si assicura che gli indici siano validi, 
cioè nell’intervallo semiaperto [0, length)
18

<!-- pagina 19 -->
Rappresentazione del testo
Nozione di carattere e stringa, testo 
come array di caratteri
19

<!-- pagina 20 -->
Array di caratteri: le stringhe
In C il testo è un array di elementi di tipo char1.
• Lettere, cifre, simboli sono rappresentati come unità elementari, 
dette caratteri
• Il tipo char è il tipo che rappresenta un singolo carattere.
• Un array di caratteri forma una stringa di testo
• I caratteri corrispondono a codici numerici convenzionali, descritti 
da degli standard. Lo standard fondamentale è l’ASCII2
• Abbiamo già usato il testo sotto forma di letterali stringa (string 
literals) non modiﬁcabili , scrivendo i caratteri tra doppi apici ("")
20
1 Si legge /tʃɑːr/ (circa “ciàr”) anche se è l’abbreviazione di character.
2 American Standard Code for Information Interchange. Si legge /ˈæski/ (circa “àski”).

<!-- pagina 21 -->
I 128 caratteri dell’ASCII
0
NUL
16
DLE
32
48
0
64
@
80
P
96
`
112
p
1
SOH
17
DC1
33
!
49
1
65
A
81
Q
97
a
113
q
2
STX
18
DC2
34
"
50
2
66
B
82
R
98
b
114
r
3
ETX
19
DC3
35
#
51
3
67
C
83
S
99
c
115
s
4
EOT
20
DC4
36
$
52
4
68
D
84
T
100
d
116
t
5
ENQ
21
NAK
37
%
53
5
69
E
85
U
101
e
117
u
6
ACK
22
SYN
38
&
54
6
70
F
86
V
102
f
118
v
7
BEL
23
ETB
39
55
7
71
G
87
W
103
g
119
w
8
BS
24
CAN
40
(
56
8
72
H
88
X
104
h
120
x
9
HT
25
EM
41
)
57
9
73
I
89
Y
105
i
121
y
10
LF
26
SUB
42
*
58
:
74
J
90
Z
106
j
122
z
11
VT
27
ESC
43
+
59
;
75
K
91
[
107
k
123
{
12
FF
28
FS
44
,
60
<
76
L
92
\
108
l
124
|
13
CR
29
GS
45
-
61
=
77
M
93
]
109
m
125
}
14
SO
30
RS
46
.
62
>
78
N
94
^
110
n
126
~
15
SI
31
US
47
/
63
?
79
O
95
_
111
o
127
DEL
Terminatore: 
NUL → '\0'
Line feed:
LF → '\n'
Horizontal tab: 
HT → '\t'
Carriage return:
CR → '\r'
21

<!-- pagina 22 -->
Da ASCII alle codepages a Unicode
Un po di storia della codiﬁca del testo nei sistemi digitali.
1963: ASCII. 
• Codiﬁca a 7bit, permette di codiﬁcare a malapena gli alfabeti 
Latini. 
• È subito evidente che non è sufﬁciente per codiﬁcare la 
complessità degli alfabeti in uso nel mondo (greco, cirillico, arabo, 
bengalese, tamil, devanagari, …) e ancora meno adatto per i tre 
alfabeti ideograﬁci (CJK - cinese, giapponese, coreano). Mancano 
inoltre molti simboli utili
Φ  Я   غ  ই  ஹ  ऄ        碼  人  법       ∃  ∀  ∊  ∞
22

<!-- pagina 23 -->
Da ASCII alle codepages a Unicode
Anni 70-80: Le Codepages.
• Per non consumare troppo spazio, emerge l’idea di usare i 128 
caratteri aggiuntivi a seconda di un ﬂag di sistema.
• Il sistema può quindi usare un set di caratteri esteso a 8bit, 
detto codepage, ma non più di uno alla volta.
• Un ﬁle di testo può essere interpretato correttamente solo 
sapendo per quale codepage è stato pensato.
• Più di 1400 codepages deﬁnite, molto difﬁcile da gestire.
La più usata in EU/US è la ISO/IEC 
8859-1 (detta Latin-1), che 
aggiunge le lettere accentate.
23

<!-- pagina 24 -->
Da ASCII alle codepages a Unicode
24
1988: Unicode 1.0
• Prima proposta di sistema che codiﬁca caratteri a 16bit e 
non a 8, e che non usa codepages ma standardizza e 
uniﬁca tutti i codici dei caratteri (detti codepoints).
• 16bit sembrano tanti (65˙536 valori), ma in verità sono 
insufﬁcienti - ad esempio solo gli ideogrammi uniﬁcati 
CJK sono 97˙680.
• I primi 256 caratteri sono ASCII + Latin-1
• Usa 16bit per carattere, che è meno 
efﬁciente.

<!-- pagina 25 -->
Codifica con Unicode
25
1996: Unicode 2.0 e successivi.
• Deﬁnisce 149˙813 codepoints a 21bit (max 2˙097˙152), organizzati in 
161 alfabeti. Include tutto il CJK.
• Purtroppo è meno efﬁciente in spazio.
Per ovviare al problema, Unicode separa la deﬁnizione dalla codiﬁca:
• Codiﬁche (encoding) wide-character:
– UCS-16: 16bit per carattere (subset)
– UCS-32: 32bit per carattere (completo ma occupa molto spazio)
• Codiﬁche (encoding) multi-byte:
– UTF-8: dati su 8bit, ogni carattere occupa 
uno spazio variabile da 1 a 6 bytes. 
Efﬁciente ma complesso da gestire.

<!-- pagina 26 -->
Testo in programmazione 1
Il linguaggio C supporta 3 codiﬁche per il testo:
• single-byte: char, va bene per ASCII e Latin-1
• wide: wchar_t
• multi-byte: sempre char ma con interpretazione più 
elaborata per identiﬁcare i caratteri
In Programmazione 1 useremo solo il testo single-byte, per 
semplicità, e non considereremo le altre codiﬁche.
26

<!-- pagina 27 -->
Terminatore della stringa
• Una stringa ha una differenza fondamentale rispetto agli array 
generici: per convenzione è sempre terminata da un valore sentinella, il 
carattere ‘\0’, detto anche terminatore della stringa o NUL.
• Esempio: la stringa di testo “ciao” è un array di 5 elementi di tipo 
char con questi valori:
27
‘c’
‘i’
‘a’
‘o’
‘\0’
• Una stringa modiﬁcabile può essere inizializzata come array:
char txt[] = { 'c', 'i', 'a', 'o', '\0' };
char txt[] = "ciao"; // il compilatore aggiunge il NUL
• Possiamo fare riferimento a un letterale stringa tramite un puntatore:
const char* txt = "ciao"; // il compilatore aggiunge il NUL

<!-- pagina 28 -->
Accesso alle stringhe: array vs puntatori
Dato che una stringa in C è un array di char terminato da '\0', possiamo scandire 
la stessa sequenza di caratteri usando un indice oppure un puntatore:
[1] Come array:
28
1.
char parola[] = "ciao";
2.
3.
for (size_t i = 0; parola[i] != '\0'; i++) {
4.
    printf("%c\n", parola[i]);
5.
}
NOTA: la scansione lineare usa come condizione di terminazione “ripeti 
ﬁno al terminatore della stringa”

<!-- pagina 29 -->
Accesso alle stringhe: array vs puntatori
Dato che una stringa in C è un array di char terminato da '\0', possiamo scandire 
la stessa sequenza di caratteri usando un indice oppure un puntatore:
[2] Come puntatore:
29
Usiamo un puntatore ai caratteri, inizialmente impostato al primo 
carattere della stringa, che scorre per incrementi (p++) un carattere alla 
volta ﬁnchè non viene trovato il terminatore
1.
char parola[] = "ciao";
2.
char* p = parola; // conversione di parola[0] in puntatore
3.
4.
while (*p != '\0') {
5.
    printf("%c\n", *p);
6.
    p++;   // passa al carattere successivo
7.
}

<!-- pagina 30 -->
Lettura “parole” (stringhe) da input
Possiamo leggere una stringa di caratteri (cioè un array di char) usando 
scanf con il formato %s, con queste avvertenze
• %s legge una “parola”, e termina alla prima spazio, tab o newline. Non 
legge frasi con spazi
• Bisogna limitare la lunghezza per evitare buffer overﬂow (%19s se l’array è 
di 20 chars)
30
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    char nome[20];   // spazio per massimo 19 caratteri + '\0'
5.
    printf("Inserisci il tuo nome: ");
6.
    scanf("%19s", nome);  // legge una parola (senza spazi)
7.
    printf("Ciao, %s!\n", nome);
8.
}
•
scanf("%s", nome); non richiede & davanti all’array nome: nella chiamata, 
l'espressione viene automaticamente convertita in un char* che punta a nome[0].

<!-- pagina 31 -->
Lettura stringhe da input
• Per leggere una stringa contenente spazi (es. nome e cognome, frasi, 
titoli, ecc.), possiamo usare scanf con uno speciﬁcatore di formato 
speciale che si chiama maschera di scansione
31
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    char frase[50];
5.
    printf("Inserisci una frase: ");
6.
    scanf(" %49[^\n]", frase);
7.
    printf("Hai scritto: %s\n", frase);
8.
}

<!-- pagina 32 -->
Lettura stringhe da input
• Interpretiamo la maschera " %49[^\n]" in questo modo
32
Parte
Signiﬁcato
" "
ignora eventuali spazi o newline iniziali
%
inizio speciﬁcatore di formato
49
numero massimo di caratteri letti (lascia spazio per '\0')
[^\n]
legge tutti i caratteri ﬁno al newline ('\n' non incluso)
• Se l’utente digita più di 49 caratteri, il resto rimane nel buffer di input
• Per input più complessi o multilinea esiste una funzione alternativa, 
fgets(), che non vedremo

<!-- pagina 33 -->
Errori comuni
Inizializzare dimenticando il terminatore ‘\0’:
1.
char nome[4] = {'A', 'n', 'n', 'a'};   // ERRORE: manca '\0'
2.
printf("%s\n", nome);  // comportamento indefinito
Per inizializzare una stringa come array usare:
3.
char nome[5] = {'A', 'n', 'n', 'a', '\0'};
oppure:
4.
char nome[] = "Anna";  // il compilatore aggiunge '\0'
• In generale in C tutte le operazioni sulle stringhe (printf, scanf, e altre 
che vedremo come strlen) assumono sempre che la stringa sia 
terminata da ‘\0’, e in assenza del terminatore procedono a scorrere la 
stringa fuori dai suoi limiti.
33

<!-- pagina 34 -->
Errori comuni
Tentare di modiﬁcare un letterale stringa, che abbiamo detto essere non 
modiﬁcabile, produce comportamento indeﬁnito.
1.
char* s = "ciao";
2.
s[0] = 'm';    // ERRORE: comportamento indefinito
• Sulle piattaforme di uso comune questa modiﬁca produce un errore runtime.
Se invece inizializziamo un array di char, otteniamo un array distinto e 
modiﬁcabile:
3.
char s[] = "ciao";
4.
s[0] = 'm';         // ok: "miao"
34

<!-- pagina 35 -->
Errori comuni
Uso scorretto di scanf per leggere la stringa
1.
char parola[20];
2.
scanf("%s", &parola);   // ERRORE: & non necessario
Motivo:
• Usato come argomento della funzione, parola viene convertito in un 
char* che punta al primo elemento.
• Passare &parola genera un tipo char (*)[20] → tipo incompatibile
Il modo corretto è
1.
scanf("%s", parola);   // OK, conversione a char*
Inoltre é buona pratica indicare sempre la lunghezza massima dell’array, 
perchè scanf non può saperlo e può scrivere oltre i limiti dell’array se si 
usa solo %s invece che %<length>s
2.
scanf("%19s", parola);   // posso leggere massimo 19 char + ‘\0’
35
