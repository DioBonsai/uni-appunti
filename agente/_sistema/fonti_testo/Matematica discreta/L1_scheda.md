# L1_scheda

<!-- pagina 1 -->
Scheda di Studio — Lezione 1
Matematica Discreta — UniTO (Canale B)
Lezione 1: Teoria degli Insiemi
Fondamenti, Notazioni, Operazioni e Propriet`a Algebriche
Data lezione: 1 Ottobre 2026
—
UniTO — Corso di Laurea in Informatica (Canale B)
1. Introduzione e Notazione degli Insiemi
Deﬁnizione Formale: Un insieme `e una collezione di oggetti ben deﬁnita, identiﬁcata tramite un criterio
oggettivo di appartenenza.
Criterio di Oggettivit`a (Avvertenza): La propriet`a d’appartenenza dev’essere priva di ambiguit`a.
→Esempio corretto: “L’insieme dei numeri naturali minori di 10” (oggettivo).
→Esempio errato (Soggettivo): “L’insieme degli attori bravi” non `e un insieme matematico valido.
Modalit`a di Rappresentazione:
1. Per Elencazione (Extensionale): Si elencano esplicitamente gli elementi →A = {a, b, c, 1, 6, 8}.
2. Per Propriet`a / Comprensione (Intensionale): Si speciﬁca la condizione logica →B = {n ↑N | 1 ↓n ↓
109}.
Cardinalit`a (|A|): Indica il numero di elementi distinti appartenenti all’insieme A.
Unicit`a degli Elementi: Un insieme non ammette elementi ripetuti. L’ordine e la ripetizione non contano:
Esempio: A = {a, b, c}
e
B = {a, a, b, c} =↔A = B
2. Insieme Vuoto e Relazioni tra Insiemi
Insieme Vuoto: L’unico insieme privo di elementi, indicato con il simbolo ⊋oppure {}.
Relazione di Sottoinsieme (↗): Un insieme S `e sottoinsieme di T (S ↗T) se ogni elemento contenuto in S
appartiene anche a T.
Formulazione Logica: S ↗T ↘↔≃z ↑S, z ↑T
|
Propriet`a Cardinalit`a: S ↗T =↔|S| ↓|T|
Uguaglianza tra Insiemi (Doppia Inclusione): Tecnica fondamentale per dimostrare che due insiemi sono
uguali:
A = B ↘↔A ↗B ⇐B ↗A
TRABOCCHETTO D’ESAME: Elemento (↑) vs Sottoinsieme (↗)
Consideriamo gli insiemi A = {1, 2} e B = {A, 3} = {{1, 2}, 3}:
• A `e un elemento di B, ovvero A ↑B (l’oggetto {1, 2} compare direttamente dentro B).
• A NON `e un sottoinsieme di B, cio`e A ⫅̸ B (gli elementi 1, 2 non appartengono direttamente a B).
• Cardinalit`a di B: |B| = 2 (gli unici due elementi di B sono l’insieme A e il numero 3).
4. Operazioni Insiemistiche e Diagrammi di Venn
Siano X e Y due insiemi nello stesso universo:
Intersezione (⇒): Elementi appartenenti sia a X sia a Y =↔X ⇒Y = {x | x ↑X ⇐x ↑Y }.
Unione (⇑): Elementi appartenenti a X oppure a Y (o a entrambi) =↔X ⇑Y = {x | x ↑X ⇓x ↑Y }.
X
Y
X →Y
Intersezione a 2 Insiemi
X
Y
Z
X →Y →Z
Intersezione a 3 Insiemi
Corso di Laurea in Informatica 2026/2027
Pagina 1 di 2

<!-- pagina 2 -->
Scheda di Studio — Lezione 1
Matematica Discreta — UniTO (Canale B)
5. Propriet`a Algebriche e Dimostrazione
Propriet`a Commutativa: X ⇒Y = Y ⇒X
e
X ⇑Y = Y ⇑X
Propriet`a Associativa: (X ⇒Y ) ⇒Z = X ⇒(Y ⇒Z)
e
(X ⇑Y ) ⇑Z = X ⇑(Y ⇑Z)
DIMOSTRAZIONE RIGOROSA: Propriet`a Associativa dell’Intersezione
Vogliamo dimostrare che (X ⇒Y ) ⇒Z = X ⇒(Y ⇒Z). Sia x un generico elemento:
x ↑(X ⇒Y ) ⇒Z ↘↔[x ↑(X ⇒Y )] ⇐x ↑Z
(Deﬁnizione di ⇒)
↘↔(x ↑X ⇐x ↑Y ) ⇐x ↑Z
(Deﬁnizione di ⇒)
↘↔x ↑X ⇐(x ↑Y ⇐x ↑Z)
(Associativit`a del connettivo logico ⇐)
↘↔x ↑X ⇐[x ↑(Y ⇒Z)]
(Deﬁnizione di ⇒)
↘↔x ↑X ⇒(Y ⇒Z)
(Deﬁnizione di ⇒)
Poich´e tutte le implicazioni sono doppiamente valide ( ↘↔), la propriet`a associativa `e formalmente dimostrata.
6. Prodotto Cartesiano
Deﬁnizione Formale: Il prodotto cartesiano A ⇔B `e l’insieme di tutte le coppie ordinate (a, b) con a ↑A e
b ↑B:
A ⇔B = {(a, b) | a ↑A ⇐b ↑B}
Importanza dell’Ordine delle Coppie: Nelle coppie ordinate l’ordine `e vincolante: se a ↖= b =↔(a, b) ↖= (b, a)
(es. (2, 1) ↖= (1, 2)).
Cardinalit`a del Prodotto Cartesiano: Se A e B sono insiemi ﬁniti: |A ⇔B| = |A| · |B|.
Corso di Laurea in Informatica 2026/2027
Pagina 2 di 2
