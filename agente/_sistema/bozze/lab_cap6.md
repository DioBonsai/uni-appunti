# Capitolo 6: Laboratorio 2: Operatori, Ordine di Valutazione ed Errori in C
## Di che cosa si occupa il laboratorio 2
Il secondo laboratorio di Programmazione I, intitolato "Operatori e Tipi", riprende gli argomenti della teoria sulle variabili, sugli operatori aritmetici e sui tipi numerici (capitoli 6, 8 e 13-16 del riassunto di teoria) e li fa provare al computer. Questo capitolo raccoglie la parte sugli operatori, sull'ordine di valutazione delle espressioni e sulla ricerca degli errori; il capitolo successivo tratta i tipi, la documentazione del linguaggio e gli esercizi di sintesi.

Per compilare si usa il comando gcc con l'opzione -Wall, che attiva un ampio insieme di avvisi del compilatore: in Unix `gcc -Wall aritmetica.c -o aritmetica`, in Windows `gcc -Wall aritmetica.c -o aritmetica.exe` (come visto nel capitolo 4 di questo riassunto).

## Aritmetica
Il primo esercizio chiede di provare il programma **aritmetica.c** leggendo attentamente il codice prima di eseguirlo: l'idea è di prevedere il risultato di ogni operazione e poi confrontarlo con l'output.

## Operazioni su interi
Il secondo esercizio è scrivere un programma **operazioni_su_interi.c** che:
1. chieda all'utente di inserire due numeri interi, che chiamiamo n1 e n2 (con scanf, come visto a lezione);
2. calcoli la somma di n1 e n2 e ne stampi il valore;
3. stampi il prodotto di n1 con n2;
4. stampi la divisione intera n1 / n2;
5. stampi la divisione reale n1 / n2;
6. stampi il resto della divisione intera tra n1 e n2.

I due tipi di divisione sono il punto delicato, e si ricollegano al capitolo 16 della teoria. Con n1 = 7 e n2 = 2, la divisione tra interi `n1 / n2` dà 3 (la parte frazionaria si perde) e il resto `n1 % n2` dà 1. Per ottenere la divisione reale 3.5 bisogna invece convertire almeno uno degli operandi in float con un cast, per esempio `(float)n1 / n2`, e stampare il risultato con `%f`.

## Ordine di valutazione
Un esercizio chiede quali risultati si ottengono in C da tre espressioni. Per risolverlo bisogna ricordare che in un'espressione senza parentesi la moltiplicazione, la divisione e il resto hanno la precedenza su somma e sottrazione, e che a parità di precedenza si procede da sinistra a destra. Le parentesi si valutano per prime, dalle più interne.
- `int x = 7 + 3 * 6 / 2 - 1;` si calcola prima `3 * 6` = 18, poi `18 / 2` = 9, infine `7 + 9 - 1` = **15**.
- `int x = 2 % 2 + 2 * 2 - 2 / 2;` dà `0 + 4 - 1` = **3**.
- `int x = (3 * 9 * (3 + (9 * 3 / (3))));` si parte dalle parentesi più interne: `9 * 3 / 3` = 9, poi `3 + 9` = 12, infine `3 * 9 * 12` = **324**.

Un secondo esercizio chiede quali tra sei espressioni corrispondono a y = a·x^{3} + 7. Quelle corrette sono tre, perché in tutte e tre il prodotto a·x·x·x viene calcolato per intero prima di sommare 7:
- `int y = a * x * x * x + 7;`
- `int y = (a * x) * x * x + 7;`
- `int y = a * (x * x * x) + 7;`

Le altre tre sono sbagliate perché una parentesi fa sommare 7 prima di moltiplicare, per esempio `a * x * x * (x + 7)`, che calcola a·x^{2}·(x + 7) e non a·x^{3} + 7. Con a = 2 e x = 3 le tre espressioni corrette danno tutte 61, mentre le altre danno valori diversi (per esempio 180 oppure 96).

## La circonferenza
L'esercizio sul programma **circonferenza.c** chiede di completare la parte che calcola la circonferenza di un cerchio di raggio r, ricordando che la circonferenza è 2πr e l'area è πr^{2}. Se il programma usa le funzioni dell'header math.h, su Linux può essere necessario compilare con `gcc -Wall circonferenza.c -o circonferenza -lm`, dove -lm indica di aggiungere le funzioni matematiche (capitolo 15 della teoria).

## Gli errori in C
Un esercizio propone di individuare gli errori in questo codice:

```c
#include <stdio.h>
int main() {
int x, y;
printf("Inserisci due interi: ");
scanf("%d %d", &x, y)
z = x + y;
printf("La somma %d + %d vale ", x, y);
printf("%d\n", &z);
}
```

Leggendolo con attenzione si trovano quattro problemi, di natura diversa: due sono veri errori di compilazione, gli altri due il compilatore li segnala come avvisi con -Wall (oppure producono un comportamento sbagliato in esecuzione).

- nella scanf manca l'operatore & davanti a y: scanf vuole l'indirizzo di ogni variabile in cui scrivere (capitoli 9 e 10 della teoria); senza & il programma scriverebbe all'indirizzo contenuto in y, con ogni probabilità facendolo bloccare;
- manca il punto e virgola alla fine della riga della scanf;
- la variabile z non è stata dichiarata prima di essere usata;
- l'ultima printf stampa `&z`, cioè l'indirizzo di z, con %d, mentre per stampare il valore bisogna scrivere `z`.

Il `main()` senza `void` e l'assenza di `return 0;`, invece, non sono errori in C.

Un secondo esercizio chiede di leggere il file **errori.c** e, senza compilare, individuare tutti gli errori presenti: nel testo dell'esercizio si dice che sono 8. Il metodo è lo stesso: rileggere il codice riga per riga, cercando errori dei tipi appena visti.

## Media di tre numeri
Infine l'esercizio su **media.c** chiede di leggere il codice, sperimentare input differenti seguendo gli esercizi proposti e rispondere alle domande indicate nei commenti del codice.
