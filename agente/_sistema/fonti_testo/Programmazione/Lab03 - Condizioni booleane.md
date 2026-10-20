# Lab03 - Condizioni booleane

<!-- pagina 1 -->
A.A. 2026/27
Programmazione I
Laboratorio
DIPARTIMENTO DI 
INFORMATICA
CORSO DI LAUREA 
TRIENNALE
Condizioni booleane
Lezione nº 3

<!-- pagina 2 -->
Espressioni booleane
Quali valori assumono queste espressioni logiche:
• 3>5 || 10 == 7+3
• 3 != 5 && (6 < 2 || 5+2 == 10 - 3)
• 3 < 5 < 7
• 4 > 3 > 2
• 3 < 5 && 5 < 7
• 3 < 5 && 7 < 5
• true && false
• true && 5 < 7
• false || 5 < 10
2

<!-- pagina 3 -->
Espressioni booleane
Quali valori assumono queste espressioni logiche:
• 3>5 || 10 == 7+3
• 3 != 5 && (6 < 2 || 5+2 == 10 - 3)
• 3 < 5 < 7
• 4 > 3 > 2
• 3 < 5 && 5 < 7
• 3 < 5 && 7 < 5
• true && false
• true && 5 < 7
• false || 5 < 10
3
true
true
NO!
NO!
true
false
false
true
(3<5)<7 ⇒1<7 
vero ma per il motivo sbagliato!
(4>3)>2 ⇒1>2 ⇒FALSO!
true

<!-- pagina 4 -->
Booleani
Leggere il codice del file booleani.c per vedere vari esempi 
di operazioni booleane in C. 
Procedere con gli esercizi successivi solo dopo aver capito 
tutte le operazioni di questo codice.
NOTA: le leggi di De Morgan stabiliscono relazioni di 
equivalenza tra gli operatori di congiunzione e disgiunzione
logica. Si possono sintetizzare come
¬(a ∧b)  =  ¬a ∨¬b
¬(a ∨b)  =  ¬a ∧¬b
4
REMINDER: compiliamo usando i comandi:
●Unix:  
gcc -Wall booleani.c -o booleani
●Windows:  gcc -Wall booleani.c -o booleani.exe

<!-- pagina 5 -->
Esercizi booleani da completare
Aprire il codice di esercizi_booleani.c, e implementare i 6 
punti indicati:
1. dati i due interi a e b, stampa 1 se il primo intero è multiplo del 
secondo, 0 altrimenti;
2. dato l’intero a (un voto), stampa "true" se a è compreso fra 1 e 
30 (inclusi), "false" altrimenti;
3. dati i due booleani b1 e b2, stampa a video il booleano “false" 
se b1 e b2 sono entrambi veri, "true" altrimenti;
4. dati i due interi a e b, stampa a video il massimo; se sono uguali 
stampa a video "I due valori sono uguali".
5. dati tre interi a, b e c, stampa a video il massimo (si usi una 
variabile di supporto max); 
6. dati tre interi a, b e c, stampa a video "ordinati" se questi sono 
ordinati in modo crescente, altrimenti non stampare nulla.
5

<!-- pagina 6 -->
Saluti!
Scrivere un programma saluta.c che chieda l'ora all'utente 
(come numero intero) e stampi a terminale il saluto più 
appropriato tra: 
• “Buongiorno”
• “Buon pomeriggio”
• “Buonasera”
• “Buona notte”
Definite voi quali intervalli usare per decidere il saluto più 
appropriato.
6

<!-- pagina 7 -->
Scelte su interi
Sulla pagina Moodle trovate un esercizio con nome
Aprite il link e premete il tasto
per avviare l’esercizio.
7
Lab03-Es1 Scelte su Interi
Tenta il quiz adesso

<!-- pagina 8 -->
Come funziona Coderunner
8
Testo dell’esercizio
Leggere con cura prima di 
iniziare a scrivere il codice!
Area di lavoro in cui scrivere il 
codice C del programma.
Compila ed esegui.
Potete verificare il codice quante 
volte volete.
Il programma viene eseguito per 
diversi input, e viene controllato 
che le stampe generate con printf 
corrispondano con quelle attese

<!-- pagina 9 -->
Esiti della verifica della risposta
9
Errore di compilazione!
NOTA: viene compilato con:  -Wall -Werror
Il programma compila ed esegue, ma non 
passa tutti i test definiti, cioè non produce in 
output il testo atteso.
Il programma compila, esegue, e passa tutti 
i test, cioè produce tutti gli output attesi.

<!-- pagina 10 -->
Niente panico!
• La compilazione e l’esecuzione con degli input 
predefiniti (test) è automatica: l’obiettivo è scrivere 
un codice robusto, che risponda correttamente a 
input diversi.
• Gli input proposti sono formulati per testare varie 
casistiche.
Non è l’esame, l’esercizio non viene valutato!
NOTA: l’interfaccia web riporta in alcuni punti dei 
messaggi sui punteggi, che potete ignorare.
10

<!-- pagina 11 -->
Errori 1/2
Quali errori vedete in questo codice?
#include <stdio.h>
int main() {
int voto;
scanf("%d", &voto);
if (voto >= 18);
printf("Esame passato.\n");
}
11

