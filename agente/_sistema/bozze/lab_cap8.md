# Capitolo 8: Laboratorio 3: Espressioni Booleane ed Errori con if
## Di che cosa parla il laboratorio 3
Il laboratorio 3, «Condizioni booleane», mette in pratica quanto visto a teoria sulle espressioni booleane (capitoli 17 e 18) e sul costrutto `if` (capitolo 19). Le prime attività sono la valutazione di espressioni, la lettura del codice di `booleani.c` e sei esercizi da completare; poi si passa agli errori tipici con `if`/`else`, agli esercizi su Moodle (capitolo 9 di questo riassunto) ai programmi `saluta.c` e `selezione_operazioni.c` (capitolo 9) e a due programmi più lunghi, l'equazione di secondo grado e il gioco sasso-carta-forbici-lucertola-Spock (capitolo 10).

## Quali valori assumono queste espressioni
Il laboratorio propone nove espressioni da valutare. Le risposte sono queste:
- `3 > 5 || 10 == 7 + 3`: **true** (la prima parte è falsa, la seconda è vera);
- `3 != 5 && (6 < 2 || 5 + 2 == 10 - 3)`: **true** (3 è diverso da 5, e nella parentesi la seconda parte è vera: 7 == 7);
- `3 < 5 < 7`: **non va scritta così** (vedi sotto);
- `4 > 3 > 2`: **non va scritta così**;
- `3 < 5 && 5 < 7`: **true**;
- `3 < 5 && 7 < 5`: **false**;
- `true && false`: **false** (`true` e `false` richiedono `<stdbool.h>`, capitolo 17);
- `true && 5 < 7`: **true**;
- `false || 5 < 10`: **true**.

Le due espressioni «con la catena» sono il trabocchetto dell'esercizio. In C i confronti si valutano **uno alla volta, da sinistra a destra**, e il risultato di un confronto è un intero, 1 se vero e 0 se falso. Quindi `3 < 5 < 7` diventa `(3 < 5) < 7`, cioè `1 < 7`, che è vero, ma **per il motivo sbagliato**: non si è confrontato 5 con 7. E `4 > 3 > 2` diventa `(4 > 3) > 2`, cioè `1 > 2`, che è **falso**, mentre in matematica 4 > 3 > 2 è vero. La scrittura corretta per dire «5 sta fra 3 e 7» è, come già visto nel capitolo 18, `3 < 5 && 5 < 7`.

(In parole povere: in C non esiste la catena di disuguaglianze della matematica. Per dire «x sta fra a e b» bisogna scrivere due confronti separati e unirli con `&&`.)

## Il codice di booleani.c e le leggi di De Morgan
Il laboratorio chiede di leggere il file `booleani.c`, che contiene vari esempi di operazioni booleane in C, e di **procedere con gli esercizi successivi solo dopo aver capito tutte le operazioni di quel codice**. Come promemoria, per compilare si usano i comandi `gcc -Wall booleani.c -o booleani` (Unix) oppure `gcc -Wall booleani.c -o booleani.exe` (Windows).

Il laboratorio ricorda anche le **leggi di De Morgan**, che stabiliscono una relazione di equivalenza fra congiunzione e disgiunzione logica e si possono riassumere così:
- ¬(a ∧ b) = ¬a ∨ ¬b
- ¬(a ∨ b) = ¬a ∧ ¬b

In C si scrivono `!(a && b)` equivalente a `!a || !b`, e `!(a || b)` equivalente a `!a && !b`.

