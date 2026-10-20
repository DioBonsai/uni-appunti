# 04A_iterazioni

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
Cicli e ripetizioni
Iterazioni strutturate per eseguire azioni 
più volte

<!-- pagina 2 -->
Iterazioni
• Quando un programma deve ripetere un’operazione più volte, 
non ha senso copiare lo stesso codice decine di volte: serve 
un meccanismo di ripetizione controllata
• Le iterazioni (o cicli) sono gli strumenti della 
programmazione strutturata per ripetere blocchi di istruzioni 
in modo controllato e leggibile
2

<!-- pagina 3 -->
Il ciclo while
• Serve a ripetere un blocco di istruzioni ﬁnché una condizione 
logica è vera.
3
1.
while (condizione) {
2.
    // blocco di istruzioni da ripetere
3.
}
SINTASSI
Funzionamento:
• Viene valutata la condizione. Se è vera, il blocco di istruzioni viene 
eseguito, poi si ripete. Se è falsa, il ciclo termina e si passa 
all’istruzione immediatamente successiva al while.
• Se la condizione è inizialmente falsa → nessuna esecuzione del blocco
• Se la condizione rimane sempre vera → ciclo inﬁnito

<!-- pagina 4 -->
Stampare i numeri da 0 a 9
• Terna fondamentale di ogni ciclo: 
inizializzazione, condizione, aggiornamento
• Itera per i = 0, 1, 2, …, 8, 9. 
• Quando i==10 la condizione i < 10 è falsa ed il ciclo termina. 
4
1. #include <stdio.h>
2.
3. int main(void) {
4.    int i = 0;
5.
6.    while (i < 10) {
7.        printf("%d\n", i);
8.        i++;
9.    }
10. }

<!-- pagina 5 -->
Stampare i numeri da 0 a 9
La terna fondamentale di ogni ciclo 
(inizializzazione, condizione, aggiornamento) si 
presta a una spiegazione graﬁca con un diagramma 
di ﬂusso, per evidenziare il ruolo di ciascun 
elemento nel controllo del ciclo.
5
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    int i = 0;
5.
6.
    while (i < 10) {
7.
        printf("%d\n", i);
8.
        i++;
9.
    }
10.
}
print(i)
i < 10 ?
true
false
inizio
ﬁne
i ← 0
i ← i + 1

<!-- pagina 6 -->
Conto alla rovescia
• Manteniamo: inizializzazione, condizione, aggiornamento
• Non esiste solo l’incremento: l’aggiornamento può essere un 
decremento e la condizione può essere “invertita”. 
• La logica del ciclo dipende dal problema, non ha una forma ﬁssa.
6
1. #include <stdio.h>
2.
3. int main(void) {
4.    int i = 5;
5.
6.    while (i > 0) {
7.        printf("%d\n", i);
8.        i--;
9.    }
10. }

<!-- pagina 7 -->
Sommatoria e variabili accumulatore
• Il ciclo while non serve solo a ripetere istruzioni, ma spesso serve a 
costruire progressivamente un risultato, come ad esempio una 
somma accumulata
• Usiamo quindi una variabile accumulatore opportunamente 
inizializzata e modiﬁcata
7
1. int n = 5, i = 1, somma = 0;
2. while (i <= n) {
3.    somma = somma + i;
4.    i++;
5. }
6. printf("Somma = %d\n", somma);

<!-- pagina 8 -->
Lettura input con valore di terminazione
• Valore di terminazione (o valore 
sentinella): qualsiasi altezza 
negativa
• Ogni altezza valida (≥0) aggiorna 
somma (variabile accumulatore) e 
count (variabile contatore)
• Ciclo termina quando utente 
inserisce intero negativo
• Accumulatore e contatore permette 
di calcolare la media al termine
8
1. int somma = 0, count = 0, altezza = 0;
2.
3. while (altezza >= 0) {
4.    printf("Inserisci altezza: ");
5.    scanf("%d", &altezza);
6.
7.    if (altezza >= 0) {
8.        somma += altezza;
9.        count++;
10.    }
11. }
12. printf("Media = %f\n", 
13.       somma / (float)count);
• Non sempre possiamo stabilire subito quante iterazioni dobbiamo 
effettuare, come ad esempio quando leggiamo un input.
• Esempio: media altezze