<!-- pagina 12 -->
Errori 1/2
Quali errori vedete in questo codice?
#include <stdio.h>
int main() {
int voto;
scanf("%d", &voto);
if (voto >= 18);
printf("Esame passato.\n");
}
12
È un errore particolarmente insidioso perché il codice compila senza 
segnalare problemi. Per il linguaggio C è come se avessimo scritto:
if (voto >= 18)
;     // istruzione vuota
printf("Esame passato.\n");

<!-- pagina 13 -->
Errori 2/2
Quali errori vedete in questo codice?
#include <stdio.h>
int main() {
int voto;
scanf("%d", &voto);
if (voto >= 18)
printf("Esame passato.\n"); 
else
printf("Esame non passato.\n"); 
printf("Ripresentarsi al prossimo appello.\n");
}
13

<!-- pagina 14 -->
Errori 2/2
Quali errori vedete in questo codice?
#include <stdio.h>
int main() {
int voto;
scanf("%d", &voto);
if (voto >= 18)
printf("Esame passato.\n"); 
else {
printf("Esame non passato.\n"); 
printf("Ripresentarsi al prossimo appello.\n");
}
}
14
Mancano le graffe per un blocco else con più di un’istruzione!
Anche questo è un errore particolarmente insidioso perché il codice 
compila senza segnalare problemi. Per il linguaggio C solo la prima 
istruzione dopo la parola chiave else è eseguita nel blocco 
condizionale. L’ultima printf è quindi eseguita sempre!

<!-- pagina 15 -->
Errori 2/2
È sempre meglio mettere i blocchi condizionali tra parentesi 
graffe, a meno che non siano molto brevi ed evidenti.
#include <stdio.h>
int main() {
int voto;
scanf("%d", &voto);
if (voto >= 18) {
printf("Esame passato.\n"); 
}
else {
printf("Esame non passato.\n"); 
printf("Ripresentarsi al prossimo appello.\n");
}
}
15

<!-- pagina 16 -->
Emersione del massimo con 4 variabili
Sulla pagina Moodle trovate un esercizio con nome
Avete visto a lezione un esercizio simile (ma più semplice). 
Completate il programma, assicurandovi che passi tutti i 
test proposti.
16
Lab03-Es2 Emersione del Massimo

<!-- pagina 17 -->
Selezione operazioni
Scrivere un programma selezione_operazioni.c che:
1. Chiede all’utente di inserire tre numeri interi x1, x2 e x3.
2. Stampa il seguente testo:
a. “scrivi 1 per calcolare la somma”
b. “scrivi 2 per calcolare il prodotto”
c. “scrivi 3 per calcolare la media”
3. Chiede all’utente di inserire un numero (tra 1, 2 o 3) 
corrispondente ad un’operazione.
4. Se l'operazione selezionata non è tra quelle proposte, 
deve essere stampato a video un messaggio di errore 
appropriato.
5. Altrimenti effettua l’operazione selezionata sugli interi 
x1, x2 e x3, e visualizza il risultato ottenuto.
17

<!-- pagina 18 -->
Risoluzione equazioni di secondo grado
Avete visto a lezione il flusso semplificato per la risoluzione 
di equazioni di secondo grado. Realizzate lo schema di 
risoluzione completo, che considera anche tutti i casi limite.
18
Scrivere un programma 
equaz_secondo.c che prende in 
ingresso i tre coefficienti a, b e c, e 
calcola, ove possibile, le radici 
dell’equazione di secondo grado
ax2 + bx + c = 0
e le stampa. Quando non 
possibile, stampa invece un 
messaggio di errore appropriato, e 
termina.

<!-- pagina 19 -->
Flusso risoluzione:   ax2+ bx + c = 0

<!-- pagina 20 -->
Risoluzione equazioni
Trovare le soluzioni usando i seguenti coefficienti:
20
a
b
c
x1
x2
0
0
0
Indeterminata
0
0
4
Impossibile
0
2
-4
2
1
0
-121
11
-11
1
2
1
-1
1
-3
10
Radici complesse coniugate
5
20
0
0
-4
NOTA: per calcolare la radice quadrata, usare la funzione sqrt( )
definita in <math.h>.  Per calcolare il valore assoluto, usare la 
funzione abs( ) definita in <stdlib.h>.

<!-- pagina 21 -->
Sasso-carta-forbici-lucertola-Spock
•
Sasso-carta-forbici-lucertola-Spock (rock-paper-scissors-lizard-Spock)
è una variante fantasiosa inventata da due studenti statunitensi, 
Sam Kass e Karen Bryla, e resa successivamente famosa nel 
telefilm The Big Bang Theory[1]. 
•
È un'estensione a cinque stati della Morra Cinese, in cui vengono 
aggiunti la lucertola e Spock (celebre personaggio della saga Star Trek).
21
[1] Da Wikipedia Italia. https://it.wikipedia.org/wiki/Morra_cinese

<!-- pagina 22 -->
Sasso-carta-forbici-lucertola-Spock
Sulla pagina Moodle trovate un esercizio con nome
Seguite il testo e completate l’esercizio.
NOTA: come fare a determinare se “gli input non sono stati 
letti”? Avete visto a lezione che la funzione scanf restituisce 
il numero di specificatori di conversione che sono stati letti 
con successo dallo standard input.
22
Lab03-Es3 Sasso-carta-forbici-lucertola-Spock
