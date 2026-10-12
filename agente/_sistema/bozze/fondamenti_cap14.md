# 14. Le Tavole di Verità
## A che cosa servono
Una **tavola di verità** è un elenco di **tutte** le combinazioni possibili dei valori di verità delle componenti atomiche, con a fianco, per ciascuna combinazione, il valore di verità della proposizione composta. È un modo alternativo di definire un connettivo: non più come circuito, ma come tabella. Serve perché non è facile stabilire se due circuiti sono equivalenti, mentre si possono leggere come formule proposizionali e confrontare le loro tavole: è l'applicazione principale delle tavole di verità in informatica.

## Come si costruisce
Nella tavola si mettono a sinistra le componenti atomiche (indicate con lettere minuscole, p, q, r, …) e nell'ultima colonna la proposizione composta. Le componenti possono essere qualsiasi affermazione a cui si sa assegnare un valore di verità; per le equazioni vanno prima assegnati i parametri. Per ogni riga si scrive il valore di verità della formula seguendo la definizione del connettivo: nella tavola della disgiunzione, per esempio, si scrive 1 ogni volta che c'è almeno un 1 tra gli argomenti, e 0 solo quando sono entrambi 0.

Una formula più complessa si calcola **a passi**, con una colonna per ogni sottoformula. Esempio del docente, la formula (p ∨ q) ∧ ¬p: ci sono due variabili, ma più sottoformule (p ∨ q, ¬p e l'intera congiunzione).

```
p q | p∨q  ¬p | (p∨q)∧¬p
1 1 |  1    0  |    0
1 0 |  1    0  |    0
0 1 |  1    1  |    1
0 0 |  0    1  |    0
```

La congiunzione ha un solo 1, quello della riga in cui p è falsa e q è vera. Lo stesso risultato si ottiene ragionando: se p è falsa, il primo argomento p ∨ q è vero solo se lo è q; se p è vera, ¬p è falsa e la congiunzione è falsa. Quindi (p ∨ q) ∧ ¬p equivale a ¬p ∧ q, una formula più breve: un modo per semplificare e, in un circuito, risparmiare una porta.

## Quante righe ci sono
Con **n** proposizioni atomiche le righe sono **2ⁿ**: 1 proposizione dà 2 righe, 2 danno 4, 3 danno 8 (come nell'esempio del libro). È un teorema che si dimostra per induzione e che si vedrà anche in Matematica discreta.

Bisogna elencare **tutti** i casi, e **una volta sola**. La prima richiesta è di correttezza: se manca un caso la definizione o il confronto non sono corretti. La seconda è di efficienza: ripetere uno stesso caso è uno spreco.

## Come essere sicuri di averli scritti tutti
Il docente ne ha mostrati due e ha descritto un terzo, quello del libro.
1. **Contare e confrontare** (principio della piccionaia): se le righe sono 2ⁿ e nessuna compare due volte, allora sono tutte, perché se ne avessi dimenticata una dovrebbe comparirne una ripetuta. Si contano le righe, poi si controlla riga per riga che non sia già stata scritta.
2. **Contare all'indietro**: le n proposizioni atomiche, se si rappresentano con 0 e 1, formano un numero binario di n cifre. Si scrive prima la riga con tutti 1 (cioè 2ⁿ − 1) e si scende fino alla riga di tutti 0. Con 3 variabili: 111 (7), 110 (6), 101 (5), 100 (4), 011 (3), 010 (2), 001 (1), 000 (0). Scrivere la lista all'incontrario non cambia nulla, perché conta solo che ci siano tutti i casi.
3. **Il metodo dei periodi del libro**: con n variabili le righe sono 2ⁿ. La prima variabile si scrive a blocchi lunghi quanto metà delle righe (nel caso di 8 righe: 4 volte 1, poi 4 volte 0); la seconda con blocchi dimezzati (2 volte 1, 2 volte 0, e si ripete); la terza con blocchi di lunghezza 1 (1, 0, 1, 0, …); con 4 variabili i blocchi sono lunghi 8, 4, 2, 1 (il docente li chiama periodi). È un terzo modo per prenderli tutti, una volta ciascuno.

## Dualità tra and e or
Nell'ordine del libro la congiunzione ha un solo 1 (quello con tutti gli argomenti veri, in cima alla tavola), mentre la disgiunzione ha un solo 0 (quello con tutti gli argomenti falsi, in fondo). Quindi le due tavole si ottengono l'una dall'altra **scambiando 0 e 1** (e scambiando sopra e sotto): si dice che congiunzione e disgiunzione sono **duali**. La negazione è duale di sé stessa, perché scambiando 0 e 1 nella sua tavola si ottiene la stessa tavola (è **autoduale**). Il docente ha anticipato che torneranno più avanti, perché è più importante di quanto sembri: tornerà quando si studieranno le leggi di De Morgan.

Il prossimo capitolo usa le tavole per confrontare formule: equivalenze, tautologie e contraddizioni.
