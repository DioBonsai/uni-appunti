# Algebra lineare, Lezione 5: note dall'audio (registrazione 1 ott 2025, prof. Radeschi)

Fonte: trascrizione `_sistema/trascrizioni/algebra_L5_2025.txt` (Whisper small, con errori di termini) incrociata con le lavagne (`L5_lavagne_video2025.md`). Qui solo ciò che il docente dice a voce e NON compare nelle lavagne. Durata 102 min, pausa di 10 minuti a circa 50 min. Gli ultimi ~8 minuti sono domande e esercizi di numeri complessi di uno studente, e un tratto 1:31-1:36 è corrotto dalla trascrizione (ripetizioni).

## Motivazione e spazio euclideo (0-17 min)
- Dopo aver "accumulato abbastanza tecnologia" (campi, complessi, polinomi) si possono definire gli spazi vettoriali, "gli oggetti fondamentali del corso". Si comincia da un esempio speciale: lo spazio euclideo.
- Lo spazio euclideo è lo spazio della geometria classica (punti, rette…); però quelli che si riescono a vedere hanno dimensione 2 o 3, mentre nelle applicazioni servono spazi più grandi, che non si possono visualizzare: per questo si definisce lo spazio euclideo in modo **algebrico**.
- ℝⁿ è il prodotto cartesiano di ℝ con sé stesso n volte (richiamo a Matematica discreta): n copie di ℝ, gli elementi sono n-uple di numeri reali. Per pura comodità le n-uple si scrivono **in verticale**.
- "Vettore" è in realtà un termine più generale: per ora è un elemento di ℝⁿ; x_i è la i-esima componente o coordinata.
- ℝ² si rappresenta nel piano cartesiano (il vettore di coordinate a, b è il punto di coordinate a e b), ℝ³ nello spazio: si parte dall'origine e ci si sposta di a unità lungo x, poi b lungo y, poi c lungo z. I tre assi sono "indipendenti" (la z esce dalla lavagna: non si può disegnare in prospettiva).
- Un vettore di ℝⁿ si può vedere come n-upla (modo più usato, perché permette di fare i conti), come punto o come freccia dall'origine; "sceglieremo sempre la scrittura che ci conviene di più, con la sicurezza che queste tre rappresentazioni sono sostanzialmente equivalenti".
- Esempi fatti: il punto (3, 2) in ℝ²: 3 unità in direzione x e 2 verso l'alto; in ℝ³ il punto con x = 3, y = 4, z = 2 corrisponde al vettore (3, 4, 2).
- Domanda: "che dimensione ha ℝⁿ?" → la dimensione non è ancora definita; per ora "n-dimensionale" va letto come una parola unica, si vedrà "non troppo in futuro" che ℝⁿ ha dimensione n.

