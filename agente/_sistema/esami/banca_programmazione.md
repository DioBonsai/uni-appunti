# Banca di quiz Programmazione I (linguaggio C)

Nota: domande originali scritte a partire dai riassunti Word di Programmazione (capitoli 1-12) e Laboratorio (capitoli 1-5). Una sola risposta corretta su cinque.

## [prg-001] argomenti: algoritmi
Quali sono i due requisiti fondamentali che un algoritmo valido deve soddisfare?
1. Correttezza e terminazione
2. Velocità e portabilità
3. Compilabilità e indentazione
4. Ricorsività e uso dei puntatori
5. Determinismo hardware e uso dei registri
RISPOSTA: 1
SPIEGAZIONE: Un algoritmo deve produrre l'output esatto per ogni input ammissibile (correttezza) e concludersi in un numero finito di passi (terminazione).

## [prg-002] argomenti: algoritmi
Nell'algoritmo di moltiplicazione per somme ripetute (accumulatore s, contatore i, entrambi inizializzati a 0), se la prima somma viene eseguita prima di controllare se i = n, che cosa succede con n = 0?
1. Restituisce correttamente 0
2. Restituisce m, cioè una somma in più del dovuto, e poi termina
3. Termina subito con un errore di overflow
4. Il caso n = 0 non è ammesso e l'algoritmo salta automaticamente il ciclo
5. Il contatore supera il valore di arresto e l'algoritmo non termina (ciclo infinito)
RISPOSTA: 5
SPIEGAZIONE: Con n = 0 la somma viene eseguita una volta e i diventa 1, quindi i = n non sarà mai vero: ciclo infinito. Per questo si controlla la condizione prima di eseguire le operazioni.

## [prg-003] argomenti: algoritmi
Quali sono i tre pilastri della programmazione strutturata?
1. Sequenza, salto incondizionato, ricorsione
2. Sequenza, selezione, iterazione
3. Selezione, iterazione, assegnamento
4. Dichiarazione, assegnamento, stampa
5. Compilazione, collegamento, esecuzione
RISPOSTA: 2
SPIEGAZIONE: Ogni algoritmo calcolabile si può esprimere combinando sequenza, selezione (scelta condizionata) e iterazione (ripetizione condizionata).

## [prg-004] argomenti: algoritmi
Secondo il principio di Niklaus Wirth riportato nel riassunto, un programma è l'unione di:
1. Sintassi e compilatore
2. Istruzioni e registri della CPU
3. Algoritmi e strutture dati
4. Codice sorgente e commenti
5. Algoritmi e linguaggio macchina
RISPOSTA: 3
SPIEGAZIONE: Programma = Algoritmi + Strutture Dati: la rappresentazione dei dati e le procedure che li trasformano.

## [prg-005] argomenti: assembly
Quale delle seguenti è una caratteristica del modello di Von Neumann?
1. Istruzioni e dati stanno in memorie fisicamente separate
2. Dati e istruzioni del programma sono memorizzati nello stesso spazio di memoria
3. Per cambiare programma bisogna ricablare la macchina
4. Le informazioni sono rappresentate in forma decimale
5. La CPU lavora direttamente sulle celle della RAM, senza usare registri
RISPOSTA: 2
SPIEGAZIONE: Le tre intuizioni dell'EDVAC sono programma memorizzato, memoria unificata e rappresentazione binaria. La CPU carica i dati dalla RAM nei registri e poi li elabora con l'ALU.

## [prg-006] argomenti: assembly
Che cosa contiene il Program Counter (PC) della CPU?
1. Il codice numerico dell'istruzione attualmente in decodifica
2. L'indirizzo di memoria della prossima istruzione da prelevare ed eseguire
3. Il risultato dell'ultima operazione dell'ALU
4. Il numero di istruzioni eseguite finora
5. L'indirizzo della prossima variabile da allocare sullo stack
RISPOSTA: 2
SPIEGAZIONE: Il PC punta alla prossima istruzione e viene incrementato (o sovrascritto da un salto). Il codice dell'istruzione in esecuzione sta nell'Instruction Register (IR).

