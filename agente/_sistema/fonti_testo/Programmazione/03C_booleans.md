# 03C_booleans

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
Espressioni booleane
Operatori logici per decidere nei 
programmi

<!-- pagina 2 -->
Perché servono le espressioni booleane?
• Un programma non si limita a fare calcoli: deve prendere 
decisioni
• Le condizioni ci permettono di dire al computer “se succede 
questo, allora fai quello”
• Le espressioni booleane sono il linguaggio delle condizioni, 
con cui traduciamo domande del tipo:
– “Il numero di somme ripetute richieste è stato raggiunto?”
– “L’input da tastiera è corretto?”
– “Lo studente ha superato l’esame?”
• Sono il ponte tra dati (numerici) e scelte logiche.
• Senza logica, un programma sarebbe solo una lunga sequenza 
rigida di calcoli.
2

<!-- pagina 3 -->
Operatori logici e relazionali in C
3
Notazione 
matematica
Operatore 
C
Signiﬁcato logico
Espressione in C
Risultato
x = y
==
Uguaglianza
x == y
1 se uguali, altrimenti 0
x ≠ y
!=
Diversità
x != y
1 se diversi, altrimenti 0
x > y
>
Maggiore
x > y
1 se vero, altrimenti 0
x < y
<
Minore
x < y
1 se vero, altrimenti 0
x ≥ y
>=
Maggiore o uguale
x >= y
1 se vero, altrimenti 0
x ≤ y
<=
Minore o uguale
x <= y
1 se vero, altrimenti 0
b ∧ c
&&
AND (congiunzione)
x > 0 && y > 0
1 se entrambe vere
b ∨ c
||
OR (disgiunzione)
x == 0 || y == 0
1 se almeno una vera
¬b
!
NOT (negazione)
!(x > 0)
Inverte il valore logico

<!-- pagina 4 -->
Espressioni tra numeri: esempi
• Veriﬁca completamento delle ripetizioni
contatore != n
• Controllo uguaglianza di password numeriche
pinInserito == pinCorretto
• Veriﬁca ordine tra valori
temperatura <= limiteMax
• Controllo sufﬁcienza all’esame
voto >= 18
4
ATTENZIONE:
== è l’uguaglianza, mentre
 = è l’assegnamento

<!-- pagina 5 -->
Il tipo bool in C
• Le condizioni in logica di Bool⁕ possono assumere solo due valori:
true (vero)
e
false (falso)
• Storicamente, il C non aveva un tipo booleano tra i tipi primitivi, e si usavano 
gli interi (int), con questa interpretazione
– 0 
→ falso
– diverso da 0 → vero
• Nel C moderno (dal C99) esiste l’header
#include <stdbool.h>
• che introduce:
– Il tipo bool (simile ad int, ma chiarisce che le variabili sono booleane)
– Le costanti true e false
• Cercheremo di usare il C moderno dove possibile.
5
⁕ La logica di Bool (o algebra booleana) è un sistema matematico basato su due valori (vero/falso) e sugli 
operatori fondamentali AND, OR e NOT, alla base di circuiti digitali e programmazione.

<!-- pagina 6 -->
Variabili di tipo bool
#include <stdio.h>
#include <stdbool.h>
int main(void) {
    int x = 1;
    bool b = false;
    int y = 2;
}
Area codice
0
1
x
2
y
b
Rappresentiamo in 
memoria una 
variabile booleana 
come un singolo bit 
(0 o 1)

<!-- pagina 7 -->
Variabili condizionali
#include <stdio.h>
#include <stdbool.h>
int main(void){
    int votoScritto = 25;
    int sogliaSuff = 18;
    bool superato = votoScritto >= sogliaSuff;
    printf("Lo studente supera l’esame? %d\n", superato);
}
$ ./boolean 
Lo studente supera l’esame? 1
superato é una variabile 
booleana che memorizza il 
risultato della valutazione di una 
condizione
Non c’è uno specificatore di 
formato per il tipo bool: si usa 
%d, come per gli interi, e quindi 
verrà stampato 0 oppure 1.

<!-- pagina 8 -->
Espressioni booleane
• Nella programmazione spesso non basta veriﬁcare una singola 
condizione. Occorre stabilire il rapporto logico tra più condizioni 
contemporaneamente.
• Le variabili booleane, che assumono solo i valori vero o falso, 
possono essere combinate per esprimere:
– Congiunzione (AND): entrambe le condizioni devono essere vere
condizione1 && condizione2
– Disgiunzione (OR): è sufﬁciente che almeno una sia vera
condizione1 || condizione2
– Negazione (NOT): l’opposto del valore della condizione
!condizione
8

<!-- pagina 9 -->
Espressioni booleane: esempi
Il login è possibile se il numero di tentativi < 3 e l’account non è bloccato
bool login = (numTentativi < 3) && !accountBloccato;
Il riscaldamento si accende se la temperatura < 18 e il termostato è attivo
bool riscaldamento = (temperatura < 18) && termostatoOn;
————————————————————————————————
Lo sconto è applicato se l’età < 12 oppure l’utente è tesserato
bool sconto = (eta < 12) || tesserato;
Il ventilatore si accende se temperatura >= 28 oppure é in modo manuale
bool ventolaAccesa = (temperatura >= 28) || modoManuale;
9

<!-- pagina 10 -->
Tavola di verità – Operatore AND
Deﬁnizione: L’operatore logico AND restituisce vero (1) solo se entrambe 
le condizioni sono vere. 
In tutti gli altri casi restituisce falso (0).
10
condizione1
condizione2
condizione1 && condizione2
0 (falso)
0 (falso)
0 (falso)
0 (falso)
1 (vero)
0 (falso)
1 (vero)
0 (falso)
0 (falso)
1 (vero)
1 (vero)
1 (vero)
condizione1
condizione2
condizione1 && condizione2