<!-- pagina 9 -->
Visibilità delle variabili nei blocchi
• Ogni blocco { ... } introduce un ambito 
di visibilità (scope) locale
• Le variabili dichiarate all’interno (es. y) 
esistono solo durante l’esecuzione di 
quel blocco
• Ad ogni iterazione del ciclo, una nuova 
istanza delle variabili locali viene 
allocata sullo stack e poi deallocata
9
#include <stdio.h>
int main(void) {
   int x = 1; // visibile in tutto main()
   while (x < 3) {
       // y visibile solo dentro il blocco
       int y = x * 2;  
       printf("x=%d, y=%d\n", x, y);
       x++;
   }
   // printf("%d", y); 
   // ERRORE: y non è più visibile qui
}
Area codice
…
x
Area codice
…
x
…
y
Blocco main
Blocco while

<!-- pagina 10 -->
Visibilità delle variabili nei blocchi
10
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
▶   int x = 1;
5.
6.
    while (x < 3) {
7.
        int y = x * 2;  
8.
        printf("x=%d, y=%d\n", x, y);
9.
        x++;
10.
    }
11.
    printf("x finale=%d", x);
12.
}
Area codice
1
x
Indirizzi di memoria crescenti
word size
$ ./stampaDoppi

<!-- pagina 11 -->
Visibilità delle variabili nei blocchi
11
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    int x = 1;
5.
6.
▶   while (x < 3) {
7.
        int y = x * 2;  
8.
        printf("x=%d, y=%d\n", x, y);
9.
        x++;
10.
    }
11.
    printf("x finale=%d", x);
12.
}
Area codice
1
x
Indirizzi di memoria crescenti
word size
$ ./stampaDoppi
La condizione di 
continuazione (x < 3) è 
soddisfatta

<!-- pagina 12 -->
Visibilità delle variabili nei blocchi
12
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    int x = 1;
5.
6.
    while (x < 3) {
7.
▶       int y = x * 2;  
8.
        printf("x=%d, y=%d\n", x, y);
9.
        x++;
10.
    }
11.
    printf("x finale=%d", x);
12.
}
Area codice
1
x
Indirizzi di memoria crescenti
word size
$ ./stampaDoppi
2
y
La variabile y viene allocata 
sullo stack e diventa visibile 
(cioè accessibile)

<!-- pagina 13 -->
Visibilità delle variabili nei blocchi
13
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    int x = 1;
5.
6.
    while (x < 3) {
7.
        int y = x * 2;  
8.
▶       printf("x=%d, y=%d\n", x, y);
9.
        x++;
10.
    }
11.
    printf("x finale=%d", x);
12.
}
Area codice
1
x
Indirizzi di memoria crescenti
word size
$ ./stampaDoppi
x=1 y=2
2
y

<!-- pagina 14 -->
Visibilità delle variabili nei blocchi
14
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    int x = 1;
5.
6.
    while (x < 3) {
7.
        int y = x * 2;  
8.
        printf("x=%d, y=%d\n", x, y);
9.
▶       x++;
10.
    }
11.
    printf("x finale=%d", x);
12.
}
Area codice
1 2
x
Indirizzi di memoria crescenti
word size
$ ./stampaDoppi
x=1 y=2
2
y
Incremento x di 1

<!-- pagina 15 -->
Visibilità delle variabili nei blocchi
15
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    int x = 1;
5.
6.
    while (x < 3) {
7.
        int y = x * 2;  
8.
        printf("x=%d, y=%d\n", x, y);
9.
        x++;
10.
▶   }
11.
    printf("x finale=%d", x);
12.
}
Area codice
2
x
Indirizzi di memoria crescenti
word size
$ ./stampaDoppi
x=1 y=2
y
Quando il blocco di codice {...} 
termina le variabili visibili solo 
al suo interno vengono 
deallocate dallo stack

<!-- pagina 16 -->
Visibilità delle variabili nei blocchi
16
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    int x = 1;
5.
6.
▶   while (x < 3) {
7.
        int y = x * 2;  
8.
        printf("x=%d, y=%d\n", x, y);
9.
        x++;
10.
    }
11.
    printf("x finale=%d", x);
12.
}
Area codice
2
x
Indirizzi di memoria crescenti
word size
$ ./stampaDoppi
x=1 y=2
La condizione di 
continuazione (x < 3) è ancora 
soddisfatta - ripetiamo di 
nuovo il ciclo

<!-- pagina 17 -->
Visibilità delle variabili nei blocchi
17
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    int x = 1;
5.
6.
    while (x < 3) {
7.
▶       int y = x * 2;  
8.
        printf("x=%d, y=%d\n", x, y);
9.
        x++;
10.
    }
