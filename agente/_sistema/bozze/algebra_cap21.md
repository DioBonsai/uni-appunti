# 21. Sottospazi di Matrici Quadrate
## Matrici quadrate e diagonale principale
Una matrice n × n, cioè con lo stesso numero di righe e di colonne, si dice **quadrata**. Lo spazio delle matrici quadrate si indica con M(n, 𝕂), o semplicemente M(n) quando il campo è chiaro. Dentro M(n) vivono tanti sottospazi importanti, che si ottengono imponendo condizioni sulle entrate.

Una matrice quadrata ha due diagonali, ma ce n'è una che conta. Gli elementi a_{11}, a_{22}, …, a_{nn}, cioè quelli con i due indici uguali, formano la **diagonale principale**; l'altra diagonale, detta **diagonale secondaria**, non ha nessuna importanza per quello che si fa in questo corso. Quando si dice «la diagonale» si intende sempre quella principale.

**Definizione.** Una matrice quadrata A = (a_{ij}) di taglia n × n si dice:
- **diagonale** se a_{ij} = 0 per ogni i ≠ j (fuori dalla diagonale principale tutto è zero);
- **triangolare superiore** se a_{ij} = 0 per ogni i > j (tutto ciò che sta sotto la diagonale è zero);
- **triangolare inferiore** se a_{ij} = 0 per ogni i < j (tutto ciò che sta sopra la diagonale è zero);
- **simmetrica** se a_{ij} = a_{ji} per ogni i, j;
- **antisimmetrica** se a_{ij} = −a_{ji} per ogni i, j.

**In parole povere:** immagina di disegnare la diagonale principale, quella che va dall'alto a sinistra al basso a destra.
- **Diagonale**: i numeri possono stare solo sulla diagonale, tutto il resto è zero.
- **Triangolare superiore**: i numeri stanno sulla diagonale e sopra di essa, sotto è tutto zero (un triangolo in alto). **Triangolare inferiore**: il contrario, i numeri stanno sulla diagonale e sotto.
- **Simmetrica**: se «specchi» la matrice rispetto alla diagonale (scambi righe e colonne), non cambia nulla. L'entrata in posizione (1, 2) e quella in posizione (2, 1) sono uguali.
- **Antisimmetrica**: lo specchio cambia il segno di ogni numero: l'entrata in posizione (1, 2) è l'opposto di quella in posizione (2, 1).

![Come sono fatte le matrici diagonali, triangolari, simmetriche e antisimmetriche: in grigio le entrate nulle, in colore quelle libere o legate.](figure/alg/matrici_speciali.png|13.5)

Un chiarimento sulla condizione «a_{ij} = 0 per i > j» delle triangolari: i > j significa che l'indice della riga è più grande di quello della colonna, cioè l'entrata sta **sotto** la diagonale. Per esempio a_{31} (terza riga, prima colonna) sta sotto. L'indice che conta la riga viene sempre per primo. Una matrice triangolare superiore include la diagonale: lì si possono avere numeri diversi da zero, e tutto ciò che sta sotto deve sparire.

## Esempi
Le cinque matrici seguenti sono, nell'ordine, diagonale, triangolare superiore, triangolare inferiore, simmetrica e antisimmetrica (le righe sono separate da punto e virgola):
- ( 2 0 ; 0 −1 ) è diagonale;
- ( 1 √2 ; 0 9 ) ha zero sotto la diagonale: è triangolare superiore;
- ( −1 0 ; 7 2 ) ha zero sopra la diagonale: è triangolare inferiore;
- ( −1 2 ; 2 4 ) ha le entrate in posizione (1, 2) e (2, 1) uguali: è simmetrica;
- ( 0 1 ; −1 0 ) ha le entrate (1, 2) e (2, 1) opposte e zeri sulla diagonale: è antisimmetrica.

In dimensione 3: ( 1 2 3 ; 0 4 5 ; 0 0 6 ) è triangolare superiore, ( 1 0 0 ; 2 4 0 ; 3 5 6 ) è triangolare inferiore, ( 1 0 0 ; 0 2 0 ; 0 0 3 ) è diagonale (si scrive anche diag(1, 2, 3)), ( 1 2 3 ; 2 4 5 ; 3 5 6 ) è simmetrica e ( 0 1 2 ; −1 0 3 ; −2 −3 0 ) è antisimmetrica.

## Una matrice può stare in più classi
Una stessa matrice può appartenere a più classi, e la matrice nulla appartiene a tutte e cinque. Per esempio ( 0 0 ; 0 1 ) è diagonale, triangolare superiore, triangolare inferiore e simmetrica.

**Antisimmetriche e diagonale.** In una matrice antisimmetrica gli elementi della diagonale sono necessariamente nulli. La condizione a_{ij} = −a_{ji} applicata agli indici uguali (i = j) dice a_{ii} = −a_{ii}: un numero che è uguale al proprio opposto può essere solo 0 (in ℝ o in ℂ, e più in generale in ogni campo in cui 1 + 1 ≠ 0: da a = −a segue 2a = 0). Geometricamente, lo specchio rispetto alla diagonale lascia ferme le entrate della diagonale, ma cambia loro il segno, quindi devono essere zero.

**Simmetria e antisimmetria non si escludono.** Nel caso dei numeri reali o complessi la matrice nulla è sia simmetrica sia antisimmetrica, ed è l'unica: se a_{ij} = a_{ji} e a_{ij} = −a_{ji} allora a_{ij} = −a_{ij}, quindi a_{ij} = 0.

Gli insiemi di queste matrici si indicano con D(n) (diagonali), T_{s}(n) (triangolari superiori), T_{i}(n) (triangolari inferiori), S(n) (simmetriche) e A(n) (antisimmetriche).

## Sono tutti sottospazi
**Proposizione.** I sottoinsiemi D(n), T_{s}(n), T_{i}(n), S(n) e A(n) sono tutti sottospazi vettoriali di M(n).

**In parole povere:** se sommi due matrici dello stesso tipo, o ne moltiplichi una per un numero, il risultato resta dello stesso tipo. Due matrici diagonali sommate danno una diagonale; due simmetriche sommate danno una simmetrica; e così via.

Per ciascuno dei cinque insiemi basta verificare le tre condizioni dei sottospazi: la matrice nulla appartiene all'insieme, e somma e prodotto per scalare conservano la proprietà che lo definisce. Per esempio, per le simmetriche:
1. la matrice nulla è simmetrica (tutte le entrate sono 0, quindi a_{ij} = a_{ji});
2. se A e B sono simmetriche, la somma ha entrate a_{ij} + b_{ij} = a_{ji} + b_{ji}, che sono le entrate in posizione (j, i) della somma: A + B è simmetrica (in simboli, scambiare righe e colonne di A + B lascia A + B invariata);
3. se A è simmetrica e λ ∈ 𝕂, la matrice λA ha entrate λ·a_{ij} = λ·a_{ji}: è ancora simmetrica.

Per le antisimmetriche e per le altre classi il ragionamento è analogo. Come sottolineato a lezione, le verifiche sono abbastanza intuitive e non serve scriverle tutte; per chi trova la teoria astratta troppo complicata è però utile rifarle in modo formale, per esempio controllando le antisimmetriche con la vera definizione.

Il capitolo successivo introduce l'altro modo di costruire sottospazi: invece di imporre condizioni si fanno entrare solo i vettori che servono, cioè lo Span.
