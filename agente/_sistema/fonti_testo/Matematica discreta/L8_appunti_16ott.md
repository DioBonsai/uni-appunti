# L8 – appunti a mano (16 ott 2026), trascritti dall'immagine

**A insieme finito.** Ordinare A equivale a dare una funzione biettiva f: {1,2,…,n} → A, cioè I_n → A.
Tabella I_n | A: posizione 1 → n scelte; posizione 2 → n−1 scelte; …; posizione n−1 → 2 scelte; posizione n → 1 scelta. (Albero con n, n−1, … diramazioni.)
n(n−1)(n−2)…3·2·1 = n!, «n fattoriale».
1! = 1, 2! = 2, 3! = 6, 4! = 24, 5! = 120, 6! = 720.
Convenzionale: 0! = 1. Ricorsiva: n! = n·(n−1)!.

**Anagramma.** A alfabeto, cioè insieme di simboli; es. A = {A,…,Z}. Una parola è una successione finita di lettere, es. TUZAAB.
Fissare una parola di lunghezza ℓ vuol dire fissare una funzione P: I_ℓ → A.
Un anagramma di P è un rimescolamento delle lettere in P. Es.: AGO, DAG... → ordinando l'insieme {A,G,O}: AGO, AOG, GAO, GOA, OAG, OGA. PORTA → 5! anagrammi.
In generale: una parola di lunghezza ℓ avrà k simboli ripetuti, dove lo j-esimo simbolo ripetuto compare r_j > 1 volte.

Problemi proposti: ① contare i possibili podi nella finale dei 100 m alle Olimpiadi. ② Un falegname produce 5 oggetti diversi e ha a disposizione 4 smalti con cui colorare.

**Disposizioni.** Sia A un insieme. Una disposizione è una scelta ordinata di elementi di A. 2 tipi: (due trattini non compilati nell'immagine).
**Disposizioni con ripetizione:** insieme A, |A| = n. In A devo fare le scelte ordinate (k scelte).