11.
    printf("x finale=%d", x);
12.
}
Area codice
2
x
Indirizzi di memoria crescenti
word size
$ ./stampaDoppi
x=1 y=2
4
y
La variabile y viene 
nuovamente allocata sullo 
stack e diventa visibile.

<!-- pagina 18 -->
Visibilità delle variabili nei blocchi
18
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    int x = 1;
5.
6.
    while (x < 3) {
7.
        int y = x * 2;  
8.
▶       printf("x=%d, y=%d\n", x, y);
9.
        x++;
10.
    }
11.
    printf("x finale=%d", x);
12.
}
Area codice
2
x
Indirizzi di memoria crescenti
word size
$ ./stampaDoppi
x=1 y=2
x=2 y=4
4
y

<!-- pagina 19 -->
Visibilità delle variabili nei blocchi
19
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    int x = 1;
5.
6.
    while (x < 3) {
7.
        int y = x * 2;  
8.
        printf("x=%d, y=%d\n", x, y);
9.
▶       x++;
10.
    }
11.
    printf("x finale=%d", x);
12.
}
Area codice
2 3
x
Indirizzi di memoria crescenti
word size
$ ./stampaDoppi
x=1 y=2
x=2 y=4
4
y
Incremento x di 1

<!-- pagina 20 -->
Visibilità delle variabili nei blocchi
20
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    int x = 1;
5.
6.
    while (x < 3) {
7.
        int y = x * 2;  
8.
        printf("x=%d, y=%d\n", x, y);
9.
        x++;
10.
▶   }
11.
    printf("x finale=%d", x);
12.
}
Area codice
3
x
Indirizzi di memoria crescenti
word size
$ ./stampaDoppi
x=1 y=2
x=2 y=4
y
Quando il blocco di codice {...} 
termina le variabili visibili solo 
al suo interno vengono 
deallocate dallo stack

<!-- pagina 21 -->
Visibilità delle variabili nei blocchi
21
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    int x = 1;
5.
6.
▶   while (x < 3) {
7.
        int y = x * 2;  
8.
        printf("x=%d, y=%d\n", x, y);
9.
        x++;
10.
    }
11.
    printf("x finale=%d", x);
12.
}
Area codice
3
x
Indirizzi di memoria crescenti
word size
$ ./stampaDoppi
x=1 y=2
x=2 y=4
La condizione di 
continuazione (x < 3) non è 
più soddisfatta, quindi il ciclo 
termina

<!-- pagina 22 -->
Visibilità delle variabili nei blocchi
22
1.
#include <stdio.h>
2.
3.
int main(void) {
4.
    int x = 1;
5.
6.
    while (x < 3) {
7.
        int y = x * 2;  
8.
        printf("x=%d, y=%d\n", x, y);
9.
        x++;
10.
    }
11.
▶   printf("x finale=%d", x);
12.
}
Area codice
3
x
Indirizzi di memoria crescenti
word size
$ ./stampaDoppi
x=1 y=2
x=2 y=4
x finale=3
La variabile y non è quindi accessibile dopo il 
completamento del ciclo. 
Se il suo valore ci servisse, possiamo:
●
dichiarare y fuori dall’iterazione
●
copiarne il valore in una variabile visibile 
nel main prima della terminazione

<!-- pagina 23 -->
Indovinare numeri
• Un ciclo può anche terminare per una condizione di successo dipendente 
dal contesto (non contatori o valori di terminazione)
• Cicli while sono molto ﬂessibili e generali, è sufﬁciente:
– esprimere opportuna condizione booleana 
– provvedere a inizializzazione/aggiornamento variabili di controllo
23
1. int segreto = 12345, guess = -1;
2. while (guess != segreto) {
3.    printf("Indovina il pin segreto: ");
4.    scanf("%d", &guess);
5. }
6. printf("Bravo, hai indovinato!\n");

<!-- pagina 24 -->
Errori comuni
Se la condizione non è mai falsa, abbiamo un ciclo inﬁnito
24
1. #include <stdio.h>
2.
3. int main(void) {
4.    int i = 0;
5.
6.    while (i < 10) {
7.        printf("%d\n", i);
8.        // manca i++;
9.    }
10. }

