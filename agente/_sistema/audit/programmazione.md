# Audit fattuale - Riassunto Programmazione I (Amparore)

Capitoli controllati: 1, 2, 3, 4, 5, 6, 7, 8 (Word: Riassunto Programmazione.docx). Tabelle e blocchi di codice inclusi. I numeri di paragrafo sono quelli dello script di estrazione (paragrafi numerati da 1, vuoti inclusi).
Fonti: 00_introduzione, 01A_primo_algoritmo, 01B_architettura, 02A_da_assembly_a_c, 02B_assegnamento_memory_model (in `_sistema/fonti_testo/Programmazione/`).

## Riepilogo

Problemi totali: 26 (alta: 2, media: 8, bassa: 16).

| Capitolo | Alta | Media | Bassa |
|---|---|---|---|
| 1 | 1 | 0 | 0 |
| 2 | 0 | 0 | 0 (nessun problema trovato) |
| 3 | 0 | 1 | 2 |
| 4 | 0 | 2 | 6 |
| 5 | 0 | 3 | 1 |
| 6 | 1 | 1 | 4 |
| 7 | 0 | 1 | 1 |
| 8 | 0 | 0 | 2 |

Verificato e corretto (non segnalato): definizione di algoritmo, algoritmo della moltiplicazione e caso n = 0, ruoli di PC/IR/CU/ALU/registri, ciclo fetch-decode-execute, traccia assembly di somma e moltiplicazione (12 + (-8) = 4, 10 righe, JMPEQ riga 10, JMP riga 5), relazioni di sizeof, intervalli di int/unsigned (2^32-1 = 4.294.967.295), troncamento 8.89 -> 8, specificatori printf (%c %hd %d %ld %zu %f %lf), FP/SP, stack che cresce verso indirizzi bassi, allocazione in ordine di dichiarazione, lvalue/rvalue, tabella degli operatori composti (tutti i risultati sono corretti con x = 5 di partenza: 8, 3, 20, 1, 2), schemi dello stack (x, y, z con FP in alto e SP in basso), %6d e %06d. Il codice C dei paragrafi 166-169, 195-199, 226-230, 247-249, 259-260, 279, 287-289 compila (con `-Wall -Werror` gli esempi con variabili inutilizzate darebbero errore di warning, ma sono frammenti illustrativi come nelle slide). Gli esponenti (2^N, 2^8, 2^32) sono in apice reale nel Word.

---

## Capitolo 1

### [GRAVITÀ: alta] Capitolo 1, paragrafo 9
**Testo attuale:** «Anni '70: con l'invenzione del transistor e dei circuiti elettronici, si afferma il calcolatore automatico ad altissima velocità.»
**Problema:** Affermazione non presente nelle slide e storicamente falsa/incoerente (il transistor è del 1947 e i calcolatori elettronici esistono dagli anni '40, come dice il Cap. 4 con ENIAC 1943-45); la slide dice solo «dagli anni '50, dispositivo elettromeccanico programmabile».
**Correzione proposta:** eliminare il paragrafo (o sostituirlo con): «Dagli anni '50: un dispositivo elettromeccanico programmabile in grado di svolgere calcoli anche complessi (vedi Cap. 4 per l'evoluzione fino ai calcolatori elettronici).»
**Fonte/verifica:** 01A_primo_algoritmo.md, slide 2 «Vocabolario»; 01B_architettura.md slide 9 (ENIAC 1943).

## Capitolo 2

Nessun problema trovato (definizione di algoritmo, al-Khwarismi, accumulatore/contatore, Wirth, caso n = 0 e regola «prima verificare le condizioni» coerenti con 01A slide 5, 14-20).

## Capitolo 3

