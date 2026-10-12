# Banca di domande Matematica Discreta (capitoli 1-19 del Riassunto)

Nota: domande originali (non d'esame) nello stile dei quiz UniTo, basate solo sugli argomenti già trattati. Ogni calcolo è verificato per forza bruta con script.

## [mat-001] argomenti: insiemi
Quale delle seguenti uguaglianze tra insiemi è vera?
1. {1, 2} = {(1, 2)}
2. {1, 2, 3} = {1, 2}
3. {∅} = ∅
4. {1, 2, 2, 3} = {3, 2, 1}
5. {1, {2}} = {1, 2}
RISPOSTA: 4
SPIEGAZIONE: Un insieme non ammette ripetizioni e l'ordine non conta, quindi {1, 2, 2, 3} = {1, 2, 3} = {3, 2, 1}. Nelle altre l'oggetto (1,2) è una coppia, {∅} ha un elemento mentre ∅ ne ha zero, {2} è diverso da 2.

## [mat-002] argomenti: insiemi
Sia X = {1, {1, 2}, {2, 3, 4}, ∅}. Allora |X| vale
1. 7
2. 4
3. 6
4. 3
5. 5
RISPOSTA: 2
SPIEGAZIONE: Gli elementi di X sono 1, {1,2}, {2,3,4} e ∅: sono quattro oggetti distinti; ciò che sta dentro gli insiemi-elemento non si conta.

## [mat-003] argomenti: insiemi
Sia B = {n ∈ ℕ | n² < 30 ∧ n è dispari}. Allora B è uguale a
1. {1, 3, 5, 7}
2. {0, 1, 3, 5}
3. {1, 3, 5}
4. {1, 3}
5. {1, 2, 3, 4, 5}
RISPOSTA: 3
SPIEGAZIONE: Si cercano i naturali con n² < 30, cioè 0,…,5, e tra questi solo i dispari: 1, 3, 5 (5² = 25 < 30, 7² = 49 > 30).

## [mat-004] argomenti: insiemi
Quale delle seguenti collezioni è un insieme matematico ben definito?
1. i numeri naturali interessanti
2. i numeri naturali minori di 10
3. gli attori bravi
4. le canzoni più belle degli anni '80
5. i numeri molto grandi
RISPOSTA: 2
SPIEGAZIONE: Serve il criterio di oggettività: l'appartenenza deve essere decisa da una proprietà verificabile e priva di ambiguità. «Interessante», «bravo», «bello», «molto grande» sono giudizi soggettivi.

## [mat-005] argomenti: appartenenza-inclusione
Sia A = {1, {2}, {1, 2}}. Quale delle seguenti affermazioni è vera?
1. {2} ⊆ A
2. {2} ∈ A
3. 2 ∈ A
4. {1} ∈ A
5. {1, 2} ⊆ A
RISPOSTA: 2
SPIEGAZIONE: {2} è uno degli elementi elencati in A, quindi {2} ∈ A. Invece 2 ∉ A, perciò {2} ⊄ A e {1,2} ⊄ A; {1} non compare tra gli elementi.

## [mat-006] argomenti: appartenenza-inclusione
Sia C = {∅, {∅}}. Quale delle seguenti affermazioni è FALSA?
1. ∅ ∈ C
2. ∅ ⊆ C
3. {∅} ∈ C
4. {∅} ⊆ C
5. {{∅}} ∈ C
RISPOSTA: 5
SPIEGAZIONE: Gli elementi di C sono ∅ e {∅}. Quindi ∅ ∈ C e {∅} ∈ C; ∅ ⊆ C vale sempre e {∅} ⊆ C perché ∅ ∈ C. {{∅}} non è un elemento di C, quindi {{∅}} ∈ C è falsa.

## [mat-007] argomenti: appartenenza-inclusione
Siano A = {1, 2} e B = {A, 3}. Quale delle seguenti affermazioni è vera?
1. A ⊆ B
2. A ∈ B
3. 1 ∈ B
4. {1, 2} ⊆ B
5. 3 ⊆ B
RISPOSTA: 2
SPIEGAZIONE: B ha due elementi: l'insieme A e il numero 3. Quindi A ∈ B, ma A ⊆ B richiederebbe 1 ∈ B e 2 ∈ B, che sono falsi. A ∈ B non implica A ⊆ B. Inoltre 3 è un elemento, non un insieme, e non si scrive 3 ⊆ B.

## [mat-008] argomenti: appartenenza-inclusione
Quale delle seguenti affermazioni è vera per OGNI insieme A?
1. ∅ ∈ A
2. A ∈ A
3. ∅ ⊆ A
4. A ⊂ A (inclusione stretta)
5. A ≠ ∅
RISPOSTA: 3
SPIEGAZIONE: L'insieme vuoto è sottoinsieme di ogni insieme (nessun suo elemento può violare la condizione). ∅ ∈ A dipende da A, nessun insieme è sottoinsieme proprio di sé stesso, e A può essere vuoto.

## [mat-009] argomenti: appartenenza-inclusione
Quale delle seguenti affermazioni sugli insiemi numerici è vera?
1. ℚ ⊆ ℤ
2. ℤ ⊆ ℚ
3. √2 ∈ ℚ
4. −3 ∈ ℕ
5. ℝ ⊂ ℚ
RISPOSTA: 2
SPIEGAZIONE: Vale la catena ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ: ogni intero è una frazione (n = n/1). √2 è irrazionale, −3 non è naturale e ℚ è contenuto in ℝ, non viceversa.

## [mat-010] argomenti: operazioni-insiemi
Siano A = {1, 2, 3, 4, 5, 6} e B = {2, 4, 6, 8}. Allora (A ∖ B) ∪ (B ∖ A) è
1. {1, 3, 5, 8}
2. {1, 3, 5}
3. {1, 2, 3, 4, 5, 6, 8}
4. {1, 2, 3, 5, 8}
5. {8}
RISPOSTA: 1
SPIEGAZIONE: A ∖ B = {1, 3, 5} e B ∖ A = {8}; l'unione è {1, 3, 5, 8}. Le altre scelte omettono 8 oppure contengono elementi comuni (2, 4, 6).

## [mat-011] argomenti: operazioni-insiemi
Sia A = {1, 2, 3, 4, 5, 6, 7, 8}, S = {1, 2, 3} e T = {3, 4, 5}. Allora il complementare 𝒞_A(S ∪ T) è
1. {6, 7}
2. {1, 2, 4, 5, 6, 7, 8}
3. {6, 7, 8}
4. {3}
5. {4, 5, 6, 7, 8}
RISPOSTA: 3
SPIEGAZIONE: S ∪ T = {1, 2, 3, 4, 5}, quindi il complementare è {6, 7, 8}, che coincide con 𝒞(S) ∩ 𝒞(T) (De Morgan). L'unione dei complementari è invece il complementare di S ∩ T = {3}.

## [mat-012] argomenti: operazioni-insiemi
Sia A = {1, 2, 2, 3, 3, 3, 4}. Allora |𝒫(A)| vale
1. 16
2. 128
3. 32
4. 8
5. 7
RISPOSTA: 1
SPIEGAZIONE: Gli elementi distinti sono 1, 2, 3, 4, quindi |A| = 4 e |𝒫(A)| = 2⁴ = 16. Le ripetizioni nella scrittura non contano.

## [mat-013] argomenti: operazioni-insiemi
Sia A = {a, b}. Quanti elementi ha 𝒫(𝒫(A))?
1. 16
2. 8
3. 4
4. 32
5. 6
RISPOSTA: 1
SPIEGAZIONE: |𝒫(A)| = 2² = 4, e 𝒫(A) è un insieme di 4 elementi, quindi |𝒫(𝒫(A))| = 2⁴ = 16.

## [mat-014] argomenti: operazioni-insiemi
Quale dei seguenti è un elemento di 𝒫({1, 2, 3})?
1. 1
2. {1, 3}
3. {{1}}
4. {1, 4}
5. {1, 2, 3, 4}
RISPOSTA: 2
SPIEGAZIONE: Gli elementi di 𝒫(A) sono i sottoinsiemi di A. {1,3} ⊆ A; 1 è un elemento di A, non un sottoinsieme; {{1}} contiene l'insieme {1} che non appartiene ad A; {1,4} e {1,2,3,4} contengono 4 ∉ A.

## [mat-015] argomenti: operazioni-insiemi
Per ogni terna di insiemi X, Y, Z vale l'uguaglianza
1. (X ∩ Y) ∪ Z = (X ∪ Z) ∪ (Y ∪ Z)
2. (X ∪ Y) ∩ Z = (X ∪ Z) ∩ (Y ∪ Z)
3. (X ∩ Y) ∪ Z = (X ∩ Z) ∪ (Y ∩ Z)
4. (X ∖ Y) ∖ Z = X ∖ (Y ∖ Z)
5. (X ∩ Y) ∪ Z = (X ∪ Z) ∩ (Y ∪ Z)
RISPOSTA: 5
SPIEGAZIONE: Vale la distributività dell'unione rispetto all'intersezione: (X ∩ Y) ∪ Z = (X ∪ Z) ∩ (Y ∪ Z). Le altre scambiano i ruoli di ∪ e ∩ oppure non valgono: per X = Y = ∅ e Z = {1} la quarta darebbe {1} = ∅, e la differenza non è associativa.

## [mat-016] argomenti: prodotto-cartesiano
Siano A = {1, 2, 2, 3} e B = {a, b}. Quanti elementi ha A × B?
1. 8
2. 5
3. 12
4. 6
5. 9
RISPOSTA: 4
SPIEGAZIONE: Gli elementi di A sono 1, 2, 3 (la ripetizione non conta), quindi |A| = 3 e |A × B| = 3 · 2 = 6.

## [mat-017] argomenti: prodotto-cartesiano
Siano A = {1, 2, 5} e B = {2, 3}. La terna (5, 3, 1) è un elemento di
1. A × A × A
2. B × A × A
3. A × B × B
4. B × B × A
5. A × B × A
RISPOSTA: 5
SPIEGAZIONE: Si controlla componente per componente: 5 ∈ A (ma 5 ∉ B), 3 ∈ B (ma 3 ∉ A), 1 ∈ A (ma 1 ∉ B). La terna sta solo in A × B × A.

## [mat-018] argomenti: prodotto-cartesiano
Siano A = {1, 2, 3} e B = {2, 3, 4}. Quanti elementi ha (A × B) ∩ (B × A)?
1. 2
2. 9
3. 6
4. 0
5. 4
RISPOSTA: 5
SPIEGAZIONE: Una coppia (x, y) sta in entrambi se x ∈ A ∩ B e y ∈ A ∩ B. Poiché A ∩ B = {2, 3}, l'insieme è (A ∩ B) × (A ∩ B) = {(2,2), (2,3), (3,2), (3,3)}, di 4 elementi.

## [mat-019] argomenti: prodotto-cartesiano
Siano A e B insiemi non vuoti. Allora A × B = B × A se e solo se
1. A ⊆ B
2. A ∩ B ≠ ∅
3. A = B
4. |A| = |B|
5. vale sempre
RISPOSTA: 3
SPIEGAZIONE: Le coppie (a, b) con a ∈ A, b ∈ B devono essere anche coppie di B × A: ciò forza a ∈ B e b ∈ A per ogni scelta, quindi A = B. Se A ≠ B esiste una coppia (a,b) il cui scambio (b,a) non sta nel prodotto.

## [mat-020] argomenti: prodotto-cartesiano
Quale delle seguenti affermazioni è vera?
1. (1, 2) = (2, 1) perché hanno gli stessi elementi
2. {1, 2} ≠ {2, 1} perché l'ordine è diverso
3. (1, 1) = {1}
4. Se A = {1} e B = {2}, allora A × B ⊆ A ∪ B
5. (1, 2) ≠ (2, 1), mentre {1, 2} = {2, 1}
RISPOSTA: 5
SPIEGAZIONE: Nelle coppie ordinate la posizione conta: (1,2) ≠ (2,1); negli insiemi l'ordine è irrilevante. Il prodotto cartesiano contiene coppie, non elementi di A ∪ B: A × B = {(1,2)} non è contenuto in {1,2}.

## [mat-021] argomenti: induzione
Sull'insieme X = {0, 1, 2, 3} con elemento iniziale 0 si definisce S(0) = 1, S(1) = 2, S(2) = 3, S(3) = 3. Quale assioma di Peano NON è soddisfatto?
1. l'iniettività del successore (assioma 3)
2. l'esistenza dello zero (assioma 1)
3. l'esistenza del successore (assioma 2)
4. lo zero non è successore di nessuno (assioma 4)
5. l'assioma di induzione (assioma 5)
RISPOSTA: 1
SPIEGAZIONE: S è definita su tutti gli elementi, 0 non è un successore, e partendo da 0 si raggiungono tutti gli elementi (induzione valida). Ma S(2) = S(3) = 3 con 2 ≠ 3: non è iniettiva.

## [mat-022] argomenti: induzione
Usando la formula 1² + 2² + … + n² = n(n+1)(2n+1)/6, la somma 1² + 2² + … + 10² vale
1. 330
2. 55
3. 3025
4. 440
5. 385
RISPOSTA: 5
SPIEGAZIONE: Si sostituisce n = 10: 10 · 11 · 21 / 6 = 2310 / 6 = 385. (3025 è il quadrato della somma 1+…+10, cioè 55².)

## [mat-023] argomenti: induzione
Sia P(n) la proprietà «2n + 1 è pari». Che cosa si può dire?
1. P(n) è vera per ogni n ≥ 0 per il principio di induzione
2. P(0) è vera, quindi la proprietà vale per ogni n
3. il passo induttivo P(n) ⟹ P(n+1) è falso
4. P(n) è vera per n pari e falsa per n dispari
5. P(n) ⟹ P(n+1) vale per ogni n, ma P(n) è falsa per ogni n: manca la base dell'induzione
RISPOSTA: 5
SPIEGAZIONE: Se 2n+1 fosse pari, anche 2n+3 lo sarebbe: l'implicazione P(n) ⟹ P(n+1) regge, ma la base P(0) è falsa (1 è dispari). Senza la base il principio di induzione non permette di concludere nulla.

## [mat-024] argomenti: partizioni
Sia X = {1, 2, 3, 4, 5, 6}. Quale delle seguenti famiglie è una partizione di X?
1. {{1, 2, 3}, {3, 4, 5, 6}}
2. {{1, 2}, {3, 4}}
3. {{1, 2}, {3, 4}, {5, 6}, ∅}
4. {{1, 2}, {3, 4}, {5, 6}}
5. {{1, 2, 3}, {4, 5}, {4, 6}}
RISPOSTA: 4
SPIEGAZIONE: Una partizione è un ricoprimento di blocchi non vuoti e a due a due disgiunti. La seconda ha 3 in comune, la terza non copre 5 e 6, la quarta contiene ∅, la quinta ha 4 in due blocchi.

## [mat-025] argomenti: partizioni
Sia X = {1, 2, 3, 4, 5}, A₁ = {1, 2, 3}, A₂ = {3, 4, 5}. La famiglia {A₁, A₂} è
1. un ricoprimento di X ma non una partizione
2. una partizione di X
3. né un ricoprimento né una partizione di X
4. una partizione ma non un ricoprimento di X
5. l'insieme quoziente di X
RISPOSTA: 1
SPIEGAZIONE: A₁ ∪ A₂ = X, quindi è un ricoprimento; ma A₁ ∩ A₂ = {3} ≠ ∅, quindi i blocchi non sono disgiunti e non è una partizione.

## [mat-026] argomenti: partizioni
Sia Y = {1, 2, 3, 4} e ℱ = {{1, 2}, {3, 4}, ∅}. Perché ℱ NON è una partizione di Y?
1. perché i blocchi {1, 2} e {3, 4} non sono disgiunti
2. perché contiene l'insieme vuoto, e i blocchi devono essere non vuoti
3. perché l'unione dei blocchi non è Y
4. perché i blocchi hanno meno di tre elementi
5. ℱ è una partizione di Y
RISPOSTA: 2
SPIEGAZIONE: L'unione è Y e i blocchi non vuoti sono disgiunti, ma la presenza di ∅ viola la condizione di non vuotezza dei blocchi.

## [mat-027] argomenti: partizioni
Sia P l'insieme dei naturali pari, D quello dei dispari e Q = {P, D} l'insieme quoziente della partizione di ℕ. Quale affermazione è vera?
1. P ⊆ Q
2. Q ⊆ ℕ
3. P ∈ Q
4. |Q| = ∞
5. Q ∈ 𝒫(ℕ)
RISPOSTA: 3
SPIEGAZIONE: Gli elementi di Q sono i blocchi: P ∈ Q (P è un elemento, non un sottoinsieme, di Q). Q contiene 2 oggetti, quindi |Q| = 2; Q ⊆ 𝒫(ℕ), non Q ∈ 𝒫(ℕ), e i suoi elementi sono insiemi di numeri, non numeri.

## [mat-028] argomenti: partizioni
Quale delle seguenti famiglie è una partizione di ℤ?
1. {n ∈ ℤ | n > 0}, {n ∈ ℤ | n < 0}
2. {n ∈ ℤ | n ≥ 0}, {n ∈ ℤ | n ≤ 0}
3. {multipli di 2}, {multipli di 3}
4. {n ∈ ℤ | n ≥ 1}, {n ∈ ℤ | n ≤ 0}
5. {pari}, {dispari}, ∅
RISPOSTA: 4
SPIEGAZIONE: I numeri ≥ 1 e quelli ≤ 0 coprono ℤ senza sovrapporsi. Nella seconda manca 0, nella terza 0 sta in due blocchi, nella quarta 6 è in entrambi e 1 non è in nessuno, nella quinta c'è il blocco vuoto.

## [mat-029] argomenti: relazioni
Sull'insieme {1, 2, 3} sia R = {(1,1), (2,2), (3,3), (1,2), (2,1)}. Allora R è
1. riflessiva e antisimmetrica
2. simmetrica ma non riflessiva
3. riflessiva ma non transitiva
4. antisimmetrica e transitiva
5. una relazione di equivalenza
RISPOSTA: 5
SPIEGAZIONE: R contiene tutte le coppie (x,x) (riflessiva), con (1,2) c'è anche (2,1) (simmetrica) ed è transitiva. Non è antisimmetrica perché 1 R 2 e 2 R 1 con 1 ≠ 2.

## [mat-030] argomenti: relazioni
Quale affermazione sulla relazione di divisibilità è vera?
1. su ℕ non è antisimmetrica
2. è simmetrica
3. su ℤ non è antisimmetrica, perché 1 | −1 e −1 | 1 ma 1 ≠ −1
4. è una relazione di equivalenza su ℕ
5. non è transitiva
RISPOSTA: 3
SPIEGAZIONE: La proprietà dipende dall'insieme: su ℕ a | b e b | a implicano a = b (antisimmetrica), su ℤ no (1 e −1). Non è simmetrica (2 | 4 ma 4 ∤ 2) quindi non è di equivalenza, ed è transitiva.

## [mat-031] argomenti: relazioni
La perpendicolarità tra rette del piano euclideo è una relazione
1. di equivalenza
2. simmetrica, ma né riflessiva né transitiva
3. riflessiva e transitiva
4. simmetrica e transitiva
5. antisimmetrica
RISPOSTA: 2
SPIEGAZIONE: Se r ⊥ s allora s ⊥ r (simmetrica); nessuna retta è perpendicolare a sé stessa (non riflessiva); se r ⊥ s e s ⊥ t allora r ∥ t, quindi r non è perpendicolare a t (non transitiva). Non è antisimmetrica perché r ⊥ s e s ⊥ r con r ≠ s.

## [mat-032] argomenti: relazioni
Sia R la relazione su ℤ definita da m R n ⟺ m < n. Allora R è
1. una relazione di equivalenza
2. transitiva e antisimmetrica, ma non riflessiva
3. riflessiva e antisimmetrica
4. simmetrica e transitiva
5. riflessiva e transitiva
RISPOSTA: 2
SPIEGAZIONE: m < m è falso per ogni m, quindi non è riflessiva; m < n e n < m non si verificano mai, quindi l'antisimmetria vale (a vuoto); m < n e n < k danno m < k, quindi è transitiva; non è simmetrica.

## [mat-033] argomenti: relazioni
Quante sono le relazioni binarie su un insieme S di 3 elementi?
1. 512
2. 9
3. 64
4. 81
5. 8
RISPOSTA: 1
SPIEGAZIONE: Una relazione è un sottoinsieme di S × S, che ha 3 · 3 = 9 elementi; i sottoinsiemi sono |𝒫(S × S)| = 2⁹ = 512.

## [mat-034] argomenti: equivalenze
Quale delle seguenti è una relazione di equivalenza su ℤ?
1. m R n ⟺ m ≤ n
2. m R n ⟺ m divide n
3. m R n ⟺ m − n è dispari
4. m R n ⟺ m e n sono entrambi pari o entrambi dispari
5. m R n ⟺ m · n > 0
RISPOSTA: 4
SPIEGAZIONE: «Avere la stessa parità» è riflessiva, simmetrica e transitiva. ≤ non è simmetrica; la divisibilità non è simmetrica; «differenza dispari» non è riflessiva (m − m = 0); m·n > 0 non è riflessiva per m = 0.

## [mat-035] argomenti: equivalenze
Su {1, 2, 3, 4, 5} sia x R y ⟺ |x − y| ≤ 1. Allora R è
1. una relazione di equivalenza
2. riflessiva e transitiva, ma non simmetrica
3. riflessiva e simmetrica, ma non transitiva
4. simmetrica, ma non riflessiva
5. antisimmetrica
RISPOSTA: 3
SPIEGAZIONE: È riflessiva (|x − x| = 0) e simmetrica, ma 1 R 2 e 2 R 3 senza che 1 R 3: manca la transitività, quindi non è di equivalenza.

## [mat-036] argomenti: equivalenze
Su ℕ si dice che x ∼ y se x e y hanno lo stesso numero di cifre in notazione decimale. La classe [47] è
1. {0, 1, …, 99}
2. {40, 41, …, 49}
3. {10, 11, …, 99}
4. {47}
5. {40, 41, …, 99}
RISPOSTA: 3
SPIEGAZIONE: 47 ha due cifre, quindi [47] contiene i naturali con due cifre: da 10 a 99. Lo 0 e i numeri da 1 a 9 hanno una sola cifra e stanno nella classe [3] = {0, …, 9}.

## [mat-037] argomenti: equivalenze
Sia ∼ una relazione di equivalenza su S e siano x, y ∈ S. Se le classi [x] e [y] hanno almeno un elemento in comune, allora
1. [x] = [y]
2. [x] ⊂ [y] con inclusione stretta
3. x = y
4. [x] ∩ [y] = ∅
5. [x] ∪ [y] = S
RISPOSTA: 1
SPIEGAZIONE: È il teorema fondamentale: due classi sono disgiunte oppure coincidono. Se z ∈ [x] ∩ [y], per simmetria e transitività x ∼ y e quindi [x] = [y]. Non si può concludere x = y: elementi diversi possono stare nella stessa classe.

## [mat-038] argomenti: equivalenze
Sia R la relazione di equivalenza su {1, 2, 3, 4, 5} associata alla partizione {{1, 2}, {3}, {4, 5}} (x R y ⟺ x e y stanno nello stesso blocco). Quante coppie contiene R?
1. 5
2. 7
3. 3
4. 25
5. 9
RISPOSTA: 5
SPIEGAZIONE: Ogni blocco B contribuisce |B|² coppie (anche le coppie (x,x) e le coppie ordinate in entrambi i versi): 2² + 1² + 2² = 4 + 1 + 4 = 9.

## [mat-039] argomenti: funzioni
Siano A = {a, b, c} e B = {1, 2}. Quale dei seguenti sottoinsiemi Γ definisce una funzione f : A → B?
1. Γ = {(a,1), (a,2), (b,1), (c,2)}
2. Γ = {(a,1), (b,2)}
3. Γ = {(1,a), (1,b), (2,c)}
4. Γ = {(a,1), (b,1), (c,2)}
5. Γ = {(a,1), (b,1), (c,1), (a,2)}
RISPOSTA: 4
SPIEGAZIONE: Serve esattamente una coppia (a, b) per ogni a ∈ A. La prima la soddisfa (anche se 1 compare due volte come valore). La seconda e la quinta danno due valori ad a, la terza non assegna nulla a c, la quarta non è un sottoinsieme di A × B.

## [mat-040] argomenti: funzioni
Quale delle seguenti coppie di funzioni sono uguali?
1. f, g : ℝ → ℝ, f(x) = 3x² − 1 e g(x) = x³ + 2x − 1
2. f, g : {0, 1, 2} → ℝ, f(x) = 3x² − 1 e g(x) = x³ + 2x − 1
3. f : {0, 1} → ℝ, f(x) = x², e g : {0, 1} → ℕ, g(x) = x
4. f, g : {0, 1, 2} → ℝ, f(x) = x² e g(x) = 2x
5. f, g : {0, 1, 2, 3} → ℝ, f(x) = 3x² − 1 e g(x) = x³ + 2x − 1
RISPOSTA: 2
SPIEGAZIONE: Due funzioni sono uguali se coincidono dominio, codominio e grafico. Nella prima i valori sono −1, 2, 11 per entrambe. Su ℝ i grafici sono diversi; nella terza il codominio è diverso; nella quarta f(1) = 1 ≠ 2 = g(1); nella quinta f(3) = 26 ≠ 32 = g(3).

## [mat-041] argomenti: funzioni
Siano f, g : ℝ → ℝ con f(x) = 3x² − 1 e g(x) = x³ + 2x − 1. Per quale sottoinsieme S ⊆ ℝ le restrizioni f|S e g|S sono uguali?
1. S = {0, 3}
2. S = {−1, 0, 1}
3. S = {1, 2, 3}
4. S = {1, 2}
5. S = [0, 3]
RISPOSTA: 4
SPIEGAZIONE: f(x) = g(x) significa x³ − 3x² + 2x = 0, cioè x(x−1)(x−2) = 0: i valori coincidono solo per x ∈ {0, 1, 2}. Quindi f|S = g|S esattamente quando S ⊆ {0, 1, 2}: tra le scelte solo {1, 2}.

## [mat-042] argomenti: funzioni
Siano A = {1, 2, 3}, B = {a, b} e p₁ : A × B → A la prima proiezione, p₁(x, y) = x. Allora la controimmagine p₁⁻¹({2}) è
1. {2}
2. {(2, a)}
3. {(1, 2), (2, 2), (3, 2)}
4. {(2, a), (2, b), (3, a)}
5. {(2, a), (2, b)}
RISPOSTA: 5
SPIEGAZIONE: p₁⁻¹({2}) = {(x, y) ∈ A × B | x = 2}: tutte le coppie con prima componente 2, cioè (2,a) e (2,b). È un sottoinsieme del dominio A × B, non di A.

## [mat-043] argomenti: funzioni
Su ℤ si considera la relazione «stessa parità», con classi [pari] e [dispari]. Quale regola definisce una funzione ben definita F : Q → Q, cioè indipendente dal rappresentante?
1. F([x]) = [⌊x/2⌋]
2. F([x]) = [⌊x/3⌋]
3. F([x]) = [⌈x/2⌉]
4. F([x]) = [x + 3]
5. F([x]) = [⌊x/4⌋]
RISPOSTA: 4
SPIEGAZIONE: Se x e y hanno la stessa parità, anche x+3 e y+3 l'hanno. Con le divisioni il risultato cambia classe: 0 ∼ 2 ma ⌊0/2⌋ = 0 (pari) e ⌊2/2⌋ = 1 (dispari); 0 ∼ 4 ma ⌊0/3⌋ = 0 e ⌊4/3⌋ = 1; 0 ∼ 6 ma ⌊0/4⌋ = 0 e ⌊6/4⌋ = 1; 1 ∼ 3 ma ⌈1/2⌉ = 1 e ⌈3/2⌉ = 2.

## [mat-044] argomenti: funzioni
Su ℕ si pone x ∼ y se x e y hanno lo stesso numero di cifre. Per mostrare che F([x]) = [2x] NON è ben definita, quale coppia di rappresentanti si può usare?
1. x = 1 e y = 2
2. x = 12 e y = 15
3. x = 3 e y = 8
4. x = 20 e y = 30
5. x = 100 e y = 200
RISPOSTA: 3
SPIEGAZIONE: 3 e 8 hanno una cifra, quindi [3] = [8], ma 2·3 = 6 ha una cifra e 2·8 = 16 ne ha due: la stessa classe verrebbe mandata in due classi diverse. Con le altre coppie i raddoppi hanno ancora lo stesso numero di cifre e non si vede il problema.

## [mat-045] argomenti: funzioni
Sia f : ℤ → ℤ, f(n) = n² − 3n, e sia S = {−1, 0, 1, 2, 3}. Allora f(S) è
1. {0, 4, -2}
2. {0, 4}
3. {0, 4, 6, -2}
4. {0, 1, 2, 3, -1}
5. {0, 4, -1, -2}
RISPOSTA: 1
SPIEGAZIONE: f(−1) = 4, f(0) = 0, f(1) = −2, f(2) = −2, f(3) = 0. L'immagine è l'insieme dei valori, senza ripetizioni: {−2, 0, 4}. È un sottoinsieme del codominio, non di S.

## [mat-046] argomenti: funzioni
Sia f : ℤ → ℤ, f(n) = n². Allora f⁻¹({0, 1, 4}) è
1. {0, 1, 2}
2. {−2, −1, 0, 1, 2}
3. {0, 1, 4}
4. {−4, −1, 0, 1, 4}
5. {0, 1, 2, 4}
RISPOSTA: 2
SPIEGAZIONE: Si cercano gli interi n con n² ∈ {0, 1, 4}: n = 0, n = ±1, n = ±2. La controimmagine è un sottoinsieme del dominio e contiene entrambi i segni.

## [mat-047] argomenti: funzioni
Sia f : ℝ → ℝ, f(x) = x². Allora la controimmagine f⁻¹([−1, 4]) è
1. [−2, 2]
2. [0, 2]
3. [−1, 2]
4. [−2, −1] ∪ [1, 2]
5. ∅
RISPOSTA: 1
SPIEGAZIONE: x² ∈ [−1, 4] equivale a x² ≤ 4 (la condizione x² ≥ −1 è sempre vera), cioè −2 ≤ x ≤ 2. La parte negativa [−1, 0) del sottoinsieme non viene mai raggiunta e non aggiunge nulla.

## [mat-048] argomenti: funzioni
Sia f : A → B una funzione qualsiasi, S ⊆ A e T ⊆ B. Quale affermazione è sempre vera?
1. se T ≠ ∅ allora f⁻¹(T) ≠ ∅
2. per ogni b ∈ B, f⁻¹(b) ha esattamente un elemento
3. |f(S)| = |S|
4. f⁻¹(T) ⊆ T
5. se S ≠ ∅ allora f(S) ≠ ∅
RISPOSTA: 5
SPIEGAZIONE: L'immagine di un insieme non vuoto non è mai vuota (f assume un valore su ogni elemento). La controimmagine invece può essere vuota anche con T ≠ ∅, una fibra può avere 0 o più elementi, f può far collassare elementi (|f(S)| < |S|), e f⁻¹(T) è un sottoinsieme del dominio, non di T.

## [mat-049] argomenti: iniettiva-suriettiva-inversa
La funzione f : ℤ → ℤ, f(n) = 2n + 1, è
1. suriettiva ma non iniettiva
2. biettiva
3. né iniettiva né suriettiva
4. suriettiva, perché per ogni y ∈ ℤ l'equazione 2x + 1 = y ha soluzione
5. iniettiva ma non suriettiva
RISPOSTA: 5
SPIEGAZIONE: 2n₁ + 1 = 2n₂ + 1 implica n₁ = n₂: iniettiva. L'immagine è l'insieme dei dispari: per esempio 2 = 2x + 1 darebbe x = 1/2 ∉ ℤ, quindi i numeri pari non hanno controimmagine e f non è suriettiva.

## [mat-050] argomenti: iniettiva-suriettiva-inversa
Quale delle seguenti funzioni (con la stessa espressione x²) è biettiva?
1. ℝ → ℝ, x ↦ x²
2. ℝ → [0, +∞), x ↦ x²
3. [0, +∞) → [0, +∞), x ↦ x²
4. [0, +∞) → ℝ, x ↦ x²
5. [−1, 1] → [0, 1], x ↦ x²
RISPOSTA: 3
SPIEGAZIONE: Serve che ogni y del codominio abbia esattamente una controimmagine. Su ℝ → ℝ mancano i negativi e −1, 1 coincidono; ℝ → [0,+∞) è suriettiva ma non iniettiva; [0,+∞) → ℝ è iniettiva ma non suriettiva; su [−1,1] vale f(−1) = f(1). Su [0,+∞) → [0,+∞) vale la radice quadrata come inversa.

## [mat-051] argomenti: iniettiva-suriettiva-inversa
La funzione f : ℝ → ℝ, f(x) = 3x − 6 è biettiva. La sua inversa f⁻¹ : ℝ → ℝ è
1. f⁻¹(y) = (y − 6)/3
2. f⁻¹(y) = 3y + 6
3. f⁻¹(y) = 1/(3y − 6)
4. f⁻¹(y) = (y + 6)/3
5. f⁻¹(y) = y/3 − 6
RISPOSTA: 4
SPIEGAZIONE: Si risolve y = 3x − 6 in x: 3x = y + 6, quindi x = (y + 6)/3. Si verifica che f(f⁻¹(y)) = y. 1/(3y − 6) è il reciproco di f(y), non l'inversa.

## [mat-052] argomenti: iniettiva-suriettiva-inversa
Quale delle seguenti funzioni è biettiva?
1. ℕ → ℕ, n ↦ n + 1
2. ℤ → ℕ, n ↦ |n|
3. ℤ → ℤ, n ↦ 2n
4. ℤ → ℤ, n ↦ n + 1
5. ℤ → ℕ, n ↦ n²
RISPOSTA: 4
SPIEGAZIONE: n ↦ n + 1 su ℤ ha inversa n ↦ n − 1. Su ℕ manca la controimmagine di 0 (solo iniettiva); |n| è suriettiva ma |−1| = |1|; 2n non raggiunge i dispari; n² non è iniettiva e non raggiunge 2.

## [mat-053] argomenti: iniettiva-suriettiva-inversa
Siano a, b interi e f : ℤ → ℤ, f(x) = ax + b. Allora f è biettiva se e solo se
1. a ≠ 0
2. a è dispari
3. a = 1 oppure a = −1
4. a > 0
5. b = 0
RISPOSTA: 3
SPIEGAZIONE: Per a ≠ 0 è sempre iniettiva, ma la suriettività richiede che x = (y − b)/a sia intero per ogni y intero: ciò accade solo se a divide ogni intero, cioè a = ±1 (per a = 2 i valori hanno tutti la parità di b).

## [mat-054] argomenti: iniettiva-suriettiva-inversa
Siano A e B insiemi non vuoti e p₁ : A × B → A, p₁(a, b) = a. Allora p₁ è sempre suriettiva e inoltre
1. è iniettiva se e solo se B ha un solo elemento
2. è sempre iniettiva
3. non è mai iniettiva
4. è iniettiva se e solo se A ha un solo elemento
5. è iniettiva se e solo se A = B
RISPOSTA: 1
SPIEGAZIONE: Due coppie diverse con la stessa prima componente (come (1,2) e (1,5)) hanno la stessa immagine, quindi p₁ non è iniettiva appena B ha almeno due elementi. Se B ha un solo elemento, coppie diverse differiscono nella prima componente e p₁ è iniettiva.

## [mat-055] argomenti: iniettiva-suriettiva-inversa
Quale delle seguenti funzioni è biettiva?
1. sen : ℝ → ℝ
2. sen : ℝ → [−1, 1]
3. sen : [−π/2, π/2] → [−1, 1]
4. sen : [−π/2, π/2] → ℝ
5. sen : [0, π] → [−1, 1]
RISPOSTA: 3
SPIEGAZIONE: Sull'intervallo [−π/2, π/2] il seno cresce da −1 a 1: ogni valore del codominio è assunto una volta sola. Su ℝ → ℝ non raggiunge 2 e non è iniettiva; ℝ → [−1,1] è suriettiva ma non iniettiva; [−π/2,π/2] → ℝ è iniettiva ma non suriettiva; su [0, π] il seno non è suriettivo su [−1,1] (valori ≥ 0).

## [mat-056] argomenti: iniettiva-suriettiva-inversa
Sia f : ℝ → ℝ, f(x) = x². Quale affermazione è corretta?
1. f⁻¹({4}) non esiste perché f non è invertibile
2. f⁻¹({4}) = {2}, perché la radice quadrata è positiva
3. f⁻¹({4}) = {16}
4. f non è invertibile, ma f⁻¹({4}) = {−2, 2} è comunque definita
5. f è invertibile, con inversa x ↦ √x
RISPOSTA: 4
SPIEGAZIONE: La controimmagine f⁻¹(T) esiste per qualunque funzione e non richiede che f sia invertibile: qui è {x ∈ ℝ | x² = 4} = {−2, 2}. L'inversa esiste solo per le funzioni biettive, e f non lo è (non iniettiva né suriettiva).

## [mat-057] argomenti: composizione
Siano f, g : ℝ → ℝ con f(x) = x² − 1 e g(x) = 2x + 3. Allora (g ∘ f)(x) è
1. 4x² + 12x + 8
2. 2x² + 3
3. 2x² − 1
4. 2x² + 1
5. 2x² − 2
RISPOSTA: 4
SPIEGAZIONE: (g ∘ f)(x) = g(f(x)) = 2(x² − 1) + 3 = 2x² + 1. L'espressione 4x² + 12x + 8 = (2x+3)² − 1 è invece (f ∘ g)(x).

## [mat-058] argomenti: composizione
Siano f : {1, 2, 3, 4} → {a, b, c} con f(1) = a, f(2) = b, f(3) = a, f(4) = c e g : {a, b, c} → {x, y} con g(a) = x, g(b) = y, g(c) = x. Allora (g ∘ f)⁻¹({x}) è
1. {1, 3, 4}
2. {1, 3}
3. {a, c}
4. {x}
5. {1, 2, 3, 4}
RISPOSTA: 1
SPIEGAZIONE: g ∘ f manda 1 → x, 2 → y, 3 → x, 4 → x. La controimmagine di {x} è l'insieme degli elementi del dominio {1,2,3,4} che finiscono in x: {1, 3, 4}.

## [mat-059] argomenti: composizione
Siano f : A → B e g : B → C due funzioni tali che g ∘ f è biettiva. Allora
1. f è iniettiva e g è suriettiva
2. f è suriettiva e g è iniettiva
3. f e g sono entrambe biettive
4. f è suriettiva
5. g è iniettiva
RISPOSTA: 1
SPIEGAZIONE: Se g ∘ f è iniettiva lo è f; se g ∘ f è suriettiva lo è g. Non si può dire di più: con f : {0} → {0,1}, f(0) = 0 e g : {0,1} → {0} costante, g ∘ f è biettiva ma f non è suriettiva e g non è iniettiva.

## [mat-060] argomenti: composizione
Siano f(x) = x + 1, g(x) = x² e h(x) = 2x − 3, funzioni da ℝ in ℝ. Il valore di (h ∘ g ∘ f)(3) è
1. 10
2. 29
3. 25
4. 17
5. 16
RISPOSTA: 2
SPIEGAZIONE: Si applica prima f (la più vicina all'argomento), poi g, poi h: f(3) = 4, g(4) = 16, h(16) = 29. Gli altri valori si ottengono applicando le funzioni in un ordine diverso: la composizione non è commutativa.
