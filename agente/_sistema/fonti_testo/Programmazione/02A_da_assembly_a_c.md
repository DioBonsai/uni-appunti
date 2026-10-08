# 02A_da_assembly_a_c

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
Dal linguaggio macchina al 
C
Dai bit e registri alla programmazione 
strutturata di alto livello e portabile

<!-- pagina 2 -->
Dal codice macchina al linguaggio assembly
• I primi computer erano 
programmati direttamente in 
linguaggio macchina 
manipolando i bit dei registri 
tramite interruttori o schede 
perforate
• Simile all’esecuzione 
step-by-step utilizzata oggi 
per il debug dell’hardware in 
fase di progetto
2

<!-- pagina 3 -->
Vocabolario: linguaggio macchina e assembly
Il linguaggio macchina è il linguaggio direttamente eseguibile 
dal processore:
•
è costituito da codici numerici, rappresentati come sequenze 
di bit, che identiﬁcano istruzioni e operandi;
•
ogni architettura deﬁnisce il proprio insieme di istruzioni 
macchina (instruction set);
•
dipende quindi dal processore e non è portabile tra 
architetture diverse.
3
Il linguaggio assembly è una rappresentazione testuale e 
simbolica del linguaggio macchina:
•
usa mnemonici come mov, add, ldr al posto dei codici 
numerici delle istruzioni;
•
viene tradotto in linguaggio macchina da un programma 
chiamato assembler;
•
è più leggibile per il programmatore, ma rimane 
strettamente legato all’architettura hardware.

<!-- pagina 4 -->
Dal codice macchina al linguaggio assembly
4
●Un software chiamato assembler ha il compito di tradurre 
(compilare) ogni istruzione di assembly in istruzione 
macchina
Assembler
Sorgente assembly
Codice macchina
ADDR   A = 400
ADDR   B = 404
LOAD,  R0, @A
LOAD,  R1, @B
ADD,   R0, R1
STORE, R0, @A
0010000110010000
0010010110010010
0100000100000000
0011000100000000

<!-- pagina 5 -->
Esempio: addizionare tra interi
5
Vediamo un esempio con il linguaggio assembly.
Sommiamo due numeri interi in memoria, rispettivamente agli indirizzi 
A=400 e B=404, e mettiamo il risultato nella cella di memoria 
nell’indirizzo A
Il programma in linguaggio assembly (tipo RISC come MIPS32) avrà 
questa forma:
1. Deﬁnisce gli indirizzi A e B
2. Carica i numeri interi agli indirizzi A e B nei registri R0 ed R1 della CPU 
con due istruzioni LOAD
3. Esegue l’addizione tra i registri R0 ed R1 con una istruzione ADD
4. Copia il risultato dal registro R0 all’indirizzo A in memoria con una 
istruzione STORE

<!-- pagina 6 -->
Esempio: addizione tra interi
6
LOAD, R0, @A
LOAD, R1, @B
ADD, R0, R1
STORE, R0, @A
001000000...0110010000
001000010...0110010010
010000000...0100000000
001100000...0100000000
Operazione
Sorgente assembly
Linguaggio macchina (bits)
ADDR A = 400
ADDR B = 404
Deﬁnisce i due
indirizzi A e B
Carica numero 
all’indirizzo A in R0
Carica numero 
all’indirizzo B in R1
Addiziona R0 ed R1, 
risultato in R0
Copia risultato da
R0 ad indirizzo A

<!-- pagina 7 -->
Esempio: addizione tra interi
7
0010000110010000
-8
12
byte 404
byte 400
byte 256
programma
dati
PC
byte 1020
0010010110010010
0100000100000000
0011000100000000
carica la prossima istruzione 
leggendo il program counter (PC) 
nell’instruction register (IR), per 
poterla eseguire.
1. ▶LOAD, 
R0, @A
2.
LOAD, 
R1, @B
3.
ADD, 
R0, R1
4.
STORE, R0, @A
Memoria
principale
(RAM)
Unità di
controllo
ALU
Registri
R0
-
R1
-
IR
LOAD
PC
0
SP
-
SR
-

