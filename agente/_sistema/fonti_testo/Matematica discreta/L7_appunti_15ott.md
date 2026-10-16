# L7 – appunti a mano (15 ott 2026), trascritti dall'immagine

**Problema:** |A ∪ B| ?  Disegno di due insiemi con elementi a (solo in A), b (solo in B), x (in entrambi).
Tabella dei contributi alla cardinalità: |A ∪ B| conta 1 per a, 1 per b, 1 per x; |A| + |B| conta 1 per a, 1 per b, **2** per x. L'elemento comune è contato due volte, quindi
|A ∪ B| = |A| + |B| − |A ∩ B|.

**Principio di inclusione-esclusione (per due insiemi):** |A ∪ B| + |A ∩ B| = |A| + |B|.

Esempio I: Matematica 152 superato, Fisica 144 superato, 89 hanno superato entrambi. M = studenti che hanno superato Mate, F = Fisica, |M| = 152, |F| = 144. Quanti hanno superato almeno un esame? x + 89 = 152 + 144 → x = 207.

Esempio II: quanti sono i numeri naturali tra 1 e 3000 che non sono divisibili né per 3 né per 5? I_n = {1,…,n}; D₃, D₅ sottoinsiemi di I₃₀₀₀. Il problema chiede |I₃₀₀₀| − |D₃ ∪ D₅|. |D₃ ∪ D₅| = |D₃| + |D₅| − |D₃ ∩ D₅| = 1000 + 600 − 200 = 1400 (D₃ ∩ D₅ = D₁₅, |D₁₅| = 200). Risposta 3000 − 1400 = 1600.

**I/E per 3 insiemi:** diagramma di Venn con A, B, C e le regioni a (solo A), b (solo B), c (solo C), x (A∩B senza C), y (B∩C senza A), z (A∩C senza B), s (centro, A∩B∩C).
Tabella dei contributi (colonna x,y,z e colonna s):
- |A ∪ B ∪ C|: 1 e 1
- |A| + |B| + |C|: 2 e 3
- − |A∩B| − |A∩C| − |B∩C|: 1 per ciascun elemento di x,y,z; −3 per s
- + |A∩B∩C|: +1 per s → «lo raggiungo»: s torna a 3 − 3 + 1 = 1.
Formula finale: |A ∪ B ∪ C| + |A∩B| + |A∩C| + |B∩C| = |A| + |B| + |C| + |A∩B∩C|.

Es.: 123 biglietti da vendere – trilogia: film 1 visto da 109, film 2 da 76, film 3 da 55 (poi «da completare»).

Es. 2: quanti sono gli n ∈ ℕ tra 1 e 660 divisibili per almeno uno tra 5, 6, 11.

In fondo: |A| = m, |B| = n, |A × B| = m·n.
