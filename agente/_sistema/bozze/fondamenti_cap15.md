# 15. Equivalenze, Tautologie e Contraddizioni
## Formule equivalenti
Due formule sono **equivalenti** se hanno gli stessi valori di verità per tutti i valori di verità delle loro componenti atomiche, cioè se hanno la **stessa tavola di verità**. Non sono la stessa formula, ma si possono scambiare l'una con l'altra, scegliendo quella più utile in un dato contesto. Questo vale per i circuiti (due circuiti equivalenti si possono sostituire), ma anche per i programmi: prima di sostituire la condizione di uscita di un ciclo con un'altra formula più leggibile bisogna essere sicuri che sia equivalente, altrimenti si cambia il comportamento del programma.

## Esempio: la negazione di una disgiunzione
Si vuole vedere che **¬(p ∨ q)** è equivalente a **¬p ∧ ¬q**. Con le tavole di verità:

```
p q | p∨q  ¬(p∨q) | ¬p  ¬q  ¬p∧¬q
1 1 |  1      0    |  0   0    0
1 0 |  1      0    |  0   1    0
0 1 |  1      0    |  1   0    0
0 0 |  0      1    |  1   1    1
```

Le colonne ¬(p∨q) e ¬p∧¬q coincidono. Lo stesso risultato si ottiene anche con un ragionamento, che il docente ha presentato passo per passo:
1. ¬(p ∨ q) è vera se e solo se p ∨ q è falsa;
2. una disgiunzione è falsa se e solo se i suoi argomenti sono entrambi falsi: p è falsa e q è falsa;
3. questo accade se e solo se ¬p e ¬q sono entrambe vere;
4. cioè se e solo se è vera la loro congiunzione ¬p ∧ ¬q.

È un caso delle leggi di De Morgan, che il corso riprenderà più in dettaglio. Si può dimostrare con le tavole oppure con un ragionamento a parole.

## Tautologie e contraddizioni
Una **tautologia** è una formula che è **sempre vera**, qualunque siano i valori delle sue componenti: nella colonna finale della sua tavola ci sono solo 1. Una **contraddizione** è l'opposto: una formula **sempre falsa**. La negazione di una tautologia è una contraddizione, e viceversa. Il **problema della tautologia** è appunto quello di stabilire se una formula vale sempre.

Le tavole di verità servono a controllare:
- se due formule sono equivalenti;
- se una formula è sempre vera (una legge logica), come le leggi di De Morgan o l'associatività della disgiunzione.

## Esempi svolti a lezione
**¬p ∨ q ∨ p.** Costruita la tavola, in ogni riga c'è almeno un 1: è una **tautologia**.

**p ∨ ¬p**, chiamata **terzo escluso**. Se p è vera la disgiunzione è vera perché un argomento è vero; se p è falsa, ¬p è vera e di nuovo la disgiunzione è vera. Il nome dice che "o p è vera o è falsa, e non c'è un terzo caso": in realtà, ha sottolineato il docente, la logica è costruita con soli due valori di verità, e ne esistono altre, con valori intermedi, usate in informatica per scopi diversi, ma qui si usa sempre la logica a due valori.

**(p ∨ q) ∧ ¬p.** È vera in una sola riga, quella con p falsa e q vera: non è né una tautologia né una contraddizione, ma equivale a ¬p ∧ q, più semplice (come visto nel capitolo precedente).

## Una dimostrazione algebrica
Lo stesso fatto si può dimostrare con un ragionamento algebrico, senza tavola, usando due proprietà della disgiunzione:
- **commutatività**: p ∨ q e q ∨ p hanno la stessa tavola di verità; la definizione dice che la disgiunzione è vera se almeno un argomento è vero, senza nominare l'ordine;
- **associatività**: (p ∨ q) ∨ r equivale a p ∨ (q ∨ r); si possono spostare le parentesi.

Per ¬p ∨ q ∨ p: con la commutatività si sposta p accanto a ¬p, con l'associatività si raggruppa (¬p ∨ p) ∨ q; la parte tra parentesi è un terzo escluso, sempre vera, quindi si ottiene vero ∨ q, che è vera perché un argomento è vero. Il risultato non dipende dal valore di q.

## Perché le tavole non bastano sempre
Le tavole di verità hanno un limite: le righe sono 2ⁿ. Con 1000 proposizioni atomiche sono 2¹⁰⁰⁰, un po' più di 10³⁰⁰ righe, un numero più grande del numero di particelle dell'universo. Con questa dimensione non si può usare la tavola, e servono metodi più veloci, che il corso accennerà più avanti. Il caso non è teorico: nella **verifica di sistemi complessi** (*model checking*) si descrive il sistema con una formula proposizionale che dice "non esiste una situazione di pericolo", con migliaia di affermazioni atomiche (la posizione e la velocità dei treni, lo stato dei segnali, la rete elettrica, il comportamento delle persone). Il docente ha citato studi di questo tipo per la metropolitana di Londra e per le ferrovie svedesi. Il model checking non fa parte del corso, ma è una delle motivazioni: a Fondamenti si impara la logica come base del ragionamento automatico.

Nella prossima lezione si introduce l'implicazione.
