## Algoritmo
D: Che cos'è un algoritmo e quali requisiti deve avere?
R: Un insieme ordinato di operazioni non ambigue e computabili che, dato un input, produce un output e termina in tempo finito. Requisiti: correttezza (output esatto per ogni input ammissibile) e terminazione.

## Informatica
D: Che cosa studia l'informatica secondo Dijkstra?
R: Gli algoritmi, non i dispositivi: "L'informatica non è la scienza dei calcolatori più di quanto l'astronomia sia la scienza dei telescopi".

## Programmazione imperativa
D: Cosa significa programmare in modo imperativo e cosa indica "variabile"?
R: Descrivere una sequenza ordinata di istruzioni che modificano lo stato della memoria. In informatica una variabile è una cella di memoria il cui valore cambia tramite assegnamento. Wirth: Programma = Algoritmi + Strutture dati.

## Algoritmo di moltiplicazione
D: Come si calcola m·n con sole somme e qual è l'errore da evitare per n = 0?
R: Un accumulatore s (a 0) e un contatore i (a 0): si somma m a s finché i ≠ n. Bisogna controllare la condizione PRIMA di eseguire la somma, altrimenti per n = 0 si va in un ciclo infinito.

## Programmazione strutturata
D: Quali sono i tre pilastri della programmazione strutturata?
R: Sequenza, selezione (scelta condizionata), iterazione (ripetizione condizionata): ogni algoritmo calcolabile si esprime con queste strutture, con blocchi annidati e indentazione invece di salti.

## Von Neumann
D: Quali sono le tre intuizioni del modello di Von Neumann?
R: Programma memorizzato, memoria unificata per istruzioni e dati, rappresentazione binaria di tutto. Componenti: RAM, CPU (unità di controllo, ALU, registri), bus, storage secondario.

## CPU
D: Cosa fanno Program Counter, Instruction Register, ALU e unità di controllo?
R: - PC: indirizzo della prossima istruzione.
- IR: istruzione in esecuzione.
- ALU (Arithmetic Logic Unit): operazioni aritmetiche e logiche sui registri.
- Unità di controllo: legge, decodifica e coordina.

## Ciclo di esecuzione
D: Descrivi il ciclo fetch-decode-execute.
R: Fetch: si legge in RAM l'istruzione indicata dal PC, la si mette nell'IR e si incrementa il PC. Decode: la CU interpreta l'istruzione. Execute: si attivano i circuiti (ALU, salto con modifica del PC, ecc.). È deterministico e senza "fine" a livello hardware.

## Assembly
D: Differenza tra linguaggio macchina e assembly.
R: Il linguaggio macchina è fatto di codici binari dipendenti dall'ISA (non portabile). L'assembly li rappresenta con mnemonici (LOAD, STORE, ADD, JMP) con corrispondenza 1 a 1, tradotti dall'assembler; resta di basso livello e non portabile.

## Assembly
D: Come si somma A e B in memoria a basso livello?
R: LOAD R0,@A; LOAD R1,@B; ADD R0,R1; STORE R0,@A: la CPU non opera direttamente su due celle di RAM, quindi passa dai registri.

## Linguaggio C
D: Quali sono le quattro caratteristiche del C?
R: Compilato, imperativo, strutturato (blocchi con { } e funzioni), fortemente tipizzato. Progettato nel 1972 da Dennis Ritchie ai Bell Labs per UNIX.

## Tipi
D: Quali sono le sei dimensioni che un tipo di dato qualifica?
R: Nome, dimensione in memoria, dominio di valori, operazioni consentite, rappresentazione interna (complemento a 2, IEEE 754), compatibilità e conversione.

## Tipi
D: Quali tipi primitivi ha il C e cosa garantisce sizeof?
R: int/short/long/long long, unsigned per i naturali, float/double per i reali, char (1 byte), bool, size_t. sizeof(char) ≤ sizeof(short) ≤ sizeof(int) ≤ sizeof(long) ≤ sizeof(long long) e sizeof(float) ≤ sizeof(double).

## Tipi
D: Cosa succede con overflow e con int y = 8.89?
R: Con int x = 2147483647; x = x + 1; si ha overflow e x diventa −2147483648. Assegnando 8.89 a un int la parte frazionaria viene troncata (non arrotondata): y vale 8.

## Variabili
D: Quali quattro attributi identificano una variabile in C? Quanto vale una variabile locale non inizializzata?
R: Nome, tipo, indirizzo, valore. Una variabile locale non inizializzata ha valore indeterminato (bit residui della RAM).

## Stack
D: Come funziona l'allocazione sullo stack con FP e SP?
R: FP (Frame Pointer) è l'indirizzo base fisso del blocco corrente; SP (Stack Pointer) viene decrementato della dimensione del tipo a ogni dichiarazione (lo stack cresce verso indirizzi bassi). Scope = dove è visibile; lifetime = quando esiste. Troppe allocazioni causano stack overflow.

## Assegnamento
D: Cosa sono lvalue e rvalue in variabile = espressione;?
R: L'lvalue (sinistra) è una locazione di memoria modificabile; l'rvalue (destra) è un valore o espressione che viene valutata e poi copiata nella cella dell'lvalue. Operatori composti: +=, -=, *=, /=, %=, ++, --.

## Input/Output
D: Perché scanf richiede l'operatore & e quali specificatori usa printf per int, float, double, char?
R: scanf riceve l'indirizzo della variabile (&n) per sapere quale cella sovrascrivere. Specificatori: %d (int), %f (float), %lf (double), %c (char), %ld (long), %zu (size_t); %06d riempie con zeri fino a 6 cifre.
