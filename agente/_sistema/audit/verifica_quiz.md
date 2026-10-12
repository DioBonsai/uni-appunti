# Verifica dei quiz di Matematica discreta (150 domande)

Data: 2026-10-12. File verificati: quiz_2324.md, quiz_2425.md, quiz_2526.md (non modificati).

## Riepilogo

- Domande esaminate: 150
- OK: 147
- ERRORE risposta: 0
- ERRORE spiegazione: 2
- AMBIGUA: 1
- non verificabile: 0

Ogni risposta indicata (RISPOSTA) e' risultata corretta. I problemi riguardano solo il testo delle spiegazioni (2) e una formulazione ambigua (1, gia' marcata ATTENZIONE nel file).

Metodo: script Python (SymPy + forza bruta, scratchpad `verif.py`, 115 controlli automatici, convenzione permutazioni da destra a sinistra) per basi numeriche, generatori di Z_N, phi di Eulero, inversi, potenze modulari, numero di soluzioni delle congruenze (conteggio diretto su tutte le classi, confrontato per ogni opzione), tipi e potenze di permutazioni, composizioni (anche simboliche), ordini degli elementi di Z*_77, combinatoria (enumerazione di anagrammi, combinazioni, disposizioni), operazioni su insiemi. Le domande teoriche (appartenenza/inclusione, prodotti cartesiani, partizioni/ricoprimenti, parita' di permutazioni, periodo e relazioni di potenza, Lagrange, definibilita' di composizioni, omomorfismi Z24->Z60, minimo n per ordine 110 in S_n) sono state controllate sia a mano sia, dove possibile, in codice. Per ogni domanda e' stata riletta anche la spiegazione, confrontando i valori numerici citati.

## Problemi riscontrati

### 2324-v4-Q06 - ERRORE spiegazione