### [GRAVITÀ: media] Capitolo 3, paragrafo 49
**Testo attuale:** «Linguaggi di basso livello: come il linguaggio macchina o l'assembly, espressi direttamente in sequenze di bit»
**Problema:** L'assembly non è espresso in sequenze di bit ma in mnemonici testuali; contraddice il Cap. 5 (par. 107) e la slide, dove solo il linguaggio macchina è fatto di bit.
**Correzione proposta:** «Linguaggi di basso livello: come il linguaggio macchina (sequenze di bit) o l'assembly (mnemonici testuali che lo rappresentano), strettamente legati all'architettura fisica della CPU.»
**Fonte/verifica:** 02A_da_assembly_a_c.md slide 3 «Vocabolario: linguaggio macchina e assembly»; 01A slide 27.

### [GRAVITÀ: bassa] Capitolo 3, paragrafo 39
**Testo attuale:** «qualsiasi algoritmo o funzione calcolabile può essere espresso combinando esclusivamente tre strutture di controllo elementari»
**Problema:** È corretto (teorema di Böhm-Jacopini) ma non compare nelle slide fornite; le tre strutture non sono enunciate così nel materiale del docente. Da segnalare come aggiunta esterna, non da imparare come «detto dal docente».
**Correzione proposta:** aggiungere «(teorema di Böhm-Jacopini; non presente nelle slide del docente)» oppure ridurre a «Gli algoritmi di questo corso si esprimono con sequenza, selezione e iterazione.»
**Fonte/verifica:** nessuna delle 5 slide cita Böhm-Jacopini né le «tre strutture»; conoscenza generale.

### [GRAVITÀ: bassa] Capitolo 3, paragrafo 42
**Testo attuale:** «... finché una specifica condizione rimane valida o viene soddisfatta»
**Problema:** Frase senza punto finale (troncata) e «o viene soddisfatta» è ambiguo (while vs do-while).
**Correzione proposta:** «Iterazione (ripetizione condizionata): la riesecuzione di un blocco di istruzioni finché una specifica condizione rimane valida.»
**Fonte/verifica:** 01A slide 25-26 («Ripetizione Condizionata»).

## Capitolo 4

### [GRAVITÀ: media] Capitolo 4, paragrafo 59
**Testo attuale:** «I primi calcolatori automatici progettati fino alla prima metà del Novecento erano macchine cablate ... (ad esempio solo addizioni o tabelle balistiche)»
**Problema:** «Fino alla prima metà del Novecento» e «tabelle balistiche» non sono nelle slide (che parlano di operazioni limitate, tipicamente addizione e sottrazione); il secondo è un'aggiunta non verificata.
**Correzione proposta:** «Queste prime macchine erano progettate per eseguire un insieme limitato di operazioni specifiche, tipicamente addizione e sottrazione. La logica era cablata nell'hardware (hardwired): introdurre nuove funzionalità, come confronti o salti condizionati, richiedeva modifiche o una riprogettazione dell'hardware; moltiplicazione e divisione erano difficili da realizzare con le tecnologie dell'epoca.»
**Fonte/verifica:** 01B_architettura.md slide 5 «Calcolatori cablati».

### [GRAVITÀ: media] Capitolo 4, paragrafo 65
**Testo attuale:** «Nel 1944-1945, nell'ambito del progetto EDVAC, il matematico John von Neumann formalizzò il celebre Modello di Von Neumann (o architettura EDVAC), introducendo tre intuizioni rivoluzionarie»
**Problema:** Le slide attribuiscono il progetto EDVAC (1944) a Mauchly ed Eckert e le tre idee all'EDVAC; Von Neumann era consulente e «descrisse e pubblicò per primo» l'architettura nel 1945. Attribuirgli le tre idee è impreciso.
**Correzione proposta:** «L'EDVAC, progettato nel 1944 da John Mauchly e J. Presper Eckert (già sviluppatori dell'ENIAC), introdusse tre idee fondamentali. Il matematico John von Neumann, consulente del progetto, descrisse e pubblicò per primo questa architettura nel 1945: da qui il nome «architettura di Von Neumann» (più corretto: «architettura EDVAC»).»
**Fonte/verifica:** 01B_architettura.md slide 10 (EDVAC) e slide 14 (Von Neumann). Le slide scrivono «John Adam Presper»: il nome completo è J. Presper Eckert (conoscenza generale, da verificare col docente).