<!-- pagina 8 -->
Esempio: addizione tra interi
8
0010000110010000
-8
12
byte 404
byte 400
byte 256
programma
dati
PC
byte 1020
0010010110010010
0100000100000000
0011000100000000
decodiﬁca IR ed esegue 
l’istruzione elementare.
1. ▶LOAD, 
R0, @A
2.
LOAD, 
R1, @B
3.
ADD, 
R0, R1
4.
STORE, R0, @A
Memoria
principale
(RAM)
Unità di
controllo
ALU
Registri
R0
12
R1
-
IR
LOAD
PC
0
SP
-
SR
-

<!-- pagina 9 -->
Esempio: addizione tra interi
9
0010000110010000
-8
12
byte 404
byte 400
byte 256
programma
dati
PC
byte 1020
0010010110010010
0100000100000000
0011000100000000
1.
LOAD, 
R0, @A
2. ▶LOAD, 
R1, @B
3.
ADD, 
R0, R1
4.
STORE, R0, @A
Memoria
principale
(RAM)
Unità di
controllo
ALU
Registri
R0
12
R1
-
IR
LOAD
PC
4
SP
-
SR
-

<!-- pagina 10 -->
Esempio: addizione tra interi
10
0010000110010000
-8
12
byte 404
byte 400
byte 256
programma
dati
PC
byte 1020
0010010110010010
0100000100000000
0011000100000000
1.
LOAD, 
R0, @A
2. ▶LOAD, 
R1, @B
3.
ADD, 
R0, R1
4.
STORE, R0, @A
Memoria
principale
(RAM)
Unità di
controllo
ALU
Registri
R0
12
R1
-8
IR
LOAD
PC
4
SP
-
SR
-

<!-- pagina 11 -->
Esempio: addizione tra interi
11
0010000110010000
-8
12
byte 404
byte 400
byte 256
programma
dati
PC
byte 1020
0010010110010010
0100000100000000
0011000100000000
1.
LOAD, 
R0, @A
2.
LOAD, 
R1, @B
3. ▶ADD, 
R0, R1
4.
STORE, R0, @A
Memoria
principale
(RAM)
Unità di
controllo
ALU
Registri
R0
12
R1
-8
IR
ADD
PC
8
SP
-
SR
-

<!-- pagina 12 -->
Esempio: addizione tra interi
12
0010000110010000
-8
12
byte 404
byte 400
byte 256
programma
dati
PC
byte 1020
0010010110010010
0100000100000000
0011000100000000
1.
LOAD, 
R0, @A
2.
LOAD, 
R1, @B
3. ▶ADD, 
R0, R1
4.
STORE, R0, @A
Memoria
principale
(RAM)
Unità di
controllo
ALU
Registri
R0
12 4
R1
-8
IR
ADD
PC
8
SP
-
SR
-
R0 = R0 + R1

<!-- pagina 13 -->
Esempio: addizione tra interi
13
0010000110010000
-8
12
byte 404
byte 400
byte 256
programma
dati
PC
byte 1020
0010010110010010
0100000100000000
0011000100000000
1.
LOAD, 
R0, @A
2.
LOAD, 
R1, @B
3.
ADD, 
R0, R1
4. ▶STORE, R0, @A
Memoria
principale
(RAM)
Unità di
controllo
ALU
Registri
R0
4
R1
-8
IR
STORE
PC
12
SP
-
SR
-

<!-- pagina 14 -->
Esempio: addizione tra interi
0010000110010000
-8
12  4
byte 404
byte 400
byte 256
programma
dati
PC
byte 1020
0010010110010010
0100000100000000
0011000100000000
1.
LOAD, 
R0, @A
2.
LOAD, 
R1, @B
3.
ADD, 
R0, R1
4. ▶STORE, R0, @A
Memoria
principale
(RAM)
Unità di
controllo
ALU
Registri
R0
4
R1
-8
IR
STORE
PC
12
SP
-
SR
-

<!-- pagina 15 -->
Esempio: moltiplicazione tra interi
15
Rivediamo l’esempio della moltiplicazione tramite somme 
ripetute, per questo linguaggio assembly.
●Moltiplichiamo due numeri interi che si trovano agli indirizzi 
simbolici m ed n, ed il risultato viene memorizzato 
all'indirizzo m al termine del programma
●Usiamo il linguaggio assembly per questo algoritmo di 
moltiplicazione, usando anche l’accumulatore s e il contatore 
delle ripetizioni i come visto in precedenza.

