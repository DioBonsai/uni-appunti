# 06A_funzioni

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
Funzioni
Strumenti per organizzare e riutilizzare il 
codice, deﬁnizione e realizzazione delle 
funzioni.
1

<!-- pagina 2 -->
Funzioni
• Finora abbiamo scritto tutto dentro main(). Per programmi semplici può 
bastare, ma appena il codice cresce diventa lungo, ripetitivo, difﬁcile da 
capire e mantenere.
• Scrivere programmi grandi richiede strumenti adeguati per organizzare il 
codice.
“The key to writing large programs is to never write large programs.” 
  - Gerald M. Weinberg, The Psychology of Computer Programming, 1971
• Esempio: supponiamo di dover calcolare più volte il massimo tra due 
numeri.
– Senza funzioni: ogni volta copiamo il codice, con rischio di errori, 
duplicazioni inutili e codice ripetitivo e noioso
– Con funzioni: separiamo il codice per il calcolo del massimo, e lo 
riutilizziamo quando serve
2

<!-- pagina 3 -->
Funzioni
• Nel linguaggio C una funzione* è un blocco di codice con un 
nome, che può ricevere dati in ingresso (parametri), eseguire 
istruzioni e restituire un risultato (valore di ritorno).
• Le funzioni servono a organizzare il programma in parti 
indipendenti, riutilizzabili e più facili da leggere e mantenere.
• Il concetto di funzione in C ha un forte parallelo con quello 
matematico, ma non coincide completamente con esso.
3
* Talvolta chiamate anche metodi, procedure, subroutines.

<!-- pagina 4 -->
Concetto matematico di funzione
Rivediamo il concetto matematico di funzione.
• Siano A e B due insiemi di valori. Una funzione 
f : A → B 
associa ad ogni elemento x ∈ A un unico elemento f(x) ∈ B
–
A è il dominio
–
B è il codominio
–
f(x) è il valore associato all’argomento x
• Esempio:
f : ℝ → ℝ,
f(x) = x²
–
La scrittura f : ℝ → ℝ speciﬁca dominio e codominio;
–
La regola di corrispondenza f(x) = x² speciﬁca come viene determinato il valore 
associato a ogni argomento.
• Applicazione / valutazione:   f(3) = 9
Vediamo ora come questi elementi (argomenti, regola di corrispondenza e 
valore restituito) vengono rappresentati nella sintassi delle funzioni C.
4

<!-- pagina 5 -->
Funzioni
5
Sintassi generale delle funzioni:
1.
<tipo_ritorno> nomeFunzione(<lista_parametri>) {
2.
    // corpo della funzione
3.
    istruzioni;
4.
    return valore;   // opzionale se tipo_ritorno è void
5.
}
SINTASSI
• <tipo_ritorno>: il tipo del valore che la funzione restituisce (int, ﬂoat, …, oppure 
void se non restituisce alcun valore)
• nomeFunzione: identiﬁcatore che permette di chiamare la funzione da altre parti 
del programma
• <lista_parametri>: parametri di ingresso usate dalla funzione, con tipo e nome
• Corpo (function body): insieme di istruzioni da eseguire
• return: valore restituito al chiamante (obbligatorio se il tipo di ritorno non è void)

<!-- pagina 6 -->
Funzioni
Deﬁniamo una funzione C square:
6
1.
float square(float x);
1.
float square(float x) {
2.
    return x * x;
3.
}
Analogo alla specifica di dominio e codominio f : ℝ → ℝ
La funzione è poi deﬁnita speciﬁcando il codice da eseguire:
Realizza la regola di corrispondenza:   f(x) = x²
La chiamata applica la funzione ad un argomento:
1.
float x2 = square(3.14f);
2.
float y2 = square(y);
Analogo alla valutazione della funzione:   y = f(x)
Il prototipo della funzione dichiara il nome della funzione, il tipo dei 
parametri e il tipo del valore restituito.

<!-- pagina 7 -->
Prototipo, Definizione e Chiamata di Funzione
• Prototipo (function prototype)  [opzionale]
– Dice al compilatore che la funzione esiste, e quali sono il 
suo nome, il tipo di ritorno e i tipi dei parametri
– Non contiene il codice
• Deﬁnizione (function deﬁnition o implementation)
– Contiene il codice con le istruzioni da eseguire
– Deve rispettare il prototipo (tipi e numero parametri, tipo 
di ritorno)
• Chiamata (function call o invocation)
– Usa la funzione in un’espressione o istruzione
– Passa valori attuali ai parametri formali
7

