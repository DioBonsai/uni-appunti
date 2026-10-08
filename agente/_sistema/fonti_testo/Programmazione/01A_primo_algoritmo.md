# 01A_primo_algoritmo

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
Un primo algoritmo
Introduzione passo-passo al concetto di 
algoritmo

<!-- pagina 2 -->
Vocabolario
Calcolatore (IT) / Computer (EN) 
• Originariamente persona che 
eseguiva calcoli manualmente, 
con l’ausilio di strumenti come 
carta e penna o calcolatrici 
meccaniche
• Dagli anni ‘50, un dispositivo 
elettromeccanico 
programmabile al ﬁne di 
svolgere calcoli anche 
complessi
2

<!-- pagina 3 -->
L’informatica non è la scienza dei 
calcolatori. Non più di quanto 
l’astronomia sia la scienza dei 
telescopi o la chirurgia la scienza dei 
bisturi.
– Edsger W. Dijkstra
L’informatica studia gli algoritmi, 
non i dispositivi.
Che cosa non è l’Informatica
3

<!-- pagina 4 -->
Che cos'è l’Informatica
Informatica = lo studio degli algoritmi, che comprende: 
• Le loro proprietà formali e matematiche: studiare 
algoritmi corretti, efﬁcienti
• Le loro realizzazioni ﬁsica: progettare e realizzare 
computer per eseguire gli algoritmi
• Le loro realizzazioni linguistiche: progettare linguaggi di 
programmazione per scrivere eseguire gli algoritmi
• Le loro applicazioni: progettare applicazioni software 
(algoritmi implementati) per problemi importanti 
4

<!-- pagina 5 -->
Vocabolario: Algoritmo
• Un procedimento di calcolo ben deﬁnito 
eseguibile meccanicamente da un essere umano 
o da una macchina per ottenere un dato risultato 
(output) a partire da certi dati di partenza (input)
• Prende il nome dal matematico persiano 
Muhammad al-Khwarismi (vissuto intorno 
all’anno 800), il cui libro “Calcoli con i numerali 
indiani” descrive algoritmi di calcolo per le 
operazioni aritmetiche con i numeri indiani.
5
• Algoritmo: Un insieme ordinato di operazioni non 
ambigue ed effettivamente computabili che, 
quando eseguito, produce un risultato e si arresta 
in un tempo ﬁnito

<!-- pagina 6 -->
In informatica tutto è numero
Prima di parlare di programmi, ﬁssiamo un’idea fondamentale:
ogni informazione che un computer manipola 
è rappresentata come numero.
• Testi, immagini, suoni, istruzioni e dati diversi sembrano 
oggetti molto differenti, ma nella memoria del computer 
sono tutti codiﬁcati come numeri, precisamente come 
sequenze di bit (numeri in formato binario).
• Un programma imperativo lavora modiﬁcando valori numerici 
memorizzati nello stato della macchina.
• Programmare signiﬁca descrivere come questi valori devono 
essere trasformati passo dopo passo.
6

<!-- pagina 7 -->
Programmazione imperativa
•
Nella programmazione imperativa il programma è composto 
da una sequenza ordinata di istruzioni al computer, nella forma 
di un’istruzione per riga (una riga = una istruzione)
•
Terminata l’esecuzione della riga n-esima, viene eseguita 
l’istruzione della riga (n+1)-esima se non speciﬁcato 
diversamente
•
Esempi di istruzioni per la macchina
– assegna un valore ad una variabile
– somma due variabili e  memorizza il risultato in una terza variabile
– confronta due variabili
– salta ad una riga diversa dalla successiva (sotto una certa 
condizione)
7

<!-- pagina 8 -->
Progettare un algoritmo
•
Consideriamo il problema di calcolare la moltiplicazione fra due numeri 
interi m ed n ≥ 0.
•
Dobbiamo deﬁnire:
–
Input: i due valori m ed n
–
Output: il valore m x n
–
Passi: una sequenza non ambigua di operazioni che la macchina è in grado di 
eseguire
–
Terminazione: la sequenza deve raggiungere l'output e arrestarsi dopo un 
numero ﬁnito di passi
•
Assumiamo che la nostra macchina non disponga direttamente della 
moltiplicazione, ma sappia eseguire operazioni elementari come somma, 
assegnamento e confronto.
•
Progettare l'algoritmo signiﬁca quindi costruire il risultato richiesto 
usando soltanto queste operazioni disponibili.
8

