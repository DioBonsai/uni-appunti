# 01B_architettura

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
Storia e principi del 
calcolo automatico
Storia e architettura dei calcolatori dalle 
macchine cablate alla macchina di Von 
Neumann

<!-- pagina 2 -->
Storia del computer
2
Da sinistra: Patsy Simmers contiene una scheda di ENIAC (1945); Gail 
Taylor tenendo una scheda EDVAC (1949); Milly Beck con una scheda 
ORDVAC 1952 e Norma Stec tenendo un BRLESC (1962)

<!-- pagina 3 -->
L’abaco
• É la prima “macchina” di 
calcolo nota dall’antichità
• É uno strumento per tenere 
traccia di quanto già fatto
• La logica e la correttezza 
dell’operazione dipendono 
interamente dall’utente
3

<!-- pagina 4 -->
La Pascalina
•Inventata nel 1642 dal matematico francese Blaise Pascal
•Su ogni ingranaggio sono rappresentate le cifre da 0 a 9
•La macchina funziona come un abaco ma effettua il riporto 
dell’addizione mediante una leva inserita tra due 
ingranaggi successivi
4

<!-- pagina 5 -->
Calcolatori cablati
• Queste prime macchine erano progettate per eseguire un 
insieme limitato di operazioni speciﬁche, tipicamente 
addizione e sottrazione.
• La logica di funzionamento era cablata nell’hardware 
(hardwired).
• Introdurre nuove funzionalità, come confronti o salti 
condizionati, richiedeva modiﬁche o una riprogettazione 
dell’hardware.
• Operazioni più complesse, come moltiplicazione e 
divisione, erano difﬁcili da realizzare direttamente con le 
tecnologie disponibili all’epoca.
5

<!-- pagina 6 -->
Calcolatori programmabili
L’idea decisiva è separare le operazioni che la macchina sa eseguire 
direttamente dalla sequenza con cui devono essere eseguite.
• Individuiamo un insieme base di operazioni elementari, ad esempio 
addizione e confronto, realizzabili direttamente in hardware.
• Combiniamo queste operazioni, anche ripetendole, per realizzare 
operazioni più complesse, come la moltiplicazione.
• L’ordine delle operazioni, il numero di ripetizioni e i relativi 
argomenti possono essere codiﬁcati mediante numeri interi.
• Possiamo quindi descrivere il comportamento della macchina 
mediante dati numerici che speciﬁcano le operazioni da eseguire.
Nasce così l’idea di calcolatore programmabile: la stessa macchina 
può eseguire compiti diversi cambiando la sequenza di istruzioni, senza 
modiﬁcarne l’hardware.
6

<!-- pagina 7 -->
La macchina analitica di Babbage
• Descritta da Charles Babbage intorno 
al 1840, è il primo esempio di 
macchina di calcolo programmabile
• Dati ed istruzioni memorizzati su 
schede perforate bidirezionali
• Linguaggio di programmazione simile 
all’assembly (inclusi salti condizionati)
• Macchina a posteriori turing-completa
7

<!-- pagina 8 -->
Alan Turing
• Matematico inglese, considerato l‘inventore della la teoria 
della calcolabilità (e secondo alcuni, dell’informatica)
• Nel 1936 introduce il concetto di macchina universale: un 
modello astratto di calcolatore 
• É usato da Turing al ﬁne di analizzare l’insieme delle 
funzioni che possono essere calcolate in modo 
automatico
• Diversi tentativi di costruire un calcolatore 
Turing-completo si scontrano con i limiti tecnologici 
dell’epoca
8

<!-- pagina 9 -->
Electronic Numerical Integrator and Computer (ENIAC)
9
• Progettato nel 1943 da John Mauchly 
e John Adam Presper 
• Primo computer general purpose
• Rappresentazione decimale dei numeri
• Le operazioni erano realizzate da 
diversi blocchi funzionali
• Per programmare la macchina occorreva conﬁgurare 
interruttori e collegare i blocchi mediante cavi
• Cambiare programma richiedeva quindi una riconﬁgurazione 
manuale complessa

<!-- pagina 10 -->
Electronic Discrete Variable Automatic Calculator (EDVAC)
10
https://it.wikipedia.org/wiki/EDVAC
• Progettato nel 1944 da John Mauchly e John 
Adam Presper, già sviluppatori dell’ENIAC
• Introduce alcune idee fondamentali rispetto 
all’ENIAC:
a. programma memorizzato nella memoria 
centrale
b. memoria uniﬁcata per istruzioni e dati
c. rappresentazione binaria dei numeri
• Il programma non deve più essere realizzato 
riconﬁgurando ﬁsicamente i collegamenti 
della macchina, ma può essere memorizzato 
e modiﬁcato come dato

<!-- pagina 11 -->
La rappresentazione binaria dei dati
• Binary Information Token, è l’elemento base 
dell’informazione
– Acceso/spento,  vero/falso,  sì/no, 1/0, etc.
• Può essere realizzato tramite vari dispositivi hardware 
(relais, valvole, transistors, ...)
• Da qui la sua adozione nei calcolatori moderni rispetto 
alla rappresentazione decimale usata dai primi calcolatori 
ﬁno all’ENIAC
11

