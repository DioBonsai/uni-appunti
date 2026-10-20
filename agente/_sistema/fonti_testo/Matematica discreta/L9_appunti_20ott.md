# Matematica discreta, lezione 9 (20 ottobre 2026): appunti a mano di Emanuele
(Trascrizione dalle 2 pagine di `fonti/Matematica discreta/L9_appunti_20ott.pdf`; le formule sono rese in testo. Tra parentesi quadre le mie note di lettura.)

## Pagina 1
**COMBINAZIONI SEMPLICI.** A insieme con |A| = n. Fissiamo k, 0 ≤ k ≤ n, e scegliamo un S ⊆ A con |S| = k.
Problema: calcolare il numero C^S_{n,k} delle scelte possibili: C^S_{n,k} = |{ S ⊆ A : |S| = k }|.

Per scegliere S scelgo i suoi elementi in un certo ordine. Questa è una disposizione: ne ho D^S_{n,k} = n!/(n−k)!.
Esempio: S = {c, e, f} = {e, c, f} = {f, c, e} = … sono 3! riordinamenti. In generale una disposizione è una funzione I_k → A (1 → a₁, 2 → a₂, …, k → a_k) con S = {a₁, …, a_k}; lo stesso S si ottiene da k! riordinamenti.

Poiché ogni combinazione semplice si può ottenere da k! riordinazioni diverse:
C^S_{n,k} = (1/k!) · D^S_{n,k} = n! / (k! (n−k)!) = (n k)   ← **coefficienti binomiali**.

Casi: C^S_{n,0} = (n 0) = n!/(n! · 0!) = 1; C^S_{n,n} = (n n) = n!/(n! · 0!) = 1.
Esempio: (6 3) = 6!/(3! 3!) = 720/36 = 20.

**Problema #1.** Quante sono le sestine possibili nel superenalotto? I₉₀ = {1, …, 90}; C^S_{90,6} = 90!/(6! 84!) = (90·89·88·87·86·85)/720 [a margine, circa 622 milioni].

**Problema #2.** Una scuola di ballo ha 10 studenti maschi e 12 donne. I maestri, per una coreografia, scelgono 4 maschi e 4 femmine. Quante sono le scelte possibili? Totale = (10 4)·(12 4) = (10!/(4! 6!))·(12!/(4! 8!)) = 210 · 495. [schema ad albero: Donne / Uomini; "ho (10 4) possibili scelte"]

**Problema #3.** Una gelateria propone gelati di 15 gusti ed è possibile acquistare coni piccoli / medi / grandi (1 gusto / 2 gusti / 3 gusti).
- Piccolo: C^S_{15,1} = 15!/(1! 14!) = 15.
- Medio: C^S_{15,2} = 15!/(2! 13!) = (15·14)/2 = 105.
- Grande: C^S_{15,3} = 15!/(3! 12!) = (15·14·13)/(3·2·1) = 455.
[schema ad albero con i tre rami 15, 105, 455]

## Pagina 2
**Problema #4.** Una squadra di calcio ha una rosa formata da 3 portieri, 8 difensori, 7 centrocampisti, 4 attaccanti. L'allenatore decide di schierare 1 portiere, 4 difensori, 4 centrocampisti, 2 attaccanti.
- a (attaccanti): C^S_{4,2} = 4!/(2! 2!) = 6
- c (centrocampisti): C^S_{7,4} = 7!/(4! 3!) = 35
- d (difensori): C^S_{8,4} = 8!/(4! 4!) = 70
- p (portieri): C^S_{3,1} = 3
Totale: 6 · 35 · 70 · 3 = 44100.

**Monomi e combinazioni con ripetizione.** Monomio x³ y² z⁵ ; grado = somma degli esponenti. 3 variabili, grado 10.
Si rappresenta con 10 caselle di lettere e 2 separazioni: X X X | Y Y | Z Z Z Z Z ↔ x³ y² z⁵; X X X X | Y Y Y | Z Z Z ↔ x⁴ y³ z³ [nel disegno: 12 caselle in cui 10 sono lettere e 2 sono separatori, con i separatori indicati da un punto].
«Tutta l'informazione per scrivere il monomio sta dove metto le separazioni.»
Contare i monomi di 3 variabili di grado 10 equivale a contare quante scelte posso fare per 2 caselle di separazione. Ma scegliere arbitrariamente 2 caselle su 12 è una combinazione semplice di ordine 2 sulle 12:
C^R_{10,3} = C^S_{12,2} = 12!/(2! 10!) = 66.
[Attenzione: con la formula generale sotto (n = 3 variabili, k = 10 grado) l'esempio andrebbe scritto C^R_{3,10}; negli appunti gli indici sono scambiati. Il valore 66 è giusto: (12 2) = 66.]
Formula generale: C^R_{n,k} = C^S_{k+n−1, n−1} = (k+n−1)! / ((n−1)! k!)  [n = numero di tipi/variabili, k = quanti elementi si prendono].

**Problema #5.** 20 tipi di pasticcini; volete un vassoio con 30 pasticcini: C^R_{20,30} = C^S_{49,19} = (49 19) = 49!/(19! 30!).
