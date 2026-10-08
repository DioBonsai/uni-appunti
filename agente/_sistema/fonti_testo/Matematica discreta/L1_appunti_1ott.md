# Matematica discreta, lezione 1 (1 ottobre 2026): appunti a mano
(trascrizione dell'appunto manoscritto, prof. Mori; fonte: L1_appunti_1ott.pdf)

## Teoria degli insiemi. Cos'è un insieme? È una collezione di "oggetti"
È importante che ci sia un **criterio oggettivo** per dire che un certo oggetto appartiene a un dato insieme. Es.: "insieme di attori bravi" → soggettivo, non va bene.

Come li posso scrivere? A = {a, b, c, 1, 6, 8} → non va sempre bene scritta così (es.: tutti i numeri da 1 a 1 miliardo). B = {n ∈ ℕ tale che 1 ≤ n ≤ 10⁹} → meglio.
Possono essere rappresentati anche con i **diagrammi di Venn**: a ∈ A ⟺ ellisse con a, b, c, 1, 6, 8; 4 ∉ A. X ∩ Y ∩ Z: intersezione tra X, Y, Z; X ∩ Y: intersezione tra X, Y.

**Cardinalità** |A| = numero degli elementi dell'insieme A (è possibile che |A| sia infinito). Un insieme non può avere elementi ripetuti: A = {a,b,c}, B = {a,a,b,c} → A = B.
**Insieme vuoto**: ∅ → { }.
**Sottoinsieme**: S ⊆ T = ogni elemento del sottoinsieme è anche elemento dell'insieme: S ⊆ T ⟺ ∀z ∈ S, z ∈ T. (S è sottoinsieme di T)

Riquadri:
- A ⊆ A
- ∅ ⊆ A qualunque sia A
- se S ⊆ T allora |S| ≤ |T|
- A = B ⟺ A ⊆ B e B ⊆ A

⚠ **Attenzione**: A = {1,2}; B = {A, 3} = {{1,2}, 3}; |B| = 2. Un insieme può essere un *elemento* di un altro insieme. Diverso da essere un *sottoinsieme* di esso.

## Operazioni algebriche
Siano X, Y due insiemi:
- **Intersezione** di X, Y: X ∩ Y = { x | x ∈ X **e** x ∈ Y }
- **Unione** di X, Y: X ∪ Y = { x | x ∈ X **o** x ∈ Y }
- **Prodotto cartesiano**: A × B = coppie (a, b) dove a: elemento di A, b: elemento di B. "(2,1)" ≠ "(1,2)".

## Proprietà
- Dimostrazione della proprietà associativa dell'intersezione: x ∈ (X∩Y)∩Z ⟹ (x ∈ X ∧ x ∈ Y) ∧ x ∈ Z ⟹ x ∈ X ∧ (x ∈ Y ∧ x ∈ Z) ⟹ x ∈ X ∩ (Y ∩ Z). Forma sintetica: (X∩Y)∩Z = X∩(Y∩Z); (X∪Y)∪Z = X∪(Y∪Z).
- Proprietà commutativa: X∩Y = Y∩X; X∪Y = Y∪X.
