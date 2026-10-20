# Capitolo 10: Laboratorio 3: Equazioni di Secondo Grado e Sasso-Carta-Forbici-Lucertola-Spock
## L'equazione di secondo grado
L'esercizio chiede di realizzare lo **schema di risoluzione completo** dell'equazione di secondo grado ax² + bx + c = 0, che a lezione era stato visto in forma semplificata, considerando **anche tutti i casi limite**. Il programma `equaz_secondo.c` prende in ingresso i tre coefficienti a, b e c e calcola, quando è possibile, le radici dell'equazione e le stampa; quando non è possibile stampa un messaggio di errore appropriato e termina.

I casi limite nascono dal fatto che la formula risolutiva vale solo se a è diverso da zero. Il flusso di risoluzione del laboratorio si legge così:

![Il flusso di risoluzione di ax² + bx + c = 0 ridisegnato dalle slide (in verde il «sì», in rosso il «no»).](figure/lab/ch10_flow_equazione.png|13)

1. Se **a = 0** l'equazione non è di secondo grado e si guarda b.
2. Se a = 0 e **b = 0**, l'equazione diventa c = 0: se anche **c = 0** è **indeterminata** (ogni x è soluzione), altrimenti è **impossibile** (nessuna x la soddisfa).
3. Se a = 0 ma b ≠ 0 l'equazione è di primo grado e ha l'unica soluzione **x₁ = −c / b**.
4. Se **a ≠ 0** si calcolano il discriminante **δ = b² − 4ac** e tre grandezze di servizio: **W = 2a**, **W₁ = −b / W** e **W₂ = √|δ| / W**.
5. Se **δ = 0** c'è una **singola radice**, x₁ = W₁.
6. Se **δ < 0** non ci sono radici reali, ma **radici complesse coniugate**.
7. Se **δ > 0** ci sono due **radici reali**, x₁ = W₁ + W₂ e x₂ = W₁ − W₂.

