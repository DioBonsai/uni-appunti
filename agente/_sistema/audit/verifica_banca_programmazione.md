# Verifica banca_programmazione.md (40 domande)

Metodo: simulazione in Python (troncamento verso zero, % col segno del dividendo) di tutte le domande con codice o calcolo (prg-007, 008, 011, 013, 014, 017, 018, 019, 021, 022, 023, 026, 027, 035, 039); le domande di concetto confrontate con Riassunto Programmazione.docx e Riassunto Laboratorio.docx (algoritmo: due requisiti, Wirth, EDVAC, PC/IR, overflow indefinito, stack decrescente e SP decrementato, variabile non inizializzata indeterminata, gcc -c, -Wall/-Werror).

Risultato: 40/40 domande OK, 0 errori, nessuna modifica al file.

- Esattamente una opzione corretta per domanda, coincidente con RISPOSTA e SPIEGAZIONE.
- Valori simulati: 011 -> 16; 017 -> 4 3; 018 -> 3 3 10; 019 -> 1; 021 -> 3 2; 022 -> 6 7; 023 -> 6; 026 -> 11 11; 027 -> 7 9; 039 -> 13; 035 -> "000007|     7"; 008 -> 2 ADD, @m = 6; 007 -> A = 4, B = -8.
- Nessuna affermazione falsa o non supportata dai Word trovata.

Note minori (nessuna azione necessaria):
- prg-010: lo "x resta indeterminato / riparte dal minimo" e' presentato correttamente come UB con comportamento tipico.
- prg-015: la descrizione di SP decrementato per ogni dichiarazione segue il modello didattico del corso (i compilatori reali possono riservare lo spazio in blocco).
- prg-002: assume che il controllo sia solo i = n (come nel testo); in pratica l'int overflowerebbe prima o poi, ma e' coerente con l'algoritmo teorico.
- prg-034: l'esito dipende dal fatto che scanf %d si fermi al punto; comportamento standard e definito.
