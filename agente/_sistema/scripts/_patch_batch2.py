from pathlib import Path

B = Path(__file__).resolve().parent.parent / "bozze"


def leggi(f):
    return (B / f).read_text(encoding="utf-8")


def scrivi(f, t):
    (B / f).write_text(t, encoding="utf-8")


def sub(t, a, b):
    assert a in t, a[:70]
    return t.replace(a, b, 1)


# ---------------- lab_cap11
f = "lab_cap11.md"
t = leggi(f)
t = sub(t, "(la domanda è quale ciclo sia più appropriato: un `for`, perché il numero di iterazioni è noto)", "(la domanda posta è quale ciclo sia più appropriato; considerazione nostra: un `for`, perché il numero di iterazioni è noto)")
t = sub(t, "- `for (int i = 20; i >= 2; i -= 7)`: i parte da 20 e scende di 7 alla volta (20, 13, 6);", "- `for (int i = 20; i >= 2; i -= 7)`: i parte da 20 e scende di 7 alla volta: assume i valori 20, 13 e 6 (la slide dice «da 20 a 2 inclusi», ma il 2 non viene mai raggiunto: l'ultimo valore è 6);")
t = sub(t, "ed è quindi necessario per scendere fino a 0 incluso (cap. 24).", "ed è quindi necessario, con la condizione `i >= 0`, per scendere fino a 0 incluso (cap. 24; il tipo è definito in `<stddef.h>`).")
t = sub(t, "Secondo modo, più efficiente: si scorrono direttamente solo i numeri pari, con passo 2:", "Secondo modo: si scorrono direttamente solo i numeri pari, con passo 2 (considerazione nostra: così le iterazioni sono 50 invece di 101):")
t = sub(t, "Attenzione alla divisione fra interi (cap. 16): per ottenere una media in virgola mobile bisogna convertire uno dei due operandi.", "Come aggiunta nostra: attenzione alla divisione fra interi (cap. 16): per ottenere una media in virgola mobile bisogna convertire uno dei due operandi.")
t = sub(t, "Nel ciclo si usa inoltre la valutazione **cortocircuitata** (~lazy~) dell'`&&` (cap. 18): se `scanf` non ha letto nulla, la seconda condizione non viene nemmeno valutata.", "Nel ciclo si usa inoltre la valutazione **cortocircuitata** (~lazy~) dell'`&&` (cap. 18): se `scanf` non ha letto nulla, la seconda condizione non viene nemmeno valutata.\n\n(In parole povere: «cortocircuitata» vuol dire che il C si ferma appena il risultato è deciso, senza guardare il resto della condizione.)")
t = sub(t, "Servono due variabili di supporto: un **accumulatore** che somma i numeri letti e un **contatore** di quanti numeri sono stati letti; alla fine del ciclo", "Servono due variabili di supporto: un **accumulatore** che somma i numeri letti e un **contatore** di quanti numeri sono stati letti (in parole povere: l'accumulatore è il «totale parziale» e il contatore è il «conto dei numeri»); alla fine del ciclo")
t = sub(t, "Il capitolo successivo prosegue con quantificatori sulle sequenze, il triangolo di Floyd, i pattern, Fibonacci e il gioco dell'indovina il numero.", "Il capitolo successivo prosegue con i divisori, il triangolo di Floyd, i pattern, i quantificatori sulle sequenze, Fibonacci e il gioco dell'indovina il numero.")
scrivi(f, t)

# ---------------- lab_cap12
f = "lab_cap12.md"
t = leggi(f)
t = sub(t, "# Capitolo 12: Laboratorio 4: Quantificatori sulle Sequenze, Pattern, Fibonacci e Ricerca per Dimezzamenti", "# Capitolo 12: Laboratorio 4: Divisori, Pattern, Quantificatori sulle Sequenze, Fibonacci e Ricerca per Dimezzamenti")
t = sub(t, "La domanda di fondo è, come sempre, quale ciclo sia più adatto al problema: qui il numero di candidati da controllare è noto in anticipo, quindi un `for`.", "La domanda posta è quale ciclo sia più adatto al problema (la scelta tipica quando i candidati da controllare sono noti in anticipo è un `for`: considerazione nostra, perché il testo dell'esercizio sta su Moodle).")
t = sub(t, "I numeri di Floyd non c'entrano nulla con la logica di Floyd (nota delle slide).", "I numeri di Floyd non c'entrano nulla con la logica di Floyd (precisazione del docente).")
t = sub(t, "Suggerimento delle slide: **due cicli annidati**,", "Suggerimento: **due cicli annidati**,")
t = sub(t, "È una quantificazione universale (cap. 21).", "È una quantificazione universale (Fondamenti, cap. 21).")
t = sub(t, "(cap. 22). Si usa una variabile `esiste`, inizialmente falsa:", "(Fondamenti, cap. 22). Si usa una variabile `esiste`, inizialmente falsa:")
t = sub(t, "```c\nbool tutti = true;", "Nei frammenti seguenti `n` è un intero già dichiarato e «Cond» è uno **pseudocodice** per una condizione qualunque.\n\n```c\nbool tutti = true;")
t = sub(t, "La domanda delle slide è se per questo aggiornamento serva una variabile temporanea: sì, perché assegnando una variabile si perde il valore vecchio, che serve ancora per calcolare l'altra (come nello scambio di variabili, cap. 13).",
        "La domanda posta è se per questo aggiornamento serva una variabile temporanea. Considerazione nostra: scrivendo di seguito `n = m; m = n + m;` si sbaglia, perché la prima assegnazione fa perdere il valore vecchio di n, che serve ancora per calcolare il nuovo m (come nello scambio di variabili, cap. 13); la variabile temporanea risolve il problema (esistono anche trucchi aritmetici senza temporanea).")
