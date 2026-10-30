# Capitolo 12: Laboratorio 4: Divisori, Pattern, Quantificatori sulle Sequenze, Fibonacci e Ricerca per Dimezzamenti
## Esercizio: i divisori interi
Sulla pagina Moodle c'è l'esercizio **Lab04-Es1 Divisori Interi**: si deve completare il programma in modo che superi tutti i test proposti. La domanda posta è quale ciclo sia più adatto al problema (la scelta tipica quando i candidati da controllare sono noti in anticipo è un `for`: considerazione nostra, perché il testo dell'esercizio sta su Moodle).

## Numeri di Floyd e un quadrato di caratteri
**Triangolo di Floyd.** Un programma `floyd.c` legge n e stampa le prime n righe del triangolo di Floyd, cioè i numeri naturali scritti in modo consecutivo per riempire righe di 1, 2, 3, … valori. Per n = 5:

```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

I numeri di Floyd non c'entrano nulla con la logica di Floyd (precisazione del docente).

**Quadrato.** Un programma `quadrato.c` legge n e stampa un quadrato di n · n caratteri tra `*`, `\` e `:` seguendo un pattern. Per n = 6:

```
\:::::
*\::::
**\:::
***\::
****\:
*****\
```

Suggerimento: **due cicli annidati**, uno esterno per le righe e uno (o più) interno per i caratteri della stessa riga.

(In parole povere: in un pattern a righe il ciclo esterno decide «a che riga sono» e quello interno decide «quanti caratteri e quali scrivere su questa riga».)

## Quantificazione universale su una sequenza
Si scrive un ciclo che legge una sequenza di interi terminata dallo 0, e ci si chiede: **tutti i numeri della sequenza soddisfano una condizione Cond?** È una quantificazione universale (Fondamenti, cap. 21). Si usa una variabile booleana `tutti`, inizialmente vera:

Nei frammenti seguenti `n` è un intero già dichiarato e «Cond» è uno **pseudocodice** per una condizione qualunque.

```c
bool tutti = true;
while (1 == scanf("%d", &n) && n != 0) {
    if (!(Cond valutata su n))
        tutti = false;
}
```

Basta un solo numero che non soddisfa la condizione per rendere `tutti` falsa. Lo 0 che chiude la sequenza è un **valore sentinella** (~sentinel value~).

## Quantificazione esistenziale su una sequenza
La domanda ora è: **esiste almeno un numero della sequenza che soddisfa una condizione Cond?** (Fondamenti, cap. 22). Si usa una variabile `esiste`, inizialmente falsa:

```c
bool esiste = false;
while (1 == scanf("%d", &n) && n != 0) {
    if (Cond valutata su n)
        esiste = true;
}
```

**In parole povere:** per «tutti» si parte da «sì» e si cambia in «no» appena si trova un caso che non va; per «esiste» si parte da «no» e si cambia in «sì» appena si trova un caso che va.

Se non si devono leggere tutti gli elementi (ad esempio perché sono già in memoria), si può aggiungere la variabile `tutti` (o `esiste`) anche **nella condizione del `while`**: il ciclo termina non appena la variabile che accumula la condizione diventa falsa (nel caso universale) o vera (nel caso esistenziale). Questo schema si vedrà in un prossimo laboratorio.

Sulla pagina Moodle c'è l'esercizio **Lab04-Es2 Condizioni su sequenza**: si deve completare il programma determinando correttamente tutte le condizioni «esiste» e «per ogni» richieste.

## Fibonacci
Un programma `fibonacci.c` legge un numero k e stampa i primi k numeri della successione di Fibonacci; per k = 10 la stampa attesa è `0 1 1 2 3 5 8 13 21 34` (per semplicità si assume k ≥ 2). La successione parte da due numeri, 0 e 1, e ogni elemento successivo è la somma dei due precedenti.

Suggerimento: si parte da due variabili n = 0 e m = 1 e si stampano; a ogni iterazione si aggiornano
n′ = m,  m′ = n + m
e si stampa m′. La domanda posta è se per questo aggiornamento serva una variabile temporanea. Considerazione nostra: scrivendo di seguito `n = m; m = n + m;` si sbaglia, perché la prima assegnazione fa perdere il valore vecchio di n, che serve ancora per calcolare il nuovo m (come nello scambio di variabili, cap. 13); la variabile temporanea risolve il problema (esistono anche trucchi aritmetici senza temporanea).

## Fai indovinare un numero e ricerca per dimezzamenti
Il programma `fai_indovinare_numero.c` (nel codice iniziale) è il gioco in cui il computer sceglie un numero casuale e l'utente deve indovinarlo. Poi si scrive l'algoritmo che **indovina** il numero scelto dal computer.

**Strategia lenta.** Si sa che il numero è compreso tra 0 incluso e 100 escluso, per esempio 62. Si prova 0: «il numero è maggiore di 0», e l'intervallo diventa [1, 100); si prova 1, poi 2, e così via, riducendo l'intervallo di un valore alla volta.

**Strategia con dimezzamenti.** Si prova ogni volta il **punto di mezzo** dell'intervallo:
- intervallo [0, 100), tentativo 50 = (0 + 100)/2: il numero è maggiore di 50, quindi l'intervallo diventa [51, 100);
- tentativo 75 = (51 + 100)/2: il numero è minore di 75, quindi l'intervallo diventa [51, 75);
- tentativo (51 + 75)/2 = 63: il numero è minore di 63, quindi l'intervallo diventa [51, 63), e si continua a dimezzare (57, 60, 61…) fino al tentativo 62. Nelle slide il terzo passo è scritto «62 = (51 + 75)/2», ma il punto di mezzo è 63: è una svista della slide, e conta soprattutto l'idea di dimezzare.

(In parole povere: invece di provare i numeri uno per uno, si tira a indovinare nel mezzo e ogni risposta «più grande» o «più piccolo» elimina metà dei candidati rimasti.)

Sulla pagina Moodle c'è l'esercizio **Lab04-Es3 Indovina tu il numero!**: si deve completare il programma assicurandosi che indovini tutti i valori nel **numero massimo di tentativi concessi**. Anche qui la domanda posta è quale ciclo sia più adatto: considerazione nostra, la ricerca prosegue finché non si indovina, quindi un ciclo che si ferma su una condizione (un `while`) è la scelta naturale.