<!-- pagina 12 -->
Il bit
Combinando più bit [b] si rappresentano più informazioni
• Con 1 bit si rappresentano 2 informazioni (21)
• Con 2 bit si rappresentano 4 informazioni (22)
• Con 3 bit si rappresentano 8 informazioni (23)
• Con 4 bit si rappresentano 16 informazioni (24)
• . . .
• Con 8 bit si rappresentano 256 informazioni (28) -> byte [B]
• . . .
• Con N bit si rappresentano 2N informazioni
12

<!-- pagina 13 -->
Il design dell’EDVAC
13
CPU
CPU
Unità di
controllo
ALU
Registri
R0
R1
IR
PC
SP
SR
Memoria
principale
(RAM)
Storage
secondario
(hard disk)
Bus di sistema
•
Una memoria primaria pari a 1024 parole di 44 
bit (circa 5.5 KB) 
•
Uno storage secondario a nastro magnetico per 
la lettura/scrittura
•
Una Central Processing Unit (CPU) composta a 
sua volta da
–
Una unità di controllo che pilota i 
componenti della CPU ed il bus di sistema
–
Una Algebraic Logic Unit (ALU) che esegue 
operazioni aritmetiche logiche sui registri
–
I registri che possono contenere dati utente o 
di stato e controllo della macchina
•
Tutti connessi dal bus di sistema

<!-- pagina 14 -->
L’architettura di Von Neumann
14
●Matematico, consulente del progetto 
EDVAC
●Descrisse e pubblicò per primo 
l’architettura EDVAC nel 1945
●Da qui il termine usato ancora oggi
«Architettura di Von Neumann», ma 
sarebbe più corretto «Architettura 
EDVAC»

<!-- pagina 15 -->
L’architettura di Von Neumann
15
• Dati ed istruzioni memorizzati nella 
stessa memoria principale (RAM)
• Una CPU esegue operazioni sui dati in 
memoria e salva il risultato in memoria
• CPU, memoria primaria e storage 
secondario sono connessi tramite un bus 
di sistema
• La macchina modiﬁca l’area dati della 
memoria seguendo le istruzioni del 
programma e secondo i dati di input
CPU
CPU
Unità di
controllo
ALU
Registri
R0
R1
IR
PC
SP
SR
Memoria
principale
(RAM)
Storage
secondario
(hard disk)
Bus di sistema

<!-- pagina 16 -->
Un primo modello di memoria
16
●La memoria è vista dalla CPU come una sequenza di byte.
●Ogni byte può contenere un piccolo valore numerico.
●Per poter accedere ai singoli byte, ciascuno è identiﬁcato da un 
indirizzo.
●Il byte è l’unità base di indirizzamento della memoria.
○Esempio: 256 byte per il programma e 768 byte per i dati → 1024 
byte complessivi, con indirizzi da 0 a 1023
7
byte 0
12 …
byte 255
byte 256
byte 1023
programma
dati
valori

<!-- pagina 17 -->
Un primo modello della memoria
• Un singolo byte non basta, nella maggior 
parte dei casi, per rappresentare numeri di 
uso comune nei calcoli.
• Per questo la memoria viene organizzata in 
parole (words) di 16, 32 o 64 bit, a seconda 
dell’architettura.
• Questa scelta è motivata da ragioni di 
efﬁcienza: elaborare parole è più veloce e 
naturale per il processore invece che lavorare 
1 byte alla volta.
• Nell’esempio consideriamo parole da 32 bit, e 
le rappresentiamo graﬁcamente
17
programma
64 words
byte 0
byte 256
byte 255
byte 1023
dati
192 words
32 bit
(word size)

<!-- pagina 18 -->
L’architettura Von Neumann - funzionamento 
18
• Un programma di controllo (monitor, oggi sistema operativo) carica 
programma e dati dalla memoria secondaria nella memoria principale, 
in opportune posizioni identiﬁcate da indirizzi.
• La CPU esegue quindi, una dopo l’altra, le istruzioni macchina del 
programma. Ogni istruzione può leggere o modiﬁcare dati e quindi 
trasformare progressivamente lo stato della macchina.
• Al termine dell’esecuzione, il risultato del programma è rappresentato 
nello stato ﬁnale della memoria (ad esempio, in una posizione di 
memoria nota).
• Fissati programma e stato iniziale, l’esecuzione produce sempre lo 
stesso stato ﬁnale: il comportamento della macchina è deterministico.

<!-- pagina 19 -->
CPU
CPU
Unità di
controllo
ALU
Registri
R0
R1
IR
PC
SP
SR
Funzionamento di una CPU
19
• La control unit preleva dalla memoria e decodiﬁca una 
istruzione alla volta
• A seconda dell’istruzione, attiva le opportune componenti 
della ALU per svolgere le operazioni elementari
• La ALU esegue semplici operazioni fra i registri della CPU 
(addizioni, confronti)
• Tra i registri vi è il program counter (PC), che memorizza 
l’indirizzo della prossima istruzione.
Il PC viene viene normalmente incrementato per puntare 
all’istruzione successiva, oppure modiﬁcato per gestire i 
salti condizionati e non
• Un altro registro importante è l’instruction register (IR): 
contiene l’istruzione attualmente in esecuzione, appena 
caricata dalla memoria.
Memoria
principale
(RAM)