<!-- pagina 25 -->
Il ciclo for
• In molti casi sappiamo già quante iterazioni servono
• Il ciclo for è una variante sintattica più compatta e leggibile
25
1.
for (inizializzazione; condizione; aggiornamento) {
2.
    // blocco di istruzioni da ripetere
3.
}
SINTASSI
Funzionamento:
• Inizializzazione: eseguita una sola volta prima del ciclo, le variabili che 
dichiara sono visibili sono dentro al for
• Condizione: valutata prima di ogni iterazione
• Aggiornamento: eseguito dopo ogni iterazione
Equivale ad un caso particolare del while, ma più ordinato (gli elementi di 
controllo sono scritti vicino, riduce errori)

<!-- pagina 26 -->
Equivalenza del ciclo for e while
• Il ciclo for è un modo compatto per scrivere un ciclo while 
assieme alla terna di controllo fondamentale (inizializzazione, 
condizione, aggiornamento) 
26
1.
for (inizializzazione; condizione; aggiornamento) {
2.
    // blocco di istruzioni da ripetere
3.
}
1.
{
2.
    inizializzazione;
3.
    while (condizione) {
4.
        // blocco di istruzioni da ripetere
5.
        aggiornamento;
6.
    }
7.
}

<!-- pagina 27 -->
Il ciclo for
• Il for è il modo naturale per percorrere un intervallo di valori numerici
– Deﬁniamo un intervallo di valori numerici come:
• un valore iniziale (es. 0)
• una condizione di appartenenza all’intervallo (es. x<10)
• un passo (es. +1, +2, -1, …)
27
• Esempio: numeri nell’intervallo semiaperto [0, 10)
  (inizio 0, condizione: <10, passo: +1)
1.
for (int i = 0; i < 10; i++) {
2.
    printf("%d\n", i);
3.
}

<!-- pagina 28 -->
Il ciclo for
28
• Esempio: numeri pari nell’intervallo chiuso [0, 40]
  (inizio 0, condizione: ≤40, passo: +2)
1.
for (int i = 0; i <= 40; i += 2) {
2.
    ...
3.
}
• Esempio: numeri nell’intervallo chiuso [0, n] e in ordine decrescente
  (inizio n, condizione: ≥0, passo: -1)
1.
int n = 10;
2.
for (int i = n; i >= 0; i--) {
3.
    ...
4.
}

<!-- pagina 29 -->
Il ciclo for
29
• Esempio: calcolare la somma ﬁno ad N:
quindi intervallo [1, N]
• Esempio: stampare tabellina del 5
  quindi intervallo [1, 10]
1.
int somma = 0;
2.
for (int i = 1; i <= N; i++) {
3.
    somma += i;
4.
}
1.
for (int i = 1; i <= 10; i++) {
2.
    printf("%d x 5 = %d\n", i, i*5);
3.
}

<!-- pagina 30 -->
I cicli annidati
• Gli elementi della programmazione strutturata sono combinabili: un 
ciclo può contenere nel suo blocco di codice un altro ciclo annidato
• Esempio: stampa griglia di numeri
30
1.
for (int r = 0; r < 3; r++) {
2.
    for (int c = 0; c < 3; c++) {
3.
        printf("(%d,%d) ", r, c);
4.
    }
5.
    printf("\n");
6.
}
• Ogni blocco introduce un ambito di visibilità locale (local scope)
• Le variabili di un ciclo sono visibili all’interno del proprio blocco (e quindi 
anche dentro a blocchi annidati)
• Esempio: r visibile sia nel ciclo esterno che in quello interno, mentre c é 
visibile sono nel ciclo interno.

<!-- pagina 31 -->
Errori comuni nei cicli for
• Condizione sempre vera → ciclo inﬁnito
for (int i = 0; i >= 0; i++) { ... }  // mai falso
• Aggiornamento mancante
for (int i = 0; i < 10; ) { ... }  // i non cambia, ciclo inﬁnito
• Off-by-one (indice errato)
for (int i = 0; i <= 10; i++) { ... }  // 11 iterazioni invece di 10
• Uso improprio della variabile di controllo
for (int i = 0; i < 10; i++) {
    i = i + 2;   // altera manualmente il contatore
}
• Scope della variabile contatore
for (int i = 0; i < 5; i++) { ... }
printf("%d", i);  // ERRORE: i non esiste fuori dal for
31

<!-- pagina 32 -->
Quando usare while o for
• for
– Iterazioni note a priori
– Intervalli numerici (con passo costante)
– Contatore gestito in modo naturale e regolare
• while
– Iterazioni ignote in anticipo
– Condizione dipendente da input o eventi esterni
– Aggiornamento non numerico o irregolare
32