<!-- pagina 8 -->
Funzioni: un primo esempio
1. #include <stdio.h>
2.
3. // PROTOTIPO (dichiarazione)
4. float square(float x);
5.
6. int main(void) {
7.    float a = 3.14f;
8.    float risultato = square(a);   // CHIAMATA alla funzione
9.    printf("%f al quadrato = %f\n", a, risultato);
10. }
11.
12. // DEFINIZIONE (implementazione)
13. float square(float x) {
14.    return x * x;   // RETURN: restituisce un float al chiamante
15. }
8

<!-- pagina 9 -->
Funzioni matematiche e funzioni C
La nozione di funzione in C riprende molti elementi della nozione 
matematica di funzione, ma non è equivalente
• Il dominio A trova una corrispondenza nei valori ammessi per il 
parametro, rappresentati in C dal tipo degli argomenti.
• Il codominio B trova una corrispondenza nei valori che la funzione 
può restituire, determinati dal tipo di ritorno.
• La regola di corrispondenza f(x) è realizzata dalle istruzioni nel 
corpo della funzione.
• La valutazione:    y = f(a) 
corrisponde alla chiamata della funzione:  B y = f(a);
Una funzione C può quindi essere usata per realizzare
 una funzione matematica come procedimento di calcolo.
9

<!-- pagina 10 -->
Ma una funzione C è diversa
Fin dove arriva il parallelo?
• Una funzione matematica
– è una deﬁnizione, una relazione tra valori;
– associa a ogni elemento del dominio un unico risultato nel codominio;
– non implica esecuzione né stato: a parità di argomento, il risultato è lo 
stesso.
• Una funzione C
– descrive un comportamento computazionale eseguito su una macchina;
– può calcolare e restituire un valore, oppure non restituirne alcuno (void);
– può leggere o modiﬁcare lo stato del programma, producendo effetti 
collaterali;
– può quindi produrre comportamenti diversi anche con gli stessi argomenti.
10

<!-- pagina 11 -->
Esempi di funzioni in C
Funzioni con valore di ritorno e parametri. 
Ricevono dati in ingresso e restituiscono un 
risultato.
11
int max(int a, int b) {
    return (a > b) ? a : b;
}
Funzioni con valore di ritorno ma senza parametri.
Non ricevono input, ma calcolano e restituiscono 
qualcosa.
Senza valore di ritorno (void) ma con parametri.
Eseguono un’azione ma non restituiscono un valore.
Senza valore di ritorno e senza parametri.
Usate per azioni generali, es. messaggi di servizio.
int leggiNumero(void) {
    int x;
    scanf("%d", &x);
    return x;
}
void stampaQuadrato(float x) {
    printf("%f\n", x * x);
}
void saluto(void) {
    printf("Ciao!\n");
}

<!-- pagina 12 -->
Istruzioni e memoria
12
0x0010
0x004B
main
square
...
1.
#include <stdio.h>
2.
3.
int square(int x);
4.
5.
int main(void) {
6.
    printf("main addr %p\n", main);
7.
    printf("square addr %p\n", square);
8.
}
9.
10.
int square(int x) {
11.
 return x * x;
12.
}
• Le funzioni, dopo la compilazione, sono memorizzate nella sezione codice del 
programma
• In C, il nome della funzione rappresenta l’indirizzo della sua prima istruzione, 
e di fatto è un puntatore al codice (puntatore a funzione)
word size
$ ./func_addr
main addr 0x0010
square addr 0x004B

<!-- pagina 13 -->
Funzioni
Parametri multipli. Una funzione può avere più parametri separati da 
virgola. Ogni parametro ha tipo e nome.
float potenza(float base, int exp);
La chiamata di funzione passa in ordine i parametri
float risultato = potenza(10, 3); // base=10, exp=3
Singolo valore di ritorno. In C una funzione può restituire al massimo un 
valore tramite return. Se serve restituire più valori ci sono due possibilità
• si usano puntatori/parametri di uscita
• oppure si costruiscono strutture dati (struct) [non lo vedremo]
13