t = sub(t, "- tentativo 62 = (51 + 75)/2: il numero da indovinare era 62.", "- tentativo (51 + 75)/2 = 63: il numero è minore di 63, quindi l'intervallo diventa [51, 63), e si continua a dimezzare (57, 60, 61…) fino al tentativo 62. Nelle slide il terzo passo è scritto «62 = (51 + 75)/2», ma il punto di mezzo è 63: è una svista della slide, e conta soprattutto l'idea di dimezzare.")
t = sub(t, "Anche qui la domanda è quale ciclo sia più adatto: il numero di tentativi non è noto in anticipo e dipende dalle risposte, quindi un `while` (o un ciclo che continua finché non si indovina).", "Anche qui la domanda posta è quale ciclo sia più adatto: considerazione nostra, la ricerca prosegue finché non si indovina, quindi un ciclo che si ferma su una condizione (un `while`) è la scelta naturale.")
t = sub(t, "Si chiede un programma", "Si chiede un programma") if "Si chiede un programma" in t else t
t = sub(t, "**Strategia lenta.** Si sa che il numero è compreso tra 0 incluso e 100 escluso, per esempio 62. Si prova 0: «il numero è maggiore di 0», e l'intervallo diventa [1, 100); si prova 1, poi 2, e così via, riducendo l'intervallo di un valore alla volta: molti tentativi.", "**Strategia lenta.** Si sa che il numero è compreso tra 0 incluso e 100 escluso, per esempio 62. Si prova 0: «il numero è maggiore di 0», e l'intervallo diventa [1, 100); si prova 1, poi 2, e così via, riducendo l'intervallo di un valore alla volta.")
scrivi(f, t)

# ---------------- programmazione_cap27
f = "programmazione_cap27.md"
t = leggi(f)
t = sub(t, "Il concetto ha un forte parallelo con quello matematico, ma non coincide completamente con esso.\n", "Il concetto ha un forte parallelo con quello matematico, ma non coincide completamente con esso.\n\n(In parole povere: una funzione C è un pezzo di programma con un nome, che prende dei dati, fa qualcosa e può restituire un risultato.)\n")
t = sub(t, "**applicare** (o valutare) la funzione a un argomento dà f(3) = 9.", "**applicare** (o valutare) la funzione a un argomento dà f(3) = 9.\n\n(In parole povere: una funzione matematica è una regola che a ogni valore di partenza ne associa uno solo di arrivo.)") if "**applicare** (o valutare)" in t else t
t = sub(t, "Stampando gli indirizzi di `main` e di `square` con `printf(\"%p\", …)` si vedono due indirizzi diversi nell'area codice (nell'esempio delle slide 0x0010 e 0x004B).", "Stampando gli indirizzi di `main` e di `square` con `printf(\"%p\", …)` si vedono due indirizzi diversi nell'area codice (nell'esempio 0x0010 e 0x004B). Come nell'esempio, il nome della funzione viene passato direttamente a `%p`; in C rigoroso `%p` richiederebbe un `void *`, ma qui interessa solo l'idea che il nome indichi un indirizzo.")
scrivi(f, t)

# ---------------- programmazione_cap28
f = "programmazione_cap28.md"
t = leggi(f)
t = sub(t, "**4. Funzioni troppo «pesanti».** Una funzione `gestisciTutto(void)` che fa input, calcoli, stampa e scrittura su file è difficile da leggere e da testare: meglio spezzarla in più funzioni semplici, una funzione per ogni compito.", "**4. Funzioni troppo «pesanti».** Una funzione `gestisciTutto(void)` che fa input, calcoli, stampa e scrittura su file è meglio spezzarla in più funzioni semplici: una funzione per ogni compito (e una funzione molto lunga è anche più difficile da leggere e da testare, cap. 29).")
t = sub(t, "**5. Nomi poco chiari.** Con", "**Chiarezza nei nomi.** Con")
t = sub(t, "Il compilatore di solito segnala un ~warning~", "Il compilatore di solito segnala un ~warning~")
scrivi(f, t)