<!-- pagina 33 -->
Sentinelle nei cicli
• In molti casi non possiamo determinare all’inizio quante volte 
un ciclo dovrà ripetersi
• Serve quindi un meccanismo per decidere quando fermarsi
• Deﬁniamo due concetti importanti:
– Valore sentinella: un valore speciale che segnala la ﬁne 
delle iterazioni (es. leggo da input il valore -1)
– Variabile sentinella: una variabile booleana che controlla 
il proseguimento del ciclo
• Spesso vengono usati insieme: il valore sentinella serve ad 
aggiornare una variabile sentinella che controlla la 
terminazione del ciclo
33

<!-- pagina 34 -->
Sentinelle nei cicli
34
• Valore sentinella: valore speciale che segnala la ﬁne dei dati
Altri nomi comunemente usati:
– valore di terminazione
– marcatore di ﬁne input
– codice di arresto
– EOF (end of ﬁle)
• Variabile sentinella: variabile booleana di controllo del ciclo
Altri nomi comunemente usati:
– ﬂag di controllo (ﬂag=bandierina di segnalazione)
– controllo di ciclo (loop ﬂag)
– variabile di controllo di terminazione

<!-- pagina 35 -->
Esempio controllo con sentinelle
35
Esempio: trova il primo numero il cui quadrato è maggiore di 500
1.
int n = 1;
2.
bool trovato = false; // variabile sentinella
3.
4.
while (!trovato) {
5.
    int q = n * n;
6.
    if (q > 500) {
7.
        trovato = true;
8.
    }
9.
    else {
10.
        n++;
11.
    }
12.
}
13.
printf("%d x %d = %d\n", n, n, n*n);
1.
int n = 1;
2.
// n*n ≤ 500 valore sentinella
3.
while (n * n <= 500) {
4.
    n++;
5.
}
6.
printf("%d x %d = %d\n", n, n, n*n);

<!-- pagina 36 -->
Esempio controllo con sentinelle
36
1.
int somma = 0, count = 0;
2.
bool continua = true;   // variabile sentinella
3.
4.
while (continua) {
5.
    int altezza;
6.
    printf("Inserisci altezza (negativa per terminare): ");
7.
    scanf("%d", &altezza);
8.
9.
    if (altezza >= 0) {
10.
        somma += altezza;
11.
        count++;
12.
    } 
13.
    else { // altezza é un valore sentinella (<0)
14.
        continua = false; // aggiorna la sentinella, il ciclo finisce
15.
    }
16.
}
17.
printf("Media = %f\n", somma / (float)count);
Esempio: calcola la media delle altezze lette in input, ﬁnché l'utente non 
inserisce valore negativo.

<!-- pagina 37 -->
Controllo di flusso esplicito
• Il linguaggio deﬁnisce due keywords per il controllo esplicito del ﬂusso di 
controllo in un ciclo
– istruzione break: interrompe immediatamente il ciclo corrente. Il ﬂusso 
riprende immediatamente dopo il ciclo
– istruzione continue: salta il resto del blocco di codice per l’iterazione 
corrente, e passa subito alla prossima valutazione della condizione
• Possono essere utili in casi particolari, peggiorano la leggibilità
• Eviteremo di usarli: meglio esplicitare le condizioni di terminazione tramite 
variabili sentinella di controllo
37
1.
for (int i = 0; i < 10; i++) {
2.
    if (i == 5)
3.
        break;   // stop al ciclo
4.
    printf("%d ", i);
5.
}
1.
for (int i = 0; i < 10; i++) {
2.
    if (i % 2 == 0)
3.
        continue; // salta i pari
4.
    printf("%d ", i);
5.
}

<!-- pagina 38 -->
Il ciclo do..while
Variante del while in cui la valutazione della condizione è posticipata.
38
1.
do {
2.
    // blocco di istruzioni da ripetere
3.
} while (condizione);
SINTASSI
Funzionamento:
• Viene sempre eseguito il blocco di codice almeno una volta, poi si 
ripete se la condizione è vera.
• Utile per alcuni scenari speciﬁci (es. validazione dell’input)
1.
int x, retval;
2.
do {
3.
    printf("Inserisci un numero [1,10]: ");
4.
    retval = scanf("%d", &x);
5.
    // ripeti se input non valido o non compreso nell’intervallo [1,10]
6.
} while (retval == 0 || !(1 <= x || x <= 10));
7.
8.
printf("Hai inserito %d\n", x);