(In parole povere: per negare «a e b insieme» basta dire «manca almeno uno dei due», cioè «non a oppure non b». E per negare «a oppure b» bisogna dire «mancano tutti e due», cioè «non a e non b». Si cambia l'operatore e si nega ciascun pezzo.)

## I sei esercizi booleani
Il file `esercizi_booleani.c` va aperto e completato implementando sei punti. Le soluzioni qui sotto sono ricavate da noi ragionando sul testo (le slide non le riportano):

1. **Multiplo**: dati due interi a e b, stampare 1 se il primo è multiplo del secondo, 0 altrimenti. Un numero a è multiplo di b quando la divisione dà resto zero (con b diverso da zero): `printf("%d\n", a % b == 0);`. Il risultato di un confronto è già 0 o 1, quindi si può stampare direttamente.
2. **Voto valido**: dato un voto a, stampare «true» se è compreso fra 1 e 30 inclusi, «false» altrimenti. Servono due confronti uniti da `&&`: la condizione è `a >= 1 && a <= 30`, e per stampare la parola e non 0/1 si scrive `printf("%s\n", (a >= 1 && a <= 30) ? "true" : "false");` (operatore ternario, capitolo 18).
3. **Negazione dell'and**: dati due booleani b1 e b2, stampare «false» se sono entrambi veri, «true» altrimenti. È la negazione dell'and, `!(b1 && b2)`, che per De Morgan equivale a `!b1 || !b2`; anche qui si stampa la parola con `printf("%s\n", !(b1 && b2) ? "true" : "false");`.
4. **Massimo di due, con uguali**: dati a e b, stampare il massimo; se sono uguali stampare «I due valori sono uguali». Servono tre casi distinti:

```c
if (a > b) {
    printf("%d\n", a);
}
else if (b > a) {
    printf("%d\n", b);
}
else {
    printf("I due valori sono uguali\n");
}
```

5. **Massimo di tre**: dati a, b e c, stampare il massimo usando una variabile di supporto `max`. L'idea è quella dell'«emersione del massimo»: si parte da un candidato e lo si sostituisce quando se ne trova uno più grande:

```c
int max = a;
if (b > max) {
    max = b;
}
if (c > max) {
    max = c;
}
printf("%d\n", max);
```

6. **Ordinati**: dati tre interi a, b e c, stampare «ordinati» se sono in ordine crescente, altrimenti niente. Basta confrontare le coppie vicine: `if (a <= b && b <= c) { printf("ordinati\n"); }`. Il testo non precisa se «crescente» sia in senso stretto o largo: con `<` al posto di `<=` si richiederebbe che siano tutti distinti,: il testo non lo dice, quindi la scelta va fatta in base a come lo intende l'esercizio.

Notare che nel punto 6 la condizione non si scrive `a <= b <= c`: sarebbe lo stesso errore delle espressioni a catena viste sopra.

## Errori insidiosi con if e else
Il laboratorio fa osservare due frammenti di codice sbagliati, chiedendo di trovare gli errori. Sono entrambi **insidiosi** perché il codice **compila senza segnalare problemi**.

Il primo è:

```c
#include <stdio.h>
int main() {
    int voto;
    scanf("%d", &voto);
    if (voto >= 18);
    printf("Esame passato.\n");
}
```

L'errore è il **punto e virgola** subito dopo la condizione. Per il linguaggio C è come se fosse scritto `if (voto >= 18) ;` seguito da `printf(...)`: il `;` è un'**istruzione vuota**, e la `printf` non fa parte dell'`if` e viene eseguita **sempre**, anche se il voto è inferiore a 18.

Il secondo è:

```c
if (voto >= 18)
    printf("Esame passato.\n");
else
    printf("Esame non passato.\n");
    printf("Ripresentarsi al prossimo appello.\n");
```

Mancano le **graffe** per un blocco `else` con più di un'istruzione (nelle slide il codice è privo di indentazione, e compila senza segnalazioni; un compilatore recente con `-Wall` può avvisare dell'indentazione ingannevole, ma non dà errore). Per il C solo la **prima** istruzione dopo la parola chiave `else` appartiene al blocco condizionale: l'ultima `printf` è quindi eseguita sempre, anche per chi ha passato l'esame. La versione corretta racchiude il blocco fra graffe:

```c
if (voto >= 18) {
    printf("Esame passato.\n");
}
else {
    printf("Esame non passato.\n");
    printf("Ripresentarsi al prossimo appello.\n");
}
```

La regola pratica del laboratorio è: **è sempre meglio mettere i blocchi condizionali fra parentesi graffe**, a meno che non siano molto brevi ed evidenti.

(In parole povere: l'`if` da solo «controlla» una sola istruzione, quella che viene subito dopo. Se ne vuoi controllare di più, le graffe servono a dire al C «tutte queste insieme». E un punto e virgola messo a caso dopo la parentesi dice al C «qui l'`if` ha già finito», con effetti disastrosi che il compilatore non nota.)

Il prossimo capitolo riguarda l'uso di Coderunner su Moodle e gli esercizi sulle scelte.
