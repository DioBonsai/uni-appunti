# L3_scheda

<!-- pagina 1 -->
Lezione 3: Partizioni, Relazioni ed Equivalenze
Matematica Discreta — Universit`a di Torino
Scheda di Studio: Lezione 3 di Matematica Discreta
Partizioni, Insieme Quoziente, Relazioni d’Equivalenza e Classi
Corso di Laurea in Informatica (1° Anno, Canale B) — Prof. Andrea Mori (Rif. Libro: Cap. 1 Par. 1.5 e Appendice A)
1. Ricoprimenti e Partizioni di un Insieme
Definizione: Ricoprimento e Partizione (Cap. 1, Par. 1.5, Def. 1.21)
Sia S un insieme non vuoto.
1. Un ricoprimento di S `e una collezione di sottoinsiemi {Ai}i∈I di S tale che la loro unione riempia tutto S:
[
i∈I
Ai = S
2. Una partizione di S `e una famiglia di sottoinsiemi {Ai}i∈I che soddisfa tre condizioni vincolanti:
(i) S
i∈I Ai = S
(`e un ricoprimento);
(ii) Ai̸ = ∅
∀i ∈I
(nessun blocco `e vuoto);
(iii) Ai ∩Aj = ∅
∀i̸ = j
(i blocchi sono a due a due disgiunti).
Esempi Fondamentali e Trabocchetti d’Esame
 Partizione Corretta di Z: Z = P ∪D, dove P = {2k | k ∈Z} (Pari) e D = {2k + 1 | k ∈Z} (Dispari). I
blocchi non sono vuoti, coprono tutto Z e P ∩D = ∅.
 Ricoprimento che NON `e una partizione: Per N = {0, 1, 2, . . . }, la collezione
{{0, . . . , 10}, {10, . . . , 20}, {20, . . . , 30}, . . . }
ricopre tutto N, ma non `e una partizione perch´e gli insiemi si sovrappongono negli estremi (es.
10 ∈
{0..10} ∩{10..20}̸ = ∅).
2. L’Insieme Quoziente
Definizione: Insieme Quoziente (Cap. 1, Par. 1.5, Def. 1.22)
Data una partizione {Ai}i∈I dell’insieme S, l’insieme che ha come elementi i singoli blocchi della partizione si
chiama Insieme Quoziente associato alla partizione, indicato con:
Q = {Ai | i ∈I}
Osservazione Fondamentale: Poich´e ogni Ai `e un sottoinsieme di S (Ai ⊆S), l’insieme quoziente `e un
sottoinsieme dell’insieme delle parti:
Q ⊆P(S)
3. Relazioni in un Insieme
Definizione: Relazione Binaria (Appendice A, Def. A.1)
Sia S un insieme. Una relazione R su S `e un qualsiasi sottoinsieme del prodotto cartesiano S × S:
R ⊆S × S
Se la coppia ordinata (x, y) ∈R, diciamo che x `e in relazione con y e scriviamo simbolicamente xRy.
1

<!-- pagina 2 -->
Lezione 3: Partizioni, Relazioni ed Equivalenze
Matematica Discreta — Universit`a di Torino
Esempio: La Relazione d’Ordine ≤su Z
Rappresentare la relazione ≤nell’insieme degli interi Z equivale a considerare il sottoinsieme:
R = {(m, n) ∈Z × Z | m ≤n}
Ad esempio: (1, 3) ∈R perch´e 1 ≤3 (vale 1R3), mentre (2, −4) /∈R perch´e 2 ≰−4.
Propriet`a delle Relazioni Binarie
Sia R ⊆S × S una relazione. Essa pu`o soddisfare le seguenti propriet`a:
 Riflessiva: ∀x ∈S,
xRx.
 Simmetrica: ∀x, y ∈S,
xRy =⇒yRx.
 Antisimmetrica: ∀x, y ∈S,
(xRy ∧yRx) =⇒x = y.
 Transitiva: ∀x, y, z ∈S,
(xRy ∧yRz) =⇒xRz.
4. Relazioni di Equivalenza e Classi di Equivalenza
Definizione: Relazione di Equivalenza (Appendice A, Def. A.2)
Una relazione R ⊆S × S si dice relazione di equivalenza se `e contemporaneamente:
Riflessiva,
Simmetrica
e
Transitiva.
Definizione: Classe di Equivalenza
Sia R una relazione di equivalenza su S e sia x ∈S. Si definisce classe di equivalenza di x (indicata con Cx o
[x]) l’insieme di tutti gli elementi di S in relazione con x:
Cx = [x] = {y ∈S | xRy}
L’elemento x si chiama rappresentante della classe Cx.
Propriet`a Immediata delle Classi
Poich´e R `e riflessiva, per ogni x ∈S si ha xRx, quindi x ∈Cx.
Questo garantisce che nessuna classe
di equivalenza `e vuota (Cx̸ = ∅
∀x ∈S).
Inoltre, l’unione di tutte le classi ricopre l’intero insieme:
S
x∈S Cx = S.
5. Il Teorema Fondamentale di Equivalenza e Partizioni
Teorema Fondamentale (Le Classi di Equivalenza formano una Partizione)
Sia R una relazione di equivalenza su S. Per ogni due elementi x, y ∈S, per le relative classi di equivalenza Cx
e Cy sussistono solo due possibilit`a mutuamente esclusive:
Cx ∩Cy = ∅
oppure
Cx = Cy
Di conseguenza, la famiglia delle classi di equivalenza {Cx | x ∈S} costituisce una partizione di S. L’insieme
quoziente viene denotato con S/R.
2

<!-- pagina 3 -->
Lezione 3: Partizioni, Relazioni ed Equivalenze
Matematica Discreta — Universit`a di Torino
Dimostrazione Formale del Teorema
Supponiamo che Cx ∩Cy̸ = ∅. Dobbiamo dimostrare che allora Cx = Cy.
1. Poich´e Cx ∩Cy̸ = ∅, esiste un elemento z ∈Cx ∩Cy.
2. Per definizione di classe: z ∈Cx =⇒xRz, e z ∈Cy =⇒yRz.
3. Per la simmetria di R, da yRz segue zRy.
4. Per la transitivit`a di R, da xRz e zRy deduciamo che xRy.
5. Sia ora un generico w ∈Cy (ovvero yRw). Poich´e xRy e yRw, per transitivit`a si ha xRw, cio`e w ∈Cx. Ci`o
prova che Cy ⊆Cx.
6. Invertendo i ruoli per simmetria si ottiene anche Cx ⊆Cy, da cui l’uguaglianza Cx = Cy.
Il Viceversa: Dalla Partizione alla Relazione di Equivalenza
Data una qualsiasi partizione {Ai}i∈I di S, possiamo definire una relazione R su S ponendo:
xRy ⇐⇒x e y appartengono allo stesso blocco Ai
Esercizio d’Esame: Verificare che R cos`ı definita `e riflessiva (x sta nello stesso blocco di x), simmetrica (se x, y
stanno nello stesso blocco, y, x vi stanno) e transitiva (se x, y e y, z sono nello stesso blocco Ai, allora x, z ∈Ai).
Sintesi Didattica: Esiste una corrispondenza biunivoca perfetta tra le partizioni di un insieme S e le relazioni di equivalenza
su S.
3