<!-- pagina 9 -->
Algoritmo per moltiplicazione tra interi
• Riconduciamo la moltiplicazione a un'operazione che 
la nostra ipotetica macchina sa eseguire: l'addizione.
• Per n ≥ 0 vale
m  x  n   =  m  +  m  +  ...  +  m
9
Sommo m a sé stesso n-1 volte
• Possiamo scrivere la stessa operazione partendo 
dall'elemento neutro della somma:
s = 0 +  m  +  m  +  ...  +  m
Sommo n volte m all’elemento neutro 0
elemento 
neutro
• Resta da stabilire come eseguire meccanicamente 
esattamente n addizioni e poi fermarsi.

<!-- pagina 10 -->
Algoritmo per moltiplicazione tra interi
• Esempio per m = 4  e  n = 3
• Deﬁnisco la somma parziale 
   
s = 0
10
 s=0
         
parziale
iniziale
●Tengo traccia delle 
addizioni già effettuate 
con le dita della mano
s = 0

<!-- pagina 11 -->
Algoritmo per moltiplicazione tra interi
• Esempio per m = 4  e  n = 3
• Dopo la 1° addizione, s vale 4.
11
   0 +
   4 =
------ 
 s=4  
      
1o parziale
Ho completato 
una addizione
s = 0 + 4

<!-- pagina 12 -->
Algoritmo per moltiplicazione tra interi
• Esempio per m = 4  e  n = 3
• Dopo la 2° addizione, s vale 8.
12
   0 +
   4 =
------ 
   4 +
   4 =
------
 s=8  
   
1o parziale
2o parziale
Ho completato 
due addizioni
s = 0 + 4 + 4

<!-- pagina 13 -->
Algoritmo per moltiplicazione tra interi
• Esempio per m = 4  e  n = 3
• Dopo la 3° addizione, s vale 12.
13
   0 +
   4 =
------ 
   4 +
   4 =
------
   8 +
   4 =
------
s=12
1o parziale
2o parziale
3o parziale
e totale
Ho completato 
tre addizioni e 
mi fermo
s = 0 + 4 + 4 + 4

<!-- pagina 14 -->
Algoritmo per moltiplicazione tra interi
•
La moltiplicazione è realizzata sommando ripetutamente il valore 
m ad una somma parziale s, inizialmente uguale a 0, per n volte
•
Per poter eseguire questo algoritmo in modo meccanico dobbiamo 
disporre di due strumenti:
–
un accumulatore s per tenere traccia della somma parziale (equivalente 
del foglio di carta su cui faccio le addizioni)
–
un contatore i per tenere traccia del numero di addizioni
(equivalente al numero di dita della mano usate per contare le ripetizioni)
14
Due concetti essenziali della programmazione, su cui torneremo spesso: 
1.
DATI: i valori su cui il programma opera, e il modo in cui vengono organizzati.
2.
PROCEDURE: le operazioni e i procedimenti che trasformano questi dati.
Questa idea si può sintetizzare con la frase (di Niklaus Wirth):
Programma = Algoritmi + Strutture Dati
Un programma è la combinazione di come rappresentiamo i dati e di come deﬁniamo 
le operazioni che li elaborano.

<!-- pagina 15 -->
Algoritmo per moltiplicazione tra interi
Scriviamo ora l’algoritmo di moltiplicazione tra due interi m 
ed n ≥ 0 come una sequenza esplicita di passi basata su 
somme ripetute.
1.
Preliminarmente, impostare al valore neutro 0 
l’accumulatore s, ed impostare a 0 il contatore i. 
2.
Sommare m a s esattamente n volte, aggiornando il 
contatore i per tenere traccia del numero di addizioni 
effettuate, e contemporaneamente aggiornare 
l’accumulatore s per tenere traccia del risultato parziale
15
Punto 2 semanticamente complesso.