<!-- pagina 14 -->
Funzioni
Prototipi con soli tipi. Nei prototipi, i nomi dei parametri sono facoltativi 
(utile per brevità, ma per chiarezza è sempre meglio indicare i nomi).
float potenza(float, int);
Regole per return. Separiamo i due casi:
1. Funzioni con ritorno (int, ﬂoat, …)
a. Ogni percorso di esecuzione di una funzione non-void deve arrivare a un 
return <espressione> appropriato.
b. Buona pratica: un solo return alla ﬁne
2. Funzioni void
a. Possono omettere return.
b. Facoltativo: esplicitare il punto di uscita con:   return;
14

<!-- pagina 15 -->
Passaggio dei parametri
Parametro formale. Variabile deﬁnita nella dichiarazione/deﬁnizione della 
funzione. È come una variabile locale alla funzione che contiene il valore 
passato all’inizio della chiamata
int square(int x) {   // x è un parametro formale
    return x * x;
}
Argomento (o parametro attuale). Valore che viene passato alla funzione al 
momento della chiamata, e viene copiato nel parametro formale 
corrispondente
int y = square(5);    // 5 è un argomento
int z = square(y);    // y è un argomento
Passaggio. In C l'argomento viene passato per valore (by value): il suo valore 
viene copiato nel parametro formale corrispondente.
15

<!-- pagina 16 -->
Passaggio per valore (per copia)
Il passaggio dei parametri attuali alla funzione chiamata 
avviene sempre per valore (by value). Viene cioè passata 
una copia del valore, assegnata al parametro formale 
corrispondente.
La funzione può modiﬁcare quindi solo una copia locale, non 
può inﬂuenzare eventuali variabili del chiamante. 
void incr(int x) { x++; } // non modifica il chiamante
Tuttavia possiamo passare (by value) un puntatore. 
Vedremo nel dettaglio questo schema più avanti.
16

<!-- pagina 17 -->
Passaggio dei parametri
17
Termine
Dove si trova
Significato
Esempio in C
Parametro 
formale
Nella definizione 
della funzione
Variabile locale alla funzione che riceve 
un valore quando la funzione viene 
chiamata
int square(int x) 
→ x è formale
Argomento (o 
parametro attuale)
Nella chiamata 
della funzione
Valore passato al parametro formale
square(5) 
→ 5 è attuale
Passaggio by 
value
Meccanismo 
predefinito in C
L’argomento viene copiato nel parametro 
formale, il chiamante non cambia
incr(x) 
non modifica x
Passaggio di un 
indirizzo
Con puntatori
Si passa per valore un puntatore alla 
variabile del chiamante; attraverso il 
puntatore la funzione può effettuare un 
accesso indiretto.
incrPtr(&x) 
modifica x nel 
chiamante
Chiamata di 
funzione
Nel codice del 
chiamante
Applicazione della funzione agli 
argomenti
y = square(5);

<!-- pagina 18 -->
Errori comuni
• Dimenticare il return in funzioni non void
int square(int x) {
    x * x;   // ERRORE: manca return
}
Il compilatore tipicamente segnala un warning: una funzione non-void 
deve restituire il valore previsto.
• Tipi incoerenti tra prototipo e deﬁnizione
// Prototipo
float square(float x);
// Definizione
int square(int x) { // ERRORE: tipi diversi dal prototipo
    return x * x;
}
18

<!-- pagina 19 -->
Errori comuni
• Numero o ordine errato di parametri
int max(int a, int b);
int main(void) {
    int m = max(10);      // ERRORE: manca un argomento
    int n = max(10, 3.5); // conversione implicita: 3.5 → 3
}
• Funzioni troppo “pesanti”
void gestisciTutto(void) {
    // fa input, calcoli, stampa, scrittura su file...
}
Meglio spezzare in più funzioni semplici (una funzione = un compito)
19

<!-- pagina 20 -->
Chiarezza nei nomi
• Parametri confusi o poco chiari
// cosa fa f?  cosa significano a, b, c?
int f(int a, int b, int c);
Meglio:
int calcolaPrezzo(int quantita, int sconto, int iva);
20

<!-- pagina 21 -->
Dividere un programma in 
funzioni
Pianiﬁcare le funzioni necessarie 
usando la strategia divide et impera
21