<!-- pagina 16 -->
Esempio: moltiplicazione tra interi
16
1.
LOAD, 
R0, 0
// inizializza R0 come accumulatore s
2.
LOAD, 
R1, 0
// inizializza R1 come contatore i
3.
LOAD, 
R2, @m 
// carica valore indirizzo m in R2
4.
LOAD, 
R3, @n
// carica valore indirizzo n in R3
5.
CMP 
R1, R3
// confronta R1 ed R3, ovvero i ed n
6.
JMPEQ <riga 10>
// Se i=n salta alla riga 10, altrimenti continua
7.
ADD, 
R0, R2
// R0 ← R0 + R2, ovvero s ← s + m
8.
INC, 
R1
// R1 ← R1 + 1, ovvero i ← i + 1
9.
JMP 
<riga 5>
// salto incondizionato a riga 5 
10.
STORE, R0, @m
// salva R0, ovvero il risultato, s all’indirizzo di m

<!-- pagina 17 -->
Verso i linguaggi di alto livello
17
• Programmare in assembly è faticoso ed è facile fare errori
– 4 righe codice per addizione, 10 righe per moltiplicazione
– Richiede la conoscenza dell’architettura della CPU
– Non è evidente la struttura del codice, né la logica
• Il codice scritto per una CPU X deve essere riscritto da capo per 
funzionare sulla CPU Y se usano linguaggi macchina differenti
• Per queste ragioni, a partire dagli anni ‘50 si è incominciato a 
sviluppare linguaggi di programmazione con istruzioni dal 
livello semantico più vicino al linguaggio matematico e 
naturale, e che permettessero di astrarre il programma dalle 
caratteristiche dell’hardware

<!-- pagina 18 -->
Il linguaggio FORTRAN
18
• All’inizio degli anni ‘50 IBM progetta il 
calcolatore modello 704 per calcoli 
scientiﬁci con i requisiti seguenti:
– Gli scienziati devono potersi focalizzare 
sulla programmazione di formule, 
ignorando i dettagli della CPU
– I programmi devono poter essere 
facilmente trasportati su futuri modelli 
IBM senza riscrivere il programma da 
capo

<!-- pagina 19 -->
Il linguaggio FORTRAN
19
• Per IBM 704 viene sviluppato il linguaggio FORmula TRANslator 
per superare i limiti dell’assembly
• Un compilatore traduce ogni istruzione FORTRAN in una o più 
istruzioni assembly speciﬁche per la macchina utilizzata
• Se cambia la macchina utilizzata, è sufﬁciente ricompilare il 
programma per l’hardware relativo
• Insieme a LISP, ALGOL, COBOL rappresentano i capostipiti dei 
«linguaggi di terza generazione», famiglia a cui appartiene il 
linguaggio C originario che è oggetto di questo insegnamento
• Versioni moderne di FORTRAN offrono costrutti if, while, etc. 
(FORTRAN 90)

<!-- pagina 20 -->
Moltiplicazione tra interi in FORTRAN
20
https://www.onlinegdb.com/online_fortran_compiler

<!-- pagina 21 -->
I linguaggi di alto livello
21

<!-- pagina 22 -->
Punti rilevanti
22
• Abbiamo sviluppato un semplice algoritmo per la 
moltiplicazione tra interi come somma ripetuta
• E’ possibile programmare una macchina a basso livello 
(assembly) ma la scrittura di programmi è lunga e difﬁcile
• Come vedremo, i linguaggi di alto livello come il 
linguaggio C nascondono molti dei dettagli speciﬁci 
dell’hardware sottostante

<!-- pagina 23 -->
Introduzione al linguaggio C
Storia, princìpi di base
23