<!-- pagina 16 -->
Algoritmo per moltiplicazione tra interi
Miglioriamo la formulazione per l’algoritmo di 
moltiplicazione tra due interi m ed n ≥ 0 come una 
sequenza esplicita di passi basata su somme ripetute.
1.
Preliminarmente, imposta al valore neutro 0 
l’accumulatore s, ed imposta a 0 il contatore i. 
2.
Somma m all’accumulatore s 
3.
Somma 1 al contatore i
4.
Se i = n allora il numero di addizioni richieste è stato 
effettuato e s corrisponde con al totale, altrimenti 
ripetere il punto 2
16

<!-- pagina 17 -->
Verifica dell’algoritmo di moltiplicazione
• Abbiamo sviluppato un algoritmo che risolve la 
moltiplicazione tra interi attraverso quattro punti in 
ordine dato.
• L’algoritmo è stato sviluppato a partire da una coppia di 
valori «di prova» di m ed n pari a m=4 ed n=3 
• L’algoritmo ritorna un risultato corretto anche per un 
input diverso?
• Veriﬁchiamo il funzionamento per un caso particolare 
dove n=0 per cui il risultato atteso è 0 (m x 0 = 0)
17

<!-- pagina 18 -->
Verifica dell’algoritmo di moltiplicazione
• Esempio per m=4  e  n = 0
• Risultato atteso s = 0
18
 s=0
i=0

<!-- pagina 19 -->
Verifica dell’algoritmo di moltiplicazione
• Esempio per m=4  e  n = 0
• Risultato atteso s = 0
• Dopo la 1° addizione, s vale 4
ed i viene incrementato ad 1
• La condizione i = n non sarà mai 
veriﬁcata!
• L’algoritmo non termina mai!
19
   0 +
   4 =
------ 
 s=4 +
i=1

<!-- pagina 20 -->
Analisi dell’algoritmo di moltiplicazione
• Nella formulazione precedente, prima aggiorno s ed i, e dopo 
confronto il contatore i con il numero di addizioni n
• Se n è pari a 0, l’algoritmo non terminerà mai (sempre i>n)
• Dobbiamo quindi prima veriﬁcare che il contatore i sia 
inferiore ad n, e solo dopo eventualmente eseguire 
l’addizione
• Il paradigma di progetto degli algoritmi 
«prima veriﬁcare le condizioni e solo dopo 
 eseguire (la prima di una serie di) operazioni» 
ci accompagnerà nel resto di questo insegnamento
• La gestione del caso iniziale è una tipica fonte di errori, 
anche in sede d’esame
20

<!-- pagina 21 -->
Algoritmo per moltiplicazione tra interi
Scriviamo una terza formulazione dell’algoritmo  di 
moltiplicazione fra numeri interi m ed n tramite somme 
ripetute.
• [1] Preliminarmente, imposta l’accumulatore s al valore 
neutro 0, ed imposta il contatore i a 0. 
• [2] Se i = n allora il numero di addizioni richieste è stato 
effettuato e s corrisponde con al totale, quindi 
terminiamo. Altrimenti continuiamo.
• [3] Somma m all’accumulatore s 
• [4] Somma 1 al contatore i
• [5] Ritorna alla riga 2.
21

<!-- pagina 22 -->
Algoritmo per moltiplicazione tra interi
Introduciamo una notazione più formale: 
• ←operatore di assegnamento di numero intero a variabile
• = operatore di confronto tra variabili intere
Quindi:
• [1] s ← 0,  i ← 0
• [2] Se i = n l’algoritmo termina, altrimenti
•    [3] s ← s + m 
▷ somma m ad s
•    [4] i ← i + 1 
▷ incrementa di 1 il contatore i
•    [5] ritorna alla riga 2
22
Rientro lasciato di proposito per indicare che le operazioni sono condizionate alla valutazione 
della condizione alla riga [2]
É troppo forte parlare di terminazione: potremmo voler 
eseguire altre istruzioni dopo la moltiplicazione. Riformuliamo.

<!-- pagina 23 -->
Algoritmo per moltiplicazione tra interi
Quindi:
• [1] s ← 0,  i ← 0
• [2] Se i = n vai alla riga 6, altrimenti
– [3] s ← s + m 
– [4] i ← i + 1 
– [5] salta alla riga 2
• [6] Fine
23
• Introduciamo quindi una speciale istruzione Fine per terminare l’algoritmo.
• Usiamo il salto verso un’istruzione numerata per ripetere passi o 
terminare.
• Riformuliamo ancora una volta l’algoritmo usando questa convenzione.