Risposta 2 corretta. Nella spiegazione, l'ultima frase dice che pi^3 "ha 3 cicli: due 4-cicli e 3 punti fissi": e' sbagliato contare 3 cicli. Con il calcolo type_pow([4,4,3],3): il 4-ciclo resta 4-ciclo (MCD(3,4)=1), il 3-ciclo diventa 3 punti fissi; pi^3 ha tipo (4,4) (due 4-cicli + 3 punti fissi, cioe' 5 cicli contando i fissi), quindi non e' un ciclo. Proposta: "π³ ha tipo (4,4) con 3 punti fissi, quindi non è un ciclo".

### 2425-v3-Q09 - ERRORE spiegazione

Risposta 2 corretta (unico MCD=1). La parentesi finale "con 20X ≡ 33 priva di soluzioni, le altre con 4, 8, 4, 2 soluzioni" e' incoerente: i numeri di soluzioni mod 56 calcolati a forza bruta sono 20X≡33: 0; 24X≡16: 8; 12X≡44: 4; 50X≡26: 2 (opzioni 1,3,4,5). Proposta: "opzione 1: 0 soluzioni (4∤33); opzioni 3, 4, 5: 8, 4, 2 soluzioni".

### 2425-v5-Q10 - AMBIGUA

Risposta 2 e' l'intesa del docente (gia' segnalata dalla riga ATTENZIONE) ma la formulazione e' davvero ambigua. Forza bruta (classi risolutive): opz.1 nessuna sol.; opz.2 8X≡22 mod 42 -> 2 sol. mod 42, 1 sola classe mod 21 (X≡8); opz.3 3 sol. mod 42, classi mod 21 {1,8,15}; opz.4 12X≡15 mod 21 -> 3 sol. {3,10,17}; opz.5 25X≡4 mod 42 -> 1 sol. mod 42 (X≡22), che riduce a 1 sola classe mod 21 (X≡1; 25X≡4 mod 21 -> 4X≡4). Quindi anche l'opz.5 e' "unica soluzione" (addirittura mod 42, e per riduzione mod 21). Le uniche opzioni con modulo 21 (1 e 4) hanno 0 e 3 soluzioni, quindi la risposta 2 regge solo leggendo "unica soluzione modulo 21" come unicita' della classe mod 21 dopo la riduzione. Nota anche: la spiegazione dice dell'opz.5 "una soluzione mod 42 (non mod 21)", ma la sua soluzione e' unica anche mod 21. Suggerimento: tenere 2, marcare come ambigua e aggiungere che l'opz.5 ha una soluzione unica mod 42.

## Tabella completa

| id | verdetto | note / correzione proposta |
|---|---|---|
| 2324-v1-Q01 | OK |  |
| 2324-v1-Q02 | OK |  |
| 2324-v1-Q03 | OK |  |
| 2324-v1-Q04 | OK |  |
| 2324-v1-Q05 | OK |  |
| 2324-v1-Q06 | OK |  |
| 2324-v1-Q07 | OK |  |
| 2324-v1-Q08 | OK |  |
| 2324-v1-Q09 | OK |  |
| 2324-v1-Q10 | OK |  |
| 2324-v2-Q01 | OK |  |
| 2324-v2-Q02 | OK |  |
| 2324-v2-Q03 | OK |  |
| 2324-v2-Q04 | OK |  |
| 2324-v2-Q05 | OK |  |
| 2324-v2-Q06 | OK |  |
| 2324-v2-Q07 | OK |  |
| 2324-v2-Q08 | OK |  |
| 2324-v2-Q09 | OK |  |
| 2324-v2-Q10 | OK |  |
| 2324-v3-Q01 | OK |  |
| 2324-v3-Q02 | OK |  |
| 2324-v3-Q03 | OK |  |
| 2324-v3-Q04 | OK |  |
| 2324-v3-Q05 | OK |  |
| 2324-v3-Q06 | OK |  |
| 2324-v3-Q07 | OK |  |
| 2324-v3-Q08 | OK |  |
| 2324-v3-Q09 | OK |  |
| 2324-v3-Q10 | OK |  |
| 2324-v4-Q01 | OK |  |
| 2324-v4-Q02 | OK |  |
| 2324-v4-Q03 | OK |  |
| 2324-v4-Q04 | OK |  |
| 2324-v4-Q05 | OK |  |
| 2324-v4-Q06 | ERRORE spiegazione | Risposta 2 corretta. Nella spiegazione, l'ultima frase dice che pi^3 "ha 3 cicli: due 4-cicli e 3 punti fissi": e' sbagliato contare 3 cicli. Con il calcolo type_pow([4,4,3],3): il 4-ciclo resta 4-ciclo (MCD(3,4)=1), il 3-ciclo diventa 3 punti fissi; pi^3 ha tipo (4,4) (due 4-cicli + 3 punti fissi, cioe' 5 cicli contando i fissi), quindi non e' un ciclo. Proposta: "π³ ha tipo (4,4) con 3 punti fissi, quindi non è un ciclo". |
| 2324-v4-Q07 | OK |  |
| 2324-v4-Q08 | OK |  |
| 2324-v4-Q09 | OK |  |
| 2324-v4-Q10 | OK |  |
| 2324-v5-Q01 | OK |  |
| 2324-v5-Q02 | OK |  |
| 2324-v5-Q03 | OK |  |
| 2324-v5-Q04 | OK |  |
| 2324-v5-Q05 | OK |  |
| 2324-v5-Q06 | OK |  |
| 2324-v5-Q07 | OK |  |
| 2324-v5-Q08 | OK |  |
| 2324-v5-Q09 | OK |  |
| 2324-v5-Q10 | OK |  |
| 2425-v1-Q01 | OK |  |
| 2425-v1-Q02 | OK |  |
| 2425-v1-Q03 | OK |  |
| 2425-v1-Q04 | OK |  |
| 2425-v1-Q05 | OK |  |
| 2425-v1-Q06 | OK |  |
| 2425-v1-Q07 | OK |  |
| 2425-v1-Q08 | OK |  |
| 2425-v1-Q09 | OK | OK (nota: le opz. 4 e 5 sono modulo 48; comunque conteggi 1 e 6 mod 48, nessuna con esattamente 2: la risposta 2 resta unica) |
| 2425-v1-Q10 | OK |  |
| 2425-v2-Q01 | OK |  |
| 2425-v2-Q02 | OK |  |
| 2425-v2-Q03 | OK |  |
| 2425-v2-Q04 | OK |  |
| 2425-v2-Q05 | OK |  |
| 2425-v2-Q06 | OK |  |
| 2425-v2-Q07 | OK |  |
| 2425-v2-Q08 | OK |  |
| 2425-v2-Q09 | OK |  |
| 2425-v2-Q10 | OK |  |
| 2425-v3-Q01 | OK |  |
| 2425-v3-Q02 | OK |  |
| 2425-v3-Q03 | OK |  |
| 2425-v3-Q04 | OK |  |
| 2425-v3-Q05 | OK |  |
| 2425-v3-Q06 | OK |  |
| 2425-v3-Q07 | OK |  |
| 2425-v3-Q08 | OK |  |
| 2425-v3-Q09 | ERRORE spiegazione | Risposta 2 corretta (unico MCD=1). La parentesi finale "con 20X ≡ 33 priva di soluzioni, le altre con 4, 8, 4, 2 soluzioni" e' incoerente: i numeri di soluzioni mod 56 calcolati a forza bruta sono 20X≡33: 0; 24X≡16: 8; 12X≡44: 4; 50X≡26: 2 (opzioni 1,3,4,5). Proposta: "opzione 1: 0 soluzioni (4∤33); opzioni 3, 4, 5: 8, 4, 2 soluzioni". |
| 2425-v3-Q10 | OK |  |
| 2425-v4-Q01 | OK |  |
| 2425-v4-Q02 | OK |  |
| 2425-v4-Q03 | OK |  |
| 2425-v4-Q04 | OK |  |
| 2425-v4-Q05 | OK |  |
| 2425-v4-Q06 | OK |  |
| 2425-v4-Q07 | OK |  |
| 2425-v4-Q08 | OK |  |
| 2425-v4-Q09 | OK |  |
| 2425-v4-Q10 | OK |  |
| 2425-v5-Q01 | OK |  |
| 2425-v5-Q02 | OK |  |
| 2425-v5-Q03 | OK |  |
| 2425-v5-Q04 | OK |  |
| 2425-v5-Q05 | OK |  |
| 2425-v5-Q06 | OK |  |
| 2425-v5-Q07 | OK |  |
| 2425-v5-Q08 | OK |  |
| 2425-v5-Q09 | OK |  |
| 2425-v5-Q10 | AMBIGUA | Risposta 2 e' l'intesa del docente (gia' segnalata dalla riga ATTENZIONE) ma la formulazione e' davvero ambigua. Forza bruta (classi risolutive): opz.1 nessuna sol.; opz.2 8X≡22 mod 42 -> 2 sol. mod 42, 1 sola classe mod 21 (X≡8); opz.3 3 sol. mod 42, classi mod 21 {1,8,15}; opz.4 12X≡15 mod 21 -> 3 sol. {3,10,17}; opz.5 25X≡4 mod 42 -> 1 sol. mod 42 (X≡22), che riduce a 1 sola classe mod 21 (X≡1; 25X≡4 mod 21 -> 4X≡4). Quindi anche l'opz.5 e' "unica soluzione" (addirittura mod 42, e per riduzione mod 21). Le uniche opzioni con modulo 21 (1 e 4) hanno 0 e 3 soluzioni, quindi la risposta 2 regge solo leggendo "unica soluzione modulo 21" come unicita' della classe mod 21 dopo la riduzione. Nota anche: la spiegazione dice dell'opz.5 "una soluzione mod 42 (non mod 21)", ma la sua soluzione e' unica anche mod 21. Suggerimento: tenere 2, marcare come ambigua e aggiungere che l'opz.5 ha una soluzione unica mod 42. |
| 2526-v1-Q01 | OK |  |
| 2526-v1-Q02 | OK |  |
| 2526-v1-Q03 | OK |  |
| 2526-v1-Q04 | OK |  |
| 2526-v1-Q05 | OK |  |
| 2526-v1-Q06 | OK |  |
| 2526-v1-Q07 | OK |  |
| 2526-v1-Q08 | OK |  |
| 2526-v1-Q09 | OK |  |
| 2526-v1-Q10 | OK |  |
| 2526-v2-Q01 | OK |  |
| 2526-v2-Q02 | OK |  |
| 2526-v2-Q03 | OK |  |
| 2526-v2-Q04 | OK |  |
| 2526-v2-Q05 | OK |  |
| 2526-v2-Q06 | OK |  |
| 2526-v2-Q07 | OK |  |
| 2526-v2-Q08 | OK |  |
| 2526-v2-Q09 | OK |  |
| 2526-v2-Q10 | OK |  |
| 2526-v3-Q01 | OK |  |
| 2526-v3-Q02 | OK |  |
| 2526-v3-Q03 | OK |  |
| 2526-v3-Q04 | OK |  |
| 2526-v3-Q05 | OK |  |
| 2526-v3-Q06 | OK |  |
| 2526-v3-Q07 | OK |  |
| 2526-v3-Q08 | OK |  |
| 2526-v3-Q09 | OK |  |
| 2526-v3-Q10 | OK |  |
| 2526-v4-Q01 | OK |  |
| 2526-v4-Q02 | OK |  |
| 2526-v4-Q03 | OK |  |
| 2526-v4-Q04 | OK |  |
| 2526-v4-Q05 | OK |  |
| 2526-v4-Q06 | OK |  |
| 2526-v4-Q07 | OK |  |
| 2526-v4-Q08 | OK |  |
| 2526-v4-Q09 | OK |  |
| 2526-v4-Q10 | OK |  |
| 2526-v5-Q01 | OK |  |
| 2526-v5-Q02 | OK |  |
| 2526-v5-Q03 | OK |  |
| 2526-v5-Q04 | OK |  |
| 2526-v5-Q05 | OK |  |
| 2526-v5-Q06 | OK |  |
| 2526-v5-Q07 | OK |  |
| 2526-v5-Q08 | OK |  |
| 2526-v5-Q09 | OK |  |
| 2526-v5-Q10 | OK |  |