<!-- pagina 24 -->
Il linguaggio C
24
• 1969: Ken Thompson (Bell Labs, AT&T) sviluppa 
Unix per il minicomputer PDP-7, inizialmente 
scritto in linguaggio assembly.
• L’esperienza dimostra che l’assembly rende lo 
sviluppo di un sistema operativo oneroso e poco 
ﬂessibile.
• Per superare questi limiti, Dennis Ritchie progetta 
il linguaggio C, concepito per unire efﬁcienza e 
portabilità.
• Unix viene progressivamente riscritto in C, 
aprendo la strada alla sua diffusione (a partire 
dalle università) e inﬂuenzando in modo 
determinante la storia dell’informatica moderna.

<!-- pagina 25 -->
Il linguaggio C
25
• 1972: Prima versione del C, inizialmente 
sviluppata per uso interno sui computer 
PDP-7 e PDP-11 e oggi nota come K&R C
• Verso la ﬁne degli anni ‘80 è 
standardizzato da ANSI e ISO per uso su 
una varietà di hardware differente 
(ANSI-C, C89)
• Lo standard ha subito numerose numerosi 
aggiornamenti (C99, C11, C17, C23, etc.)
• Il libro di testo fa riferimento a C11

<!-- pagina 26 -->
Il linguaggio C
• Nonostante la sua età, il C é un linguaggio centrale 
dell’informatica
• È il linguaggio di riferimento per lo sviluppo di sistemi 
operativi, compilatori, driver, librerie di basso livello e 
applicazioni ad alte prestazioni, sistemi embedded/IoT. 
• Offre un controllo diretto sull’hardware e sulla memoria 
mantenendo al tempo stesso un livello di astrazione molto 
superiore all’assembly
26

<!-- pagina 27 -->
Caratteristiche del linguaggio C
Il C è un linguaggio di programmazione:
• compilato: un compilatore traduce i sorgenti C 
nel linguaggio macchina del computer
• imperativo: il programma è un insieme di 
istruzioni pensate come ordini per il compilatore
• strutturato: il codice sorgente è strutturato in 
blocchi, racchiusi da delimitatori
• fortemente tipizzato: il programmatore deve 
speciﬁcare il tipo di ogni variabile
27

<!-- pagina 28 -->
Radiografia di un semplice programma C
1.
// Un primo programma in C
2.
#include <stdio.h>
3.
4.
// La funzione "main" e' il punto di ingresso del programma
5.
int main(void) {
6.
    printf("Buongiorno dal C.\n");
7.
}
8.
// fine della funzione main
28
Le linee che iniziano con ‘//’ non sono 
istruzioni ma sono commenti, e sono 
ignorati dal compilatore
Le linee che iniziano con ‘#’ sono 
direttive per il preprocessore
I blocchi strutturati del codice sono delimitati dalle 
parentesi graffe { e }, e contengono:
●
dichiarazione di variabili
●
operazioni (es: stampa in output)

<!-- pagina 29 -->
Direttiva di inclusione
• Le righe che iniziano con il carattere ‘#’ sono direttive per il preprocessore 
(argomento che vedremo limitatamente e sarà trattato in Programmazione II)
• La direttiva 
#include <stdio.h>
include un ﬁle che si chiama stdio.h (standard input/output header) nel 
nostro programma, e ne importa deﬁnizioni e contenuti.
• I ﬁles ‘.h’ sono detti “di intestazione” (header) e contengono dichiarazioni di 
funzioni, ad es. fornite in librerie di sistema (printf() in libc.so) 
• L’header ﬁle stdio.h dichiara funzioni come printf() e scanf()
• I nostri esempi useranno spesso vari header (talvolta li omettiamo se é ovvio, 
solo per ragioni di spazio nelle slide)
29

<!-- pagina 30 -->
Radiografia di un semplice programma C
1.
// Un primo programma in C
2.
#include <stdio.h>
3.
4.
// La funzione "main" e' il punto di ingresso del programma
5.
int main(void) {
6.
    printf("Buongiorno dal C.\n");
7.
}
8.
// fine della funzione main
30
La funzione main è il punto da cui 
comincia l’esecuzione del programma
La funzione main riceve 
un input vuoto (void)
La funzione main ha un output di tipo intero 
(int). Il compilatore ci consente di ometterlo, ma 
potremmo scriverlo esplicitamente:
    return 0;

