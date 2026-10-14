# 03D_decisioni

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
Dal flusso sequenziale 
alle decisioni
Introduzione al controllo di ﬂusso nella 
programmazione strutturata.

<!-- pagina 2 -->
La programmazione strutturata
2
Sequenza
Selezione
Iterazione
true
false
true
false
• Finora abbiamo scritto programmi in cui le istruzioni 
vengono eseguite prevalentemente una dopo l’altra.
• Per costruire algoritmi più articolati dobbiamo poter 
controllare l’ordine con cui vengono eseguite le 
istruzioni.
• La programmazione strutturata utilizza tre strutture di 
controllo fondamentali:
– Sequenza: esecuzione ordinata di istruzioni
– Selezione: scelta fra alternative (if)
– Iterazione: ripetizione condizionata (while, for, do-while)

<!-- pagina 3 -->
Tre strutture sono sufficienti
• Negli anni ’60 non era ancora chiaro quale fosse il giusto insieme 
di astrazioni per esprimere il ﬂusso di controllo di un programma.
3
• Nel 1966 Corrado Böhm e Giuseppe Jacopini 
mostrarono che sequenza, selezione e iterazione 
sono sufﬁcienti per rappresentare qualsiasi funzione 
calcolabile (teorema di Böhm–Jacopini).
• Questo risultato è alla base della programmazione strutturata e 
ha profondamente inﬂuenzato i linguaggi di programmazione 
moderni:
– poche strutture di controllo elementari, componibili e annidabili, 
permettono di costruire algoritmi arbitrariamente complessi.

<!-- pagina 4 -->
Dal flusso lineare alle decisioni
• Vediamo quindi come rappresentare le scelte:
– Se la condizione è vera → esegui un blocco di codice
– Se la condizione è falsa → fai qualcos’altro o passa oltre
• Questo meccanismo si chiama controllo di ﬂusso condizionato
4
Esempio
●Se piove → prendo l’ombrello
●Altrimenti → esco senza
1.
if (piove) {
2.
    printf("Prendi l'ombrello.\n");
3.
} 
4.
else {
5.
    printf("Esci senza.\n");
6.
}
SI
NO
inizio
piove?
prendi ombrello
esci senza
fine

<!-- pagina 5 -->
Il costrutto if
È il costrutto che permette al programma di “scegliere” cosa fare in 
base a una condizione logica (vero/falso).
5
1.
if (condizione) {
2.
    // codice eseguito solo se condizione è vera
3.
}
SINTASSI
• Se la condizione è vera (1) → entra nel blocco
• Se la condizione è falsa (0) → salta il blocco e continua dopo
1.
int voto = 25;
2.
if (voto >= 18) {
3.
    printf("Esame superato!\n");
4.
}

<!-- pagina 6 -->
Il costrutto if-else
Estende il costrutto if permettendo di gestire due percorsi alternativi.
6
1.
if (condizione) {
2.
    // blocco A: se condizione vera
3.
} 
4.
else {
5.
    // blocco B: se condizione falsa
6.
}
SINTASSI
• Se la condizione è vera (1) → entra nel blocco A
• Se la condizione è falsa (0) → entra nel blocco B
1.
int batteria = 15;
2.
3.
if (batteria < 20) {
4.
    printf("Batteria quasi scarica! Collega il caricatore.\n");
5.
} 
6.
else {
7.
    printf("Batteria sufficiente.\n");
8.
}

<!-- pagina 7 -->
Il costrutto if-elseif-else
Generalizzazione del costrutto if-else
7
1.
if (condizione1) {
2.
    // blocco 1
3.
} 
4.
else if (condizione2) {
5.
    // blocco 2
6.
} 
7.
else {
8.
    // blocco di default
9.
}
SINTASSI
• Se la condizione1 è vera (1) → entra nel blocco 1
• Altrimenti, se la condizione2 è vera (1) → entra nel blocco 2
• …
• Se tutte le condizioni precedenti sono false (0)
→ entra nel blocco di default

<!-- pagina 8 -->
Il costrutto if-elseif-else
8
char colore = 'G';   // R = Rosso, G = Giallo, V = Verde
if (colore == 'R') {
    printf("Fermati!\n");
} 
else if (colore == 'G') {
    printf("Attenzione, rallenta.\n");
} 
else if (colore == 'V') {
    printf("Puoi passare.\n");
} 
else {
    printf("Colore non valido!\n");
}

