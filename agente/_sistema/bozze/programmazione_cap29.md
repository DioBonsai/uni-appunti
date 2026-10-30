# Capitolo 29: Dividere un Programma in Funzioni: Divide et Impera
## Dalla complessità ai mattoncini
Programmi complessi sono difficili da leggere e da mantenere se scritti in un unico blocco. La strategia è **scomporre il problema in sottoproblemi più semplici**, dove **ogni sottoproblema diventa una funzione**. Il metodo è noto come **divide et impera**.

I passi sono quattro:
1. identificare il problema principale;
2. suddividerlo in sottoproblemi logici;
3. scrivere una funzione per ciascun sottoproblema;
4. combinare le funzioni per ricostruire la soluzione completa.

La scomposizione può essere **iterata**: un sottoproblema può essere diviso a sua volta in problemi ancora più semplici.

**In parole povere:** invece di scrivere un unico programma lunghissimo, si ragiona come per montare un mobile: si prepara ogni pezzo separatamente e poi si assembla.

## Un esempio: area e circonferenza di un cerchio
**Problema.** Letto in input un valore reale non negativo r che rappresenta il raggio di un cerchio, calcolare e mostrare la circonferenza C = 2πr e l'area A = πr². Ripetere l'acquisizione dell'input se non è valido (manca o r < 0).

**Scomposizione** in sottoproblemi:
- leggere e validare l'input;
- calcolare la circonferenza;
- calcolare l'area;
- presentare i risultati.

Si scrive prima il `main()`, con i prototipi delle funzioni:

```c
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
```

Poi le implementazioni. La funzione di input con validazione ripete la lettura finché il valore non è accettabile:

```c
float leggiRaggio(void) {
    float r;
    bool ripeti;
    do {
        printf("Inserisci il raggio (>= 0): ");
        int esito = scanf("%f", &r);
        // Validazione dell'input
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
```

Qui `esito` è il valore restituito da `scanf`, cioè il numero di valori letti con successo: se non è 1, l'utente non ha inserito un numero (spiegazione nostra, coerente con il Laboratorio 4). Nota: `M_PI` non fa parte del C standard, ma di molti compilatori; e se l'utente scrive un carattere non numerico, `scanf` lo lascia nel buffer e il ciclo può ripetersi senza fine: è un limite del codice di esempio. Poi le funzioni di calcolo e quella di presentazione:

```c
float circonferenza(float r) {
    return 2 * M_PI * r;
}

float area(float r) {
    return M_PI * r * r;
}

void stampaRisultati(float r, float c, float a) {
    printf("Raggio = %.2f\n", r);
    printf("Circonferenza = %.2f\n", c);
    printf("Area = %.2f\n", a);
}
```

(In parole povere: `main()` racconta la storia in quattro righe — leggo il raggio, calcolo la circonferenza, calcolo l'area, stampo — e i dettagli stanno ciascuno nella propria funzione.)

## I benefici della scomposizione
- **Leggibilità**: `main()` mostra solo la logica complessiva.
- **Riutilizzo**: le funzioni possono servire in altri programmi.
- **Manutenzione**: si può modificare una funzione senza toccare il resto.
- **Testabilità**: è più semplice verificare una funzione piccola e autonoma.

(In parole povere: i benefici sono tutti modi di dire che un programma a pezzi è più facile da capire, da riusare, da cambiare e da controllare.)

Ci sono due modi di scegliere l'ordine di scomposizione. Nell'approccio **top-down** si parte dal problema generale, si scrive il `main()` e poi si dettagliano le funzioni; nell'approccio **bottom-up** si costruiscono prima le funzioni elementari e poi il `main()`. Entrambi si integrano nella pratica.

(In parole povere: top-down vuol dire «parto dall'idea generale e scendo ai dettagli»; bottom-up «parto dai mattoncini e li metto insieme».)

## Progettare buone funzioni
Principi generali:
- **Una funzione = un compito chiaro**: deve fare una cosa sola, in modo semplice e leggibile (principio noto come **SRP**, ~Single Responsibility Principle~);
- **nomi significativi e coerenti**: verbi per le azioni e nomi per i valori (`stampaRisultati`, `calcolaArea`, …);
- **separazione delle responsabilità**: distinguere funzioni di input, di calcolo e di output.

Per la leggibilità e la manutenzione:
- evitare funzioni troppo lunghe, difficili da leggere e da testare;
- suddividere ulteriormente una funzione che diventa troppo complessa;
- **commentare il «cosa», non il «come»**: il codice deve spiegarsi da solo.

(In parole povere: una funzione dovrebbe essere come un buon attrezzo, che fa una cosa sola e la fa bene, con un nome che dice già cosa fa.)

Questi principi si riprenderanno, con più esperienza, nel corso di Ingegneria del Software.