<!-- pagina 31 -->
Funzioni
• I programmi nel linguaggio C sono organizzati in moduli 
detti funzioni, che contengono le istruzioni da eseguire
• La funzione main è obbligatoria ed é il punto da cui 
comincia l’esecuzione del programma
• Le funzioni deﬁniscono un input ed un output
• La funzione main “ritorna” in output un numeri intero che 
rappresenta un codice di successo/errore al sistema 
operativo (non lo useremo)
• Per il momento scriveremo tutto il codice dentro il main
31

<!-- pagina 32 -->
Radiografia di un semplice programma C
1.
// Un primo programma in C
2.
#include <stdio.h>
3.
4.
// La funzione "main" e' il punto di ingresso del programma
5.
int main(void) {
6.
    printf("Buongiorno dal C.\n");
7.
}
8.
// fine della funzione main
32
Un commento che precede una funzione o delle 
istruzioni serve a chiarirne lo scopo. 
Infatti il codice deve essere leggibile e comprensibile 
per un programmatore, non solo per il compilatore!
Per convenzione il codice C viene 
indentato tramite tabulazioni 
(il carattere tab sulla tastiera).
Le parentesi graffe delimitano il corpo (body) 
della funzione. Le parentesi strutturano 
l’annidamento dei blocchi e devono essere 
sempre bilanciate.

<!-- pagina 33 -->
Programmazione strutturata
• Il codice della funzione main() (e di ogni altra funzione) deve 
essere racchiuso tra parentesi graffe { }. 
Queste delimitano un blocco di istruzioni (o blocco di codice).
• Un blocco di codice è un’unità logica: può contenere
– dichiarazioni di dati (dette variabili), 
– comandi 
– chiamate di altre funzioni 
– altri blocchi (annidamento dei blocchi), sempre delimitati dalle 
parentesi graffe.
33

<!-- pagina 34 -->
Programmare per la chiarezza
"Il codice è letto molto più spesso di quanto venga scritto: programmate per 
la chiarezza, non per la brevità." - Donald W. Knuth
●Per mantenere il codice chiaro è fondamentale:
○
utilizzare una corretta indentazione, che evidenzi la struttura logica 
(procederemo per esempi per capire come fare e cosa signiﬁca)
○
aggiungere commenti signiﬁcativi, soprattutto per funzioni e sezioni complesse
○
scegliere nomi descrittivi per variabili e funzioni, così da rendere il codice 
autoesplicativo
○
evitare blocchi troppo lunghi, preferendo la scomposizione in funzioni più 
piccole e riutilizzabili (vedremo più avanti nel corso come si fa)
Imparare a scrivere codice chiaro e leggibile signiﬁca risparmiare tempo 
e problemi.
34