# ---------------- programmazione_cap29
f = "programmazione_cap29.md"
t = leggi(f)
t = sub(t, "Il metodo è noto come **divide et impera** (dal latino «dividi e domina»).", "Il metodo è noto come **divide et impera**.")
t = sub(t, "Qui `esito` è il valore restituito da `scanf`, cioè il numero di valori letti con successo: se non è 1, l'utente non ha inserito un numero.", "Qui `esito` è il valore restituito da `scanf`, cioè il numero di valori letti con successo: se non è 1, l'utente non ha inserito un numero (spiegazione nostra, coerente con il Laboratorio 4). Nota: `M_PI` non fa parte del C standard, ma di molti compilatori; e se l'utente scrive un carattere non numerico, `scanf` lo lascia nel buffer e il ciclo può ripetersi senza fine: è un limite del codice di esempio.")
t = sub(t, "Ci sono due modi di scegliere l'ordine di scomposizione.", "(In parole povere: i benefici sono tutti modi di dire che un programma a pezzi è più facile da capire, da riusare, da cambiare e da controllare.)\n\nCi sono due modi di scegliere l'ordine di scomposizione.")
t = sub(t, "Entrambi si integrano nella pratica.", "Entrambi si integrano nella pratica.\n\n(In parole povere: top-down vuol dire «parto dall'idea generale e scendo ai dettagli»; bottom-up «parto dai mattoncini e li metto insieme».)")
t = sub(t, "Questi principi si riprenderanno, con più esperienza, nel corso di Ingegneria del Software.", "(In parole povere: una funzione dovrebbe essere come un buon attrezzo, che fa una cosa sola e la fa bene, con un nome che dice già cosa fa.)\n\nQuesti principi si riprenderanno, con più esperienza, nel corso di Ingegneria del Software.")
scrivi(f, t)

# ---------------- algebra_cap31
f = "algebra_cap31.md"
t = leggi(f)
t = sub(t, "Come sottolineato a lezione, la definizione non è facile da decifrare e si comprende meglio esaminando i casi piccoli.", "Come osserva anche la dispensa, la definizione non è facile da decifrare e si comprende meglio esaminando i casi piccoli.")
scrivi(f, t)

# ---------------- algebra_cap32
f = "algebra_cap32.md"
t = leggi(f)
t = sub(t, "Come sottolineato a lezione, è una proposizione importante e **bisogna saperla**: in un esame era richiesto il determinante di una matrice triangolare 3 × 3 e uno studente se l'è cavata in una sola riga moltiplicando gli elementi sulla diagonale, mentre quasi tutti gli altri hanno fatto il calcolo per esteso.",
        "Come sottolineato a lezione, è una proposizione importante e **bisogna saperla**: all'esame di settembre si dovevano calcolare gli autovalori di una matrice 3 × 3 (un concetto che si vedrà più avanti), il che richiedeva un determinante, e quel determinante era quello di una matrice triangolare; uno studente l'ha scritto in una riga, moltiplicando gli elementi sulla diagonale, mentre tutti gli altri hanno fatto il calcolo per esteso.")
t = sub(t, "per le matrici «a scalini» il determinante si legge sulla diagonale", "per le matrici triangolari il determinante si legge sulla diagonale")
t = sub(t, "Una matrice è **triangolare superiore** se tutti gli elementi **sotto la diagonale principale sono zero**; gli elementi sulla diagonale e sopra possono essere qualsiasi. Si parla di matrice **triangolare inferiore** quando sono zero tutti quelli sopra la diagonale.",
        "Una matrice è **triangolare superiore** se tutti gli elementi **sotto la diagonale principale sono zero**; gli elementi sulla diagonale e sopra possono essere qualsiasi. Si parla di matrice **triangolare inferiore** quando sono zero tutti quelli sopra la diagonale.\n\n(In parole povere: una matrice triangolare ha tutti zeri da una parte della diagonale, a forma di triangolo.)")
