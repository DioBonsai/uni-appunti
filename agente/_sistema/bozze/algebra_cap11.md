# 11. Divisione con Resto fra Polinomi
## Come con i numeri interi
I polinomi assomigliano ai numeri interi sotto molti aspetti: si possono sommare, moltiplicare, sottrarre, e si può fare la **divisione con resto**, controllando il resto come si fa con gli interi. Ricordiamo come funziona con i numeri: dividendo 44 per 6 si ottiene quoziente 7 e resto 2, cioè

44 = 6 · 7 + 2.

Il 44 è il **dividendo**, il 6 il **divisore**, 7 il **quoziente** e 2 il **resto**. Il resto deve essere **strettamente minore del divisore**: se alle elementari si scrivesse 44 = 6 · 5 + 14 il maestro direbbe che è sbagliato, perché il 6 sta ancora due volte nel 14, e bisogna prendere sempre il quoziente più grande possibile. Senza questa condizione non c'è un risultato unico (44 = 6·5 + 14 vale quanto 44 = 6·7 + 2).

## Il teorema per i polinomi
Se p(x) è un polinomio (il dividendo) e d(x) un polinomio non nullo (il divisore), esistono due polinomi q(x) (il **quoziente**) e r(x) (il **resto**), e sono **unici**, tali che

p(x) = d(x) · q(x) + r(x), con grado di r(x) < grado di d(x).

Per i polinomi la condizione "il resto è più piccolo del divisore" si traduce in una condizione sul **grado**: il grado del resto deve essere strettamente minore del grado del divisore. È questa condizione che rende il risultato unico.

## Il procedimento
Alle superiori si impara a fare questa divisione con regole come quella di Ruffini, ma basta ricordare la procedura della divisione in colonna tra interi. Per esempio con 734 : 12: in 73 il 12 sta 6 volte (6 · 12 = 72), si sottrae e resta 1; si abbassa il 4 e in 14 il 12 sta 1 volta, resta 2. Quindi 734 = 12 · 61 + 2.

Con i polinomi si fa lo stesso, guardando solo i **monomi di grado massimo**. Esempio: dividiamo p(x) = x⁴ − 2x³ + 2x² + x − 1 per d(x) = x² − 1.
1. Il termine di grado massimo di p è x⁴ e quello del divisore è x²: x⁴ : x² = x². Si moltiplica x² per il divisore, x²(x² − 1) = x⁴ − x², e si sottrae da p: restano −2x³ + 3x² + x − 1.
2. Ora −2x³ : x² = −2x. Si sottrae −2x(x² − 1) = −2x³ + 2x e resta 3x² − x − 1.
3. Poi 3x² : x² = 3. Si sottrae 3(x² − 1) = 3x² − 3 e resta −x + 2.

Il resto −x + 2 ha grado 1, minore del grado di d, quindi la divisione termina. Il quoziente è x² − 2x + 3 e il resto è −x + 2:

x⁴ − 2x³ + 2x² + x − 1 = (x² − 1)(x² − 2x + 3) + (−x + 2).

Si può controllare sviluppando il secondo membro: (x² − 1)(x² − 2x + 3) = x⁴ − 2x³ + 2x² + 2x − 3, e aggiungendo −x + 2 si ritrova il polinomio di partenza.

## Quando un polinomio ne divide un altro
Con i numeri interi si dice che 9 divide 18 perché la divisione ha resto 0, mentre 7 non divide 18 perché il resto è 4. Lo stesso vale per i polinomi: se il resto è **zero**, si dice che d(x) **divide** p(x) e si scrive d(x) | p(x), con la barra verticale come simbolo di "divide". In quel caso p(x) = d(x)q(x) per qualche quoziente q(x).

Esempi: 9 | 18 ma 7 ∤ 18; (x − 1) | (x² − 1), perché x² − 1 = (x − 1)(x + 1) e la divisione non lascia resto; invece (x − 2) non divide x² − 1, perché la divisione lascerebbe un resto non nullo.

Questa nozione di divisibilità è proprio quella che serve nel capitolo successivo, per le radici di un polinomio.
