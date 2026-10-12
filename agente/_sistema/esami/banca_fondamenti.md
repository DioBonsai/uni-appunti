# Banca di domande: Fondamenti dell'Informatica (Brookshear cap. 1)

Domande a risposta multipla (5 opzioni, una sola corretta) basate sul Word "Riassunto Fondamenti Informatica" (capitoli 1-11).

## [fnd-001] argomenti: memoria
Una memoria principale ha 4096 celle da 1 byte, con indirizzi consecutivi a partire da 0. L'indirizzo dell'ultima cella, in esadecimale, è:
1. 1000
2. FFFF
3. FFF
4. 0FF
5. 800
RISPOSTA: 3
SPIEGAZIONE: Gli indirizzi vanno da 0 a 4096 - 1 = 4095 = 0xFFF (4095 = 15·256 + 15·16 + 15). 1000 esadecimale vale 4096, cioè il numero di celle, non l'ultimo indirizzo.

## [fnd-002] argomenti: virgola-mobile
Si vuole memorizzare 5 5/8 (101.101 in binario) nel formato a 8 bit con mantissa di 4 bit. Quale valore viene effettivamente registrato?
1. 5 5/8
2. 5 1/2
3. 5
4. 6
5. 5 3/4
RISPOSTA: 2
SPIEGAZIONE: 101.101 = .101101 · 2^3: la mantissa a 4 bit trattiene solo .1011, quindi si perdono gli ultimi due bit (errore di troncamento). .1011 · 2^3 = 101.1 = 5 1/2.

## [fnd-003] argomenti: complemento-eccesso
In complemento a due su 4 bit, la sottrazione 6 - 7 viene eseguita come 0110 + 1001. Il risultato a 4 bit (troncando il riporto) è:
1. 0001
2. 1110
3. 0111
4. 1111
5. 1001
RISPOSTA: 4
SPIEGAZIONE: -7 = 1001. 0110 + 1001 = 01111 su 5 bit; non c'è riporto da scartare e il pattern 1111 vale -1 (6 - 7 = -1). Non c'è overflow perché i due operandi hanno segno opposto.