(In parole povere: prima di applicare la formula bisogna controllare che l'equazione sia davvero di secondo grado, perché con a = 0 si dividerebbe per zero. Poi il segno del discriminante dice quante soluzioni reali ci sono: due se è positivo, una se è zero, nessuna se è negativo.)

Il perché di W₁ e W₂ (spiegazione nostra, non nelle slide) è la formula risolutiva x = (−b ± √δ) / (2a), che si può spezzare in due parti: x = −b/(2a) ± √δ/(2a), cioè W₁ ± W₂ (con il valore assoluto sotto la radice, perché per δ < 0 la parte reale resta W₁ e la parte immaginaria è ±W₂).

Per il calcolo il laboratorio ricorda di usare `sqrt()` per la radice quadrata, definita in `<math.h>`, e `abs()` per il valore assoluto, definita in `<stdlib.h>`. Una soluzione, nell'ipotesi che i coefficienti siano interi:

```c
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(void) {
    int a, b, c;
    printf("Inserisci a, b, c: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a == 0) {
        if (b == 0) {
            if (c == 0) {
                printf("Equazione indeterminata\n");
            }
            else {
                printf("Equazione impossibile\n");
            }
        }
        else {
            printf("x1 = %f\n", 0.0 - (double)c / b);
        }
    }
    else {
        int delta = b * b - 4 * a * c;
        double W  = 2.0 * a;
        double W1 = 0.0 - b / W;
        double W2 = sqrt(abs(delta)) / W;

        if (delta == 0) {
            printf("Singola radice: x1 = %f\n", W1);
        }
        else if (delta < 0) {
            printf("Radici complesse coniugate\n");
        }
        else {
            printf("x1 = %f, x2 = %f\n", W1 + W2, W1 - W2);
        }
    }
}
```

Alcune attenzioni. `W` è dichiarata `double` e vale `2.0 * a`, così le divisioni `-b / W` e `sqrt(...) / W` sono fra reali: se invece W fosse un intero, `-b / W` scarterebbe i decimali (capitolo 16). Nel ramo `a == 0` il cast `(double)c` evita la stessa divisione fra interi. Per le radici complesse la tabella dei casi di prova riporta solo la dicitura «Radici complesse coniugate»; volendo si potrebbe stampare la parte reale W₁ e quella immaginaria ±W₂. Infine `abs()` lavora con numeri interi: se i coefficienti fossero dei `double` bisognerebbe usare `fabs()`, anch'essa in `<math.h>` (nota nostra, il laboratorio parla solo di `abs`).

Il laboratorio propone sette casi di prova. Provando i coefficienti nello schema si ottengono questi risultati:

- a = 0, b = 0, c = 0: indeterminata;
- a = 0, b = 0, c = 4: impossibile;
- a = 0, b = 2, c = −4: x₁ = 2;
- a = 1, b = 0, c = −121: x₁ = 11, x₂ = −11;
- a = 1, b = 2, c = 1: x₁ = −1 (singola radice);
- a = 1, b = −3, c = 10: radici complesse coniugate;
- a = 5, b = 20, c = 0: x₁ = 0, x₂ = −4.

Verifichiamo l'ultimo: δ = 400, W = 10, W₁ = −20/10 = −2, W₂ = 20/10 = 2, quindi x₁ = −2 + 2 = 0 e x₂ = −2 − 2 = −4. Il penultimo ha δ = 9 − 40 = −31, negativo, e quindi nessuna radice reale.

Un dettaglio pratico: sui sistemi Unix `sqrt` richiede di collegare la libreria matematica con `gcc equaz_secondo.c -lm` (capitolo 15 della teoria). Le espressioni con `0.0 - ...` evitano di stampare «-0.000000» quando il risultato è zero (nostra precauzione, non richiesta dalle slide).

## Sasso-carta-forbici-lucertola-Spock
L'ultimo esercizio è una variante del gioco della morra cinese: **sasso-carta-forbici-lucertola-Spock** (~rock-paper-scissors-lizard-Spock~), una variante fantasiosa inventata da due studenti statunitensi, Sam Kass e Karen Bryla, e resa famosa dal telefilm ~The Big Bang Theory~. Estende la morra cinese a **cinque stati**, aggiungendo la lucertola e Spock, il celebre personaggio di ~Star Trek~. L'esercizio si svolge su Moodle con Coderunner (quiz Lab03-Es3): bisogna seguire il testo e completare l'esercizio. Il testo del quiz non è nelle slide, quindi la codifica delle scelte e il formato dell'output vanno letti nel quiz stesso.

L'unico suggerimento che il laboratorio dà riguarda gli input: come fare a determinare se «gli input non sono stati letti»? Si ricorda che la funzione `scanf` **restituisce il numero di specificatori di conversione letti con successo** dallo standard input (capitolo 10 della teoria). Per esempio, se si leggono due scelte con `scanf("%d %d", &g1, &g2)`, il valore restituito deve essere 2; se è minore, l'input non è stato letto correttamente.

(In parole povere: `scanf` non si limita a leggere, ma dice anche com'è andata, restituendo quante cose è riuscita a leggere. Confrontando quel numero con quello atteso sai se l'utente ha scritto dati validi.)

Le regole del gioco originale (che non sono scritte nelle slide) sono dieci: le forbici tagliano la carta, la carta avvolge il sasso, il sasso schiaccia la lucertola, la lucertola avvelena Spock, Spock rompe le forbici, le forbici decapitano la lucertola, la lucertola mangia la carta, la carta smentisce Spock, Spock vaporizza il sasso e il sasso rompe le forbici. Con cinque scelte diventano molti i casi da trattare con una catena di `if`; si può ridurre il lavoro osservando che le regole sono «circolari». Numerando le scelte nell'ordine forbici 0, carta 1, sasso 2, lucertola 3, Spock 4, il giocatore che ha scelto ~i~ batte quello che ha scelto ~j~ esattamente quando `(j - i + 5) % 5` vale 1 oppure 3. Uno schema possibile (nostra proposta, da adattare al testo del quiz) è:

```c
int g1, g2;
int letti = scanf("%d %d", &g1, &g2);

if (letti != 2) {
    printf("Input non letti\n");
}
else if (g1 < 0 || g1 > 4 || g2 < 0 || g2 > 4) {
    printf("Scelta non valida\n");
}
else if (g1 == g2) {
    printf("Pareggio\n");
}
else if ((g2 - g1 + 5) % 5 == 1 || (g2 - g1 + 5) % 5 == 3) {
    printf("Vince il giocatore 1\n");
}
else {
    printf("Vince il giocatore 2\n");
}
```

Con questo schema i controlli vanno **nell'ordine giusto**: prima si verifica che gli input siano stati letti (`letti`), poi che siano validi, poi si distinguono pareggio e vittorie. L'ordine conta perché ogni `else if` presuppone che i casi precedenti siano esclusi: usare `g1` e `g2` prima di sapere che sono stati letti sarebbe un errore.

Con questo il laboratorio 3 si chiude: dai confronti fra numeri si è arrivati a programmi che scelgono fra più casi, e il passo successivo della teoria, i cicli, permetterà di ripetere queste scelte.