<!-- pagina 35 -->
Radiografia di un semplice programma C
1.
// Un primo programma in C
2.
#include <stdio.h>
3.
4.
// La funzione "main" e' il punto di ingresso del programma
5.
int main(void) {
6.
    printf("Buongiorno dal C.\n");
7.
}
8.
// fine della funzione main
35
Una funzione (printf) viene “chiamata” 
(function call) passandogli i parametri di input.
Ogni istruzione (statement) termina con il 
punto e virgola “;”
Una stringa è un frammento di testo 
delimitato dai doppi apici (").
Nelle stringhe (testo tra doppi apici "") 
possono comparire dei caratteri speciali 
dette sequenze speciali (escape 
sequence), che sono precedute dalla 
barra rovesciata ‘\’ (backslash).

<!-- pagina 36 -->
La funzione printf
• Utilizzata per stampare output testuale sul terminale.
• Per ora la useremo solo con stringhe di testo racchiuse tra 
doppi apici " ".
• Esempio:
printf("Buongiorno dal C.\n");
• Le sequenze speciali (escape sequence, spesso tradotte come 
sequenze “di escape”) permettono di rappresentare caratteri 
speciali all’interno delle stringhe:
– \n → nuova riga (va a capo nella stampa a video)
– \\ → stampa il carattere backslash \
– \t → carattere di tabulazione (TAB)
– \" → stampa il doppio apice "
– \0 → terminatore della stringa (lo useremo più avanti)
36

<!-- pagina 37 -->
Dal codice al programma eseguibile
• Il linguaggio C deve essere compilato: il codice sorgente in formato 
testuale viene tradotto in linguaggio macchina, comprensibile dal 
computer
• Durante la compilazione, l’analizzatore lessicale  (parser) suddivide il 
codice in token, cioè unità sintattiche (parole chiave, identiﬁcatori, 
operatori, simboli di punteggiatura, stringhe, costanti, ecc.)
• Come in una lingua naturale, anche i linguaggi di programmazione 
hanno una sintassi, più formale, che deﬁnisce le regole per costruire 
programmi corretti
• Se le regole sintattiche non vengono rispettate, il compilatore segnala 
un errore di compilazione e non completa la compilazione.
37

<!-- pagina 38 -->
Sintassi del C
• Ogni istruzione deve terminare con il carattere ;
Errore tipico: dimenticare il ;  errore di compilazione (“expected ‘;’ before …”)
38
1.
printf("Ciao")   // ERRORE: manca il ;
2.
printf("Ciao");  // CORRETTO
3.
int area = base * altezza;  // CORRETTO
• Le istruzioni possono occupare più righe, per leggibilità
1.
printf("Questo è un messaggio "
2.
       "spezzato su più righe\n");
È possibile andare a capo ovunque sia consentito uno spazio 
(tranne dentro le stringhe). 
Errore tipico: andare a capo dentro una stringa senza chiuderla → errore di 
compilazione (“missing terminating " character”).

<!-- pagina 39 -->
Identificatori
• Gli identiﬁcatori servono a dare un nome agli elementi (variabili, 
funzioni, costanti, tipi, …) di un programma, così da poterli 
riconoscere e usare. 
• Negli identiﬁcatori, maiuscole e minuscole fanno differenza 
(case-sensitive): Var, var e VAR sono identiﬁcatori diversi.
• Gli identiﬁcatori devono essere scelti per leggibilità e chiarezza: 
evitare nomi troppo simili (genera confusione ed errori) o non 
signiﬁcativi.
• Esempi di identiﬁcatori per variabili:   somma, accumulatore
39

<!-- pagina 40 -->
Identificatori
• Non si possono usare nomi che corrispondono alle 
keywords del linguaggio:
auto, break, case, char, const, continue, default, do, double, 
else, enum, extern, ﬂoat, for, goto, if, int, long, register, return, 
short, signed, sizeof, static, struct, switch, typedef, union, 
unsigned, void, volatile, while
• Non si possono usare i nomi delle funzioni della libreria 
standard come main, printf (anche se non viene usata, es. 
sin, cos) né i nomi dei simboli deﬁniti nei ﬁle di 
intestazione associati alle librerie standard
40

<!-- pagina 41 -->
Indentazione del codice
• Le istruzioni di un blocco (NON le eventuali parentesi graffe) 
si scrivono tutte “indentate” (rientrate) di un numero ﬁsso di 
spazi (es. 4), o meglio del carattere speciale <tab>
• L’indentazione aiuta il programmatore a comprendere meglio 
il ﬂusso del programma, per cui va fatta mentre si 
programma e non dopo
41
1.
if (a > 15) {
2.
    x = 5;
3.
    y = 2;
4.
    z = a + b;
5.
}

<!-- pagina 42 -->
Come funziona la compilazione con il C
42
File di intestazione
deﬁnizioni comuni
File sorgente
codice del programma 
in forma testuale
Sono le unità di compilazione
File oggetto
unità di compilazione in 
linguaggio macchina
programma 
eseguibile
compilato in linguaggio 
macchina
#include
preprocessore +
compilatore + 
assemblatore
collegatore 
(linker)

<!-- pagina 43 -->
Il compilatore gcc
43
https://en.wikipedia.org/wiki/GNU_Compiler_Collection
• Il compilatore che useremo è lo GNU C Compiler (GCC) 
– free, standard-compliant 
– disponibile per i maggiori sistemi operativi
– compila per molteplici linguaggi macchina
• gcc è un frontend per un sistema di compilazione multi-stadio.

<!-- pagina 44 -->
Gli stadi della compilazione
1.
Il preprocessore (cpp) elabora le direttive #include, #deﬁne, ... del 
sorgente C producendo sorgente intermedio.
2.
Il compilatore (cc) traduce il sorgente C in assembly, con varie opzioni
1.
ottimizzazione della velocità di esecuzione o dimensione dell’eseguibile
2.
senza ottimizzazione (per il debug, opzione -g)
3.
L’assemblatore (as) produce un ﬁle oggetto .o in linguaggio macchina
4.
Il linker (ld) unisce i moduli in linguaggio macchina in un eseguibile
1.
i ﬁle oggetto corrispondenti a sorgenti C
2.
altri ﬁle oggetto (anche compilati da sorgenti scritti in altri linguaggi)
3.
le librerie (I/O, matematiche, network, ecc.)
44

<!-- pagina 45 -->
Compilazione ed esecuzione
Per il momento compiliamo con:
45
Unix:  
  gcc -Wall -Werror sorgente.c -o eseguibile
Windows:  gcc -Wall -Werror sorgente.c -o eseguibile.exe
Una volta che 
abbiamo il nostro 
programma 
compilato come 
eseguibile, lo 
possiamo eseguire:
C:\Users\Elvio> buongiorno
Buongiorno!
C:\Users\Elvio>
        Prompt dei comandi (Windows)
elvio@linux:\home\elvio$ ./buongiorno
Buongiorno!
elvio@linux:\home\elvio$ 
      Shell dei comandi (Unix)

<!-- pagina 46 -->
Errori di compilazione ed errori a runtime
• Un programma può compilare senza errori sintattici, ma contenere 
comunque errori che emergono solo durante l’esecuzione (runtime).
• Gli errori possono avere molte cause:
– una progettazione errata dell’algoritmo
esempio: eseguire un ciclo prima di veriﬁcarne la condizione di 
terminazione
– una realizzazione errata del programma
esempio: divisione per zero, accesso non valido alla memoria
• È quindi importante distinguere:
– Errori di compilazione: sintassi del linguaggio non rispettata, rilevati 
subito dal compilatore.
– Errori a runtime: emergono durante l’esecuzione, dovuti a logica o 
implementazione scorretta.
– Errori logici: il programma viene eseguito, ma non realizza correttamente 
il comportamento desiderato.
46

<!-- pagina 47 -->
Errori di compilazione
Vediamo un esempio di errore di sintassi.
• Manca il punto e virgola di terminazione statement
• Il compilatore ritorna un errore di compilazione alla linea 4
47
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    printf("Buongiorno dal C.\n")
5.
}

<!-- pagina 48 -->
Errori runtime
Vediamo un esempio di errore a runtime.
• Il programma compila senza errori
• Eseguire una divisione per 0 causa un errore a runtime
48
1.
#include <stdio.h>
2.
int main(void) {
3.
    int x = 5;
4.
    int y = 0;
5.
    printf("5/2 uguale a %d\n", x/y);
6.
}
attilio@debian:~$ gcc bug_2.c -o bug2
attilio@debian:~$ ./bug2 
Eccezione in virgola mobile

<!-- pagina 49 -->
Come sviluppare il codice C
• Scrivere/modiﬁcare un sorgente con editor di testo 
esempio di editor: Notepad++
• Salvare il ﬁle sorgente in una directory con estensione .c
• Compilare il ﬁle sorgente con gcc
• Analizzare e correggere eventuali errori di sintassi
Importante: leggete con attenzione cosa dice il compilatore
• Eseguire il ﬁle compilato
• Veriﬁcare se si comporta in modo corretto (test)
• Se ci sono problemi, modiﬁcare il codice e ripetere.
49

<!-- pagina 50 -->
Prerequisiti per lo sviluppo in C
• È richiesta una dimestichezza di base con il PC, in 
particolare:
– scrittura e gestione di ﬁle di testo
– navigazione del ﬁlesystem
– utilizzo essenziale della linea di comando (shell)
• Se lavorate sul vostro PC, dovrete installare un ambiente di 
sviluppo che includa il compilatore gcc 
(ce ne occuperemo nelle lezioni di laboratorio)
• In alternativa, per iniziare rapidamente senza installazioni, 
si può utilizzare un ambiente online:
https://pythontutor.com/c.html#mode=edit 
50