## [fnd-004] argomenti: memoria
Quale affermazione sulla struttura dei supporti di memorizzazione di massa è corretta?
1. Nell'HDD le tracce sono a spirale e questo favorisce l'accesso casuale
2. Nei nastri magnetici è possibile l'accesso diretto a qualsiasi punto senza scorrere il nastro
3. Nel zoned-bit recording le tracce interne hanno più settori di quelle esterne
4. Nei CD/DVD i dati sono su un'unica traccia a spirale dal centro verso l'esterno; nell'HDD sono su tracce concentriche divise in settori
5. Nei CD i dati sono su tracce concentriche, perciò sono ideali per l'accesso casuale frequente
RISPOSTA: 4
SPIEGAZIONE: Spirale per i dischi ottici (ideali per flussi continui, meno per l'accesso casuale), tracce concentriche per i dischi magnetici. Nello zoned-bit recording sono le tracce esterne, più lunghe, ad avere più settori. I nastri hanno accesso sequenziale.

## [fnd-005] argomenti: errori-hamming
Ai 7 bit di dati 1100101 si aggiunge in coda un bit di parità dispari (il numero totale di 1 deve essere dispari). Quale parola a 8 bit è corretta?
1. 11001010
2. 11001100
3. 11001111
4. 11001011
5. 11001001
RISPOSTA: 4
SPIEGAZIONE: 1100101 contiene quattro 1 (pari), quindi il bit di parità deve essere 1 per portare il totale a cinque (dispari): 11001011. Con bit 0 la parola avrebbe un numero pari di 1, segnalato come errore.

## [fnd-006] argomenti: complemento-eccesso
In complemento a due su 8 bit, il pattern 11100110 rappresenta il valore:
1. 230
2. -102
3. -25
4. -26
5. 26
RISPOSTA: 4
SPIEGAZIONE: Il bit di segno è 1, quindi è negativo. Il suo opposto si ottiene con copia e complementa: 00011010 = 26. Quindi il valore è -26 (230 è la lettura in binario puro, -102 una lettura a modulo e segno).

## [fnd-007] argomenti: circuiti-logica
Quanto vale (1010 AND 0110) OR 0001, con le operazioni booleane applicate bit a bit?
1. 1011
2. 0010
3. 0111
4. 0011
5. 1111
RISPOSTA: 4
SPIEGAZIONE: 1010 AND 0110 = 0010 (1 solo dove entrambi hanno 1); 0010 OR 0001 = 0011 (1 dove almeno uno ha 1).

## [fnd-008] argomenti: virgola-mobile
Nel formato a 8 bit del libro (1 bit di segno, 3 bit di esponente in Excess-4, 4 bit di mantissa con punto radice a sinistra), il pattern 01011100 vale:
1. 24
2. 1,5
3. 3
4. 0,75
5. -1,5
RISPOSTA: 2
SPIEGAZIONE: Segno 0; esponente 101 = 5 in Excess-4 -> 5-4 = 1; mantissa .1100 = 0,75. Valore = 0,75 · 2^1 = 1,5. Leggere l'esponente come binario puro (5) darebbe 0,75·32 = 24.

## [fnd-009] argomenti: codifica-testo
Un CD audio campiona a 44.100 campioni al secondo, con 16 bit per canale per due canali (stereo). Quanti bit al secondo vengono registrati?
1. 1.411.200
2. 705.600
3. 88.200
4. 44.100
5. 2.822.400
RISPOSTA: 1
SPIEGAZIONE: 16 bit · 2 canali = 32 bit per campione; 44.100 · 32 = 1.411.200 bit al secondo (oltre 1 milione, come nel testo). 705.600 sarebbe un solo canale.

## [fnd-010] argomenti: compressione
Un dizionario di controllo ortografico contiene circa 25.000 parole. Quanti bit bastano per identificare una parola con un indice, e quanti ne servono per una parola di 6 lettere in UTF-8 (carattere per carattere)?
1. 25 bit contro 48 bit
2. 15 bit contro 6 bit
3. 48 bit contro 15 bit
4. 15 bit contro 48 bit
5. 12 bit contro 24 bit
RISPOSTA: 4
SPIEGAZIONE: 2^14 = 16.384 < 25.000 <= 2^15 = 32.768, quindi servono 15 bit. In UTF-8 ogni lettera occupa 1 byte: 6 · 8 = 48 bit.

## [fnd-011] argomenti: complemento-eccesso
Perché i calcolatori adottano la notazione in complemento a due per gli interi con segno?
1. Perché rappresenta lo zero con due configurazioni distinte e semplifica i confronti
2. Perché evita sempre l'overflow nelle addizioni tra numeri dello stesso segno
3. Perché la sottrazione A - B si riduce all'addizione A + (-B), per cui basta un solo circuito sommatore con riporto finale ignorato
4. Perché usa meno bit del binario puro per ogni valore positivo
5. Perché il bit di segno è l'unico bit che cambia passando da un numero al suo opposto
RISPOSTA: 3
SPIEGAZIONE: Il vantaggio principale è la semplificazione dei circuiti: una sola operazione (addizione), con il riporto oltre l'ultima colonna semplicemente troncato. Lo zero ha una sola rappresentazione e l'overflow resta possibile.

## [fnd-012] argomenti: complemento-eccesso
In complemento a due su 4 bit (intervallo da -8 a +7), quale di queste somme produce overflow?
1. 3 + 4
2. 6 + (-3)
3. (-8) + 7
4. 2 + 5
5. (-5) + (-4)
RISPOSTA: 5
SPIEGAZIONE: Il risultato esatto -9 esce dall'intervallo: 1011 + 1100 = 10111, troncato 0111 = +7 (somma di due negativi con bit di segno 0 = overflow). Le altre somme hanno risultato in [-8,+7] (3+4 = 7 e 2+5 = 7 sono ancora rappresentabili).

## [fnd-013] argomenti: virgola-mobile
Nel formato a 8 bit con mantissa di 4 bit, si calcola 2 1/2 + 1/8 + 1/8. Quale affermazione è corretta?
1. Con qualsiasi ordine si ottiene 2 3/4, perché l'addizione è sempre associativa
2. Da sinistra a destra si ottiene 2 3/4, mentre sommando prima i due 1/8 si ottiene 2 1/2
3. Da sinistra a destra si ottiene 2 1/2 (ogni 1/8 viene perso nel troncamento), sommando prima 1/8 + 1/8 si ottiene 2 3/4: l'addizione non è associativa
4. Con qualsiasi ordine si ottiene 2 1/2, perché 1/8 è troppo piccolo per essere rappresentato
5. Da sinistra a destra si ha overflow, perché l'esponente non può crescere
RISPOSTA: 3
SPIEGAZIONE: 2 1/2 + 1/8 = 2 5/8 non entra in 4 bit di mantissa e viene troncato a 2 1/2; ripetendo si resta a 2 1/2. Prima 1/8 + 1/8 = 1/4, poi 2 1/2 + 1/4 = 2 3/4. Regola: sommare per primi i numeri più piccoli.

## [fnd-014] argomenti: codifica-testo
Un'immagine bitmap a colori RGB (24 bit per pixel) di 100 × 100 pixel, non compressa, occupa:
1. 30.000 byte
2. 10.000 byte
3. 240.000 byte
4. 80.000 byte
5. 3.000 byte
RISPOSTA: 1
SPIEGAZIONE: Ogni pixel richiede 3 byte (1 per canale R, G, B): 100 · 100 · 3 = 30.000 byte. 240.000 sono i bit, 10.000 sarebbero 1 byte per pixel (scala di grigi).

## [fnd-015] argomenti: compressione
Per quale tipo di dato la compressione lossy NON è accettabile?
1. Un programma eseguibile o un codice sorgente
2. Una fotografia a colori
3. Un brano audio
4. Un filmato video
5. Un'immagine sgranata di anteprima
RISPOSTA: 1
SPIEGAZIONE: Nei file lossless-only (testo puro, sorgenti, eseguibili, dati finanziari) anche la minima alterazione renderebbe il contenuto inutilizzabile; immagini, audio e video tollerano piccole imperfezioni.

## [fnd-016] argomenti: circuiti-logica
Quanto vale 10110 XOR 01101, bit a bit?
1. 11011
2. 11111
3. 00100
4. 01001
5. 10011
RISPOSTA: 1
SPIEGAZIONE: XOR dà 1 solo dove i due bit sono diversi: 1⊕0=1, 0⊕1=1, 1⊕1=0, 1⊕0=1, 0⊕1=1 -> 11011. 11111 sarebbe l'OR, 00100 l'AND.

## [fnd-017] argomenti: compressione
Nella compressione video MPEG, come vengono trattati i fotogrammi intermedi tra gli I-frame?
1. Sono codificati integralmente con JPEG come gli I-frame
2. Vengono scartati e mai ricostruiti
3. Con codifica relativa: si registrano solo le differenze rispetto all'immagine precedente
4. Sono codificati con una palette di 256 colori come nel formato GIF
5. Sono codificati con run-length sull'intero filmato
RISPOSTA: 3
SPIEGAZIONE: Solo gli I-frame sono codificati per intero (tecniche simili a JPEG); gli altri fotogrammi sfruttano la somiglianza con quello precedente registrando solo le differenze (delta).

## [fnd-018] argomenti: memoria
Cosa succede se a un flip-flop si inviano contemporaneamente il comando di scrittura di 1 e quello di scrittura di 0 (ingressi 11)?
1. L'uscita viene forzata a 1, perché il comando di scrittura di 1 prevale
2. L'uscita viene forzata a 0, perché il comando di scrittura di 0 prevale
3. Il flip-flop mantiene il valore memorizzato, come con gli ingressi 00
4. Il flip-flop inverte il valore memorizzato
5. È una condizione non lecita: il flip-flop si comporta in modo instabile o inaffidabile
RISPOSTA: 5
SPIEGAZIONE: Con ingressi 00 il flip-flop preserva il bit; un impulso su uno solo dei due ingressi scrive 1 o 0. L'ingresso 11 non è previsto e porta a un comportamento instabile.

## [fnd-019] argomenti: errori-hamming
Una parola protetta da un singolo bit di parità subisce l'inversione di alcuni bit. In quale caso il controllo NON rileva l'errore?
1. Quando si inverte 1 bit
2. Quando si invertono 3 bit
3. Quando si invertono 5 bit
4. Quando si invertono 7 bit
5. Quando si invertono 2 bit
RISPOSTA: 5
SPIEGAZIONE: La parità cambia a ogni inversione: con un numero dispari di errori il conteggio degli 1 cambia parità e l'errore è rilevato; con un numero pari (2, 4, ...) la parità resta uguale e l'errore sfugge.

## [fnd-020] argomenti: virgola-mobile
Con lo stesso formato a 8 bit (segno, esponente Excess-4 a 3 bit, mantissa a 4 bit), il pattern 11001001 rappresenta:
1. -9
2. -0,5625
3. 0,5625
4. -1,125
5. -0,28125
RISPOSTA: 2
SPIEGAZIONE: Segno 1 (negativo); esponente 100 = 4 -> 4-4 = 0; mantissa .1001 = 9/16 = 0,5625. Valore = -0,5625 · 2^0 = -0,5625.

## [fnd-021] argomenti: complemento-eccesso
In notazione Excess-8 a 4 bit (lo zero è 1000), il pattern 1011 rappresenta il valore:
1. +3
2. +11
3. -3
4. -5
5. +5
RISPOSTA: 1
SPIEGAZIONE: In Excess-8 il valore è il binario puro meno 8: 1011 = 11, quindi 11 - 8 = +3. +11 sarebbe la lettura senza sottrarre l'eccesso.

## [fnd-022] argomenti: memoria
In un disco magnetico il tempo di ricerca (seek time) è 8 ms e la latenza di rotazione è 4 ms. Il tempo di accesso è:
1. 4 ms
2. 8 ms
3. 32 ms
4. 12 ms
5. 6 ms
RISPOSTA: 4
SPIEGAZIONE: Tempo di accesso = tempo di ricerca + latenza di rotazione = 8 + 4 = 12 ms. Non dipende dalla velocità di trasferimento.

## [fnd-023] argomenti: errori-hamming
Qual è la differenza di protezione dagli errori tra CD-DA (audio) e CD-ROM (dati)?
1. Il CD-DA ha più correzione del CD-ROM, perché l'audio non tollera alcun errore
2. Il CD-ROM aggiunge livelli di correzione basati sulla distanza di Hamming, portando l'errore residuo a circa 1 disco difettoso su 20.000 contro circa 1 su 2 del CD-DA
3. Il CD-ROM non usa alcuna correzione, perché i dati sono sempre ricostruibili dal programma
4. Entrambi hanno lo stesso tasso residuo di circa 1 disco difettoso su 20.000
5. Il CD-DA usa un bit di parità per ogni byte, il CD-ROM nessun controllo
RISPOSTA: 2
SPIEGAZIONE: Nell'audio i piccoli difetti vengono mascherati o interpolati, quindi basta la protezione di base; nei dati un solo bit errato può rendere inutilizzabile il programma, perciò il CD-ROM ha ulteriori livelli di correzione.

## [fnd-024] argomenti: memoria
Quanti bit contiene una memoria da 2 KB (con il significato informatico del prefisso Kilo)?
1. 2048
2. 16000
3. 4096
4. 2000
5. 16384
RISPOSTA: 5
SPIEGAZIONE: 1 KB = 2^10 = 1024 byte, quindi 2 KB = 2048 byte; ogni byte ha 8 bit: 2048 · 8 = 16384 bit.

## [fnd-025] argomenti: errori-hamming
Qual è la distanza di Hamming tra 10110101 e 10011100?
1. 2
2. 4
3. 3
4. 5
5. 6
RISPOSTA: 3
SPIEGAZIONE: Confronto bit a bit: le stringhe differiscono nelle posizioni 3, 5, 8 (da sinistra), cioè in 3 posizioni. La distanza di Hamming è il numero di posizioni in cui i bit differiscono.

## [fnd-026] argomenti: codifica-testo
Salvare il numero intero 25 come testo ASCII richiede 2 byte (16 bit): uno per ogni cifra. Qual è la conseguenza rispetto alla notazione binaria con gli stessi 16 bit?
1. Come testo il massimo è 255, in binario con 16 bit si arriva a 65.535
2. Come testo il massimo è 99 (due cifre), in binario con 16 bit si rappresenta ogni intero da 0 a 65.535
3. Come testo il massimo è 65.535, in binario con 16 bit si arriva a 99
4. Non c'è differenza: i due metodi rappresentano gli stessi numeri
5. Come testo si rappresentano solo numeri negativi, in binario solo positivi
RISPOSTA: 2
SPIEGAZIONE: Con due caratteri ASCII si scrivono al massimo i numeri 0-99; con 16 bit in binario si hanno 2^16 = 65.536 combinazioni, cioè da 0 a 65.535. Per questo i numeri si memorizzano in rappresentazioni binarie dedicate.

## [fnd-027] argomenti: codifica-testo
Quale affermazione su ASCII e Unicode/UTF-8 è corretta?
1. L'ASCII originale usa 8 bit e rappresenta già i caratteri di tutti gli alfabeti del mondo
2. L'ASCII originale usa 7 bit (128 simboli); Unicode assegna un codice a ogni simbolo di tutti gli alfabeti (fino a 21 bit) e in UTF-8 i caratteri ASCII occupano ancora 1 byte
3. In UTF-8 ogni carattere occupa sempre 4 byte, compresi quelli ASCII
4. Le estensioni ISO a 8 bit bastano per gestire documenti multilingue con ideogrammi cinesi
5. Unicode usa solo 7 bit per simbolo per restare compatibile con l'ASCII
RISPOSTA: 2
SPIEGAZIONE: 7 bit danno 2^7 = 128 simboli; con 8 bit (256) non si coprono ideogrammi e documenti multilingue. UTF-8 mantiene la compatibilità ASCII con 1 byte per i caratteri classici e usa da 16 a 32 bit per gli altri.

## [fnd-028] argomenti: memoria
Quale affermazione sul confronto tra HDD e SSD è corretta?
1. Gli HDD si usurano perché la testina tocca la superficie del piatto a ogni lettura
2. Gli SSD richiedono alimentazione continua per non perdere i dati memorizzati
3. Gli SSD possono essere riscritti un numero illimitato di volte, a differenza degli HDD
4. Il wear-leveling serve a velocizzare la rotazione dei piatti nei dischi magnetici
5. Gli SSD non hanno parti meccaniche e ogni ciclo di scrittura/cancellazione degrada le celle, perciò si usa il wear-leveling per distribuire le scritture
RISPOSTA: 5
SPIEGAZIONE: Nell'HDD la testina "fluttua" senza toccare il piatto, che si può smagnetizzare e rimagnetizzare illimitatamente. Nelle memorie Flash gli elettroni restano intrappolati anche senza corrente, ma le scritture le degradano; il wear-leveling ridistribuisce i dati sui blocchi.

## [fnd-029] argomenti: complemento-eccesso
Quali valori interi si rappresentano in complemento a due con 6 bit?
1. da -31 a +31
2. da -32 a +32
3. da -32 a +31
4. da -63 a +63
5. da 0 a +63
RISPOSTA: 3
SPIEGAZIONE: Con n bit l'intervallo è asimmetrico: da -2^(n-1) a +2^(n-1) - 1. Con n = 6: da -32 a +31 (lo zero è contato tra i non negativi).

## [fnd-030] argomenti: complemento-eccesso
La rappresentazione di -11 in complemento a due su 8 bit è:
1. 10001011
2. 11110100
3. 00001011
4. 11110110
5. 11110101
RISPOSTA: 5
SPIEGAZIONE: +11 = 00001011. Con copia e complementa (da destra si copia fino al primo 1 compreso, poi si invertono i bit restanti) si ottiene 11110101. 10001011 sarebbe modulo e segno, 11110100 il complemento a uno.

## [fnd-031] argomenti: binario
Il numero binario con punto radice 101.011 vale in decimale:
1. 5,75
2. 5,375
3. 5,3
4. 4,375
5. 5,11
RISPOSTA: 2
SPIEGAZIONE: Parte intera 101 = 4+1 = 5; parte frazionaria .011 = 0·1/2 + 1·1/4 + 1·1/8 = 3/8 = 0,375. Totale 5,375.

## [fnd-032] argomenti: circuiti-logica
Qual è la differenza tra un circuito combinatorio e uno sequenziale?
1. In un circuito combinatorio l'uscita dipende anche dagli ingressi passati, in uno sequenziale solo da quelli attuali
2. Il circuito sequenziale non usa porte logiche, solo il combinatorio le usa
3. Il circuito combinatorio è l'unico in grado di memorizzare un bit
4. In un circuito sequenziale l'uscita dipende anche dallo stato interno accumulato (retroazione), in uno combinatorio solo dagli ingressi presenti
5. Entrambi dipendono solo dagli ingressi correnti, ma il sequenziale è più lento
RISPOSTA: 4
SPIEGAZIONE: Il flip-flop è un circuito sequenziale: grazie ai cicli di retroazione ricorda il bit memorizzato. I circuiti combinatori fanno scorrere il segnale dagli ingressi alle uscite senza memoria; entrambi sono costruiti con porte logiche.

## [fnd-033] argomenti: virgola-mobile
Come si memorizza 2,75 nel formato a 8 bit (segno, esponente Excess-4 a 3 bit, mantissa a 4 bit)?
1. 00101011
2. 01101011
3. 01011011
4. 01101101
5. 11101011
RISPOSTA: 2
SPIEGAZIONE: 2,75 = 10.11 in binario = .1011 · 2^2. Esponente 2 in Excess-4 = 6 = 110, mantissa 1011, segno 0: 0 110 1011.

## [fnd-034] argomenti: binario
Un colore RGB a 24 bit è scritto con 6 cifre esadecimali (2 per canale, nell'ordine rosso, verde, blu). Il colore 00FF00 corrisponde a:
1. rosso alla massima intensità, verde e blu a zero
2. blu alla massima intensità, rosso e verde a zero
3. bianco (tutti i canali al massimo)
4. nero (tutti i canali a zero)
5. verde alla massima intensità, rosso e blu a zero
RISPOSTA: 5
SPIEGAZIONE: Ogni coppia di cifre esadecimale occupa un canale da 8 bit: 00 (rosso) = 0, FF (verde) = 255, 00 (blu) = 0. Il bianco sarebbe FFFFFF, il nero 000000.

## [fnd-035] argomenti: compressione
Nella codifica di Huffman applicata a un testo in inglese, come vengono assegnati i pattern di bit?
1. Lunghezza variabile e inversamente legata alla frequenza: sequenze brevi a lettere frequenti come e, t, a, sequenze lunghe a lettere rare come z, q, x
2. Tutte le lettere hanno lo stesso numero di bit, per semplificare la decodifica
3. Le lettere più frequenti ricevono le sequenze più lunghe
4. Si registrano solo le differenze rispetto al carattere precedente
5. Ogni lettera viene sostituita da un indice in un dizionario di parole
RISPOSTA: 1
SPIEGAZIONE: Huffman è una codifica dipendente dalla frequenza a lunghezza variabile. La registrazione delle differenze è la codifica relativa, il riferimento a una tabella è la codifica a dizionario (LZW).

## [fnd-036] argomenti: binario
Quanto fa 10110 + 01111 in notazione binaria (22 + 15 in decimale)?
1. 100101
2. 100011
3. 011111
4. 110101
5. 100111
RISPOSTA: 1
SPIEGAZIONE: 22 + 15 = 37 = 100101. Colonna per colonna da destra: 0+1=1; 1+1=0 con riporto; 1+1+1=1 con riporto; 0+1+1=0 con riporto; 1+0+1=0 con riporto; il riporto finale dà il bit più a sinistra.

## [fnd-037] argomenti: errori-hamming
Un codice ha distanza di Hamming minima 5 tra ogni coppia di parole legali. Quanti errori può rilevare e quanti correggere?
1. Rilevare fino a 2 bit errati e correggerne 1
2. Rilevare fino a 5 bit errati e correggerne 5
3. Rilevare fino a 4 bit errati e correggerne fino a 2
4. Rilevare fino a 4 bit errati e correggerne 4
5. Rilevare solo 1 bit errato e non correggerne nessuno
RISPOSTA: 3
SPIEGAZIONE: Distanza minima 3: rileva fino a 2 e corregge 1; distanza minima 5: rileva fino a 4 e corregge fino a 2. Il bit di parità da solo rileva soltanto, senza correggere.

## [fnd-038] argomenti: binario
Il pattern 11010110 espresso in notazione esadecimale è:
1. D6
2. E6
3. 6D
4. B6
5. D5
RISPOSTA: 1
SPIEGAZIONE: Si divide in blocchi da 4 bit da destra: 1101 = D (13) e 0110 = 6, quindi D6.

## [fnd-039] argomenti: binario
Convertendo il numero decimale 53 in binario con l'algoritmo delle divisioni successive per 2, si ottiene:
1. 101011
2. 110011
3. 110101
4. 111001
5. 101101
RISPOSTA: 3
SPIEGAZIONE: 53 = 32 + 16 + 4 + 1, cioè 110101. I resti si ottengono nell'ordine 1,0,1,0,1,1 e vanno letti in ordine inverso (dall'ultimo al primo): leggerli nell'ordine di calcolo darebbe 101011.

## [fnd-040] argomenti: circuiti-logica
Quale delle seguenti affermazioni sulle operazioni booleane è corretta?
1. OR restituisce 1 solo quando entrambi gli ingressi valgono 1
2. AND restituisce 1 quando almeno uno degli ingressi vale 1
3. NOT è un'operazione binaria con due ingressi
4. XOR restituisce 1 anche quando entrambi gli ingressi valgono 1
5. XOR restituisce 0 quando i due ingressi sono uguali, anche se entrambi valgono 1
RISPOSTA: 5
SPIEGAZIONE: OR è 1 se almeno un ingresso è 1; AND è 1 solo se entrambi lo sono; NOT è unaria; XOR è 1 solo se gli ingressi sono diversi (1 XOR 1 = 0).