<!-- pagina 9 -->
Errori comuni
Usare = invece di ==
if (a = 5) { ... }  // ERRORE: assegnamento
Dimenticare le { }
if (x > 0) 
    printf("Positivo\n");
    printf("Errore!\n"); // eseguito sempre
In C è consentito omettere le parentesi graffe se dopo l’if c’è una 
sola istruzione. Tuttavia, questo può generare errori poco visibili: 
nell’esempio la seconda printf non dipende dall’if.
Per chiarezza è meglio usare sempre le { }, anche con una sola 
istruzione, salvo casi davvero ovvi.
9

<!-- pagina 10 -->
Errori comuni
• Ordine sbagliato delle condizioni
if (num % 2 == 0) {
    printf("Pari non nullo\n");
} 
else if (num == 0) {
    printf("Zero\n");   // Mai raggiunto
}
Si corregge controllando prima i casi più speciﬁci:
if (num == 0) {
    printf("Zero\n");
} 
else if (num % 2 == 0) {
    printf("Pari non nullo\n");
}
10

<!-- pagina 11 -->
Errori comuni
• Condizioni ridondanti o mai vere
if (x > 10) { 
    ... 
}
else if (x > 20) { 
    ... // mai eseguito!
}
else if (x > 50) { 
    ... // mai eseguito!
}
• Else mancante: è buona norma gestire sempre tutti i casi possibili 
del ﬂusso, così il programma non lascia situazioni non previste.
11

<!-- pagina 12 -->
Suggerimenti e buona prassi
• Molti errori nascono da piccoli errori sintattici o logici negli if.
• Abituarsi a pensare ai casi limite evita brutte sorprese.
• Usare sempre le parentesi graffe { }, anche se c’è una sola 
istruzione (evita ambiguità e bug difﬁcili da notare)
• Ordinare le condizioni dal caso più speciﬁco al più generale
• Mantenere le condizioni semplici e leggibili
12
1.
if (a > 10 && b < 5 || c == 7 && !(d%2)) {
2.
    ...
3.
}
1.
bool condA = (a > 10 && b < 5);
2.
bool condB = (c == 7 && d % 2 == 0);
3.
4.
if (condA || condB) { ... }
5.

<!-- pagina 13 -->
Esempio: stampa in ordine
Esempio: richiedi all’utente due interi x ed y da tastiera, e stampali dal 
minore (o uguale) al maggiore
13
void main() {
    int x, y;
    printf("Inserisci x:");
    scanf("%d", &x);
    printf("Inserisci y:");
    scanf("%d", &y);
    if (y < x) {
        printf ("%d %d", y, x);
    }
    else { // y >= x
        printf ("%d %d", x, y);
    }
}

<!-- pagina 14 -->
Esempio: stampa in ordine
Esempio: richiedi all’utente due interi x ed y da tastiera, e stampali dal 
minore (o uguale) al maggiore
14
void main() {
    int x, y;
    printf("Inserisci x:");
    scanf("%d", &x);
    printf("Inserisci y:");
    scanf("%d", &y);
    if (y < x) {
        //scambio condizionato
        int temp = x;
        x = y;
        y = temp;
    }
    printf ("%d %d", x, y);
}

<!-- pagina 15 -->
Visibilità nei blocchi condizionati
void main() {
▶   int x, y;
    printf("Inserisci x:");
    scanf("%d", &x);
    printf("Inserisci y:");
    scanf("%d", &y);
    if (y < x) {
        //scambio condizionato
        int temp = x;
        x = y;
        y = temp;
    }
    printf ("%d %d", x, y);
}
Area codice
?
x
?
y
Indirizzi di memoria crescenti
word size
$ ./scambioCond 
15

<!-- pagina 16 -->
Visibilità nei blocchi condizionati
void main() {
    int x, y;
    printf("Inserisci x:");
    scanf("%d", &x);
    printf("Inserisci y:");
    scanf("%d", &y);
▶   if (y < x) {
        //scambio condizionato
        int temp = x;
        x = y;
        y = temp;
    }
    printf ("%d %d", x, y);
}
Area codice
10
x
5
y
Indirizzi di memoria crescenti
word size
$ ./scambioCond
Inserisci x: 10
Inserisci y: 5 
16