### [GRAVITÀ: bassa] Capitolo 4, paragrafo 58
**Testo attuale:** «le sequenze di operazioni venivano scorte e pilotate manualmente dall'utente»
**Problema:** «scorte» è un refuso (probabile «scandite» o «scelte»).
**Correzione proposta:** «le sequenze di operazioni venivano scelte e pilotate manualmente dall'utente.»
**Fonte/verifica:** 01B slide 4 (la Pascalina non ha il concetto di programma); refuso.

### [GRAVITÀ: bassa] Capitolo 4, paragrafo 64
**Testo attuale:** «Macchina Analitica di Charles Babbage (1840), che introdusse l'uso delle schede perforate per guidare il flusso di calcolo»
**Problema:** Le schede perforate non furono introdotte da Babbage (esistevano già, es. telai Jacquard); la slide dice solo che dati e istruzioni sono su schede perforate e che è il primo esempio di macchina programmabile (descritta intorno al 1840).
**Correzione proposta:** «la Macchina Analitica di Charles Babbage (descritta intorno al 1840), primo esempio di macchina di calcolo programmabile, con dati e istruzioni su schede perforate»
**Fonte/verifica:** 01B slide 7. Nello stesso paragrafo «ENIAC (1943-1945)» e «valvole termoioniche» sono aggiunte non nelle slide (la slide dice «progettato nel 1943»): vero in generale, ma non dal docente.

### [GRAVITÀ: bassa] Capitolo 4, paragrafo 71
**Testo attuale:** «Il Bit (Binary Information Token)»
**Problema:** Il nome corretto in letteratura è «binary digit»; «Binary Information Token» è la dicitura della slide del docente. Rischio se all'esame si usa la forma standard.
**Correzione proposta:** «Il Bit (Binary digit; nelle slide: «Binary Information Token»)»
**Fonte/verifica:** 01B slide 11 («Binary Information Token»); la forma «binary digit» è la definizione standard (conoscenza generale).

### [GRAVITÀ: bassa] Capitolo 4, paragrafo 72
**Testo attuale:** «mediante transistor a due stati stabili (latch), valvole o relè»
**Problema:** Un latch è un circuito (bistabile), non un transistor; l'elenco della slide è relè, valvole, transistor.
**Correzione proposta:** «mediante dispositivi come relè, valvole o transistor (che realizzano circuiti a due stati stabili).»
**Fonte/verifica:** 01B slide 11 («relais, valvole, transistors»).

### [GRAVITÀ: bassa] Capitolo 4, paragrafo 87 (e Cap. 5 paragrafo 110)
**Testo attuale:** «La CPU non lavora mai direttamente sui dati in RAM» (par. 87); «la CPU non possiede un'istruzione unica in grado di manipolare direttamente due celle di memoria RAM» (par. 110)
**Problema:** Vale per il modello load/store (RISC, tipo MIPS32) usato dal docente, non per tutte le CPU (x86 ammette operandi in memoria); «mai» è troppo assoluto. Inoltre la slide di 02B dice che «le operazioni agiscono direttamente su valori memorizzati a determinati indirizzi» (Cap. 6 par. 176 lo ripete), creando incoerenza interna.
**Correzione proposta:** «Nel modello usato nel corso (stile RISC, load/store) la CPU opera sui valori nei registri: carica i valori dalla RAM nei registri, li elabora con l'ALU e riscrive il risultato in RAM.» (analogo per par. 110: «nel modello del corso non esiste un'istruzione che operi direttamente su due celle di RAM»).
**Fonte/verifica:** 02A slide 5 («tipo RISC come MIPS32»); 02B slide 4.

