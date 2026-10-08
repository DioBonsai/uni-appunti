## Insiemi
D: Quando una collezione di oggetti è un insieme matematico?
R: Quando l'appartenenza è definita da un criterio oggettivo e privo di ambiguità. "Gli attori bravi" non è un insieme (criterio soggettivo).

## Insiemi
D: Quali due regole strutturali valgono per ogni insieme?
R: - Unicità: nessun elemento ripetuto ({a,a,b,c} = {a,b,c}).
- L'ordine degli elementi è irrilevante ({a,b,c} = {b,a,c}).

## Insiemi
D: Differenza tra rappresentazione estensionale e intensionale.
R: Estensionale: elenco degli elementi, A = {a, b, c, 1, 6, 8}. Intensionale: proprietà che li caratterizza, B = {n ∈ ℕ | 1 ≤ n ≤ 10⁹}.

## Appartenenza e inclusione
D: Se A = {1, 2} e B = {A, 3}, sono vere A ∈ B e A ⊆ B? Quanto vale |B|?
R: A ∈ B è vera (A è uno dei due elementi di B). A ⊆ B è falsa perché 1 ∉ B. |B| = 2.

## Sottoinsiemi
D: Come si dimostra che A = B? Quali sono le proprietà base della relazione ⊆?
R: Con la doppia inclusione: A ⊆ B e B ⊆ A. Inoltre A ⊆ A, ∅ ⊆ A per ogni A, e se S ⊆ T allora |S| ≤ |T|.

## Operazioni
D: Definisci intersezione, unione e prodotto cartesiano.
R: - X ∩ Y = {x | x ∈ X e x ∈ Y}
- X ∪ Y = {x | x ∈ X o x ∈ Y}
- A × B = {(a,b) | a ∈ A, b ∈ B}: coppie ordinate, (2,1) ≠ (1,2), e |A × B| = |A|·|B|.

## Complementare
D: Cos'è il complementare di S in A e quali proprietà ha?
R: 𝒞_A(S) = {x ∈ A | x ∉ S} per S ⊆ A. Valgono 𝒞_A(∅) = A, 𝒞_A(A) = ∅, 𝒞_A(𝒞_A(S)) = S, S ∩ 𝒞_A(S) = ∅ e S ∪ 𝒞_A(S) = A.

## De Morgan
D: Enuncia le leggi di De Morgan.
R: Il complementare scambia unione e intersezione:
- 𝒞_A(S ∪ T) = 𝒞_A(S) ∩ 𝒞_A(T)
- 𝒞_A(S ∩ T) = 𝒞_A(S) ∪ 𝒞_A(T)

## Insieme delle parti
D: Cos'è 𝒫(A) e quanti elementi ha se |A| = n? Quanto vale 𝒫(∅)?
R: 𝒫(A) = {S | S ⊆ A}; ha 2ⁿ elementi. 𝒫(∅) = {∅}, che ha 1 elemento (non è vuoto).

## Numeri naturali
D: Enuncia i 5 assiomi di Peano.
R: 1) 0 ∈ ℕ. 2) Ogni n ha un successore S(n). 3) S è iniettiva (m ≠ n ⟹ S(m) ≠ S(n)). 4) 0 non è successore di nessun n. 5) Induzione: se U ⊆ ℕ contiene 0 ed è chiuso per successore, allora U = ℕ.

## Induzione
D: Come si struttura una dimostrazione per induzione?
R: 1) Base: P(0) (o P(1)) è vera. 2) Ipotesi induttiva: P(n) vera. 3) Passo: da P(n) si deduce P(n+1). Poi P(n) vale per ogni n.

## Ricoprimenti e partizioni
D: Qual è la differenza tra ricoprimento e partizione?
R: Ricoprimento: l'unione dei sottoinsiemi è S. Partizione: ricoprimento in cui i blocchi sono non vuoti e a due a due disgiunti (Aᵢ ∩ Aⱼ = ∅ per i ≠ j). Esempio di non partizione: {1,2,3} e {3,4,5} (si sovrappongono in 3).

## Insieme quoziente
D: Che cos'è l'insieme quoziente di una partizione?
R: L'insieme Q = {Aᵢ} i cui elementi sono i blocchi. Poiché ogni Aᵢ ⊆ S, si ha Q ⊆ 𝒫(S). Per pari e dispari in ℕ: Q = {P, D}, |Q| = 2.

## Relazioni
D: Cos'è una relazione binaria su S? Quali sono le 4 proprietà fondamentali?
R: Un sottoinsieme R ⊆ S × S. Proprietà: riflessiva (xRx), simmetrica (xRy ⟹ yRx), antisimmetrica (xRy ∧ yRx ⟹ x = y), transitiva (xRy ∧ yRz ⟹ xRz).

## Relazioni
D: La divisibilità è antisimmetrica? E la relazione ≤ è di equivalenza?
R: La divisibilità è antisimmetrica in ℕ ma non in ℤ (1 | −1 e −1 | 1 con 1 ≠ −1). ≤ non è di equivalenza perché non è simmetrica.

## Equivalenze
D: Cos'è una relazione di equivalenza e cos'è la classe [x]?
R: Relazione riflessiva, simmetrica e transitiva. Classe di x: C_x = [x] = {y ∈ S | xRy}; x è il rappresentante e C_x ≠ ∅ perché xRx.

## Equivalenze
D: Qual è il teorema fondamentale sulle classi di equivalenza?
R: Per ogni x, y: C_x ∩ C_y = ∅ oppure C_x = C_y. Quindi le classi formano una partizione di S (S/R); viceversa ogni partizione definisce un'equivalenza (xRy se stanno nello stesso blocco).

## Funzioni
D: Come si definisce una funzione f: A → B in modo insiemistico?
R: Con un sottoinsieme Γ ⊆ A × B (grafico) tale che ∀a ∈ A esiste un unico b ∈ B con (a,b) ∈ Γ; si scrive f(a) = b.