## [prg-007] argomenti: assembly
Le celle A = 400 e B = 404 contengono rispettivamente 12 e -8. Dopo la sequenza LOAD R0,@A; LOAD R1,@B; ADD R0,R1; STORE R0,@A, quali valori hanno A e B?
1. A = 4 e B = 4
2. A = 12 e B = -8
3. A = -4 e B = -8
4. A = 4 e B = -8
5. A = 12 e B = 4
RISPOSTA: 4
SPIEGAZIONE: R0 = 12, R1 = -8, ADD scrive 12 + (-8) = 4 in R0 e STORE lo riscrive in A. B non viene mai scritta e resta -8.

## [prg-008] argomenti: assembly
Si esegue il programma assembly della moltiplicazione (R0 = s, R1 = i, R2 = m, R3 = n; il ciclo confronta R1 con R3 e salta all'uscita se sono uguali; alla fine STORE R0,@m) con @m = 3 e @n = 2. Quante volte viene eseguita ADD R0,R2 e che valore viene scritto in @m?
1. 3 volte, e in @m viene scritto 9
2. 2 volte, e in @m viene scritto 3
3. 2 volte, e in @m viene scritto 6
4. 3 volte, e in @m viene scritto 6
5. 1 volta, e in @m viene scritto 3
RISPOSTA: 3
SPIEGAZIONE: Con i = 0 e i = 1 il confronto con n = 2 fallisce e si somma: s = 3, poi s = 6. Con i = 2 si esce e STORE scrive 6 in @m.

## [prg-009] argomenti: assembly
Quale affermazione su assembly e linguaggio macchina è corretta?
1. Una direttiva come ADDR A = 400 viene tradotta in un'istruzione macchina di caricamento
2. Ogni istruzione assembly come LOAD o ADD corrisponde a una singola istruzione macchina, mentre una direttiva come ADDR A = 400 non produce codice macchina
3. Il codice assembly è portabile tra CPU con ISA diverse
4. La traduzione da assembly a codice macchina è svolta dal linker
5. L'assembly è l'unico livello espressivo direttamente eseguibile dall'hardware
RISPOSTA: 2
SPIEGAZIONE: L'assembly è una rappresentazione simbolica del linguaggio macchina, tradotta dall'assembler; le direttive definiscono solo indirizzi simbolici. Solo il linguaggio macchina è eseguibile direttamente e l'assembly non è portabile.

## [prg-010] argomenti: tipi-e-memoria
Che cosa afferma il riassunto sull'overflow di un int con segno, ad esempio int x = 2147483647; x = x + 1; (int a 32 bit)?
1. Il compilatore lo rileva sempre e blocca la compilazione
2. È un comportamento formalmente indefinito per lo standard C; tipicamente il valore riparte dal minimo negativo
3. Il valore diventa sempre 0
4. x resta invariato a 2147483647
5. È definito: il risultato è 2147483648, rappresentabile grazie al segno
RISPOSTA: 2
SPIEGAZIONE: L'overflow non è sempre rilevato dal compilatore; per gli interi con segno è indefinito, e in pratica si osserva -2147483648.

## [prg-011] argomenti: tipi-e-memoria
Che cosa stampa il codice seguente?  int y = 8.89; int z = y * 2; printf("%d", z);
1. 17
2. 17.78
3. 18
4. 8
5. 16
RISPOSTA: 5
SPIEGAZIONE: L'assegnamento a una variabile intera tronca la parte frazionaria senza arrotondare: y vale 8, quindi z = 16.

## [prg-012] argomenti: tipi-e-memoria
Quale relazione tra le dimensioni dei tipi è garantita formalmente dal C?
1. sizeof(char) ≤ sizeof(short) ≤ sizeof(int) ≤ sizeof(long) ≤ sizeof(long long)
2. sizeof(int) vale sempre 4 byte
3. sizeof(double) è sempre uguale a sizeof(long)
4. sizeof(float) è sempre maggiore di sizeof(double)
5. sizeof(char) è sempre uguale a sizeof(int)
RISPOSTA: 1
SPIEGAZIONE: Il C fissa solo relazioni d'ordine (e sizeof(float) ≤ sizeof(double)); le dimensioni assolute, ad esempio i 4 byte di int, sono tipiche ma dipendono dalla piattaforma.

## [prg-013] argomenti: tipi-e-memoria
Quale intervallo di valori copre un unsigned int a 32 bit?
1. Da -2.147.483.648 a 2.147.483.647
2. Da 0 a 2.147.483.647
3. Da 1 a 4.294.967.296
4. Da 0 a 4.294.967.295
5. Da -4.294.967.295 a 4.294.967.295
RISPOSTA: 4
SPIEGAZIONE: Senza il segno l'intervallo positivo raddoppia: da 0 a 2^32 - 1 = 4.294.967.295.

## [prg-014] argomenti: tipi-e-memoria
Quanti valori distinti si possono rappresentare, rispettivamente, con 1 byte e con 10 bit?
1. 255 e 1023
2. 256 e 1024
3. 128 e 512
4. 256 e 1000
5. 8 e 20
RISPOSTA: 2
SPIEGAZIONE: Con N bit si hanno 2^N combinazioni: un byte (8 bit) ne dà 2^8 = 256, 10 bit ne danno 2^10 = 1024. Il massimo valore (255, 1023) è un'unità in meno.

## [prg-015] argomenti: tipi-e-memoria
Che cosa avviene quando il flusso di esecuzione incontra la dichiarazione int x; di una variabile locale?
1. Lo Stack Pointer viene incrementato di 4 byte e x vale 0
2. Lo Stack Pointer viene decrementato di 4 byte e x vale 0
3. Viene spostato il Frame Pointer e x vale 0
4. Lo spazio viene riservato solo al primo assegnamento a x
5. Lo Stack Pointer viene decrementato di 4 byte e il valore di x resta indeterminato
RISPOSTA: 5
SPIEGAZIONE: Lo stack cresce verso indirizzi decrescenti: SP viene decrementato della dimensione del tipo e la cella conserva i bit residui, quindi il valore è indeterminato.

## [prg-016] argomenti: variabili-assegnamento
Dato il codice  int x; x = 10; float y = 3.14f;  quale affermazione è corretta?
1. int x; inizializza x a 0 se la variabile è locale
2. float y = 3.14f; è solo un assegnamento: la dichiarazione richiede una riga separata
3. int x; riserva la memoria lasciando x indeterminato, x = 10; è un assegnamento successivo, float y = 3.14f; è una inizializzazione contestuale
4. x = 10; è una dichiarazione perché usa il nome x
5. int x; non riserva memoria finché non si assegna un valore a x
RISPOSTA: 3
SPIEGAZIONE: La dichiarazione riserva lo spazio senza scriverci un valore; l'assegnamento successivo modifica la cella; la forma float y = ...; unisce dichiarazione e valore.

## [prg-017] argomenti: variabili-assegnamento
Che cosa stampa il codice seguente?  int a = 3, b = 4; a = a + b; b = a - b; a = a - b; printf("%d %d", a, b);
1. 3 4
2. 7 3
3. 4 3
4. 7 4
5. 4 7
RISPOSTA: 3
SPIEGAZIONE: Dopo a = 7; b = 7 - 4 = 3; a = 7 - 3 = 4. I valori sono scambiati: a = 4 e b = 3.

## [prg-018] argomenti: variabili-assegnamento
Che cosa stampa il codice seguente?  int a = 1, b = 2, c = 3; a = b = c; c = 10; printf("%d %d %d", a, b, c);
1. 1 2 10
2. 3 3 3
3. 10 10 10
4. 3 3 10
5. 3 2 10
RISPOSTA: 4
SPIEGAZIONE: a = b = c copia il valore 3 prima in b e poi in a. Il successivo c = 10 modifica solo la cella di c: a e b restano 3.

## [prg-019] argomenti: variabili-assegnamento
Con x = 5, quanto vale x dopo  x += 3; x *= 2; x -= 4; x /= 3; x %= 3;  ?  (x è un int)
1. 0
2. 2
3. 4
4. 1
5. 12
RISPOSTA: 4
SPIEGAZIONE: x: 8, poi 16, poi 12, poi 12/3 = 4 e infine 4 % 3 = 1.

## [prg-020] argomenti: variabili-assegnamento
Con int a, b; quale delle seguenti istruzioni è un errore, perché il lato sinistro non è un lvalue?
1. a = b + 1;
2. a = a + a;
3. a = b = 0;
4. a + 1 = b;
5. a += b;
RISPOSTA: 4
SPIEGAZIONE: Il lato sinistro dell'assegnamento deve identificare una cella di memoria modificabile; a + 1 è un risultato temporaneo, non una variabile.

## [prg-021] argomenti: operatori
Che cosa stampa il codice seguente?  int a = 17, b = 5; printf("%d %d", a / b, a % b);
1. 3.4 2
2. 4 2
3. 3 2
4. 3 3
5. 2 3
RISPOSTA: 3
SPIEGAZIONE: Tra interi / è la divisione intera (17/5 = 3, resto scartato) e % dà il resto (17 % 5 = 2).

## [prg-022] argomenti: operatori
Che cosa stampa il codice seguente?  int x = 7; int y = x / 2 * 2; int z = x * 2 / 2; printf("%d %d", y, z);
1. 7 7
2. 6 6
3. 7 6
4. 7 14
5. 6 7
RISPOSTA: 5
SPIEGAZIONE: y = (7/2)*2 = 3*2 = 6 per la divisione intera; z = (7*2)/2 = 14/2 = 7.

## [prg-023] argomenti: operatori
Che cosa stampa il codice seguente?  int i = 4; i++; i += 2; i--; printf("%d", i);
1. 6
2. 5
3. 7
4. 8
5. 4
RISPOSTA: 1
SPIEGAZIONE: i vale 4, poi 5 (i++), 7 (i += 2) e infine 6 (i--).

## [prg-024] argomenti: operatori
Quale delle seguenti istruzioni NON è equivalente a x++; ?
1. x = x + 1;
2. x += 1;
3. x = 1 + x;
4. x += 2;
5. x -= -1;
RISPOSTA: 4
SPIEGAZIONE: x++ incrementa di una sola unità; x += 2 aumenta di due. Le altre quattro aggiungono 1.

## [prg-025] argomenti: puntatori
Qual è la differenza tra gli operatori & e * applicati a una variabile e a un puntatore?
1. & accede alla variabile puntata e * restituisce l'indirizzo di una variabile
2. Sono lo stesso operatore: entrambi restituiscono l'indirizzo
3. & si usa solo in scanf e * solo per la moltiplicazione
4. & restituisce la dimensione in byte e * il valore della variabile
5. & applicato a una variabile ne restituisce l'indirizzo; * applicato a un puntatore accede alla variabile puntata
RISPOSTA: 5
SPIEGAZIONE: &x è l'indirizzo di x (tipo int* se x è int); *p è la variabile puntata da p (tipo T se p ha tipo T*). I due operatori si annullano a vicenda.

## [prg-026] argomenti: puntatori
Che cosa stampa il codice seguente?  int x = 5; int* p = &x; *p = 10; x = x + 1; printf("%d %d", x, *p);
1. 6 10
2. 11 11
3. 11 10
4. 10 11
5. 5 11
RISPOSTA: 2
SPIEGAZIONE: *p = 10 scrive nella cella di x, che poi diventa 11. x e *p sono la stessa variabile, quindi stampano entrambi 11.

## [prg-027] argomenti: puntatori
Che cosa stampa il codice seguente?  int a = 1, b = 2; int* p = &a; int* q = p; *q = 7; p = &b; *p = *p + *q; printf("%d %d", a, b);
1. 7 9
2. 7 2
3. 1 9
4. 9 7
5. 7 14
RISPOSTA: 1
SPIEGAZIONE: *q = 7 pone a = 7 (q punta ad a). Poi p punta a b, e *p + *q = 2 + 7 = 9 viene scritto in b, quindi a = 7 e b = 9.

## [prg-028] argomenti: puntatori
Con int x; quale delle seguenti espressioni è un errore, perché & va applicato a qualcosa che identifica una posizione di memoria?
1. &5
2. &x
3. int* pX = &x;
4. scanf("%d", &x);
5. printf("%p", &x);
RISPOSTA: 1
SPIEGAZIONE: & non si può applicare a un semplice valore (&5) né al risultato temporaneo di un calcolo (&(x + 1)); le altre espressioni sono lecite anche con x non inizializzata.

## [prg-029] argomenti: puntatori
Su una tipica piattaforma a 64 bit, che cosa stampa il codice seguente?  int x; int* pX; printf("%zu %zu", sizeof(x), sizeof(pX));
1. 4 4
2. 8 8
3. 8 4
4. 1 8
5. 4 8
RISPOSTA: 5
SPIEGAZIONE: Un int occupa tipicamente 4 byte; un puntatore occupa 8 byte su 64 bit, indipendentemente dal tipo puntato.

## [prg-030] argomenti: puntatori
Che cosa accade con il codice seguente?  int *p = NULL; *p = 10;
1. Viene allocata automaticamente una variabile in cui scrivere 10
2. NULL è un indirizzo valido, quindi 10 viene scritto senza problemi
3. Si dereferenzia un puntatore che non punta ad alcuna variabile: comportamento indefinito, in genere un errore che termina il programma
4. Il puntatore p assume il valore 10
5. Il codice è corretto: NULL è l'inizializzazione sicura per poter scrivere tramite il puntatore
RISPOSTA: 3
SPIEGAZIONE: NULL rende esplicito che p non punta a niente, ma proprio per questo non si può dereferenziarlo.

## [prg-031] argomenti: puntatori
Dato int x = 5; int* pX = &x; quale affermazione è vera?
1. pX e &pX coincidono sempre
2. sizeof(pX) vale sempre 4 perché x è un int
3. L'espressione *pX ha tipo int*
4. pX è una variabile come le altre: contiene l'indirizzo di x e ha un proprio indirizzo &pX, diverso dal suo valore
5. L'espressione &x ha tipo int
RISPOSTA: 4
SPIEGAZIONE: Un puntatore occupa memoria e ha un indirizzo suo; &x ha tipo int* e *pX ha tipo int; la dimensione di un puntatore dipende dalla piattaforma, non dal tipo puntato.

## [prg-032] argomenti: puntatori
In quale delle seguenti righe il simbolo * indica un dereferenziamento?  (a, b int; p di tipo int* con p = &a)
1. int z = a * b;
2. int* q = &b;
3. float* r;
4. printf("%d", a * 2);
5. int w = *p;
RISPOSTA: 5
SPIEGAZIONE: In int w = *p; l'asterisco accede alla variabile puntata. In a * b è moltiplicazione, in int* q e float* r fa parte della dichiarazione del tipo puntatore.

## [prg-033] argomenti: scanf-printf
Perché scanf("%d", &n) richiede l'operatore & davanti a n?
1. Perché & converte l'input da testo a intero
2. Perché senza & scanf legge solo il primo carattere digitato
3. Perché scanf deve ricevere l'indirizzo della cella di n per potervi scrivere il valore letto
4. Perché & è obbligatorio per ogni funzione della libreria standard, printf compresa
5. Perché & impedisce che n resti indeterminato
RISPOSTA: 3
SPIEGAZIONE: Passando il valore di n scanf non saprebbe dove scrivere; passando l'indirizzo (di tipo int*) può sovrascrivere la cella. Con un puntatore pX = &n si può scrivere anche scanf("%d", pX).

## [prg-034] argomenti: scanf-printf
Si esegue int x; int n = scanf("%d", &x); printf("%d %d", n, x); e l'utente digita 1234.56. Che cosa viene stampato?
1. 1 1234
2. 0 1234
3. 1 1235
4. 2 1234
5. 1 123456
RISPOSTA: 1
SPIEGAZIONE: Il formato %d legge "1234" e lascia ".56" nell'input: scanf restituisce 1 (valori letti) e x vale 1234.

## [prg-035] argomenti: scanf-printf
Che cosa stampa printf("%06d|%6d", 7, 7); ?
1. 000007|000007
2.      7|000007
3. 0000007|     7
4. 000007|7     
5. 000007|     7
RISPOSTA: 5
SPIEGAZIONE: %06d riempie con zeri fino a 6 caratteri (000007), %6d allinea a destra con spazi (5 spazi seguiti da 7).

## [prg-036] argomenti: compilazione-cli
Che cosa produce il comando  gcc -c sorgente.c -o oggetto.o ?
1. Un file oggetto, eseguendo preprocessing, compilazione e assemblamento ma senza collegamento
2. Un eseguibile, perché gcc include sempre il linker
3. Soltanto il testo del sorgente dopo il preprocessing
4. Il codice assembly leggibile, che poi va a mano tradotto in codice macchina
5. Un file eseguito direttamente senza salvare alcun file di output
RISPOSTA: 1
SPIEGAZIONE: -c si ferma al file oggetto; per ottenere l'eseguibile il linker deve unire i file oggetto, con lo stesso comando gcc ma senza -c.

## [prg-037] argomenti: compilazione-cli
Qual è il ruolo delle opzioni -Wall e -Werror in  gcc -Wall -Werror sorgente.c -o eseguibile ?
1. -Wall abilita gli avvertimenti; -Werror impedisce di compilare il programma se ci sono avvertimenti
2. -Wall impedisce la compilazione se ci sono errori; -Werror abilita gli avvertimenti
3. Entrambe disabilitano gli avvertimenti per velocizzare la compilazione
4. -Wall serve a collegare i file oggetto; -Werror a disassemblare il programma
5. -Wall ignora gli avvertimenti sui costrutti potenzialmente sbagliati; -Werror stampa solo gli errori
RISPOSTA: 1
SPIEGAZIONE: I warning segnalano costrutti non necessariamente errati ma sospetti; con -Werror diventano bloccanti. All'esame si usano entrambe le opzioni.

## [prg-038] argomenti: compilazione-cli
La working directory è C:\Users\jon_snow\Documenti. Quale comando equivale a  del verbale.txt ?
1. del ..\verbale.txt
2. del ..\..\verbale.txt
3. del Documenti\verbale.txt
4. del .\verbale.txt
5. del \verbale.txt
RISPOSTA: 4
SPIEGAZIONE: Il punto indica la cartella di lavoro stessa, mentre .. indica la cartella che la contiene: solo .\verbale.txt individua lo stesso file.

## [prg-039] argomenti: controllo-flusso
Che cosa stampa il codice seguente?  int s = 1; for (int i = 0; i < 4; ++i) { s = s + 2 * i; } printf("%d", s);
1. 12
2. 13
3. 7
4. 21
5. 16
RISPOSTA: 2
SPIEGAZIONE: Il ciclo esegue i = 0, 1, 2, 3 (i < 4): si aggiungono 0, 2, 4, 6 a 1, ottenendo 13.

## [prg-040] argomenti: controllo-flusso
Nel programma della tabella delle moltiplicazioni (for (int i = 1; i <= 10; ++i) printf("%d * %d = %d \n", n, i, n * i);), quale è l'ultima riga stampata con n = 4?
1. 10 * 4 = 40
2. 4 * 11 = 44
3. 4 * 10 = 40
4. 4 * 9 = 36
5. 4 * 10 = 14
RISPOSTA: 3
SPIEGAZIONE: La condizione i <= 10 è vera anche per i = 10 e falsa per i = 11; gli argomenti di printf sono n, i, n * i, quindi l'ultima riga è 4 * 10 = 40.