### [GRAVITÀ: bassa] Capitolo 4, paragrafo 102
**Testo attuale:** «a livello hardware la CPU non possiede un concetto nativo di "fine programma": essa continua ad eseguire il ciclo fetch-decode-execute all'infinito.»
**Problema:** Non presente nelle slide e non universale (molte ISA hanno istruzioni di halt/stop o la terminazione è gestita dal sistema operativo); asserito come certo. Nelle slide l'algoritmo ha un'istruzione «Fine» (livello algoritmico, non CPU).
**Correzione proposta:** «Il ciclo fetch-decode-execute si ripete finché la macchina è accesa; la terminazione di un programma va quindi programmata esplicitamente (es. tornando al sistema operativo). [aggiunta non nelle slide]»
**Fonte/verifica:** 01B slide 18-19 (nessun cenno alla terminazione hardware); ragionamento.

## Capitolo 5

### [GRAVITÀ: media] Capitolo 5, paragrafo 107
**Testo attuale:** «Tra il codice assembly e il codice macchina esiste una corrispondenza biunivoca (1 a 1): ogni riga di testo assembly equivale esattamente a una singola istruzione numerica della CPU.»
**Problema:** Falso per le righe dell'esempio: `ADDR A = 400` e `ADDR B = 404` sono direttive che definiscono simboli e non generano istruzioni (la slide mostra 6 righe assembly e 4 istruzioni macchina). Il «1 a 1» vale per le istruzioni, non per le righe; «biunivoca» è anche una formulazione non delle slide.
**Correzione proposta:** «Ogni istruzione assembly (LOAD, ADD, STORE, ...) corrisponde a una istruzione macchina; le direttive come ADDR A = 400 definiscono solo indirizzi simbolici e non producono codice macchina.»
**Fonte/verifica:** 02A_da_assembly_a_c.md slide 4 (sorgente assembly con 2 ADDR + 4 istruzioni, codice macchina con 4 righe) e slide 6.

### [GRAVITÀ: media] Capitolo 5, paragrafo 135
**Testo attuale:** «Progettato nel 1972 da Dennis Ritchie presso i Bell Labs per sviluppare il sistema operativo UNIX»
**Problema:** Secondo le slide Unix esisteva già (1969, Ken Thompson, PDP-7, scritto in assembly); Ritchie progettò il C per superare i limiti dell'assembly e Unix fu poi riscritto in C. Il 1972 è la prima versione del C (K&R C), non la data di nascita di Unix. Per memorizzare: date e nomi sono scambiabili.
**Correzione proposta:** «Nel 1969 Ken Thompson (Bell Labs, AT&T) sviluppa Unix per il PDP-7 in assembly. Per superare i limiti dell'assembly Dennis Ritchie progetta il linguaggio C (prima versione nel 1972, oggi detta K&R C) e Unix viene progressivamente riscritto in C. Standardizzato da ANSI/ISO verso la fine degli anni '80 (ANSI-C, C89); il libro di testo fa riferimento a C11.»
**Fonte/verifica:** 02A_da_assembly_a_c.md slide 24-25.

### [GRAVITÀ: media] Capitolo 5, paragrafo 139
**Testo attuale:** «Strutturato: ... eliminando l'uso dei salti incondizionati grezzi.»
**Problema:** Il C ha ancora `goto` (è nella lista delle keyword nelle slide); la slide dice solo che il codice è strutturato in blocchi racchiusi da delimitatori.
**Correzione proposta:** «Strutturato: il codice si organizza in funzioni e in blocchi di istruzioni racchiusi da delimitatori formali (le parentesi graffe {}), per cui non servono salti a numeri di riga.»
**Fonte/verifica:** 02A slide 27 (caratteristiche) e slide 40 (elenco keyword con `goto`).

