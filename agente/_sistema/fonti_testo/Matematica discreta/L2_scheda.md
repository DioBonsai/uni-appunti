# L2_scheda

<!-- pagina 1 -->
Matematica Discreta — Universit`a degli Studi di Torino (Informatica, Canale B)
Lezione 2: 02/10/2026
Scheda di Studio: Lezione 2 — Matematica Discreta
Differenza, De Morgan, Insieme delle Parti, Induzione e Partizioni
Riferimento libro di testo: A. Mori, Capitolo 1 (§ 1.2, 1.3, 1.4, 1.5) — Universit`a di Torino
1. Differenza di Insiemi e Complementare
Siano A e B due insiemi definiti in un universo comune.
Differenza di Insiemi e Complementare (§ 1.4)
 Differenza di insiemi (A \ B): L’insieme degli elementi che appartengono ad A ma non appartengono a B:
A \ B = {x | x ∈A ∧x /∈B}
 Complementare di B in A (CA(B)): Quando B `e un sottoinsieme di A (B ⊆A), la differenza A \ B prende
il nome di complementare di B rispetto ad A:
CA(B) = {x ∈A | x /∈B}
Propriet`a fondamentali del complementare: Se B ⊆A, valgono le seguenti identit`a immediate:
i) CA(∅) = A
e
CA(A) = ∅
ii) Involutivit`a del complementare: CA(CA(B)) = B
iii) B ∩CA(B) = ∅
e
B ∪CA(B) = A
2. Leggi di De Morgan e Dimostrazioni Formali
Le leggi di De Morgan stabiliscono il legame duale tra unione/intersezione e complementazione.
Teorema: Leggi di De Morgan (§ 1.4, Proposizione 1.15)
Siano S, T ⊆A. Valgono le seguenti uguaglianze:
1. CA(S ∪T) = CA(S) ∩CA(T)
(Il complementare dell’unione `e l’intersezione dei complementari)
2. CA(S ∩T) = CA(S) ∪CA(T)
(Il complementare dell’intersezione `e l’unione dei complementari)
Dimostrazione Formale della 1a Legge di De Morgan
Dimostriamo che x ∈CA(S ∪T) ⇐⇒x ∈CA(S) ∩CA(T) mediante equivalenze logiche:
x ∈CA(S ∪T) ⇐⇒x ∈A ∧x /∈(S ∪T)
⇐⇒x ∈A ∧¬(x ∈S ∨x ∈T)
⇐⇒x ∈A ∧(x /∈S ∧x /∈T)
(legge logica: ¬(P ∨Q) ⇐⇒¬P ∧¬Q)
⇐⇒(x ∈A ∧x /∈S) ∧(x ∈A ∧x /∈T)
(idempotenza e riordinamento)
⇐⇒x ∈CA(S) ∧x ∈CA(T)
⇐⇒x ∈CA(S) ∩CA(T)
■
Pagina 1

<!-- pagina 2 -->
Matematica Discreta — Universit`a degli Studi di Torino (Informatica, Canale B)
Lezione 2: 02/10/2026
Dimostrazione Formale della 2a Legge di De Morgan (Esercizio svolto)
Dimostriamo che x ∈CA(S ∩T) ⇐⇒x ∈CA(S) ∪CA(T):
x ∈CA(S ∩T) ⇐⇒x ∈A ∧x /∈(S ∩T)
⇐⇒x ∈A ∧¬(x ∈S ∧x ∈T)
⇐⇒x ∈A ∧(x /∈S ∨x /∈T)
(legge logica: ¬(P ∧Q) ⇐⇒¬P ∨¬Q)
⇐⇒(x ∈A ∧x /∈S) ∨(x ∈A ∧x /∈T)
(distributivit`a di ∧su ∨)
⇐⇒x ∈CA(S) ∨x ∈CA(T)
⇐⇒x ∈CA(S) ∪CA(T)
■
Pagina 2