t = sub(t, "Poiché è triangolare (anzi, è diagonale), il suo determinante è il prodotto dei valori sulla diagonale: **det(I_{n}) = 1**.", "Poiché è triangolare (anzi, è diagonale), il suo determinante è il prodotto dei valori sulla diagonale: **det(I_{n}) = 1**.\n\n(In parole povere: la matrice identità è la matrice «neutra» del prodotto, quella che ha tutti 1 sulla diagonale e zeri altrove.)")
t = sub(t, "il termine della permutazione σ per ᵗA corrisponde a quello della permutazione inversa per A, che ha lo stesso segno.", "il termine della permutazione σ per ᵗA corrisponde, riordinando i fattori, a quello della permutazione inversa σ^{-1} per A (osservazione nostra), e σ e σ^{-1} hanno lo stesso segno: se σ è un prodotto di k trasposizioni, σ^{-1} è il prodotto delle stesse trasposizioni in ordine inverso, quindi ne servono ancora k.")
t = sub(t, "Una conseguenza pratica è che **tutto ciò che si dimostra per le righe vale anche per le colonne**: lo si userà nel capitolo successivo per lo sviluppo lungo una colonna.", "Una conseguenza pratica è che **ogni proprietà del determinante dimostrata per le righe vale anche per le colonne**: lo si userà nel capitolo successivo per lo sviluppo lungo una colonna.")
scrivi(f, t)

# ---------------- algebra_cap33
f = "algebra_cap33.md"
t = leggi(f)
t = sub(t, "Come sottolineato a lezione, **con ogni metodo si deve sempre ottenere lo stesso risultato**, −6: è un buon modo per controllare i conti.",
        "**Sviluppo lungo la terza riga** (i = 3, segni + − +): l'elemento −1 è in riga 3, colonna 1 (3 + 1 = 4 pari, segno +) con la sottomatrice ( 2 1 ; 1 2 ); l'elemento 0 non contribuisce; l'elemento 1 è in riga 3, colonna 3 (segno +) con la sottomatrice ( 1 2 ; 2 1 ):\ndet A = (−1) · det( 2 1 ; 1 2 ) + 0 + 1 · det( 1 2 ; 2 1 ) = (−1) · 3 + 1 · (−3) = −3 − 3 = −6.\n\nCome sottolineato a lezione, **con ogni metodo si deve sempre ottenere lo stesso risultato**, −6: è un buon modo per controllare i conti.")
scrivi(f, t)

# ---------------- algebra_cap34
f = "algebra_cap34.md"
t = leggi(f)
t = sub(t, "Come sottolineato a lezione, quando si calcola un determinante bisogna **guardare la matrice** e scegliere bene come procedere, perché, come detto a lezione, tra un terzo e metà degli studenti sceglie lo sviluppo lungo la prima riga senza guardare la matrice:",
        "Come sottolineato a lezione, quando si calcola un determinante bisogna **guardare la matrice** e scegliere bene come procedere, perché tra un terzo e metà degli studenti sceglie lo sviluppo lungo la prima riga senza guardare la matrice:")
t = sub(t, "Come sottolineato a lezione, negli esami di Algebra compaiono sempre matrici triangolari o con righe o colonne piene di zeri: i professori «provano a farlo semplice».", "Come detto a lezione, negli esami compaiono spesso matrici triangolari o con molti zeri: i docenti «provano a farlo semplice».")
t = t.replace("cⁿ", "c^{n}").replace("(−1)ⁿ", "(−1)^{n}")
t = sub(t, "dove C è la matrice con colonne (1, 1, −1, −2), (1, 2, −1, 1), (0, 0, −1, 1) e (1, −1, 2, 1), cioè la matrice di soli interi\nC = ", "dove D è la matrice con colonne (1, 1, −1, −2), (1, 2, −1, 1), (0, 0, −1, 1) e (1, −1, 2, 1), cioè la matrice di soli interi\nD = ")
t = sub(t, "det B = 5i · 4√2 · √2 · det C = 40i · det C,", "det B = 5i · 4√2 · √2 · det D = 40i · det D,")
t = sub(t, "det C = (−1) · det( 1 1 1", "det D = (−1) · det( 1 1 1")
t = sub(t, "Dunque det B = 40i · (−12) = **−480i**.", "Dunque det D = −12 e det B = 40i · (−12) = **−480i**.")
t = sub(t, "Come sottolineato a lezione, si è fatto un esempio apposta «inventato» per mostrare che, scegliendo bene, anche un determinante 4 × 4 con numeri complicati si riduce a pochi conti; e che, volendo più esempi, basta inventarne altri a casa, per esempio con matrici 3 × 3 o 4 × 4.",
        "L'idea di fondo è quella della lezione: scegliendo bene la riga o la colonna e portando fuori i fattori comuni, anche un determinante con numeri complicati si riduce a pochi conti. Per fare più pratica, come suggerito a lezione, si possono inventare a casa altri esempi con matrici 3 × 3 o 4 × 4.\n\nNei capitoli successivi il determinante tornerà per decidere l'invertibilità di una matrice e per calcolare gli autovalori.")
scrivi(f, t)
print("patch ok")