## Operazioni (15-30 min)
- Ogni volta che si introduce un insieme in algebra ci si chiede **quali operazioni si possono fare**: su ℝⁿ sono due, la somma di vettori e la moltiplicazione per un numero reale.
- La somma prende due vettori e dà un vettore; si calcola **termine a termine**. Il prodotto per scalare moltiplica tutte le componenti per lo stesso numero.
- Geometria: la somma segue la **regola del parallelogramma** (il punto opposto all'origine nel parallelogramma di lati v e w è v + w). Il prodotto per a allunga il vettore di un fattore a; con a negativo il vettore ha la stessa lunghezza ma direzione opposta ("moltiplicare per un numero negativo vuol dire prendere la direzione opposta"). Esempio: v = (3, 1), 2v = (6, 2); w = (1, 2), v + w = (4, 3).
- Domanda: il coefficiente angolare cambia? No: il rapporto y/x non cambia moltiplicando per uno scalare (3/1 = 6/2).
- I numeri qui non servono a quantificare nulla ma a **moltiplicare vettori**: si chiamano **scalari**; scalare = elemento del campo scelto (ℝ → scalari reali, ℂ → scalari complessi). L'operazione si chiama "moltiplicazione per scalare".

## Proprietà (29-50 min)
- Il docente annuncia "nove" proprietà ma ne elenca e scrive 8 (la trascrizione ha probabilmente sbagliato; sulle lavagne e a voce sono 8: 4 sulla sola somma, 4 che legano somma e prodotto).
- ② elemento neutro: lo si scrive 0_ℝⁿ "per non confonderlo con il numero zero"; è il vettore con tutte le componenti nulle. ③ ogni vettore ha un opposto: se v = (x₁, …, xₙ) l'opposto è (−x₁, …, −xₙ) = −v. ④ commutativa.
- Domanda: perché la commutatività è la quarta e non subito insieme alla somma? Perché si vuole impostare tutto in modo da poterlo applicare a contesti più generali in cui serve distinguere l'ordine (gruppi non commutativi).
- ⑤: nel prodotto (ab)·v il prodotto "ab" è un prodotto di numeri (in ℝ), tutti gli altri sono moltiplicazioni per scalare. ⑥: la somma a + b è una somma di numeri reali, mentre la somma a destra è una somma di vettori. ⑦ è un'altra distributività. ⑧: 1 è l'elemento neutro della moltiplicazione (ogni campo ha un elemento neutro del prodotto, "il numero uno è speciale").
- Le proprietà andrebbero dimostrate (verificate) ma "noi non lo faremo; se volete divertirvi, fatelo": non è una lista fatta per divertimento, sono le proprietà che definiscono uno spazio vettoriale.

## Gruppi (43-50 min)
- Un insieme con un'operazione che soddisfa le proprietà ①②③ si chiama **gruppo**. "Di gruppi non ne vedremo tanti, ne vedrete molti in Matematica discreta." Un'operazione è una funzione che prende due elementi e dà un elemento; con nome astratto si usa ∗ (asterisco).
- ① associatività, ② esistenza dell'elemento neutro, ③ esistenza degli inversi. In notazione moltiplicativa si parla di inversi; nel caso speciale dell'addizione si chiamano opposti.
- Se vale anche la ④ il gruppo è **commutativo o abeliano**; in Matematica discreta si vedranno gruppi di permutazioni, che sono gruppi non abeliani ("l'ordine della somma è importante"). ℝⁿ con la somma è un gruppo abeliano.

## Spazio vettoriale (dopo la pausa, 51-70 min)
- Un insieme con due operazioni (somma e moltiplicazione per scalare) che soddisfa le stesse proprietà di ℝⁿ è uno spazio vettoriale. L'ordine corretto per definirlo: **prima si sceglie il campo degli scalari** (ℝ, ℂ, ℚ…), poi un insieme V con le due operazioni.
- (V, +) è un gruppo abeliano per le proprietà ①–④; valgono ⑤–⑧ con scalari nel campo scelto.
- Per comunicare uno spazio vettoriale (a un collega o a un computer) bisogna specificare **quattro ingredienti**: l'insieme, il campo degli scalari, come è definita la somma, come è definita la moltiplicazione per scalare ("non sono cose che potete ricavare voi").
- Esempi: ℝⁿ su ℝ; ℝ[x] con somma di polinomi "termine a termine" e moltiplicazione per uno scalare reale (si moltiplica ogni coefficiente); poi la generalizzazione: per ogni campo 𝕂 si definisce 𝕂ⁿ (ℂⁿ, ℚⁿ…) con le stesse operazioni ma scalari in 𝕂; e 𝕂[x] con coefficienti in 𝕂 e scalari in 𝕂.

## Osservazioni (70-95 min)
- Zero e opposto: per trovare lo zero di uno spazio vettoriale basta moltiplicare un qualunque vettore per lo scalare 0 (0·v = 0_V); per l'opposto basta moltiplicare per −1 ((−1)·v = −v). Esempi: lo zero di ℝ[x] è il polinomio nullo (0xⁿ + … + 0): se non si "vede", si prende un polinomio qualunque, per esempio x + 1, e lo si moltiplica per 0; in 𝕂ⁿ lo zero è (0, …, 0); l'opposto di un polinomio è quello con tutti i coefficienti cambiati di segno.
- 𝕂¹ = 𝕂: ogni campo è uno spazio vettoriale su sé stesso (la somma è quella del campo, e la moltiplicazione per scalare è il prodotto del campo). Ad esempio ℂ è uno spazio vettoriale su ℂ.
- Definire lo spazio vettoriale serve a dire **qual è l'insieme degli scalari** con cui si può moltiplicare. ℂ si può considerare anche come spazio vettoriale su ℝ, se si decide di moltiplicare solo per numeri reali: l'insieme e la somma restano gli stessi (come gruppo è lo stesso), cambiano solo gli scalari. In generale, se un campo è contenuto in un altro (come ℝ in ℂ) il campo più grande è sempre uno spazio vettoriale sul campo più piccolo. "Non è una cosa a caso: è un concetto fondamentale di una teoria, la teoria di Galois."
- Esempio funzioni ℝ → ℝ (quelle degli studi di funzione delle superiori): somma e prodotto per scalare definiti **punto per punto** (valore in ogni x). Esempi: eˣ + sin x; 3·e^{x²} ("calcolate prima e^{x²} e poi moltiplicate per 3"). Commento: spazi di funzioni e spazi come ℝⁿ sono molto diversi: gli uni "assolutamente selvaggi", gli altri più docili; il concetto di **dimensione** permetterà di distinguerli: ℝⁿ ha dimensione finita, lo spazio di tutte le funzioni dimensione infinita. [Il seguito sul corso è nel tratto corrotto della trascrizione: da verificare.]

## Esercizi (95-102 min)
- Gli esercizi sulle proprietà (verificare gli assiomi) servono "solo ad allenarsi a capire come funzionano questi oggetti" e, dice il docente, **non verranno mai all'esame** (la dimostrazione che qualcosa è uno spazio vettoriale con tutte le proprietà). [Trascrizione rumorosa: da confermare.]
- Poi domande di uno studente su esercizi di numeri complessi: trovare i numeri complessi z = a + ib per cui z + z̄ = i (z + z̄ = 2a, parte immaginaria 0 ≠ 1: nessuna soluzione); un caso con a² + b² = 1 (punti sulla circonferenza unitaria); forma esponenziale di numeri reali (2 = 2e^{i0}, −3 = 3e^{iπ}). Non fanno parte della L5.