<!-- pagina 22 -->
Dalla complessità ai mattoncini
• Programmi complessi sono difﬁcili da leggere e 
mantenere se scritti in un unico blocco
• Strategia: scomporre il problema in 
sottoproblemi più semplici
• Ogni sottoproblema = una funzione
• Metodo noto come dìvide et ìmpera
22
Strategia
1. Identiﬁcare il problema principale
2. Suddividerlo in sottoproblemi logici
3. Scrivere una funzione per ciascun sottoproblema
4. Combinare le funzioni per ricostruire la soluzione completa
La decomposizione può essere iterata (sottoproblemi ulteriormente divisi)

<!-- pagina 23 -->
Esempio 
Calcolo di area e circonferenza di un cerchio con input validato.
Letto in input un valore reale non negativo r che rappresenta il 
raggio di un cerchio, calcolare e mostrare la circonferenza C=2πr e 
l’area A=πr2. Ripetere l’acquisizione dell’input se non valido (manca 
o r<0).
23
Scomposizione in sottoproblemi:
• Leggere e validare l’input
• Calcolare la circonferenza
• Calcolare l’area
• Presentazione dei risultati

<!-- pagina 24 -->
Sviluppo del problema (1 di 3)
24
#include <stdio.h>
#include <stdbool.h>
#include <math.h>     // per M_PI
// --- Prototipi ---
float leggiRaggio(void);
float circonferenza(float r);
float area(float r);
void stampaRisultati(float r, float c, float a);
// --- Main ---
int main(void) {
    float r = leggiRaggio();
    float c = circonferenza(r);
    float a = area(r);
    stampaRisultati(r, c, a);
}
// --- Implementazioni ---
Continua

<!-- pagina 25 -->
Sviluppo del problema (2 di 3)
25
// Funzione di input con validazione
float leggiRaggio(void) {
    float r;
    bool ripeti;
    do {
        printf("Inserisci il raggio (>= 0): ");
        int esito = scanf("%f", &r);
        // Validazione dell’input
        ripeti = false;
        if (esito != 1) {
            printf("Errore: inserisci un numero reale.\n");
            ripeti = true;
        } 
        else if (r < 0) {
            printf("Errore: il raggio deve essere non negativo.\n");
            ripeti = true;
        }
    } while (ripeti);
    return r;
}
Continua

<!-- pagina 26 -->
Sviluppo del problema (3 di 3)
26
// Funzione di calcolo: circonferenza
float circonferenza(float r) {
    return 2 * M_PI * r;
}
// Funzione di calcolo: area
float area(float r) {
    return M_PI * r * r;
}
// Funzione di presentazione dei risultati
void stampaRisultati(float r, float c, float a) {
    printf("Raggio = %.2f\n", r);
    printf("Circonferenza = %.2f\n", c);
    printf("Area = %.2f\n", a);
}

<!-- pagina 27 -->
Benefici della scomposizione
• Leggibilità: main() mostra solo la logica complessiva
• Riutilizzo: le funzioni possono servire in altri programmi
• Manutenzione: modiﬁcare una funzione senza toccare il resto
• Testabilità: è più semplice veriﬁcare una funzione piccola e 
autonoma
Approcci all’ordine di scomposizione:
• Top-down: partire dal problema generale, scrivere il main(), e poi 
dettagliare le funzioni
• Bottom-up: costruire prima le funzioni elementari, e poi il main()
Entrambi gli approcci si integrano nella pratica
27

<!-- pagina 28 -->
Progettare buone funzioni
Principi generali:
• Una funzione = un compito chiaro: deve fare una cosa sola, in modo 
semplice e leggibile (noto come SRP: Single Responsibility Principle)
• Nomi signiﬁcativi e coerenti: verbi per azioni e nomi per valori 
(stampaRisultati, calcolaArea, …)
• Separazione delle responsabilità: distinguere funzioni di input, di calcolo 
e di output, ecc…
Leggibilità e manutenzione:
• Evitare funzioni troppo lunghe, difﬁcile da leggere e testare
• Suddividere ulteriormente se una funzione diventa troppo complessa
• Commentare il “cosa”, non il “come”: il codice deve spiegarsi da solo
Rivedrete questi principi (avendo più esperienza) in Ingegneria del Software
28