<!-- pagina 11 -->
Tavola di verità – Operatore OR
Deﬁnizione: L’operatore logico OR restituisce vero (1) se almeno una delle 
due condizioni è vera. 
Risulta falso (0) solo se entrambe le condizioni sono false.
11
condizione1
condizione2
condizione1 || condizione2
0 (falso)
0 (falso)
0 (falso)
0 (falso)
1 (vero)
1 (vero)
1 (vero)
0 (falso)
1 (vero)
1 (vero)
1 (vero)
1 (vero)
condizione1
condizione2
condizione1 || condizione2

<!-- pagina 12 -->
Tavola di verità – Operatore NOT
Deﬁnizione: L’operatore logico NOT restituisce l’opposto del valore della 
condizione
• Se la condizione è vera (1) → diventa falsa (0)
• Se la condizione è falsa (0) → diventa vera (1)
12
condizione1
!condizione1
0 (falso)
1 (vero)
1 (vero)
0 (falso)
condizione
!condizione

<!-- pagina 13 -->
Confronti su intervalli
• Nei programmi spesso dobbiamo veriﬁcare se un valore 
cade in un certo intervallo (indici, temperatura, età, ecc…)
• In matematica si scrive in modo compatto:
min ≤ x ≤ max
• In C invece bisogna spezzare il confronto in due 
condizioni e combinarle in AND:
min <= x && x <= max
• Questa è la forma più vicina alla notazione matematica
13

<!-- pagina 14 -->
Confronti su intervalli
14
Tipo di intervallo
Notazione per 
insiemi
Disuguaglianza
Espressione in C
Chiuso (inclusivo)
x ∈ [min, max]
  min ≤ x ≤ max
min <= x && x <= max
Semiaperto sinistro
x ∈ [min, max)
  min ≤ x < max
min <= x && x < max
Semiaperto destro
x ∈ (min, max]
  min < x ≤ max
min < x && x <= max
Aperto (esclusivo)
x ∈ (min, max)
  min < x < max
min < x && x < max
Useremo molto questa notazione per veriﬁcare se un indice 
appartiene ad un intervallo semiaperto (sinistro).

<!-- pagina 15 -->
Cortocircuitazione degli operatori logici
• Quando si combinano più condizioni logiche con AND o OR, il 
compilatore può interrompere l’esecuzione della valutazione 
appena il risultato è già determinato
• Questo comportamento si chiama cortocircuitazione (short-circuit 
evaluation)
– AND: se la prima condizione è falsa, il risultato sarà 
sicuramente falso → la seconda non viene valutata
– OR: se la prima condizione è vera, il risultato sarà sicuramente 
vero → la seconda non viene valutata
15

<!-- pagina 16 -->
16
cond1 ?
false
true
cond2 ?
cond1
cond2
cond1 && cond2
true
true
false
false
cond1 ?
false
true
cond2 ?
cond1
cond2
cond1 || cond2
true
true
false
false
Cortocircuitazione degli operatori logici

<!-- pagina 17 -->
Cortocircuitazione degli operatori logici
• Esempio: Vogliamo veriﬁcare che una variabile divisore sia diversa 
da zero e che la divisione dia un risultato maggiore di 5
bool condizione = (divisore != 0) && ((numeratore / divisore) > 5);
Se il divisore è 0, non eseguo la seconda parte (che causerebbe un errore 
runtime di divisione per 0).
• Esempio: utente ha inserito un numero, e questo é pari
int valore;
bool scanPari = (scanf("%d", &valore) == 1) && (valore % 2 == 0);
Se scanf non legge con successo, non veriﬁco cosa contiene valore.
17

<!-- pagina 18 -->
Condizioni booleane
#include <stdio.h>
#include <stdbool.h>
int main(void) {
    int numero;
    bool letto, positivo, dispari;
    printf("Inserisci un numero intero: ");
    letto = (scanf("%d", &numero) == 1); // true se scanf ha letto correttamente
    positivo = letto && (numero > 0);      // input valido e maggiore di 0
    dispari  = letto && (numero % 2 != 0); // input valido e non divisibile per 2
    // stampa i risultati (0 = falso, 1 = vero)
    printf("Input valido? %d\n", letto);
    printf("Numero positivo? %d\n", positivo);
    printf("Numero dispari? %d\n", dispari);
}
18

<!-- pagina 19 -->
Semplificare espressioni complesse
• Espressioni booleane con molti AND e OR mescolati diventano difﬁcili da 
leggere, facili da scrivere in modo sbagliato, complicate da modiﬁcare o 
estendere
• Esempio
bool sconto = registrato && spesaTotale >= 100 || 
              (codiceNonScaduto && attivatoDallUtente);
• Come procedere: spezzare l’espressione in sotto-condizioni con nomi chiari, 
usare variabili booleane intermedie, e rendere la condizione ﬁnale una 
combinazione semplice di pochi termini
bool clientePremium = registrato && (spesaTotale >= 100);
bool promoExtra     = codiceNonScaduto && attivatoDallUtente;
bool sconto         = clientePremium || promoExtra;
19

<!-- pagina 20 -->
Operatore condizionale ternario
L’operatore ternario è un operatore condizionale compatto
condizione ? valore_se_vero : valore_se_falso
Funzionamento: 
Viene valutata la condizione. L’espressione ternaria vale:
• se vera → restituisce valore_se_vero
• se falsa → restituisce valore_se_falso
È utile per piccole espressioni condizionali (ma solo se non 
pregiudica la semplicità del codice). 
int x = 5;
int y = (x % 2 == 0) ? 100 : 200;  // y = 200, perché x è dispari
Per condizioni più articolate, è meglio usare i blocchi if..else
20
