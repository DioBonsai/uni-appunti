# 21. Il Principio di Inclusione-Esclusione
## Contare gli elementi di un'unione
Il problema è questo: due insiemi finiti A e B, di cui si conosce il numero di elementi, e si vuole contare gli elementi della loro unione. Il primo tentativo è contare separatamente gli elementi di A e quelli di B e sommarli, |A ∪ B| = |A| + |B|, ma questa uguaglianza è in generale falsa. Per capire dove sbaglia basta guardare il **contributo** di ciascun elemento ai due membri.

Un elemento a che sta solo in A contribuisce 1 a |A ∪ B| e 1 a |A| + |B| (1 da |A| e 0 da |B|). Lo stesso vale per un elemento b che sta solo in B. Un elemento x che sta in entrambi gli insiemi contribuisce 1 a |A ∪ B| perché appartiene all'unione, ma 2 a |A| + |B|, perché viene contato in A e di nuovo in B. L'errore sta tutto negli elementi comuni, contati due volte, e si corregge sottraendo una volta l'intersezione.

![Il contributo di ogni elemento a |A ∪ B| e a |A| + |B|: gli elementi comuni sono contati due volte.](figure/mate/ch21_contributi_due.png|11.5)

**Proposizione (principio di inclusione-esclusione per due insiemi).** Se A e B sono insiemi finiti, allora

|A ∪ B| = |A| + |B| − |A ∩ B|,

o, in forma equivalente, |A ∪ B| + |A ∩ B| = |A| + |B|.

La seconda forma mostra bene che la formula lega quattro quantità: note tre qualunque di esse, si ricava la quarta. Se A e B sono disgiunti, cioè A ∩ B = ∅, la formula si riduce a |A ∪ B| = |A| + |B|.

## Esempi con due insiemi
Alla fine di una sessione d'esame, 152 matricole hanno superato matematica, 144 hanno superato fisica e 89 hanno superato entrambi gli esami. Se M e F sono gli insiemi di chi ha superato matematica e di chi ha superato fisica, gli studenti che hanno superato almeno un esame sono |M ∪ F| = 152 + 144 − 89 = 207.

Quanti sono i numeri naturali tra 1 e 3000 che non sono divisibili né per 3 né per 5? Sia I₃₀₀₀ = {1, 2, …, 3000} e siano D₃ e D₅ i sottoinsiemi dei numeri divisibili per 3 e per 5. Il problema chiede |I₃₀₀₀| − |D₃ ∪ D₅|, cioè quanti elementi restano togliendo l'unione. Si ha |D₃| = 3000/3 = 1000 e |D₅| = 3000/5 = 600, perché tra ogni k numeri consecutivi ce n'è uno divisibile per k (e qui k divide 3000, quindi il conteggio è esatto). Un numero è divisibile per 3 e per 5 se e solo se è divisibile per 15, quindi D₃ ∩ D₅ = D₁₅ e |D₁₅| = 3000/15 = 200. Allora |D₃ ∪ D₅| = 1000 + 600 − 200 = 1400 e la risposta è 3000 − 1400 = 1600.

![I numeri da 1 a 3000: i divisibili per 3 e per 5 si sovrappongono nei multipli di 15.](figure/mate/ch21_numeri_3000.png|9)

## Il caso di tre insiemi
Con tre insiemi A, B e C, sommando |A| + |B| + |C| gli elementi comuni a due insiemi sono contati due volte e quelli comuni a tutti e tre tre volte. La formula si ottiene correggendo a passi.

**Proposizione (inclusione-esclusione per tre insiemi).**

|A ∪ B ∪ C| = |A| + |B| + |C| − |A ∩ B| − |A ∩ C| − |B ∩ C| + |A ∩ B ∩ C|.

**Dimostrazione.**
1. Si sommano le cardinalità dei tre insiemi, |A| + |B| + |C|.
2. Un elemento comune a due insiemi (per esempio in A ∩ B) è contato due volte, quindi si sottraggono le tre intersezioni a due a due.
3. Un elemento comune a tutti e tre, invece, è contato 3 volte nel primo passo e viene tolto 3 volte nel secondo, perché sta in A ∩ B, in A ∩ C e in B ∩ C: alla fine non è contato per niente. Bisogna quindi aggiungere |A ∩ B ∩ C|, e allora torna a essere contato una volta.

![Un elemento del centro del diagramma ha contributo 3 − 3 + 1 = 1 (tabella dei contributi).](figure/mate/ch21_venn3.png|12.5)

Un'altra dimostrazione applica due volte il caso di due insiemi, a (A ∪ B) ∪ C e poi ai singoli addendi.

## Esempi con tre insiemi
Un cinema proietta la trilogia di *Matrix* e con un unico biglietto si può vedere un qualunque numero dei tre film. Alla fine della giornata sono stati venduti 129 biglietti. Il primo film ha avuto 109 spettatori, il secondo 76 e il terzo 55; 52 persone hanno visto i primi due film, 44 gli ultimi due e 28 spettatori erano presenti sia al primo sia all'ultimo. Quante persone hanno visto tutti e tre i film? Con S_{i} l'insieme degli spettatori del film i, la formula dà 129 = 109 + 76 + 55 − 52 − 44 − 28 + |S₁ ∩ S₂ ∩ S₃|, da cui |S₁ ∩ S₂ ∩ S₃| = 13.

Quanti numeri da 1 a 660 sono divisibili per almeno uno tra 5, 6 e 11? Con D₅, D₆ e D₁₁ i tre insiemi, si ha |D₅| = 660/5 = 132, |D₆| = 660/6 = 110 e |D₁₁| = 660/11 = 60. Un numero divisibile per 5 e per 6 lo è per 30, perché 5 e 6 non hanno divisori comuni, quindi |D₅ ∩ D₆| = 660/30 = 22; analogamente |D₅ ∩ D₁₁| = 660/55 = 12 e |D₆ ∩ D₁₁| = 660/66 = 10. L'intersezione dei tre è D₃₃₀ e ha 660/330 = 2 elementi. Quindi

|D₅ ∪ D₆ ∪ D₁₁| = 132 + 110 + 60 − 22 − 12 − 10 + 2 = 260.

## Più di tre insiemi
La stessa idea funziona con quattro, cinque o più insiemi: si sommano le cardinalità, si tolgono le intersezioni a due a due, si aggiungono quelle a tre a tre, e così via alternando i segni. Il principio resta valido, ma il numero di termini cresce in fretta (con 4 insiemi sono 15, con 5 sono 31) e la formula perde praticità. Esistono semplificazioni in casi particolari, per esempio quando gli insiemi sono a due a due disgiunti: in quel caso |A₁ ∪ … ∪ A_{n}| = |A₁| + … + |A_{n}|, perché non ci sono ripetizioni da correggere.