<!-- pagina 17 -->
Visibilità nei blocchi condizionati
void main() {
    int x, y;
    printf("Inserisci x:");
    scanf("%d", &x);
    printf("Inserisci y:");
    scanf("%d", &y);
    if (y < x) {
        //scambio condizionato
▶       int temp = x;
        x = y;
        y = temp;
    }
    printf ("%d %d", x, y);
}
Area codice
10
x
5
y
Indirizzi di memoria crescenti
word size
$ ./scambioCond
Inserisci x: 10
Inserisci y: 5 
17
10
temp
La variabile temp dichiarata nel 
blocco di codice dell’if diventa visibile

<!-- pagina 18 -->
Visibilità nei blocchi condizionati
void main() {
    int x, y;
    printf("Inserisci x:");
    scanf("%d", &x);
    printf("Inserisci y:");
    scanf("%d", &y);
    if (y < x) {
        //scambio condizionato
        int temp = x;
▶       x = y;
        y = temp;
    }
    printf ("%d %d", x, y);
}
Area codice
10 5
x
5
y
Indirizzi di memoria crescenti
word size
$ ./scambioCond
Inserisci x: 10
Inserisci y: 5 
18
10
temp

<!-- pagina 19 -->
Visibilità nei blocchi condizionati
void main() {
    int x, y;
    printf("Inserisci x:");
    scanf("%d", &x);
    printf("Inserisci y:");
    scanf("%d", &y);
    if (y < x) {
        //scambio condizionato
        int temp = x;
        x = y;
▶       y = temp;
    }
    printf ("%d %d", x, y);
}
Area codice
10 5
x
5 10
y
Indirizzi di memoria crescenti
word size
$ ./scambioCond
Inserisci x: 10
Inserisci y: 5 
19
10
temp

<!-- pagina 20 -->
Visibilità nei blocchi condizionati
void main() {
    int x, y;
    printf("Inserisci x:");
    scanf("%d", &x);
    printf("Inserisci y:");
    scanf("%d", &y);
    if (y < x) {
        //scambio condizionato
        int temp = x;
        x = y;
        y = temp;
    }
▶   printf ("%d %d", x, y);
}
Area codice
10 5
x
5 10
y
Indirizzi di memoria crescenti
word size
$ ./scambioCond
Inserisci x: 10
Inserisci y: 5 
5 10
20
All’uscita del blocco di codice dell’if, la 
variabile temp dichiarata nel blocco esce 
dalla visibilità, viene cioè rimossa dallo stack 
e non è più accessibile.

<!-- pagina 21 -->
Annidamenti non necessari
21
int eta;
printf("Inserisci la tua età: ");
scanf("%d", &eta);
if (eta < 6) {
    printf("Biglietto gratuito\n");
} 
else {
    if (eta < 18) {
        printf("Biglietto ridotto\n");
    } 
    else {
        printf("Biglietto intero\n");
    }
}
int eta;
printf("Inserisci la tua età: ");
scanf("%d", &eta);
if (eta < 6) {
    printf("Biglietto gratuito\n");
} 
else if (eta < 18) {
    printf("Biglietto ridotto\n");
} 
else {
    printf("Biglietto intero\n");
}
Evitare annidamenti multipli se non strettamente 
necessario (rendono meno chiaro il codice)

<!-- pagina 22 -->
Schemi ricorrenti elementari
Determinare il massimo/minimo di due variabili
22
int a, b, max;
scanf("%d%d", &a, &b);
// determina il massimo tra a e b
if (a > b) {
    max = a;
} 
else {
    max = b;
}
// in questo punto max contiene 
//   il massimo tra a e b

<!-- pagina 23 -->
Schemi ricorrenti elementari
Validazione di input (scanf riuscito?). Prima di usare i dati, 
controlla che siano stati letti correttamente.
23
int valore;
if (scanf("%d", &valore) == 1) {
    printf("Hai inserito: %d\n", valore);
} 
else {
    printf("Input non valido\n");
}

<!-- pagina 24 -->
Schemi ricorrenti elementari
Protezione da operazioni illegali (es: divisione per zero)
24
if (divisore != 0) {
    printf("Risultato: %d\n", dividendo / divisore);
} 
else {
    printf("Errore: divisione per zero!\n");
}

<!-- pagina 25 -->
Schemi ricorrenti elementari
Controllo validità valori in determinati intervalli
25
float temperatura;
bool inputOk = scanf("%f", &temperatura) == 1;
// 0 <= temperatura_valida <= 100
if (inputOk && 0 <= temperatura && temperatura <= 100) {
    printf("Temperatura entro i limiti\n");
} 
else {
    printf("Temperatura fuori intervallo o lettura errata\n");
}
