# Capitolo 9: Laboratorio 3: Coderunner ed Esercizi sulle Scelte
## Gli esercizi su Moodle con Coderunner
Tre degli esercizi del laboratorio 3 sono quiz su **Moodle**, in un ambiente che si chiama **Coderunner**: sulla pagina del corso ci sono tre quiz (Lab03-Es1 «Scelte su Interi», Lab03-Es2 «Emersione del Massimo» e Lab03-Es3 «Sasso-carta-forbici-lucertola-Spock»), e si aprono con il pulsante «Tenta il quiz adesso». Le slide non riportano i testi dei tre quiz, ma solo i titoli e le indicazioni generali di funzionamento riassunte qui.

Nella pagina dell'esercizio si trovano il **testo** (da leggere con cura prima di scrivere codice), un'**area di lavoro** in cui scrivere il codice C del programma e un pulsante per **compilare ed eseguire**, che si può usare quante volte si vuole. Il programma viene eseguito con **diversi input** e il sistema controlla che quanto stampato con `printf` corrisponda a quanto atteso.

(In parole povere: Coderunner è un correttore automatico. Scrivi il programma, premi il pulsante, e lui lo prova con una serie di input già preparati confrontando le tue stampe con quelle giuste, sulle stampe.)

## Gli esiti della verifica
Dopo ogni tentativo si può trovare uno di tre esiti:
- **errore di compilazione**: il codice non compila. Va ricordato che Coderunner compila con le opzioni `-Wall -Werror`, quindi anche un semplice ~warning~ viene trattato come errore;
- il programma **compila ed esegue, ma non passa tutti i test**: non produce in output il testo atteso;
- il programma **compila, esegue e passa tutti i test**: produce tutti gli output attesi.

Il laboratorio rassicura con un «niente panico»: la compilazione e l'esecuzione con degli input predefiniti sono automatiche, e l'obiettivo è scrivere un **codice robusto**, che risponda correttamente a input diversi. Gli input proposti sono formulati per mettere alla prova varie casistiche. **Non è l'esame e l'esercizio non viene valutato**: i messaggi sui punteggi che l'interfaccia mostra qua e là si possono ignorare.

## Esercizio: saluti
L'esercizio chiede un programma `saluta.c` che chieda all'utente l'ora, come numero intero, e stampi il saluto più appropriato fra «Buongiorno», «Buon pomeriggio», «Buonasera» e «Buona notte». Gli intervalli da usare vanno scelti da noi. Una scelta possibile (nostra soluzione), con ora da 0 a 23, è questa:

```c
#include <stdio.h>

int main(void) {
    int ora;
    printf("Che ora e'? ");
    scanf("%d", &ora);

    if (ora >= 6 && ora < 12) {
        printf("Buongiorno\n");
    }
    else if (ora >= 12 && ora < 18) {
        printf("Buon pomeriggio\n");
    }
    else if (ora >= 18 && ora < 22) {
        printf("Buonasera\n");
    }
    else {
        printf("Buona notte\n");
    }
}
```

Gli intervalli sono semiaperti sinistri, [6, 12) e così via (capitolo 18), così ogni ora appartiene a uno e un solo saluto. Il ramo finale `else` raccoglie le ore dalle 22 alle 5 e vale anche per input non validi (per esempio 40): se si vuole gestirli serve un controllo in più, ma l'esercizio non lo richiede.

## Esercizio: emersione del massimo con 4 variabili
Nel laboratorio si invita a completare un programma (quello del quiz Lab03-Es2) che trova il massimo fra **quattro variabili**, assicurandosi che passi tutti i test; l'esercizio è descritto come simile, ma più semplice, a uno visto a lezione. Il testo originale è sul quiz di Moodle. Lo schema (nostro, perché il testo del quiz non è nelle slide) è lo stesso usato per il massimo di tre numeri nel capitolo 8: si parte dal primo valore come candidato e lo si sostituisce quando se ne trova uno più grande:

```c
int max = a;
if (b > max) {
    max = b;
}
if (c > max) {
    max = c;
}
if (d > max) {
    max = d;
}
```

(In parole povere: è come una gara a eliminazione. Il campione in carica all'inizio è `a`; a ogni sfida, se lo sfidante è più grande, diventa lui il nuovo campione. Alla fine il campione è il massimo.)

I tre `if` sono indipendenti e non `else if`: ogni variabile va confrontata con il massimo trovato fin lì, anche se una precedente lo ha già cambiato.

## Esercizio: selezione delle operazioni
Il programma `selezione_operazioni.c` fa questo: chiede all'utente tre interi x1, x2 e x3; stampa il menù «scrivi 1 per calcolare la somma», «scrivi 2 per calcolare il prodotto» e «scrivi 3 per calcolare la media»; chiede un numero fra 1, 2 e 3; se l'operazione scelta non è fra quelle proposte stampa un messaggio di errore appropriato, altrimenti esegue l'operazione sui tre interi e mostra il risultato. Una soluzione:

```c
#include <stdio.h>

int main(void) {
    int x1, x2, x3, scelta;

    printf("Inserisci tre interi: ");
    scanf("%d %d %d", &x1, &x2, &x3);

    printf("scrivi 1 per calcolare la somma\n");
    printf("scrivi 2 per calcolare il prodotto\n");
    printf("scrivi 3 per calcolare la media\n");
    scanf("%d", &scelta);

    if (scelta == 1) {
        printf("Somma: %d\n", x1 + x2 + x3);
    }
    else if (scelta == 2) {
        printf("Prodotto: %d\n", x1 * x2 * x3);
    }
    else if (scelta == 3) {
        printf("Media: %f\n", (x1 + x2 + x3) / 3.0);
    }
    else {
        printf("Operazione non valida\n");
    }
}
```

Due punti da notare. La media si calcola dividendo per `3.0` e non per `3`: dividendo per l'intero 3 si avrebbe una divisione fra interi che scarta i decimali (capitolo 16), mentre con `3.0` il risultato è un reale. E lo schema `if ... else if ... else` con l'`else` finale è il modo giusto per gestire la scelta non valida, perché l'`else` scatta quando nessuna delle opzioni precedenti è vera.

Il prossimo capitolo conclude il laboratorio 3 con due programmi più articolati: l'equazione di secondo grado e il gioco sasso-carta-forbici-lucertola-Spock.
