# L4_scheda

<!-- pagina 1 -->
Lezione 4: Teoria delle Funzioni e Applicazioni
Matematica Discreta — CdL Informatica Unito
Scheda Dettagliata — Lezione 4: Funzioni e Applicazioni
Corso di Matematica Discreta — Universit`a degli Studi di Torino (Canale B 2026/2027)
Riferimento Testo: A. Mori, Lezioni di Matematica Discreta, Capitolo 2 (pag. 17–38)
1. Definizione Formale di Funzione e Grafico (Mori, §2.1)
Definizione Rigorosa (Tripla Ordinata)
Siano A e B due insiemi non vuoti. Una funzione (o applicazione) f da A in B, indicata con f : A →B, `e una
tripla ordinata
f = (A, B, Γ)
dove A `e detto Dominio, B `e detto Codominio e Γ ⊆A × B `e un sottoinsieme del prodotto cartesiano, detto
Grafico di f, che soddisfa la seguente condizione di esistenza ed unicit`a:
∀a ∈A,
∃!b ∈B
tale che
(a, b) ∈Γ
Se (a, b) ∈Γ, si scrive abitualmente b = f(a), e si dice che b `e l’immagine di a tramite f, oppure che a `e una
controimmagine di b.
Punto d’Attenzione d’Esame: Cosa NON `e una funzione
Sulla lavagna il docente ha mostrato esempi grafici di relazioni che non costituiscono funzioni:
1. Mancanza di Esistenza: Un elemento a ∈A a cui non `e associato alcun b ∈B (retta verticale in a che non
interseca il grafico).
2. Mancanza di Unicit`a: Un elemento a ∈A a cui sono associati pi`u valori b1, b2 ∈B (retta verticale che
interseca il grafico in due o pi`u punti).
2. Funzioni Notabili Fondamentali (Mori, §2.1)
Funzioni Elementari da Conoscere
 Funzione Identit`a: idA : A →A, definita da idA(a) = a per ogni a ∈A. Il suo grafico `e la diagonale
Γ = {(a, a) | a ∈A}.
 Funzione Costante: Fissato un elemento β ∈B, la funzione fβ : A →B `e definita da fβ(a) = β per ogni
a ∈A.
 Proiezioni Cartesiane: Dato il prodotto cartesiano A × B, si definiscono:
p1 : A × B →A,
p1(a, b) = a
e
p2 : A × B →B,
p2(a, b) = b
 Inclusione Canonica: Se S ⊆A, l’applicazione j : S ,→A definita da j(s) = s per ogni s ∈S.
3. Immagini e Controimmagini di Sottoinsiemi (Mori, §2.2)
Sia f : A →B una funzione.
 Immagine Diretta: Dato un sottoinsieme S ⊆A, l’immagine di S tramite f `e l’insieme dei valori assunti in B:
f(S) = {f(s) ∈B | s ∈S} = {b ∈B | ∃s ∈S t.c. f(s) = b} ⊆B
In particolare, f(A) = Im(f) `e detta Immagine della funzione.
 Controimmagine (o Immagine Inversa): Dato un sottoinsieme T ⊆B, la controimmagine di T `e l’insieme di
tutti gli elementi del dominio che vanno a finire in T:
f −1(T) = {a ∈A | f(a) ∈T} ⊆A
1

<!-- pagina 2 -->
Lezione 4: Teoria delle Funzioni e Applicazioni
Matematica Discreta — CdL Informatica Unito
 Fibra di un elemento: Se T = {b} consiste di un solo elemento, si scrive f −1(b) = {a ∈A | f(a) = b}.
Propriet`a Fondamentale degli Insiemi Vuoti
 Se S ⊆A `e non vuoto (S̸ = ∅), allora la sua immagine `e sempre non vuota: f(S)̸ = ∅.
 Al contrario, per T ⊆B non vuoto, la controimmagine f −1(T) pu`o essere vuota (∅) se nessun elemento di
A viene inviato in T.
2

<!-- pagina 3 -->
Lezione 4: Teoria delle Funzioni e Applicazioni
Matematica Discreta — CdL Informatica Unito
4. Classificazione delle Funzioni: Iniettivit`a, Suriettivit`a, Biettivit`a (Mori,
§2.2)
Sia f : A →B una funzione.
1. Funzione Suriettiva (o Epimorfismo)
La funzione f `e suriettiva se ogni elemento del codominio `e immagine di almeno un elemento del dominio:
Im(f) = B ⇐⇒∀b ∈B,
f −1(b)̸ = ∅⇐⇒∀b ∈B, ∃a ∈A t.c. f(a) = b
2. Funzione Iniettiva (o Monomorfismo)
La funzione f `e iniettiva se elementi distinti del dominio hanno immagini distinte nel codominio:
∀a1, a2 ∈A,
a1̸ = a2 =⇒f(a1)̸ = f(a2) ⇐⇒∀a1, a2 ∈A,
f(a1) = f(a2) =⇒a1 = a2
In termini di controimmagini: f `e iniettiva ⇐⇒∀b ∈B,
|f −1(b)| ≤1.
3. Funzione Biettiva (o Isomorfismo / Corrispondenza Biunivoca)
La funzione f `e biettiva se `e sia iniettiva che suriettiva:
∀b ∈B,
∃!a ∈A
tale che
f(a) = b ⇐⇒∀b ∈B,
|f −1(b)| = 1
Esempi Classici d’Esame e Analisi dei Domini/Codomini
1. f : R →R, f(x) = x2:
 Non iniettiva: f(−1) = f(1) = 1 ma −1̸ = 1.
 Non suriettiva: Im(f) = R≥0̸ = R (es. f −1(−4) = ∅).
2. g : R≥0 →R≥0, g(x) = x2: Biettiva (restringendo dominio e codominio diventa sia iniettiva che suriettiva).
3. h : Z →Z, h(n) = 2n + 1:
 Iniettiva: 2n1 + 1 = 2n2 + 1 =⇒2n1 = 2n2 =⇒n1 = n2.
 Non suriettiva: Im(h) = Insieme dei numeri dispari̸ = Z (i numeri pari non hanno controimmagine in
Z).
4. k : R →R, k(x) = x3: Biettiva (ogni numero reale ha un’unica radice cubica reale).
5. Composizione di Funzioni (Mori, §2.3)
Siano f : A →B e g : B →C due funzioni tali che il codominio di f coincida con (o sia contenuto nel) dominio di g.
Definizione di Composizione
La funzione composta g ◦f : A →C `e definita ponendo:
(g ◦f)(a) = g(f(a))
∀a ∈A
 Associativit`a: Se f : A →B, g : B →C, h : C →D, allora h ◦(g ◦f) = (h ◦g) ◦f.
 Elemento Neutro: f ◦idA = f e idB ◦f = f.
 Non Commutativit`a: In generale g ◦f̸ = f ◦g (sposto f ◦g non `e nemmeno definibile).
3

<!-- pagina 4 -->
Lezione 4: Teoria delle Funzioni e Applicazioni
Matematica Discreta — CdL Informatica Unito
6. Invertibilit`a e Funzione Inversa (Mori, §2.4)
Teorema Fondamentale dell’Invertibilit`a
Una funzione f : A →B si dice invertibile se esiste una funzione g : B →A tale che:
g ◦f = idA
e
f ◦g = idB
Teorema: Una funzione f : A →B `e invertibile se e solo se `e biettiva.
Se f `e biettiva, la funzione inversa g `e unica, si indica con f −1 : B →A ed `e definita da:
f −1(b) = a ⇐⇒f(a) = b
4