### [GRAVITÀ: bassa] Capitolo 5, paragrafo 129
**Testo attuale:** «un algoritmo descrivibile in due righe concettuali richiede circa 10 istruzioni macchina atomiche.»
**Problema:** «due righe concettuali» non è nelle slide (che confrontano 4 righe di assembly per l'addizione e 10 per la moltiplicazione) e le 10 righe sono assembly, non codice macchina.
**Correzione proposta:** «un algoritmo semplice come la moltiplicazione richiede 10 righe di assembly (e l'addizione 4).»
**Fonte/verifica:** 02A slide 17.

## Capitolo 6

### [GRAVITÀ: alta] Capitolo 6, paragrafo 171
**Testo attuale:** «L'operatore unario sizeof() permette di ricavare a runtime il quantitativo esatto di memoria occupato»
**Problema:** sizeof è valutato a tempo di compilazione (costante), salvo i VLA; «a runtime» è errato. Inoltre è un operatore, non una funzione.
**Correzione proposta:** «L'operatore unario sizeof permette di ricavare (a tempo di compilazione) il numero di byte occupati da un tipo o da una variabile, restituendo un valore di tipo size_t.»
**Fonte/verifica:** 02B slide 13 (dice solo «il risultato di sizeof ha tipo size_t»); standard C (sizeof è una costante intera a compile time, eccetto array a lunghezza variabile).

### [GRAVITÀ: media] Capitolo 6, paragrafi 163 e 167
**Testo attuale:** «int x = 2147483647; x = x + 1; // OVERFLOW: x diventa -2147483648» e «fa "ripartire" il ciclo numerico dal limite minimo negativo»
**Problema:** L'overflow di un int con segno in un'operazione aritmetica è comportamento indefinito in C: il valore -2147483648 è solo quello tipico (non garantito; con ottimizzazioni il compilatore può fare altro). Inoltre l'esempio delle slide è diverso: `int x = 2 147 483 649;` stampa -2147483647 (conversione fuori intervallo). Solo per gli unsigned il wrap-around è definito dallo standard.
**Correzione proposta:** «int x = 2147483647; x = x + 1; // OVERFLOW: comportamento indefinito per gli int con segno; tipicamente x diventa -2147483648.» e aggiungere l'esempio della slide: «int x = 2147483649; // fuori intervallo: sulla macchina del corso x vale -2147483647».
**Fonte/verifica:** 02B slide 28 (esempio `./overflow` -> -2147483647); standard C (signed overflow = UB). Nota: gcc con `-Wall -Werror` segnala come errore l'inizializzazione con costante fuori intervallo.

### [GRAVITÀ: bassa] Capitolo 6, paragrafo 146
**Testo attuale:** «Dimensione in memoria: il quantitativo fisso di byte occupati nella RAM per memorizzare un dato di quel tipo (ad esempio 4 byte per un int, 8 byte per un double).»
**Problema:** «fisso» contraddice par. 171 (il C non fissa le dimensioni); i valori sono tipici.
**Correzione proposta:** «Dimensione in memoria: quanti byte occupa un dato di quel tipo (tipicamente 4 byte per un int, 8 per un double; dipende dalla piattaforma).»
**Fonte/verifica:** 02B slide 3 («tipicamente 4B») e slide 13.

### [GRAVITÀ: bassa] Capitolo 6, paragrafo 153
**Testo attuale:** «// tipo nativo (o primitivo/built-in) è un tipo di dato fornito direttamente dal linguaggio ...»
**Problema:** Il paragrafo di testo inizia con «//» come se fosse un commento C: notazione incoerente (non è codice).
**Correzione proposta:** «Un tipo nativo (o primitivo/built-in) è un tipo di dato fornito direttamente dal linguaggio (come int, float o char) che stabilisce la dimensione occupata in memoria, la codifica binaria e le operazioni consentite.»
**Fonte/verifica:** controllo del formato del paragrafo (runs senza font Consolas); 02B slide 7.

### [GRAVITÀ: bassa] Capitolo 6, paragrafo 154
**Testo attuale:** «long (4 o 8 byte a seconda dell'architettura)»
**Problema:** Vero per la tabella del docente, ma la dimensione di long dipende anche dal sistema operativo: su Windows a 64 bit (la macchina dello studente) long è 4 byte, su Linux a 64 bit è 8. Il testo lo attribuisce solo all'architettura.
**Correzione proposta:** «long (4 o 8 byte a seconda di architettura e sistema operativo; es. 4 byte su Windows 64 bit, 8 su Linux 64 bit)».
**Fonte/verifica:** 02B slide 14 (tabella: long = 4 su 32 bit, 8 su 64 bit); modelli dati LP64 (Linux/macOS) vs LLP64 (Windows) - conoscenza generale.

### [GRAVITÀ: bassa] Capitolo 6, paragrafo 197
**Testo attuale:** «x = 10;      // Inizializzazione/Assegnamento successivo: il valore diventa 10»
**Problema:** Notazione incoerente: nel Cap. 8 (par. 252-253) «inizializzazione» è solo quella contestuale; qui `x = 10;` dopo la dichiarazione è un assegnamento successivo.
**Correzione proposta:** `x = 10;      // Assegnamento successivo: il valore diventa 10`
**Fonte/verifica:** 02B slide 27 e 39.

## Capitolo 7

### [GRAVITÀ: media] Capitolo 7, paragrafo 213
**Testo attuale:** «Stack Pointer (SP): memorizza l'indirizzo dinamico dell'ultima posizione occupata sulla pila, identificando il punto esatto in cui allocare la variabile successiva. All'avvio ... i registri FP e SP coincidono»
**Problema:** Incoerente: se FP e SP coincidono all'avvio (nessuna variabile), SP non indica una posizione «occupata». Nel modello delle slide SP indica l'indirizzo a cui allocare la prossima variabile (e dopo l'allocazione di x, y, z è sul bordo basso, come nello schema).
**Correzione proposta:** «Stack Pointer (SP): indica l'indirizzo a cui allocare la prossima variabile (la cima corrente dello stack); si sposta man mano che si allocano variabili. All'avvio FP e SP coincidono.»
**Fonte/verifica:** 02B slide 22 («SP indica l'indirizzo a cui allocare la prossima variabile»; «all'inizio FP e SP coincidono») e slide 26.

### [GRAVITÀ: bassa] Capitolo 7, paragrafo 212
**Testo attuale:** «della funzione o del blocco corrente (main())»
**Problema:** «o del blocco corrente» non è nelle slide: FP è l'indirizzo base delle variabili del programma partendo dal main (per funzione, non per blocco).
**Correzione proposta:** «Frame Pointer (FP): indirizzo base da cui inizia l'allocazione delle variabili del programma (partendo dal main()).»
**Fonte/verifica:** 02B slide 22.

## Capitolo 8

### [GRAVITÀ: bassa] Capitolo 8, paragrafo 264
**Testo attuale:** «Il compilatore la traduce nelle seguenti istruzioni macchina eseguite dalla CPU»
**Problema:** Le istruzioni elencate (LOAD, ADD, STORE con mnemonici) sono assembly, non codice macchina (che è binario), come precisato dal Cap. 5.
**Correzione proposta:** «Il compilatore la traduce in istruzioni assembly (poi tradotte in codice macchina), eseguite dalla CPU:»
**Fonte/verifica:** 02B slide 35; 02A slide 3-4.

### [GRAVITÀ: bassa] Capitolo 8, paragrafo 282
**Testo attuale:** «occupando un ampiezza minima di 6 caratteri»
**Problema:** Refuso (elisione mancante).
**Correzione proposta:** «occupando un'ampiezza minima di 6 caratteri»
**Fonte/verifica:** refuso.