<!-- pagina 3 -->
Matematica Discreta — Universit`a degli Studi di Torino (Informatica, Canale B)
Lezione 2: 02/10/2026
3. L’Insieme delle Parti P(A)
Definizione: Insieme delle Parti (§ 1.2, Definizione 1.8)
Sia A un insieme. L’insieme delle parti (o insieme potenza) di A, indicato con P(A) oppure 2A, `e l’insieme di
tutti i sottoinsiemi di A:
P(A) = {S | S ⊆A}
Nota cruciale: Gli elementi di P(A) sono anch’essi insiemi! In particolare, per qualsiasi insieme A, si ha sempre
∅∈P(A) e A ∈P(A).
Costruzione della Cardinalit`a |P(A)| per induzione intuitiva:
 Se A = ∅
(|A| = 0) =⇒P(∅) = {∅} =⇒|P(∅)| = 1 = 20.
 Se A = {a}
(|A| = 1) =⇒P(A) = {∅, {a}} =⇒|P(A)| = 2 = 21.
 Se A = {a, b}
(|A| = 2) =⇒P(A) = {∅, {a}, {b}, {a, b}} =⇒|P(A)| = 4 = 22.
 Se A = {a, b, c}
(|A| = 3) =⇒|P(A)| = 8 = 23.
Teorema sulla Cardinalit`a dell’Insieme delle Parti
Se A `e un insieme finito con |A| = n elementi, allora la cardinalit`a dell’insieme delle parti `e:
|P(A)| = 2n
4. Gli Assiomi di Peano e il Principio di Induzione Matematica
Assiomi di Peano per i Numeri Naturali N (§ 1.3)
I numeri naturali N = {0, 1, 2, 3, . . . } sono definiti formalmente dagli Assiomi di Peano tramite la funzione succes-
sore s(n) = n + 1. Il quinto assioma `e il Principio di Induzione:
Sia S ⊆N un sottoinsieme di numeri naturali. Se valgono le seguenti due condizioni:
i) Base dell’induzione: 0 ∈S
ii) Passo induttivo: ∀n ∈N, se n ∈S =⇒(n + 1) ∈S
allora S = N (l’insieme contiene tutti i numeri naturali).
Struttura di una Dimostrazione per Induzione di una propriet`a P(n):
1. Base dell’induzione: Si verifica che P(0) (oppure P(1)) sia vera.
2. Ipotesi induttiva: Si assume che P(n) sia vera per un generico n ≥0.
3. Tesi induttiva: Si dimostra che, sotto l’ipotesi P(n), ne segue necessariamente che P(n + 1) `e vera.
Pagina 3

<!-- pagina 4 -->
Matematica Discreta — Universit`a degli Studi di Torino (Informatica, Canale B)
Lezione 2: 02/10/2026
Dimostrazione per Induzione del Teorema |P(A)| = 2n
Dimostriamo per induzione su n = |A| la propriet`a P(n) : |P(A)| = 2n.
 Base dell’induzione (n = 0): Se |A| = 0, allora A = ∅.
Abbiamo P(∅) = {∅}, la cui cardinalit`a `e
|P(∅)| = 1 = 20. Dunque P(0) `e vera.
 Passo Induttivo (P(n) =⇒P(n + 1)): Assumiamo vera la tesi per ogni insieme di cardinalit`a n (Ipotesi
Induttiva: un insieme di n elementi ha 2n sottoinsiemi).
Sia ora A un insieme con |A| = n + 1. Isoliamo un elemento fissato an+1 ∈A e poniamo A′ = A \ {an+1}.
Chiaramente |A′| = n.
Possiamo dividere i sottoinsiemi S ∈P(A) in due famiglie disgiunte:
a) Sottoinsiemi che non contengono an+1: Sono esattamente i sottoinsiemi di A′, ossia P(A′). Per ipotesi
induttiva, questi sono esattamente 2n.
b) Sottoinsiemi che contengono an+1: Ciascuno di questi sottoinsiemi `e della forma T ∪{an+1} con T ∈
P(A′). Essendo in corrispondenza biunivoca con P(A′), sono anch’essi esattamente 2n.
Poich´e le due famiglie sono disgiunte, la cardinalit`a totale `e:
|P(A)| = 2n + 2n = 2 · 2n = 2n+1
La propriet`a `e dimostrata per ogni n ∈N. ■
5. Ricoprimenti e Partizioni di un Insieme
Definizione: Ricoprimento e Partizione (§ 1.5, Definizioni 1.18 e 1.20)
Sia X un insieme non vuoto e sia F = {Ai}i∈I una famiglia di sottoinsiemi di X (Ai ⊆X).
 Ricoprimento: F `e un ricoprimento di X se l’unione di tutti i suoi membri restituisce l’intero insieme X:
[
i∈I
Ai = X
 Partizione: Un ricoprimento F = {Ai}i∈I si dice Partizione di X se soddisfa due condizioni vincolanti
aggiuntive:
1. Non vuotezza: Nessun blocco `e vuoto, cio`e Ai̸ = ∅
∀i ∈I.
2. Disgiunzione a due a due: Blocchi distinti non si sovrappongono:
Ai ∩Aj = ∅
∀i, j ∈I con i̸ = j
Esempi e Trabocchetti d’Esame sulle Partizioni
 Esempio di Partizione valida su N: La divisione tra Pari e Dispari.
Sia P = {n ∈N | n `e pari} e
D = {n ∈N | n `e dispari}.
→P ∪D = N (`e un ricoprimento)
→P̸ = ∅, D̸ = ∅e P ∩D = ∅(`e una partizione valida!).
 Esempio di NON Partizione: Sia X = {1, 2, 3, 4, 5} e consideriamo A1 = {1, 2, 3} e A2 = {3, 4, 5}.
→A1 ∪A2 = X (`e un ricoprimento di X), MA A1 ∩A2 = {3}̸ = ∅. Non `e una partizione perch´e i blocchi
si sovrappongono nel punto 3.
Pagina 4