<!-- pagina 24 -->
Algoritmo per moltiplicazione tra interi
Quindi:
• [1] s ← 0,  i ← 0
• [2] Se i = n allora salta alla riga 6, altrimenti
– [3] s ← s + m 
– [4] i ← i + 1 
– [5] salta alla riga 2
• [6] Fine
24
• Per uniformità delimitiamo i blocchi con delle coppie di 
istruzioni speciali Inizio/Fine.
• Riformuliamo di nuovo.

<!-- pagina 25 -->
Algoritmo per moltiplicazione tra interi
Quindi:
• [1] Inizio Algoritmo
• [2] s ← 0,  i ← 0
• [3] Inizio Ripetizione Condizionata
      Se i = n allora salta alla riga 7, altrimenti
– [4] s ← s + m  
– [5] i ← i + 1 
– [6] salta alla riga 3
• [7] Fine Ripetizione Condizionata
• [8] Fine Algoritmo
25
Salto condizionato
Salto non condizionato

<!-- pagina 26 -->
Algoritmo per moltiplicazione tra interi
La struttura ci permette di eliminare i numeri di riga:
• Inizio Algoritmo
– s ← 0,  i ← 0
– Inizio Ripetizione Condizionata
Se i = n salta alla Fine Ripetizione Condizionata, altrimenti
• s ← s + m  
• i ← i + 1 
• salta all’Inizio Ripetizione Condizionata
– Fine Ripetizione Condizionata
• Fine Algoritmo
26
I linguaggi di programmazione strutturati organizzano le 
istruzioni in blocchi annidabili; l’indentazione rende visibile 
questa struttura gerarchica e l’appartenenza di ogni 
istruzione al proprio blocco.

<!-- pagina 27 -->
Terminologia
Programma: descrizione di un algoritmo attraverso un 
linguaggio di programmazione
Linguaggio di programmazione:
• insieme di parole e di regole, deﬁnite in modo formale, 
per consentire la programmazione di un calcolatore 
afﬁnché esegua compiti predeterminati
• I linguaggi di programmazione sono:
– di basso livello (es. linguaggio macchina, assembly, etc.)
– di alto livello vicini al linguaggio naturale (es. FORTRAN, 
C, Java, Python, etc.)
27

<!-- pagina 28 -->
“Programma” per moltiplicazione tra interi
• Prima di passare al linguaggio di programmazione vero e 
proprio, introduciamo ancora una rappresentazione 
intermedia: il diagramma di ﬂusso (ﬂow-chart).
• Il ﬂow-chart mette in evidenza il ﬂusso di controllo, 
mostrando graﬁcamente le possibili sequenze di esecuzione 
tra le istruzioni.
• A differenza della rappresentazione strutturata vista prima, il 
ﬂow-chart non rende esplicito l’annidamento dei blocchi, ma 
segue direttamente i collegamenti tra le istruzioni.
• È una forma di rappresentazione storicamente molto usata e 
talvolta utile per visualizzare il controllo; i linguaggi moderni 
preferiscono però esprimere direttamente strutture di 
controllo annidate.
28

<!-- pagina 29 -->
“Programma” per moltiplicazione tra interi
29
YES 
Inizio
Fine
NO
i = n ?
s ← s + m
i ← i +1
i ← 0
s ← 0
Il salto avviene a 
condizione che il 
contatore i sia 
uguale ad n
Il salto avviene 
senza condizioni

<!-- pagina 30 -->
“Programma” per moltiplicazione tra interi
•
Abbiamo un’idea di come implementare* il nostro algoritmo di 
moltiplicazione su un vero computer
•
Lo scopo di questo corso è imparare ad implementare algoritmi 
elementari (molto semplici) nel linguaggio C, ovvero
•
Tradurre** degli algoritmi speciﬁcati in Italiano in C
•
Ci interessa quindi studiare un modello di calcolo che può essere 
eseguito su di un calcolatore meccanico o elettronico: la macchina 
di Von Neumann.
* realizzare concretamente una procedura usando un linguaggio di programmazione, partendo 
dalla sua deﬁnizione logica.
** nell'esame di Algoritmi lo scopo sarà invece quello di analizzare e progettare nuovi 
algoritmi.
30
