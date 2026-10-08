# soluzioni_esercizi_parte2_cap1-2-3-10-11-12

<!-- pagina 1 -->
HINTS/SOLUTIONS TO Selected Exercises
Section 1.1 Review
1. A set is a collection of objects.
2. A set may be deﬁned by listing the elements in it. For exam-
ple, {1, 2, 3, 4} is the set consisting of the integers 1, 2, 3, 4.
A set may also be deﬁned by listing a property necessary for
membership. For example,
{x | x is a positive, real number}
deﬁnes the set consisting of the positive, real numbers.
3. Set
Description
Examples of Members
Z
Integers
−3, 2
Q
Rational numbers
−3/4, 2.13074
R
Real numbers
−2.13074,
√
2
Z+
Positive integers
2, 10
Q+
Positive rational numbers
3/4, 2.13074
R+
Positive real numbers
2.13074,
√
2
Z−
Negative integers
−12, −10
Q−
Negative rational numbers
−3/8, −2.13074
R−
Negative real numbers
−2.13074, −
√
2
Znonneg
Nonnegative integers
0, 3
Qnonneg
Nonnegative rational
0, 3.13074
numbers
Rnonneg
Nonnegative real numbers
0,
√
3
4. The cardinality of X (i.e., the number of elements in X)
5. x ∈X
6. x /∈X
7. ∅
8. Sets X and Y are equal if they have the same elements. Set
equality is denoted X = Y.
9. Prove that for every x, if x is in X, then x is in Y, and if x is in
Y, then x is in X.
10. Prove one of the following: (a) There exists x such that x ∈X
and x̸ ∈Y. (b) There exists x such that x̸ ∈X and x ∈Y.
11. X is a subset of Y if every element of X is an element of Y. X
is a subset of Y is denoted X ⊆Y.
12. To prove that X is a subset of Y, let x be an arbitrary element
of X and prove that x is in Y.
13. Find x such that x is in X, but x is not in Y.
14. X is a proper subset of Y if X ⊆Y and X̸ = Y. X is a proper
subset of Y is denoted X ⊂Y.
15. To prove that X is a proper subset of Y, prove that X is a subset
of Y and ﬁnd x in Y such that x is not in X.
16. The power set of X is the collection of all subsets of X. It is
denoted P(X).
17. X union Y is the set of elements that belong to either X or Y or
both. It is denoted X ∪Y.
18. The union of S is the set of elements that belong to at least one
set in S. It is denoted ∪S.
19. X intersect Y is the set of elements that belong to both X and
Y. It is denoted X ∩Y.
20. The intersection of S is the set of elements that belong to every
set in S. It is denoted ∩S.
21. X ∩Y = ∅
22. A collection of sets S is pairwise disjoint if, whenever X and
Y are distinct sets in S, X and Y are disjoint.
23. The diﬀerence of X and Y is the set of elements that are in X
but not in Y. It is denoted X −Y.
24. A universal set is a set that contains all of the sets under dis-
cussion.
25. The complement of X is U −X, where U is a given universal
set. The complement of X is denoted X.
26. A Venn diagram provides a pictorial view of sets. In a Venn
diagram, a rectangle depicts a universal set, and subsets of the
universal set are drawn as circles. The inside of a circle repre-
sents the members of that set.
27.
X
Y
Z
U
5
3
4
2
1
8
7
6
633

<!-- pagina 2 -->
634
Hints and Solutions to Selected Exercises
Region 1 represents elements in none of X, Y, or Z. Region 2
represents elements in X, but in neither Y nor Z. Region 3 rep-
resents elements in X and Y, but not in Z. Region 4 represents
elements in Y, but in neither X nor Z. Region 5 represents ele-
ments in X, Y, and Z. Region 6 represents elements in X and Z,
but not in Y. Region 7 represents elements in Y and Z, but not
in X. Region 8 represents elements in Z, but in neither X nor Y.
28. (A ∪B) ∪C = A ∪(B ∪C), (A ∩B) ∩C = A ∩(B ∩C)
29. A ∪B = B ∪A, A ∩B = B ∩A
30. A ∩(B ∪C) = (A ∩B) ∪(A ∩C), A ∪(B ∩C) =
(A ∪B) ∩(A ∪C)
31. A ∪∅= A, A ∩U = A
32. A ∪A = U, A ∩A = ∅
33. A ∪A = A, A ∩A = A
34. A ∪U = U, A ∩∅= ∅
35. A ∪(A ∩B) = A, A ∩(A ∪B) = A
36. A = A
37. ∅= U, U = ∅
38. (A ∪B) = A ∩B, (A ∩B) = A ∪B
39. A collection S of nonempty subsets of X is a partition of X if
every element in X belongs to exactly one member of S.
40. The Cartesian product of X and Y is the set of all ordered pairs
(x, y) where x ∈X and y ∈Y. It is denoted X × Y.
41. The Cartesian product of X1, X2, . . . , Xn is the set of all
n-tuples (x1, x2, . . . , xn) where xi ∈Xi for i = 1, . . . , n. It
is denoted X1 × X2 × · · · × Xn.
Section 1.1
1. {1, 2, 3, 4, 5, 7, 10}
4. {2, 3, 5}
7. ∅
10. U
13. {6, 8}
16. {1, 2, 3, 4, 5, 7, 10}
17. Y is the set of odd, positive integers.
20. {2, 4}
23. {n ∈Z+ | n = 2 or n = 4 or n ≥6}
26. {2n + 1 | n ∈Z+ and n ≥3}
28. 0
31. 5
32. If x ∈A, then x is one of 3, 2, 1. Thus x ∈B. If x ∈B, then x
is one of 1, 2, 3. Thus x ∈A. Therefore, A = B.
35. If x ∈A, then x satisﬁes x2 −4x + 4 = 1. Factoring x2−
4x + 4, we ﬁnd that (x −2)2 = 1. Thus (x −2) = ±1. If
(x −2) = 1, then x = 3. If (x −2) = −1, then x = 1. Since
x = 3 or x = 1, x ∈B. Therefore A ⊆B.
If x ∈B, then x = 1 or x = 3. If x = 1, then
x2 −4x + 4 = 12 −4 ·1 + 4 = 1
and thus x ∈A. If x = 3, then
x2 −4x + 4 = 32 −4 ·3 + 4 = 1
and again x ∈A. Therefore B ⊆A. We conclude that A = B.
36. Since 1 ∈A, but 1̸ ∈B, A̸ = B.
39. Note that A = B ∩C = {2, 4}. Since 1 ∈B, but 1̸ ∈A, A̸ = B.
40. Equal
43. Not equal
44. Let x ∈A. Then x = 1 or x = 2. In either case, x ∈B.
Therefore A ⊆B.
47. First note that B = Z+. Now let x ∈A. Then x = 2n for some
n ∈Z+. Since 2 ∈Z+, 2n ∈Z+ = B. Therefore A ⊆B.
48. Since 3 ∈A, but 3̸ ∈B, A is not a subset of B.
51. Since 3 ∈A, but 3̸ ∈B, A is not a subset of B.
52.
A
B
U
55. Same as Exercise 52
58.
A
B
C
U
60. The shaded area represents the beverage, which has great taste
and is less ﬁlling.
61. 10
64. 64
66. 4
68. {(1, a), (1, b), (1, c), (2, a), (2, b), (2, c)}
71. {(a, a), (a, b), (a, c), (b, a), (b, b), (b, c), (c, a),
(c, b), (c, c)}
72. {(1, a, α), (1, a, β), (2, a, α), (2, a, β)}
75. {(a, 1, a, α), (a, 2, a, α), (a, 1, a, β), (a, 2, a, β)}
76. The entire xy-plane
78. Parallel horizontal lines spaced one unit apart. There is a
lowest line [passing through (0, 0)] but the lines continue
indeﬁnitely above the lowest line.
81. Parallel planes stacked one above another one unit apart. The
planes continue indeﬁnitely in both directions [above and
below the origin (0, 0, 0)].
83. {{1}}
86. {{a, b, c, d}}, {{a, b, c}, {d}},
{{a, b, d}, {c}}, {{a, c, d}, {b}}, {{b, c, d}, {a}},
{{a, b}, {c}, {d}}, {{a, c}, {b}, {d}},
{{a, d}, {b}, {c}},
{{b, c}, {a}, {d}}, {{b, d}, {a}, {c}}, {{c, d}, {a}, {b}},
{{a, b}, {c, d}}, {{a, c}, {b, d}}, {{a, d}, {b, c}},
{{a}, {b}, {c}, {d}}
87. True
90. True

<!-- pagina 3 -->
Hints and Solutions to Selected Exercises
635
93. ∅, {a}, {b}, {a, b}. All but {a, b} are proper subsets.
96. 2n −1
97. A ⊆B
100. B ⊆A
101. {1, 4, 5}
104. The center of the circle
Section 1.2 Review
1. A proposition is a sentence that is either true or false, but not
both.
2. The truth table of a proposition P made up of the individual
propositions p1, . . . , pn lists all possible combinations of truth
values for p1, . . . , pn, T denoting true and F denoting false,
and for each such combination lists the truth value of P.
3. The conjunction of propositions p and q is the proposition p
and q. It is denoted p ∧q.
4.
p
q
p ∧q
T
T
T
T
F
F
F
T
F
F
F
F
5. The disjunction of propositions p and q is the proposition p or
q. It is denoted p ∨q.
6.
p
q
p ∨q
T
T
T
T
F
T
F
T
T
F
F
F
7. The negation of proposition p is the proposition not p. It is
denoted ¬p.
8.
p
¬p
T
F
F
T
Section 1.2
1. Is a proposition. Negation: 2 + 5̸ = 19
5. Not a proposition; it is a question.
8. Not a proposition; it is a command.
11. Not a proposition; it is a description of a mathematical expres-
sion (i.e., p −q, where p and q are primes).
13. Ten heads were not obtained. (Alternative: At least one tail
was obtained.)
16. No heads were obtained. (Alternative: Ten tails were ob-
tained.)
17. True
20. True
23.
p
q
p ∧¬q
T
T
F
T
F
T
F
T
F
F
F
F
26.
p
q
(p ∧q) ∧¬q
T
T
F
T
F
F
F
T
F
F
F
F
29.
p
q
(p ∨q) ∧(¬p ∨q) ∧(p ∨¬q) ∧(¬p ∨¬q)
T
T
F
T
F
F
F
T
F
F
F
F
31. p ∧q; false
34. Lee does not take computer science.
37. Lee takes computer science or Lee does not take mathematics.
40. You play football and you miss the midterm exam.
43. It is not the case that you play football or you miss the midterm
exam, or you pass the course.
45. Today is Monday or it is raining.
48. (Today is Monday and it is raining) and it is not the case that
(it is hot or today is Monday).
50. ¬p
53. ¬p ∧¬q
56. p ∧¬q
59. ¬p ∧¬r ∧¬q
61. p ∧r
64. (p ∨q) ∧¬r
68. Inclusive-or: To enter Utopia, you must show a driver’s license
or a passport or both. Exclusive-or: To enter Utopia, you must
show a driver’s license or a passport but not both. Exclusive-or
is the intended meaning.
71. Inclusive-or: The car comes with a cupholder that heats or
cools your drink or both. Exclusive-or: The car comes with
a cupholder that heats or cools your drink but not both.
Exclusive-or is the intended meaning.
74. Inclusive-or: The meeting will be canceled if fewer than 10
persons sign up or at least 3 inches of snow falls or both.
Exclusive-or: The meeting will be canceled if fewer than 10
persons sign up or at least 3 inches of snow falls but not both.
Inclusive-or is the intended meaning.
75. No, assuming the interpretation: It shall be unlawful for any
person to keep more than three [3] dogs and more than three
[3] cats upon his property within the city. A judge ruled that
the ordinance was “vague.” Presumably, the intended meaning
was: “It shall be unlawful for any person to keep more than

<!-- pagina 4 -->
636
Hints and Solutions to Selected Exercises
three [3] dogs or more than three [3] cats upon his property
within the city.”
76. “national park” “north dakota” OR “south dakota”
Section 1.3 Review
1. If p and q are propositions, the conditional proposition is the
proposition if p then q. It is denoted p →q.
2.
p
q
p →q
T
T
T
T
F
F
F
T
T
F
F
T
3. In the conditional proposition p →q, p is the hypothesis.
4. In the conditional proposition p →q, q is the conclusion.
5. In the conditional proposition p →q, q is a necessary
condition.
6. In the conditional proposition p →q, p is a suﬃcient
condition.
7. The converse of p →q is q →p.
8. If p and q are propositions, the biconditional proposition is
the proposition p if and only if q. It is denoted p ↔q.
9.
p
q
p ↔q
T
T
T
T
F
F
F
T
F
F
F
T
10. If the propositions P and Q are made up of the propositions
p1, . . . , pn, P and Q are logically equivalent provided that
given any truth values of p1, . . . , pn, either P and Q are both
true or P and Q are both false.
11. ¬(p ∨q) ≡¬p ∧¬q, ¬(p ∧q) ≡¬p ∨¬q
12. The contrapositive of p →q is ¬q →¬p.
Section 1.3
1. If Joey studies hard, then he will pass the discrete mathematics
exam.
4. If Katrina passes discrete mathematics, then she will take the
algorithms course.
7. If you inspect the aircraft, then you have the proper security
clearance.
10. If the program is readable, then it is well structured.
12. (For Exercise 1) If Joey passes the discrete mathematics exam,
then he studied hard.
14. True
17. False
20. False
23. True
26. True
29. True
32. True
33. True
36. False
39. True
42. True
43. p →q
46. q ↔(p ∧¬r)
47. p →q
50. q ↔(p ∧r)
53. If today is Monday, then it is raining.
56. It is not the case that today is Monday or it is raining if and
only if it is hot.
59. Let p: 4 < 6 and q: 9 > 12.
Given statement: p →q; false.
Converse: q →p; if 9 > 12, then 4 < 6; true.
Contrapositive: ¬q →¬p; if 9 ≤12, then 4 ≥6; false.
62. Let p: |4| < 3 and q: −3 < 4 < 3.
Given statement: q →p; true.
Converse: p →q; if |4| < 3, then −3 < 4 < 3; true.
Contrapositive:
¬p →¬q, if |4| ≥3, then −3 ≥4 or 4 ≥3; true.
63. P̸ ≡Q
66. P̸ ≡Q
69. P̸ ≡Q
72. P̸ ≡Q
73. Pat will not use the treadmill and will not lift weights.
76. To make chili, you do not need red pepper or you do not need
onions.
77.
p
q
p imp1 q
q imp1 p
T
T
T
T
T
F
F
F
F
T
F
F
F
F
T
T
Since p imp1 q is true precisely when q imp1 p is true,
p imp1 q ≡q imp1 p.
80.
p
q
p →q
¬p ∨q
T
T
T
T
T
F
F
F
F
T
T
T
F
F
T
T
Since p →q is true precisely when ¬p ∨q is true, p →q ≡
¬p ∨q.
Section 1.4 Review
1. Deductive reasoning refers to the process of drawing a con-
clusion from a sequence of propositions.
2. In the argument p1, p2, . . . , pn/∴q, the hypotheses are
p1, p2, . . . , pn.
3. “Premise” in another name for hypothesis.
4. In the argument p1, p2, . . . , pn/∴q, the conclusion is q.
5. The argument p1, p2, . . . , pn/∴q is valid provided that if p1
and p2 and . . . and pn are all true, then q must also be true.

<!-- pagina 5 -->
Hints and Solutions to Selected Exercises
637
6. An invalid argument is an argument that is not valid.
7.
p →q
p
∴q
8.
p →q
¬q
∴¬p
9.
p
∴p ∨q
10.
p ∧q
∴p
11.
p
q
∴p ∧q
12.
p →q
q →r
∴p →r
13.
p ∨q
¬p
∴q
Section 1.4
1. Valid
p →q
p
∴q
4. Invalid
(p ∨r) →q
q
∴¬p →r
6. Valid
(p →s) ∧(q →r)
p ∨q
∴r ∨s
9. Valid p →(r ∨s)
q →r
¬s
p
∴r ∨q
10. Valid. If 4 megabytes is better than no memory at all, then
we will buy a new computer. If 4 megabytes is better than no
memory at all, then we will buy more memory. Therefore, if
4 megabytes is better than no memory at all, then we will buy
a new computer and we will buy more memory.
13. Invalid. If we will not buy a new computer, then 4 megabytes is
not better than no memory at all. We will buy a new computer.
Therefore, 4 megabytes is better than no memory at all.
15. Valid. If the for loop is faulty or the while loop is faulty, then
the hardware is unreliable or the output is correct. The for loop
is faulty. The hardware is not unreliable. Therefore the output
is correct.
18. Valid. If the for loop is faulty, then the while loop is faulty. If
the while loop is faulty, then the hardware is unreliable. The
hardware is not unreliable. If the output is correct, then the
hardware is unreliable. Therefore the output is not correct.
20. Invalid
23. Invalid
26. An analysis of the argument must take into account the fact
that “nothing” is being used in two very diﬀerent ways.
27. Addition
30. Let p denote the proposition “there is gas in the car,” let q
denote the proposition “I go to the store,” and let r denote the
proposition “I get a soda.” Then the hypotheses are as follows:
p →q
q →r
p
From p →q and q →r, we may use the hypothetical syl-
logism to conclude p →r. From p →r and p, we may use
modus ponens to conclude r. Since r represents the propo-
sition “I get a soda,” we conclude that the conclusion does
follow from the hypotheses.
33. We construct a truth table for all the propositions involved:
p
q
p →q
¬q
¬p
T
T
T
F
F
T
F
F
T
F
F
T
T
F
T
F
F
T
T
T
We observe that whenever the hypotheses p →q and ¬q are
true, the conclusion ¬p is also true; therefore, the argument is
valid.
36. We construct a truth table for all the propositions involved:
p
q
p ∧q
T
T
T
T
F
F
F
T
F
F
F
F
We observe that whenever the hypotheses p and q are true,
the conclusion p ∧q is also true; therefore, the argument is
valid.
Section 1.5 Review
1. If P(x) is a statement involving the variable x, we call P a
propositional function if for each x in the domain of discourse,
P(x) is a proposition.
2. A domain of discourse for a propositional function P is a set
D such that P(x) is deﬁned for every x in D.
3. A universally quantiﬁed statement is a statement of the form
for all x in the domain of discourse, P(x).
4. A counterexample to the statement ∀x P(x) is a value of x for
which P(x) is false.
5. An existentially quantiﬁed statement is a statement of the form
for some x in the domain of discourse, P(x).
6. ¬(∀x P(x)) and ∃x ¬P(x) have the same truth values.
¬(∃x P(x)) and ∀x ¬P(x) have the same truth values.
7. To prove that the universally quantiﬁed statement ∀x P(x) is
true, show that for every x in the domain of discourse, the
proposition P(x) is true.
8. To prove that the existentially quantiﬁed statement ∃x P(x) is
true, ﬁnd one value of x in the domain of discourse for which
the proposition P(x) is true.
9. To prove that the universally quantiﬁed statement ∀x P(x) is
false, ﬁnd one value of x in the domain of discourse for which
the proposition P(x) is false.
10. To prove that the existentially quantiﬁed statement ∃x P(x) is
false, show that for every x in the domain of discourse, the
proposition P(x) is false.

<!-- pagina 6 -->
638
Hints and Solutions to Selected Exercises
11.
∀xP(x)
∴P(d) if d ∈D
12.
P(d) for every d ∈D
∴∀x P(x)
13.
∃xP(x)
∴P(d) for some d ∈D
14.
P(d) for some d ∈D
∴∃x P(x)
Section 1.5
1. Is a propositional function. The domain of discourse could be
taken to be all integers.
4. Is a propositional function. The domain of discourse is the set
of all movies.
7. 11 divides 77. True.
10. For every positive integer n, n divides 77. False.
13. There exists n such that n does not divide 77. True.
16. True
19. False
22. False
25. P(1) ∧P(2) ∧P(3) ∧P(4)
28. P(1) ∨P(2) ∨P(3) ∨P(4)
31. P(2) ∧P(3) ∧P(4)
32. Every student is taking a math course.
35. Some student is not taking a math course.
38. (For Exercise 32) ∃x ¬P(x). Some student is not taking a math
course.
39. Every professional athlete plays soccer. False.
42. Either someone does not play soccer or some soccer player is
a professional athlete. True.
45. Everyone is a professional athlete and plays soccer. False.
47. (For Exercise 39) ∃x(P(x) ∧¬Q(x)). Someone is a profes-
sional athlete and does not play soccer.
48. ∀x(P(x) →Q(x))
51. ∃x(P(x) ∧Q(x))
52. (For Exercise 48) ∃x(P(x) ∧¬Q(x)). Some accountant does
not own a Porsche.
53. False. A counterexample is x = 0.
56. True. The value x = 2 makes (x > 1) →(x2 > x) true.
59. (For Exercise 53) ∃x(x2 ≤x). There exists x such that x2 ≤x.
61. The literal meaning is: No man cheats on his wife. The in-
tended meaning is: Some man does not cheat on his wife. Let
P(x) denote the statement “x is a man,” and Q(x) denote the
statement “x cheats on his wife.” Symbolically, the clariﬁed
statement is ∃x(P(x) ∧¬Q(x)).
64. The literal meaning is: No environmental problem is a tragedy.
The intended meaning is: Some environmental problem is not
a tragedy. Let P(x) denote the statement “x is an environmen-
tal problem,” and Q(x) denote the statement “x is a tragedy.”
Symbolically, the clariﬁed statement is ∃x(P(x) ∧¬Q(x)).
67. The literal meaning is: Everything is not sweetness and light.
The intended meaning is: Not everything is sweetness and
light. Let P(x) denote the statement “x is sweetness and light.”
Symbolically, the clariﬁed statement is ∃x ¬P(x).
70. The literal meaning is: No circumstance is right for a formal
investigation. The intended meaning is: Some circumstance is
not right for a formal investigation. Let P(x) denote the state-
ment “x is a circumstance,” and Q(x) denote the statement “x
is right for a formal investigation.” Symbolically, the clariﬁed
statement is ∃x(P(x) ∧¬Q(x)).
72. (a)
p
q
p →q
q →p
T
T
T
T
T
F
F
T
F
T
T
F
F
F
T
T
One of p →q or q →p is true since in each row, one of
the last two entries is true.
(b) The statement, “All integers are positive or all positive
numbers are integers,” which is false, in symbols is
(∀x(I(x) →P(x))) ∨(∀x(P(x) →I(x))).
This is not the same as the given statement
∀x((I(x) →P(x)) ∨(P(x) →I(x))),
which is true. The ambiguity results from attempting to
distribute ∀across the or.
75. Universal instantiation
76. Let P(x) denote the propositional function “x has a graphing
calculator,” and let Q(x) denote the propositional function “x
understands the trigonometric functions.” The hypotheses are
∀x P(x) and ∀x(P(x) →Q(x)). By universal instantiation, we
have P(Ralphie) and P(Ralphie) →Q(Ralphie). The modus
ponens rule of inference now gives Q(Ralphie), which repre-
sents the proposition “Ralphie understands the trigonometric
functions.” We conclude that the conclusion does follow from
the hypotheses.
79. By deﬁnition, the proposition ∀x P(x) is true when P(x) is
true for all x in the domain of discourse. We are given that
P(d) is true for any d in the domain of discourse D. Therefore,
∀x P(x) is true.
Section 1.6 Review
1. For every x and for every y, P(x, y). Let the domain of dis-
course be X × Y. The statement is true if, for every x ∈X and
for every y ∈Y, P(x, y) is true. The statement is false if there
is at least one x ∈X and at least one y ∈Y such that P(x, y) is
false.
2. For every x, there exists y such that P(x, y). Let the domain of
discourse be X × Y. The statement is true if, for every x ∈X,
there is at least one y ∈Y for which P(x, y) is true. The state-
ment is false if there is at least one x ∈X such that P(x, y) is
false for every y ∈Y.
3. There exists x such that for every y, P(x, y). Let the domain of
discourse be X×Y. The statement is true if there is at least one
x ∈X such that P(x, y) is true for every y ∈Y. The statement
is false if, for every x ∈X, there is at least one y ∈Y such that
P(x, y) is false.

<!-- pagina 7 -->
Hints and Solutions to Selected Exercises
639
4. There exists x and there exists y such that P(x, y). Let the do-
main of discourse be X × Y. The statement is true if there is
at least one x ∈X and at least one y ∈Y such that P(x, y) is
true. The statement is false if, for every x ∈X and for every
y ∈Y, P(x, y) is false.
5. Let P(x, y) be the propositional function “x ≤y” with domain
of discourse Z × Z. Then ∀x∃yP(x, y) is true since, for every
integer x, there exists an integer y (e.g., y = x) such that x ≤y
is true. On the other hand, ∃x∀yP(x, y) is false. For every inte-
ger x, there exists an integer y (e.g., y = x −1) such that x ≤y
is false.
6. ∃x∃y¬P(x, y)
7. ∃x∀y¬P(x, y)
8. ∀x∃y¬P(x, y)
9. ∀x∀y¬P(x, y)
10. Given a quantiﬁed propositional function, you and your op-
ponent, whom we call Farley, play a logic game. Your goal
is to try to make the propositional function true, and Far-
ley’s goal is to try to make it false. The game begins with
the ﬁrst (left) quantiﬁer. If the quantiﬁer is ∀, Farley chooses
a value for that variable; if the quantiﬁer is ∃, you choose a
value for that variable. The game continues with the second
quantiﬁer. After values are chosen for all the variables, if the
propositional function is true, you win; if it is false, Farley
wins. If you can always win regardless of how Farley chooses
values for the variables, the quantiﬁed propositional function
is true, but if Farley can choose values for the variables so
that you cannot win, the quantiﬁed propositional function is
false.
Section 1.6
1. Everyone is taller than everyone.
4. Someone is taller than someone.
5. (For Exercise 1) In symbols: ∃x∃y¬T1(x, y). In words: Some-
one is not taller than someone.
6. (Exercise 1) False. Garth is not taller than Garth. (Exercise 2)
False. Erin is taller than no one. (Exercise 3) False. No one is
taller than everyone (himself, in particular). (Exercise 4) True.
Garth is taller than Erin.
9. (Exercise 1) False. Garth is not taller than Pat. (Exercise 2)
False. Garth is not taller than Pat, Sandy, or Gale. (Exercise 3)
True. Marty is taller than Pat, Sandy, and Gale. (Exercise 4)
True. Marty is taller than Pat.
12. (Exercise 1) False. Dale is not taller than Dale. (Exercise 2)
False. Erin is not taller than Dale. (Exercise 3) False. No one is
taller than Dale. (Exercise 4) False. No one is taller than Dale.
15. (Exercise 1) False. Dale is not taller than Dale. (Exercise 2)
True. Dale is taller than Garth. (Exercise 3) False. Dale is not
taller than Dale. (Exercise 4) True. Dale is taller than Garth.
18. (Exercise 1) False. Pat is not taller than Marty. (Exercise 2)
True. Pat, Sandy, and Gale are all taller than Erin. (Exercise 3)
False. Marty is taller than Pat, Sandy, and Gale. (Exercise 4)
True. Pat is taller than Erin.
21. (Exercise 1) False. Pat is not taller than Pat. (Exercise 2) False.
Pat is not taller than everyone. (Exercise 3) Pat is not taller
than Pat; Sandy is not taller than Pat; and Gale is not taller
than Pat. (Exercise 4) False. None of Pat, Sandy, or Gale is
taller than everyone.
22. Everyone is taller than or the same height as everyone.
25. Someone is taller than or the same height as someone.
26. (For Exercise 22) In symbols: ∃x∃y¬T2(x, y). In words: Some-
one is shorter than someone.
27. (For Exercises 22, 6, and 1) False. Erin is not taller than or the
same height as Garth.
28. For any two people, if they are distinct, the ﬁrst is taller than
the second.
31. There are two distinct people and the ﬁrst is taller than the
second.
32. (For Exercise 28) In symbols: ∃x∃y¬T3(x, y). In words: There
are two distinct people and the ﬁrst is shorter than or the same
height as the second.
33. (For Exercises 28, 6, and 1) False. Erin and Garth are distinct
persons, but Erin is not taller than Garth.
34. ∃x∀yL(x, y). True (think of a saint).
37. ∀x∃yL(x, y). True (according to Dean Martin’s song, “Every-
body Loves Somebody Sometime”).
38. (For
Exercise
34)
Everyone
does
not
love
someone.
∀x∃y¬L(x, y)
39. ∃y A( Brit, y)
42. ∀y∃x A(x, y)
43. False
46. True
47. (For Exercise 43) ∃x∃y¬P(x, y) or ∃x∃y(x < y)
48. False. A counterexample is x = 2, y = 0.
51. True. Take x = y = 0.
54. False. A counterexample is x = y = 2.
57. True. Take x = 1, y =
√
8.
60. True. Take x = 0. Then for all y, x2 + y2 ≥0.
63. True. For any x, if we set y = x −1, the conditional propo-
sition, if x < y, then x2 < y2, is true because the hypothesis is
false.
66. (For Exercise 48) ∃x∃y(x2 ≥y + 1)
69. (For Exercise 48) Since both quantiﬁers are ∀, Farley chooses
values for both x and y. Since Farley can choose values that
make x2 < y + 1 false (e.g., x = 2, y = 0), Farley can win the
game. Therefore, the proposition is false.
72. Since the ﬁrst two quantiﬁers are ∀, Farley chooses values
for both x and y. The last quantiﬁer is ∃, so you choose a
value for z. Farley can choose values (e.g., x = 1, y = 2)
so that no matter which value you choose for z, the
expression
(x < y) →((z > x) ∧(z < y))
is false. Since Farley can choose values for the variables so
that you cannot win, the quantiﬁed statement is false.

<!-- pagina 8 -->
640
Hints and Solutions to Selected Exercises
74. ∀x ∃y P(x, y) must be true. Since ∀x ∀y P(x, y) is true, regard-
less of which value of x is selected, P(x, y) is true for all y.
Thus for any x, P(x, y) is true for any particular y.
77. ∀x ∀y P(x, y) might be false. Let P(x, y) denote the expression
x ≤y. If the domain of discourse is Z+ × Z+, ∃x ∀y P(x, y) is
true; however, ∀x ∀y P(x, y) is false.
80. ∀x ∀y P(x, y) might be false. Let P(x, y) denote the expression
x ≤y. If the domain of discourse is Z+ × Z+, ∃x ∃y P(x, y) is
true; however, ∀x ∀y P(x, y) is false.
83. ∀x ∃y P(x, y) might be true. Let P(x, y) denote the expression
x ≤y. If the domain of discourse is Z+ × Z+, ∀x ∃y P(x, y) is
true; however, ∀x ∀y P(x, y) is false.
86. ∀x ∀y P(x, y) must be false. Since ∀x ∃y P(x, y) is false, there
exists x, say x = x′, such that for all y, P(x, y) is false. Choose
y = y′ in the domain of discourse. Then P(x′, y′) is false.
Therefore ∀x ∀y P(x, y) is false.
89. ∀x ∀y P(x, y) must be false. Since ∃x ∀y P(x, y) is false, for ev-
ery x there exists y such that P(x, y) is false. Choose x = x′ in
the domain of discourse. For this choice of x, there exists y =
y′ such that P(x′, y′) is false. Therefore ∀x ∀y P(x, y) is false.
92. ∀x ∀y P(x, y) must be false. Since ∃x ∃y P(x, y) is false, for
every x and for every y, P(x, y) is false. Choose x = x′ and
y = y′ in the domain of discourse. For these choices of x and
y, P(x′, y′) is false. Therefore ∀x ∀y P(x, y) is false.
95. ∃x ¬(∀y P(x, y)) is not logically equivalent to ¬(∀x ∃y
P(x, y)). Let P(x, y) denote the expression x < y. If the
domain of discourse is Z × Z, ∃x ¬(∀y P(x, y)) is true; how-
ever, ¬ (∀x ∃y P(x, y)) is false.
98. ∃x ∃y ¬P(x, y)
is
not
logically
equivalent
to
¬(∀x ∃y
P(x, y)). Let P(x, y) denote the expression x < y. If the do-
main of discourse is Z × Z, ∃x ∃y ¬P(x, y) is true; however,
¬ (∀x ∃y P(x, y)) is false.
99. ∀ε > 0 ∃δ > 0 ∀x ((0 < |x −a| < δ) →(|f(x) −L| < ε))
Chapter 1 Self-Test
1. [Section 1.1] ∅
2. [Section 1.2] False
3. [Section 1.3] If Leah gets an A in discrete mathematics, then
Leah studies hard.
4. [Section 1.3] Converse: If Leah studies hard, then Leah gets
an A in discrete mathematics. Contrapositive: If Leah does
not study hard, then Leah does not get an A in discrete math-
ematics.
5. [Section 1.1] A ⊆B
6. [Section 1.1] Yes
7. [Section 1.4] The argument is invalid. If p and r are true and
q is false, the hypotheses are true, but the conclusion is false.
8. [Section 1.3] True
9. [Section 1.4] Let
p:
The Skyscrapers win.
q:
I’ll eat my hat.
r:
I’ll be quite full.
Then the argument symbolically is
p →q
q →r
∴r →p
The argument is invalid. If p and q are false and r is true, the
hypotheses are true, but the conclusion is false.
10. [Section 1.5] The statement is not a proposition. The truth
value cannot be determined without knowing what “the team”
refers to.
11. [Section 1.5] The statement is a propositional function. When
we substitute a particular team for the variable “team,” the
statement becomes a proposition.
12. [Section 1.6] ∃x∀y¬K(x, y)
13. [Section 1.6] ∀x∃yK(x, y); everybody knows somebody.
14. [Section 1.1] Since |A|
=
3 and |P(A)|
=
23
=
8,
|P(A) × A| = 8 ·3 = 24.
15. [Section 1.2]
p
q
r
¬(p ∧q) ∨(p ∨¬r)
T
T
T
T
T
T
F
T
T
F
T
T
T
F
F
T
F
T
T
T
F
T
F
T
F
F
T
T
F
F
F
T
16. [Section 1.2] I take hotel management and either I do not take
recreation supervision or I take popular culture.
17. [Section 1.2] p ∨(q ∧¬r)
18. [Section 1.5] For all positive integers n, n and n + 2 are prime.
The proposition is false. A counterexample is n = 7.
19. [Section 1.5] For some positive integer n, n and n + 2 are
prime. The proposition is true. For example, if n = 5, n and
n + 2 are prime.
20. [Section 1.4] Hypothetical syllogism
21. [Section 1.4] Let
p:
The Council approves the funds.
q:
New Atlantic gets the Olympic Games.
r:
New Atlantic builds a new stadium.
s:
The Olympic Games are canceled.
Then the argument symbolically is
p →q
q →r
¬r
∴¬p ∨s
From p →q and q →r, we may use the hypothetical syllo-
gism to conclude p →r. From p →r and ¬r, we may use

<!-- pagina 9 -->
Hints and Solutions to Selected Exercises
641
the modus tollens to conclude ¬p. We may then use addition
to conclude ¬p ∨s.
22. [Section 1.6] The statement is true. For every x, there exists y,
namely the cube root of x, such that x = y3. In words: Every
real number has a cube root.
23. [Section 1.6]
¬(∀x∃y∀zP(x, y, z)) ≡∃x¬(∃y∀zP(x, y, z))
≡∃x∀y¬(∀zP(x, y, z))
≡∃x∀y∃z¬P(x, y, z)
24. [Section 1.3] (¬r ∨q) →¬q
Section 2.1 Review
1. A mathematical system consists of axioms, deﬁnitions, and
undeﬁned terms.
2. An axiom is a proposition that is assumed to be true.
3. A deﬁnition creates a new concept in terms of existing ones.
4. An undeﬁned term is a term that is not explicitly deﬁned but
rather is implicitly deﬁned by the axioms.
5. A theorem is a proposition that has been proved to be true.
6. A proof is an argument that establishes the truth of a
theorem.
7. A lemma is a theorem that is usually not too interesting in its
own right but is useful in proving another theorem.
8. A direct proof assumes that the hypotheses are true and then,
using the hypotheses as well as other axioms, deﬁnitions, and
previously derived theorems, shows directly that the conclu-
sion is true.
9. An integer n is even if there exists an integer k such that
n = 2k.
10. An integer n is odd if there exists an integer k such that n =
2k + 1.
11. Within a proof, a proof of an auxiliary result is called a
subproof.
12. To disprove the universally quantiﬁed statement ∀xP(x), we
need to ﬁnd one member x in the domain of discourse that
makes P(x) false.
Section 2.1
1. If three points are not collinear, then there is exactly one plane
that contains them.
4. If x is a nonnegative real number and n is a positive integer,
x1/n is the nonnegative number y satisfying yn = x.
7. Let m and n be even integers. Then there exist k1 and k2 such
that m = 2k1 and n = 2k2. Now
m + n = 2k1 + 2k2 = 2(k1 + k2).
Therefore m + n is even.
10. Let m and n be odd integers. Then there exist k1 and k2 such
that m = 2k1 + 1 and n = 2k2 + 1. Now
mn = (2k1 + 1)(2k2 + 1) = 4k1k2 + 2k1 + 2k2 + 1
= 2(2k1k2 + k1 + k2) + 1.
Therefore mn is odd.
13. Let x and y be rational numbers. Then there exist integers
m1, n1, m2, n2 such that x = m1/n1 and y = m2/n2. Now
x + y = m1
n1
+ m2
n2
= m1n2 + m2n1
n1n2
.
Since m1n2 + m2n1 and n1n2 are integers, x + y is a rational
number.
16. If m = 3k1 + 1 and n = 3k2 + 1, then
mn = (3k1 + 1)(3k2 + 1) = 9k1k2 + 3k1 + 3k2 + 1
= 3(3k1k2 + k1 + k2) + 1.
18. From the deﬁnition of max, it follows that d ≥d1 and d ≥d2.
From x ≥d and d ≥d1, we may derive x ≥d1 from a previous
theorem (the second theorem of Example 2.1.5). From x ≥d
and d ≥d2, we may derive x ≥d2 from the same previous
theorem. Therefore, x ≥d1 and x ≥d2.
21. Let x ∈X ∩Y. From the deﬁnition of “intersection,” we con-
clude that x ∈X. Therefore X ∩Y ⊆X.
24. Let x ∈X ∩Z. From the deﬁnition of “intersection,” we con-
clude that x ∈X and x ∈Z. Since X ⊆Y and x ∈X, x ∈Y.
Since x ∈Y and x ∈Z, from the deﬁnition of “intersection,”
we conclude that x ∈Y ∩Z. Therefore X ∩Z ⊆Y ∩Z.
27. Let x ∈Y. From the deﬁnition of “union,” we conclude that
x ∈X ∪Y. Since X ∪Y = X ∪Z, x ∈X ∪Z. From the deﬁni-
tion of “union,” we conclude that x ∈X or x ∈Z. If x ∈Z, we
conclude that Y ⊆Z. If x ∈X, from the deﬁnition of “inter-
section,” we conclude that x ∈X ∩Y. Since X ∩Y = X ∩Z,
x ∈X ∩Z. Therefore x ∈Z, and again Y ⊆Z.
The argument that Z ⊆Y is the same as that for Y ⊆Z
with the roles of Y and Z reversed. Thus Y = Z.
30. Since X ∈P(X), X ∈P(Y). Therefore X ⊆Y.
33. False. If X = {1, 2} and Y = {2, 3}, then X is not a subset of
Y since 1 ∈X, but 1 /∈Y. Also, Y is not a subset of X since
3 ∈Y, but 3 /∈X.
36. False. Let X = {1, a}, Y = {1, 2, 3}, and Z = {3}. Then
Y −Z = {1, 2} and (X ∪Y) −(X ∪Z) = {2}.
39. False. Let X = Y = {1} and U = {1, 2}. Then X ∩Y = {2},
which is not a subset of X.
42. False. Let X = Y = {1} and U = {1, 2}. Then X × Y =
{(1, 2), (2, 1), (2, 2)} and X × Y = {(2, 2)}.
45. False. Let X
= {1, 2}, Y
= {1}, and Z
= {2}. Then
X ∩(Y × Z) = ∅and (X ∩Y) × (X ∩Z) = {(1, 2)}.
46. We prove only (A∪B)∪C = A∪(B∪C). Let x ∈(A∪B)∪C.
Then x ∈A ∪B or x ∈C. If x ∈A ∪B, then x ∈A or
x ∈B. Thus x ∈A or x ∈B or x ∈C. If x ∈A, then
x ∈A ∪(B ∪C). If x ∈B or x ∈C, then x ∈B ∪C. Again,
x ∈A ∪(B ∪C).
Now suppose that x ∈A ∪(B ∪C). Then x ∈A or
x ∈B ∪C. If x ∈B ∪C, then x ∈B or x ∈C. Thus x ∈A
or x ∈B or x ∈C. If x ∈A or x ∈B, then x ∈A ∪B. Thus

<!-- pagina 10 -->
642
Hints and Solutions to Selected Exercises
x ∈(A ∪B) ∪C. If x ∈C, again x ∈(A ∪B) ∪C. Therefore
(A ∪B) ∪C = A ∪(B ∪C).
49. We prove only A ∪∅= A. Let x ∈A ∪∅. Then x ∈A or
x ∈∅. But x /∈∅, so x ∈A.
Now suppose that x ∈A. Then x ∈A ∪∅. Therefore
A ∪∅= A.
52. We prove only A ∪U = U. By deﬁnition, any set is a subset
of the universal set, so A ∪U ⊆U.
If x ∈U, then x ∈A ∪U. Thus U ⊆A ∪U. Therefore
A ∪U = U.
55. We prove only ∅= U. By deﬁnition, any set is a subset of the
universal set, so ∅⊆U.
Now suppose that x ∈U. Then x /∈∅(by the deﬁnition
of “empty set”). Thus x ∈∅and U ⊆∅. Therefore ∅= U.
57. Let x ∈A△B. Then x ∈A∪B and x /∈A∩B. Since x ∈A∪B,
x ∈A or x ∈B. Since x /∈A∩B, x /∈A or x /∈B. If x ∈A, then
x /∈B. Thus x ∈A −B; hence x ∈(A −B) ∪(B −A). If x ∈B,
then x /∈A. Thus x ∈B −A and again x ∈(A −B) ∪(B −A).
Therefore A △B ⊆(A −B) ∪(B −A).
Now suppose that x ∈(A−B)∪(B−A). Then x ∈A−B
or x ∈B−A. If x ∈A−B, then x ∈A and x /∈B. Thus x ∈A∪B
and x /∈A ∩B. Therefore x ∈(A ∪B) −(A ∩B) = A △B.
If x ∈B −A, then x ∈B and x /∈A. Then x ∈A ∪B
and x /∈A ∩B. Again x ∈(A ∪B) −(A ∩B) = A △B.
Therefore (A −B) ∪(B −A) ⊆A △B. We have proved that
(A −B) ∪(B −A) = A △B.
60. False. Let A = {1, 2, 3}, B = {2, 3, 4}, and C = {1, 2, 4}.
Then A △(B ∪C) = {4} and (A △B) ∪(A △C) = {1, 4}∪
{3, 4} = {1, 3, 4}.
63. True. Using Example 2.1.11,, we ﬁnd that
A ∩(B △C) = A ∩[(B ∪C) −(B ∩C)]
= [A ∩(B ∪C)] −[A ∩(B ∩C)].
Using the distributive law and observing that (A ∩B) ∩
(A ∩C) = A ∩(B ∩C), we ﬁnd that
(A ∩B) △(A ∩C) = [(A ∩B) ∪(A ∩C)] −[(A ∩B) ∩(A ∩C)]
= [A ∩(B ∪C)] −[A ∩(B ∩C)].
Therefore
A ∩(B △C) = (A ∩B) △(A ∩C).
Section 2.2 Review
1. A proof by contradiction assumes that the hypotheses are
true and that the conclusion is false and then, using the
hypotheses and the negated conclusion as well as other ax-
ioms, deﬁnitions, and previously derived theorems, derives a
contradiction.
2. Example 2.2.1
3. “Indirect proof” is another name for proof by contradiction.
4. To prove p →q, proof by contrapositive proves the equivalent
statement ¬q →¬p.
5. Example 2.2.5
6. Instead of proving
(p1 ∨p2 ∨· · · ∨pn) →q,
in proof by cases, we prove
(p1 →q) ∧(p2 →q) ∧· · · ∧(pn →q).
7. Example 2.2.6
8. Proof of equivalence shows that two or more statements are
all true or all false.
9. Example 2.2.11
10. If the statements are p, q, and r, we can show that they are
equivalent by proving that p →q, q →r, and r →p are all
true.
11. A proof of ∃x P(x) is called an existence proof.
12. An existence proof of ∃x P(x) that exhibits an element a of the
domain of discourse that makes P(a) true is called a construc-
tive proof.
13. Example 2.2.12
14. A proof of ∃x P(x) that does not exhibit an element a of the
domain of discourse that makes P(a) true, but rather proves
∃x P(x) some other way (e.g., using proof by contradiction), is
called a nonconstructive proof.
15. Example 2.2.14
Section 2.2
1. Suppose, by way of contradiction, that x is rational. Then there
exist integers p and q such that x = p/q. Now x2 = p2/q2 is
rational, which is a contradiction.
4. Suppose, by way of contradiction, that n is even. Then there
exists k such that n = 2k. Now n2 = 2(2k2); thus n2 is even,
which is a contradiction.
7. Suppose, by way of contradiction, that
3√
2 is rational. Then
there exist integers p and q such that
3√
2 = p/q. We assume
that the fraction p/q is in lowest terms so that p and q are not
both even. Cubing
3√
2 = p/q gives 2 = p3/q3, and multiply-
ing by q3 gives 2q3 = p3. It follows that p3 is even. An argu-
ment like that in Example 2.2.1 shows that p is even. There-
fore, there exists an integer k such that p = 2k. Substituting
p = 2k into 2q3 = p3 gives 2q3 = (2k)3 = 8k3. Canceling 2
gives q3 = 4k3. Therefore q3 is even and, thus, q is even. Thus
p and q are both even, which contradicts our assumption that
p and q are not both even. Therefore,
3√
2 is irrational.
10. Since the integers increase without bound, there exists n ∈Z
such that 1/(b −a) < n. Therefore 1/n < b −a. Choose
m ∈Z as large as possible satisfying m/n ≤a. Then, by the
choice of m, a < (m + 1)/n. Also
m + 1
n
= m
n + 1
n < a + (b −a) = b.
Therefore x = (m + 1)/n is a rational number satisfying
a < x < b.
13. True. Let a = b = 2. Then a and b are rational numbers
and ab = 4 is also rational. This is a constructive existence
proof.

<!-- pagina 11 -->
Hints and Solutions to Selected Exercises
643
16. A team can score any number of points greater than or equal
to two. To prove this, let n be an integer greater than or equal
to 2. If n is even, say n = 2k, if the team scores k safeties,
its total score is 2k = n. If n is odd, say n = 2k + 1, if the
team scores one ﬁeld goal and k −1 safeties, its total score is
3+2(k−1) = 2k+1 = n. (Note that k ≥1, so the prescribed
scoring is possible.)
19. True. We give a proof by contradiction. Suppose that (X−Y)∩
(Y −X) is nonempty. Then there exists x ∈(X −Y)∩(Y −X).
Thus x ∈X −Y and x ∈Y −X. Since x ∈X −Y, x ∈X
and x /∈Y. Since x ∈Y −X, x ∈Y and x /∈X. We now
have x ∈X and x /∈X, which is a contradiction. Therefore
(X −Y) ∩(Y −X) = ∅.
22. Suppose, by way of contradiction, that no two bags contain
the same number of coins. Suppose that we arrange the bags
in increasing order of the number of coins that they contain.
Then the ﬁrst bag contains at least one coin; the second bag
contains at least two coins; and so on. Thus the total number
of coins is at least
1 + 2 + 3 + · · · + 9 = 45.
This contradicts the hypothesis that there are 40 coins. Thus
if 40 coins are distributed among nine bags so that each bag
contains at least one coin, at least two bags contain the same
number of coins.
25. Let i be the greatest integer for which si is positive. Since s1
is positive and the set of indexes 1, 2, . . . , n is ﬁnite, such an
i exists. Since sn is negative, i < n. Now si+1 is equal to ei-
ther si + 1 or si −1. If si+1 = si + 1, then si+1 is a positive
integer (since si is a positive integer). This contradicts the fact
that i is the greatest integer for which si is positive. Therefore,
si+1 = si −1. Again, if si −1 is a positive integer, we have
contradiction. Therefore, si+1 = si −1 = 0.
27. We use proof by contradiction and assume the negation of the
conclusion
¬∃i(si ≤A).
By the generalized De Morgan’s laws for logic, this latter state-
ment is equivalent to
∀i(si > A).
Thus we assume
s1 > A
s2 > A
...
sn > A.
Adding these inequalities yields
s1 + s2 + · · · + sn > nA.
Dividing by n gives
s1 + s2 + · · · + sn
n
> A,
which contradicts the hypothesis. Therefore, there exists i such
that si ≤A.
30. Since si̸ = sj, either si̸ = A or sj̸ = A. By changing the nota-
tion, if necessary, we may assume that si̸ = A. Either si < A
or si > A. If si < A, the proof is complete; so assume that
si > A. We show that there exists k such that sk < A. Suppose,
by way of contradiction, that sm ≥A for all m, that is,
s1 ≥A
s2 ≥A
...
sn ≥A.
Adding these inequalities yields
s1 + s2 + · · · + si + · · · + sn > nA
since si > A. Dividing by n gives
s1 + s2 + · · · + sn
n
> A,
which is a contradiction. Therefore there exists k such that
sk < A.
32. Notice that if n ≥2 and m ≥1,
2m + 5n2 ≥2m + 5 ·22 > 20,
so the only possible solution is if n = 1. However, if n = 1,
2m + 5n2 = 2m + 5,
which is odd being the sum of an even integer and an odd inte-
ger. Thus this sum cannot equal 20. Therefore, 2m+5n2 = 20
has no solution in positive integers.
35. We claim that if n and n + 1 are consecutive integers, one is
odd and one is even. Suppose that n is odd. Then there exists
k such that n = 2k + 1. Now n + 1 = 2k + 2 = 2(k + 1),
which is even. If n is even, there exists k such that n = 2k. Now
n+1 = 2k +1, which is odd. Since one of n and n+1 is even
and the other is odd, their product is even (see Exercise 11,
Section 2.1).
37. We consider four cases: x ≥0, y ≥0; x < 0, y ≥0;
x ≥0, y < 0; and x < 0, y < 0.
First assume that x ≥0 and y ≥0. Then xy ≥0 and
|xy| = xy = |x||y|. Next assume that x < 0 and y ≥0. Then
xy ≤0 and |xy| = −xy = (−x)(y) = |x||y|. Next assume that
x ≥0 and y < 0. Then xy ≤0 and |xy| = −xy = (x)(−y) =
|x||y|. Finally assume that x < 0 and y < 0. Then xy > 0 and
|xy| = xy = (−x)(−y) = |x||y|.
39. We consider three cases: x > 0, x = 0, and x < 0.
If x > 0, |x| = x and sgn(x) = 1. Therefore,
|x| = x = 1 ·x = sgn(x)x.
If x = 0, |x| = 0 and sgn(x) = 0. Therefore,
|x| = 0 = 0 ·0 = sgn(x)x.
If x < 0, |x| = −x and sgn(x) = −1. Therefore,
|x| = −x = −1 ·x = sgn(x)x.
In every case, we have |x| = sgn(x)x.

<!-- pagina 12 -->
644
Hints and Solutions to Selected Exercises
42. We consider two cases: x ≥y and x < y.
If x ≥y,
max{x, y} = x
and
min{x, y} = y.
Therefore,
max{x, y} + min{x, y} = x + y.
If x < y,
max{x, y} = y
and
min{x, y} = x.
Therefore,
max{x, y} + min{x, y} = y + x = x + y.
In either case,
max{x, y} + min{x, y} = x + y.
46. We ﬁrst prove that if n is even, then n + 2 is even. Assume
that n is even. Then there exists k such that n = 2k. Now
n + 2 = 2k + 2 = 2(k + 1) is even.
We next prove that if n + 2 is even, then n is even.
Assume that n + 2 is even. Then there exists k such that
n + 2 = 2k. Now n = 2k −2 = 2(k −1) is even.
48. We ﬁrst prove that if A ⊆B, then B ⊆A. Assume that A ⊆B.
Let x ∈B. Then x /∈B. If x ∈A, then x ∈B, which is not the
case. Therefore x /∈A. Therefore x ∈A. Thus B ⊆A.
We next prove that if B ⊆A, then A ⊆B. Assume that
B ⊆A. From the ﬁrst part of the proof, we can deduce A ⊆B.
Since A = A and B = B, A ⊆B.
51. We ﬁrst show that if (a, b) = (c, d), then a = c and b = d.
Assume that (a, b) = (c, d). Then
{{a}, {a, b}} = {{c}, {c, d}}.
(∗)
First suppose that a̸ = b. Then the set on the left-hand side of
equation (*) contains two distinct sets: {a} and {a, b}. Thus
the set on the right-hand side of equation (*) also contains
two distinct sets: {c} and {c, d}. Therefore c̸ = d. (If c = d,
{c, d} = {c, c} = {c}.) Since a̸ = b and c̸ = d, we must have
{a} = {c}
and
{a, b} = {c, d}.
It follows that a = c and b = d.
Now suppose that a = b. Then
{{a}, {a, b}} = {{a}, {a, a}} = {{a}, {a}} = {{a}}.
Thus the set on the left-hand side of equation (*) contains one
set. Therefore the set on the right-hand side of equation (*)
also contains one set. We must have c = d; otherwise the set
on the right-hand side of equation (*) would contain two dis-
tinct sets. Thus
{{c}, {c, d}} = {{c}}.
Equation (*) now becomes
{{a}} = {{c}}.
It follows that a = c and, hence, b = d. We have shown that
if (a, b) = (c, d), then a = c and b = d.
If a = c and b = d, then
(a, b) = {{a}, {a, b}} = {{c}, {c, d}} = (c, d).
The proof is complete.
52. [(a) →(b)] Assume that n is odd. Then there exists k′ such
that n = 2k′ + 1. Since n = 2(k′ + 1) −1, taking k = k′ + 1,
we have n = 2k −1.
[(b) →(c)] Assume that there exists k such that n =
2k −1. Then
n2+1 = (2k−1)2+1 = (4k2−4k+1)+1 = 2(2k2−2k+1).
Therefore n2 + 1 is even.
[(c) →(a)] We prove the contrapositive: If n is even,
then n2 + 1 is odd.
Suppose that n is even. Then there exists k such that
n = 2k. Now
n2 + 1 = (2k)2 + 1 = 4k2 + 1 = 2(2k2) + 1.
Therefore n2 + 1 is odd.
Section 2.3 Review
1. p ∨q, ¬p ∨r/∴q ∨r
2. A clause consists of terms separated by or’s, where each term
is a variable or the negation of a variable.
3. A proof by resolution proceeds by repeatedly applying the rule
in Exercise 1 to pairs of statements to derive new statements
until the conclusion is derived.
Section 2.3
1.
p
q
r
p ∨q
¬p ∨r
q ∨r
T
T
T
T
T
T
T
T
F
T
F
T
T
F
T
T
T
T
T
F
F
T
F
F
F
T
T
T
T
T
F
T
F
T
T
T
F
F
T
F
T
T
F
F
F
F
T
F
2. 1. ¬p ∨q ∨r
2. ¬q
3. ¬r
4. ¬p ∨r
From 1 and 2
5. ¬p
From 3 and 4
5. First we note that p →q is logically equivalent to ¬p ∨q. We
now argue as follows:
1. ¬p ∨q
2. p ∨q
3. q
From 1 and 2

<!-- pagina 13 -->
Hints and Solutions to Selected Exercises
645
7. (For Exercise 2)
1. ¬p ∨q ∨r
Hypothesis
2. ¬q
Hypothesis
3. ¬r
Hypothesis
4. p
Negation of conclusion
5. ¬p ∨r
From 1 and 2
6. ¬p
From 3 and 5
Now 4 and 6 combine to give a contradiction.
Section 2.4 Review
1. Suppose that we have propositional function S(n) whose do-
main of discourse is the set of positive integers. Suppose that
S(1) is true and, for all n ≥1, if S(n) is true, then S(n + 1) is
true. Then S(n) is true for every positive integer n.
2. We ﬁrst verify that S(1) is true (Basis Step). We then assume
that S(n) is true and prove that S(n+1) is true (Inductive Step).
3. n(n + 1)
2
4. The geometric sum is the sum
a + ar1 + ar2 + · · · + arn.
It is equal to
a(rn+1 −1)
r −1
.
Section 2.4
1. Basis Step
1 = 12
Inductive Step
Assume true for n.
1 + · · · + (2n −1) + (2n + 1) = n2 + 2n + 1 = (n + 1)2
4. Basis Step
12 = (1 ·2 ·3)/6
Inductive Step
Assume true for n.
12 + · · · + n2 + (n + 1)2 = n(n + 1)(2n + 1)
6
+ (n + 1)2
= (n + 1)(n + 2)(2n + 3)
6
7. Basis Step
1/(1 ·3) = 1/3
Inductive Step
Assume true for n.
1
1 ·3 + · · · +
1
(2n −1)(2n + 1) +
1
(2n + 1)(2n + 3)
=
n
2n + 1 +
1
(2n + 1)(2n + 3) = n + 1
2n + 3
11. Basis Step
cos x = cos[(x/2) ·2] sin(x/2)
sin(x/2)
Inductive Step
Assume true for n. Then
cos x + · · · + cos nx + cos(n + 1)x
= cos[(x/2)(n + 1)] sin(nx/2)
sin(x/2)
+ cos(n + 1)x.
(∗)
We must show that the right-hand side of (∗) is equal to
cos[(x/2)(n + 2)] sin[(n + 1)x/2]
sin(x/2)
.
This is the same as showing that [after multiplying by the term
sin(x/2)]
cos
! x
2(n + 1)
"
sin nx
2 + cos(n + 1)x sin x
2
= cos
! x
2(n + 2)
"
sin
#(n + 1)x
2
$
.
If we let α = (x/2)(n + 1) and β = x/2, we must show that
cos α sin(α −β) + cos 2α sin β = cos(α + β) sin α.
This last equation can be veriﬁed by reducing each side to
terms involving α and β.
13. Basis Step
1/2 ≤1/2
Inductive Step
Assume true for n.
1 ·3 ·5 · · · (2n −1)(2n + 1)
2 ·4 ·6 · · · (2n)(2n + 2)
≥1
2n · 2n + 1
2n + 2
= 2n + 1
2n
·
1
2n + 2 ≥
1
2n + 2
16. Basis Step (n = 4)
24 = 16 ≥16 = 42
Inductive Step
Assume true for n.
(n + 1)2 = n2 + 2n + 1 ≤2n + 2n + 1
≤2n + 2n
by Exercise 15
= 2n+1
19. r0 + r1 + · · · + rn = 1 −rn+1
1 −r
<
1
1 −r
22. Basis Step
71 −1 = 6 is divisible by 6.
Inductive Step
Suppose that 6 divides 7n −1. Now
7n+1 −1 = 7 ·7n −1 = 7n −1 + 6 ·7n.
Since 6 divides both 7n −1 and 6 ·7n, it divides their sum,
which is 7n+1 −1.
25. Basis Step
31 + 71 −2 = 8 is divisible by 8.
Inductive Step
Suppose that 8 divides 3n + 7n −2. Now
3n+1 + 7n+1 −2 = 3(3n + 7n −2) + 4(7n + 1).
By the inductive assumption, 8 divides 3n + 7n −2. We can
use mathematical induction to show that 2 divides 7n + 1 for
all n ≥1 (the argument is similar to that given in the hint for
Exercise 22). It then follows that 8 divides 4(7n + 1). Since
8 divides both 3(3n + 7n −2) and 4(7n + 1), it divides their
sum, which is 3n+1 + 7n+1 −2.
28. We prove the assertion using induction on n. The Basis Step
is n = 1. In this case, there is one subset of {1} with an even
number of elements, namely, ∅. Since 2n−1 = 20 = 1, the
assertion is true when n = 1.
Assume that the number of subsets of {1, . . . , n} con-
taining an even number of elements is 2n−1. We must prove
that the number of subsets of {1, . . . , n+1} containing an even
number of elements is 2n.

<!-- pagina 14 -->
646
Hints and Solutions to Selected Exercises
Let E1, . . . , E2n−1 denote the subsets of {1, 2, . . . , n}
containing an even number of elements. Since there are 2n
subsets of {1, 2, . . . , n} altogether and 2n−1 contain an even
number of elements, there are 2n −2n−1 = 2n−1 subsets of
{1, . . . , n} that contain an odd number of elements. Denote
these as O1, . . . , O2n−1. Now E1, . . . , E2n−1 are the subsets of
{1, . . . , n + 1} containing an even number of elements that do
not contain n + 1, and
O1 ∪{n + 1}, . . . , O2n−1 ∪{n + 1}
are the subsets of {1, . . . , n+1} containing an even number of
elements that contain n + 1. Thus there are 2n−1 + 2n−1 = 2n
subsets of {1, . . . , n + 1} that contain an even number of ele-
ments. The Inductive Step is complete.
30. At the Inductive Step when the (n+1)st line is added, because
of the assumptions, the line will intersect each of the other n
lines. Now, imagine traveling along the (n + 1)st line. Each
time we pass through one of the original regions, it is divided
into two regions.
33.
37. We denote the square in row i, column j by (i, j). Then, by
symmetry, we need only consider 7 × 7 boards with squares
(i, j) removed where i ≤j ≤4. The solution when square
(1, 1) is removed is shown in the following ﬁgure.
233 
535 
332
Not all trominoes of the tiling are shown. By Exercise 36, the
3×2 subboards have tilings. By Exercise 33, the 5×5 subboard
with a corner square removed has a tiling. Essentially the same
ﬁgure gives tilings if square (1, 2) or (2, 2) is deleted.
A similar argument gives tilings for the remaining
cases.
40. Basis Step (n = 1)
The board is a tromino.
Inductive Step
Assume that any 2n ×2n deﬁcient board can
be tiled with trominoes. We must prove that any 2n+1 × 2n+1
deﬁcient board can be tiled with trominoes.
Given a 2n+1×2n+1 deﬁcient board, we divide the board
into four 2n × 2n subboards as shown in Figure 2.4.6. By
the inductive assumption, we can tile the subboard contain-
ing the missing square. The three remaining subboards form a
2n × 2n L-shape, which may be tiled using Exercise 39. Thus,
the 2n+1 × 2n+1 deﬁcient board is tiled. The inductive step is
complete.
41. Number the squares as shown:
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
Notice that each tromino covers exactly one 1, one 2, and
one 3. Therefore, if there is a tiling, ﬁve 2’s are covered. Since
ﬁve trominoes are required, the missing square cannot be a 2.
Similarly the missing square cannot be a 3.
The same argument applied to
1
3
2
1
2
1
3
2
3
2
1
3
1
3
2
1
shows that the only possibility for the missing square is a cor-
ner. Such a board can be tiled:
45. We prove that pow = ai−1 is a loop invariant for the while
loop. Just before the while loop begins executing, i = 1 and
pow = 1, so pow = a1−1. We have proved the Basis Step.
Assume that pow = ai−1. If i ≤n (so that the loop body
executes again), pow becomes
pow ∗a = ai−1 ∗a = ai,
and i becomes i+1. We have proved the Inductive Step. There-
fore pow = ai−1 is an invariant for the while loop.
The while loop terminates when i = n + 1. Because
pow = ai−1 is an invariant, at this point pow = an.
49. (a) S1 = 0̸ = 2;
2 + · · · + 2n + 2(n + 1) = Sn + 2n + 2
= (n + 2)(n −1) + 2n + 2
= (n + 3)n = Sn+1.
(b) We must have S′
n = S′
n−1 + 2n; thus

<!-- pagina 15 -->
Hints and Solutions to Selected Exercises
647
S′
n = S′
n−1 + 2n
= [S′
n−2 + 2(n −1)] + 2n
= S′
n−2 + 2n + 2(n −1)
= S′
n−3 + 2n + 2(n −1) + 2(n −2)
...
= S′
1 + 2[n + (n −1) + · · · + 2]
= C′ + 2
#n(n + 1)
2
−1
$
= n2 + n + C.
53. If n = 2, each person throws a pie at the other and there are
no survivors.
56. The statement is false. In
1
2
3
4
5
1 and 5 are farthest apart, but neither is a survivor.
58. Let x and y be points in X ∩Y. Then x is in X and y is in X.
Since X is convex, the line segment from x to y is in X. Simi-
larly, the line segment from x to y is in Y. Therefore, the line
segment from x to y is in X ∩Y. Thus, X ∩Y is convex.
61. Let x1, . . . , xn denote the n points, and let Xi be the circle of
radius 1 centered at xi. Apply Helly’s Theorem to X1, . . . , Xn.
63. 1
66. Basis Step (i = 1)
Since 2 is eliminated, 1 survives. Thus
J(2) = 1.
Inductive Step
Assume true for i. Now suppose that 2i+1
persons are arranged in a circle. We begin by eliminating
2, 4, 6, . . . , 2i+1. We then have 2i persons arranged in a cir-
cle, and, beginning with 1, we eliminate the second person,
then the fourth person, and so on. By the inductive assump-
tion, 1 survives. Therefore,
J(2i+1) = J(2i) = 1.
69. The greatest power of 2 less than or equal to 100,000 is 216.
Thus, in the notation of Exercise 67, n = 100,000, i = 16, and
j = n −2i = 100,000 −216 = 100,000 −65,536 = 34,464.
By Exercise 67,
J(100,000) = J(n) = 2j + 1 = 2 ·34,464 + 1 = 68,929.
70.
b1 + b2 + · · · + bn = (a2 −a1) + (a3 −a2)
+ · · · + (an+1 −an)
= −a1 + an+1 = an+1 −a1
since a2, . . . , an cancel.
73. Let
an = 1
n.
Then
%an = an+1 −an =
1
n + 1 −1
n =
−1
n(n + 1).
Let bn = %an. By Exercise 70,
−1
1 ·2 + · · · +
−1
n(n + 1) = %a1 + · · · + %an
= b1 + · · · + bn
= an+1 −a1
=
1
n + 1 −1 =
−n
n + 1.
Multiplying by −1 yields the desired formula.
Section 2.5 Review
1. Suppose that we have a propositional function S(n) whose do-
main of discourse is the set of integers greater than or equal
to n0. Suppose that S(n0) is true; and for all n > n0, if S(k) is
true for all k, n0 ≤k < n, then S(n) is true. Then S(n) is true
for every integer n ≥n0.
2. Every nonempty set of nonnegative integers has a least
element.
3. If d and n are integers, d > 0, there exist unique integers q
(quotient) and r (remainder) satisfying n = dq+r, 0 ≤r < d.
Section 2.5
1. Basis Steps (n = 6, 7)
We can make six cents postage by
using three 2-cent stamps. We can make seven cents postage
by using one 7-cent stamp.
Inductive Step
We assume that n ≥8 and postage of
k cents or more can be achieved by using only 2-cent and
7-cent stamps for 6 ≤k < n. By the inductive assumption,
we can make postage of n −2 cents. We may add a 2-cent
stamp to make n cents postage.
4. Basis Step (n = 4)
We can make four cents postage by us-
ing two 2-cent stamps.
Inductive Step
We assume that we can make n cents
postage, and we prove that we can make n + 1 cents postage.
If among the stamps that make n cents postage there
is at least one 5-cent stamp, we replace one 5-cent stamp by
three 2-cent stamps to make n + 1 cents postage. If there are
no 5-cent stamps among the stamps that make n cents postage,
there are at least two 2-cent stamps (because n ≥4). We re-
place two 2-cent stamps by one 5-cent stamp to make n + 1
cents postage.
7. In the Inductive Step, we must have k = ⌊n/2⌋≥3. Since this
inequality fails for n = 4, 5, the Basis Steps are n = 3, 4, 5.
10. c2 = 4, c3 = 9, c4 = 20, c5 = 29
12. c2 = 2, c3 = 3, c4 = 12, c5 = 13
15. Notice that
c0 = 0
c1 = c0 + 3 = 3
c2 = c1 + 3 = 6

<!-- pagina 16 -->
648
Hints and Solutions to Selected Exercises
c3 = c1 + 3 = 6
c4 = c2 + 3 = 9.
Thus the assertion cn ≤2n fails for n = 4.
In the Inductive Step, we must have k = ⌊n/2⌋≥3.
Since this inequality fails for n = 4, 5, the Basis Steps are
n = 3, 4, 5. In the fallacious proof, only the case n = 3 was
proved in the Basis Steps. In fact, since the statement is false
for n = 4, the Basis Steps n = 3, 4, 5 cannot be proved.
17. q = 5, r = 2
20. q = −1, r = 2
23. 5
6 = 1
2 + 1
3 = 1
2 + 1
4 + 1
12
27. We may assume that p/q > 1. Choose the largest integer n
satisfying
1
1 + 1
2 + · · · + 1
n ≤p
q.
(The previous Problem-Solving Corner shows that the sum
1
1 + 1
2 + · · · + 1
n
is unbounded; so such an n exists.) If we obtain an equality,
p/q is in Egyptian form, so suppose that
1
1 + 1
2 + · · · + 1
n < p
q.
(∗)
Set
D = p
q −
%1
1 + · · · + 1
n
&
.
Clearly, D > 0. Since n is the largest integer satisfying (∗),
1
1 + 1
2 + · · · + 1
n +
1
n + 1 ≥p
q.
Thus
D = p
q −
%1
1 + · · · + 1
n
&
≤
%1
1 + · · · + 1
n +
1
n + 1
&
−
%1
1 + · · · + 1
n
&
=
1
n + 1.
In particular, D < 1. By Exercise 25, D may be written in
Egyptian form:
D = 1
n1
+ · · · + 1
nk
,
where the ni are distinct. Since
1
ni
≤D ≤
1
1 + n,
for i = 1, . . . , k,
n < n + 1 ≤ni for i = 1, . . . , k. It follows that
1, 2, . . . , n, n1, . . . , nk
are distinct. Thus
p
q = D + 1
1 + · · · + 1
n = 1
n1
+ · · · + 1
nk
+ 1
1 + · · · + 1
n
is represented in Egyptian form.
28. In this solution, the induction is over the set X of odd integers
n > 5, where 3 divides n2 −1. Such an induction can be jus-
tiﬁed by considering the ﬁrst statement to be about the small-
est integer in X, the second statement to be about the second
smallest integer in X, and so on.
Basis Steps (n = 7, 11)
Exercise 37, Section 2.4, gives a
solution if n = 7.
If n = 11, enclose the missing square in a corner 7 × 7
subboard (see the following ﬁgure). Tile this subboard using
the result of Exercise 37, Section 2.4. Tile the two 6 × 4 sub-
boards using the result of Exercise 36, Section 2.4. Tile the
5 × 5 subboard with a corner square missing using the result
of Exercise 33, Section 2.4. Thus the 11×11 board can be tiled.
7 3 7 
6 3 4 
6 3 4 
5 3 5 
11
11
Inductive Step
Suppose that n > 11 and assume that if
k < n, k is odd, k > 5, and 3 divides k2 −1, then a k × k
deﬁcient board can be tiled with trominoes.
Consider an n × n deﬁcient board. Enclose the missing
square in a corner (n−6)×(n−6) subboard. By the inductive
assumption, this board can be tiled with trominoes. Tile the
two 6 × (n −7) subboards using the result of Exercise 36,
Section 2.4. Tile the deﬁcient 7 × 7 subboard using the result
of Exercise 37, Section 2.4. The n × n board is tiled, and the
inductive step is complete.
n
(n – 6)3(n – 6)
6 3 (n – 7)
6 3 (n – 7)
7 3 7
n

<!-- pagina 17 -->
Hints and Solutions to Selected Exercises
649
36. Let X be a nonempty set of nonnegative integers. We must
prove that X has a least element. Using mathematical induc-
tion, we prove that for all n ≥0, if X contains an element less
than or equal to n, then X has a least element. Notice that this
proves that X has a least element. (Since X is nonempty, X
contains an integer n. Now X contains an element less than or
equal to n; so it follow that X has a least element.)
Basis Step (n = 0)
If X contains an element less than or
equal to 0, then X contains 0 since X consists of nonnegative
integers. In this case, 0 is the least element in X.
Inductive Step
Now we assume that if X contains an ele-
ment less than or equal to n, then X has a least element. We
must prove that if X contains an element less than or equal to
n + 1, then X has a least element.
Suppose that X contains an element less than or equal
to n + 1. We consider two cases: X contains an element less
than or equal to n, and X does not contain an element less than
or equal to n. If X contains an element less than or equal to n,
by the inductive assumption, X has a least element. If X does
not contain an element less than or equal to n, since X contains
an element less than or equal to n + 1, X must contain n + 1,
which is the least element in X. The inductive step is complete.
Chapter 2 Self-Test
1. [Section 2.1] Axioms are statements that are assumed to be
true. Deﬁnitions are used to create new concepts in terms of
existing ones.
2. [Section 2.2] In a direct proof, the negated conclusion is not
assumed, whereas in a proof by contradiction, the negated
conclusion is assumed.
3. [Section 2.2] Suppose that if four teams play seven games, no
pair of teams plays at least two times; or, equivalently, if four
teams play seven games, each pair of teams plays at most one
time. If the teams are A, B, C, and D and each pair of teams
plays at most one time, the most games that can be played are:
A and B;
A and C;
A and D;
B and C;
B and D;
C and D.
Thus at most six games can be played. This is a contradiction.
Therefore, if four teams play seven games, some pair of teams
plays at least two times.
4. [Section 2.1] Since x and y are rational numbers, there exist
integers m1, n1, m2, n2 such that x = m1/n1 and y = m2/n2.
Since y̸ = 0, m2̸ = 0. Now
x
y = m1/n1
m2/n2
= m1n2
n1m2
.
Since x/y is the quotient of integers, it is rational.
5. [Section 2.2] We consider two cases: a ≤b and a > b. In each
of these two cases, we consider the two cases: b ≤c and b > c.
First suppose that a ≤b. If b ≤c, then
min{min{a, b}, c} = min{a, c} = a = min{a, b}
= min{a, min{b, c}}.
If b > c, then
min{min{a, b}, c} = min{a, c} = min{a, min{b, c}}.
In either case,
min{min{a, b}, c} = min{a, min{b, c}}.
Now suppose that a > b. If b ≤c, then
min{min{a, b}, c} = min{b, c} = b = min{a, b}
= min{a, min{b, c}}.
If b > c, then
min{min{a, b}, c} = min{b, c} = c = min{a, c}
= min{a, min{b, c}}.
In either case,
min{min{a, b}, c} = min{a, min{b, c}}.
Therefore, for all a, b, c,
min{min{a, b}, c} = min{a, min{b, c}}.
In Exercises 6–9, only the Inductive Step is given.
6. [Section 2.4] 2 + 4 + · · · + 2n + 2(n + 1) = n(n + 1) +
2(n + 1) = (n + 1)(n + 2)
7. [Section 2.4]
22 + 42 + · · · + (2n)2 + [2(n + 1)]2 = 2n(n + 1)(2n + 1)
3
+ [2(n + 1)]2 = 2(n + 1)(n + 2)[2(n + 1) + 1]
3
8. [Section 2.4]
1
2! + 2
3! + · · · +
n
(n + 1)! +
n + 1
(n + 2)!
= 1 −
1
(n + 1)! +
n + 1
(n + 2)! = 1 −
1
(n + 2)!
9. [Section 2.4]
2n+2 = 2 ·2n+1 < 2[1 + (n + 1)2n] = 2 + (n + 1)2n+1
= 1 + [1 + (n + 1)2n+1]
< 1 + [2n+1 + (n + 1)2n+1]
= 1 + (n + 2)2n+1
10. [Section 2.1] Suppose that m and m−n are odd. Then there ex-
ist integers k1 and k2 such that m = 2k1+1 and m−n = 2k2+1.
Now
n = m −(m −n) = (2k1 + 1) −(2k2 + 1) = 2(k1 −k2).
Therefore n is even.
11. [Section 2.2] [(a) →(b)] We prove the contrapositive: If
A ∩B̸ = ∅, then A is not a subset of B. Since A ∩B̸ = ∅,
31.

<!-- pagina 18 -->
650
Hints and Solutions to Selected Exercises
there exists x with x ∈A and x ∈B. Thus there exists x with
x ∈A and x /∈B. Therefore A is not a subset of B.
[(b) →(c)] If x ∈B, then x ∈A ∪B. Therefore
B ⊆A ∪B.
Let x ∈A ∪B. We must show that x ∈B. Now x ∈A
or x ∈B. If x ∈B, this part of the proof is complete; so sup-
pose that x ∈A. Since A ∩B = ∅, x /∈B. Thus x ∈B and
A ∪B ⊆B. Therefore A ∪B = B.
[(c) →(a)] Let x ∈A. Then x ∈A ∪B. Since A ∪B =
B, x ∈B. Therefore A ⊆B.
12. [Section 2.1] We ﬁrst prove that X ⊆Z. Let x ∈X. Since
X ⊆Y, x ∈Y. Since Y ⊂Z, x ∈Z. Therefore X ⊆Z.
We now show that X is a proper subset of Z. Since
Y ⊂Z, there exists z ∈Z such that z /∈Y. Now z /∈X, because
if it were, we would have z ∈Y. Therefore X ⊂Z.
13. [Section 2.5] q = 9, r = 2
14. [Section 2.5] c2 = 2, c3 = 3, c4 = 8, c5 = 9.
15. [Section 2.5] Basis Step (n = 1)
c1 = 0 ≤0 = 1 lg 1
Inductive Step
cn = 2c⌊n/2⌋+ n
≤2⌊n/2⌋lg⌊n/2⌋+ n
≤2(n/2) lg(n/2) + n
= n(lg n −1) + n = n lg n
16. [Section 2.5] Let X be a nonempty set of nonnegative integers
that has an upper bound. We must show that X contains a
largest element.
Let Y be the set of integer upper bounds for X. By
assumption, Y is nonempty. Since X consists of nonnega-
tive integers, Y also consists of nonnegative integers. By the
Well-Ordering Property, Y has a least element, say n. Since
Y consists of upper bounds for X, k ≤n for every k in X.
Suppose, by way of contradiction, that n is not in X. Then
k ≤n −1 for every k in X. Thus, n −1 is an upper bound for
X, which is a contradiction. Therefore, n is in X. Since k ≤n
for every k in X, n is the largest element in X.
17. [Section 2.3]
(p ∨q) →r ≡¬(p ∨q) ∨r
≡¬p¬q ∨r
≡(¬p ∨r)(¬q ∨r)
18. [Section 2.3]
(p ∨¬q) →¬rs ≡¬(p ∨¬q) ∨¬rs
≡¬pq ∨¬rs
≡(¬p ∨¬r)(¬p ∨s)(q ∨¬r)(q ∨s)
19. [Section 2.3]
1. ¬p ∨q
2. ¬q ∨¬r
3. p ∨¬r
4. ¬p ∨¬r
From 1 and 2
5. ¬r
From 3 and 4
20. [Section 2.3]
1. ¬p ∨q
2. ¬q ∨¬r
3. p ∨¬r
4. r
Negation of conclusion
5. ¬p ∨¬r
From 1 and 2
6. ¬r
From 3 and 5
Now 4 and 6 give a contradiction.
Section 3.1 Review
1. Let X and Y be sets. A function f from X to Y is a subset of
the Cartesian product X ×Y having the property that for each
x ∈X, there is exactly one y ∈Y with (x, y) ∈f.
2. In an arrow diagram of the function f, there is an arrow from
i to j if (i, j) ∈f.
3. The graph of a function f, whose domain and codomain are
subsets of the real numbers, consists of the points in the plane
that correspond to the elements in f.
4. A set S of points in the plane deﬁnes a function when each
vertical line intersects at most one point of S.
5. The remainder when x is divided by y
6. A hash function takes a data item to be stored or retrieved
and computes the ﬁrst choice for a location for the item.
7. A collision occurs for a hash function H if H(x) = H(y) but
x̸ = y.
8. When a collision occurs, a collision resolution policy deter-
mines an alternative location for one of the data items.
9. Pseudorandom numbers are numbers that appear random
even though they are generated by a program.
10. A linear congruential random number generator uses a for-
mula of the form
xn = (axn−1 + c) mod m.
Given the pseudorandom number xn−1, the next pseudoran-
dom number xn is given by the formula. A “seed” is used as
the ﬁrst pseudorandom number in the sequence. As an exam-
ple, the formula
xn = (7xn−1 + 5) mod 11
with seed 3 gives a sequence that begins 3, 4, 0, 5, . . . .
11. The ﬂoor of x is the greatest integer less than or equal to x. It
is denoted ⌊x⌋.
12. The ceiling of x is the least integer greater than or equal to x.
It is denoted ⌈x⌉.
13. A function f from X to Y is said to be one-to-one if for each
y ∈Y, there is at most one x ∈X with f(x) = y. The function
{(a, 1), (b, 3), (c, 0)} is one-to-one. If a function from X to
Y is one-to-one, each element in Y in its arrow diagram will
have at most one arrow pointing to it.
14. A function f from X to Y is said to be onto Y if the range of f
is Y. The function {(a, 1), (b, 3), (c, 0)} is onto {0, 1, 3}. If a

<!-- pagina 19 -->
Hints and Solutions to Selected Exercises
651
function from X to Y is onto Y, each element in Y in its arrow
diagram will have at least one arrow pointing to it.
15. A bijection is a function that is one-to-one and onto. The
function of Exercises 13 and 14 is one-to-one and onto
{0, 1, 3}.
16. If f is a one-to-one, onto function from X to Y, the inverse
function is
f −1 = {(y, x) | (x, y) ∈f}.
If f is the function of Exercises 13 and 14, we have
f −1 = {(1, a), (3, b), (0, c)}.
Given the arrow diagram for a one-to-one, onto function f
from X to Y, we can obtain the arrow diagram for f −1 by
reversing the direction of each arrow.
17. Suppose that g is a function from X to Y and f is a function
from Y to Z. The composition function from X to Z is de-
ﬁned as
f ◦g = {(x, z) | (x, y) ∈g and (y, z) ∈f for some y ∈Y}.
If g = {(1, 2), (2, 2)} and f = {(2, a)}, f ◦g = {(1, a),
(2, a)}. Given the arrow diagrams for functions g from X to
Y and f from Y to Z, we can obtain the arrow diagram of f ◦g
by drawing an arrow from x ∈X to z ∈Z provided that there
are arrows from x to some y ∈Y and from y to z.
18. A binary operator on X is a function from X × X to X. The
addition operator + is a binary operator on the set of integers.
19. A unary operator on X is a function from X to X. The minus
operator −is a unary operator on the set of integers.
Section 3.1
1. Valid
4. Invalid. The check digit should be 5.
7. When 82 is transposed to 28, the sum becomes
8+6+9+0+6+5+4+8+2+3+5+5+8+6+1 = 76
and the check digit becomes 4.
8. It is a function from X to Y; domain = X, range = {a, b, c};
it is neither one-to-one nor onto. Its arrow diagram is
X
Y
a
b
c
d
1
2
3
4
11. It is not a function (from X to Y).
13.
1
…
…
21
1
2
)
)
)
)
)
)
16.
…
…
[ )
)
[ )
[ )
[ )
)
[ )
[ )
22
21
1
2
2
1
21
17. The function f is both one-to-one and onto. To prove that f is
one-to-one, suppose that f(n) = f(m). Then n + 1 = m + 1.
Thus n = m. Therefore f is one-to-one.
To prove that f is onto, let m be an integer. Then
f(m −1) = (m −1) + 1 = m. Therefore f is onto.
20. The function f is neither one-to-one nor onto. Since f(−1) =
| −1| = 1 = f(1), f is not one-to-one. Since f(n) ≥0 for
all n ∈Z, f(n)̸ = −1 for all n ∈Z. Therefore f is not
onto.
23. The function f is not one-to-one, but it is onto. Since
f(2, 1) = 2 −1 = 1 = 3 −2 = f(3, 2), f is not one-to-one.
Suppose that k ∈Z. Then f(k, 0) = k −0 = k. Therefore f
is onto.
26. The function f is neither one-to-one nor onto. Since f(2, 1) =
22 + 12 = 12 + 22 = f(1, 2), f is not one-to-one. Since
f(m, n) ≥0 for all m, n ∈Z, f(m, n)̸ = −1 for all m, n ∈Z.
Therefore f is not onto.
29. Suppose that f(a, b) = f(c, d). Then 2a3b = 2c3d. We claim
that a = c. If not, either a > c or a < c. We assume that
a > c. (The argument is the same if a < c.) We may then can-
cel 2c from both sides of 2a3b = 2c3d to obtain 2a−c3b = 3d.
Since a −c > 0, 2a−c3b is even. Since 3d is odd, we have a
contradiction. Therefore a = c.
We may now cancel 2a from both sides of 2a3b = 2c3d
to obtain 3b = 3d. An argument like that in the preceding
paragraph shows that b = d. Since a = c and b = d, f is
one-to-one.
Since f(m, n)̸ = 5 for all m, n ∈Z+, f is not onto.
[Note that f(m, n) ≥6 for all m, n ∈Z+.]
30. f is both one-to-one and onto.
33. f is both one-to-one and onto.
36. Deﬁne a function f from {1, 2, 3, 4} to {a, b, c, d, e} as
f = {(1, a), (2, c), (3, b), (4, d)}.
Then f is one-to-one, but not onto.
39. ∀x1∀x2((f(x1) = f(x2)) →(x1 = x2))
42. ¬(∀y ∈Y∃x ∈X(f(x) = y)) ≡∃y ∈Y¬(∃x ∈X(f(x) = y))
≡∃y ∈Y ∀x ∈X¬(f(x) = y)
≡∃y ∈Y ∀x ∈X(f(x)̸ = y)
43. f −1(y) = (y −2)/4
46. f −1(y) = 1/(y −3)
49. f ◦g = {(1, x), (2, z), (3, x)}

<!-- pagina 20 -->
652
Hints and Solutions to Selected Exercises
1
2
3
w
x
y
z
f   g
X
Z
52. (f ◦f)(x) = 2⌊2x⌋, (g ◦g)(x) = x4, (f ◦g)(x) = ⌊2x2⌋,
(g ◦f)(x) = ⌊2x⌋2
54. Let g(x) = log2 x and h(x) = x2 + 2. Then f(x) = (g ◦h)(x).
57. Let g(x) = 2x and h(x) = sin x. Then f(x) = (g ◦h)(x).
60. f = {(−5, 25), (−4, 16), (−3, 9), (−2, 4), (−1, 1), (0, 0),
(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)}. f is neither one-to-one
nor onto. We omit the arrow diagram of f.
63. f = {(0, 0), (1, 4), (2, 3), (3, 2), (4, 1)}; f is one-to-one and
onto. The arrow diagram of f is
0
1
2
3
4
0
1
2
3
4
f 
X
X
66. The ISBN’s check digit is invalid. It should be 8.
69. Valid
72. If i is an untripled digit, i contributes the value i to the sum.
Thus if an untripled digit is changed, the sum will change
by an amount a satisfying 0 < |a| < 10. It follows that the
check digit will change. If a tripled digit is changed, the fol-
lowing table shows that the sum mod 10 will again change
by an amount a satisfying 0 < |a| < 10:
Digit
Digit Times 3
Contribution to Sum mod 10
0
0
0
1
3
3
2
6
6
3
9
9
4
12
2
5
15
5
6
18
8
7
21
1
8
24
4
9
27
7
Again, the check digit will change.
In the solutions to Exercises 73 and 76, a : b means “store item a
in cell b.”
73. 53 : 9, 13 : 2, 281 : 6, 743 : 7, 377 : 3, 20 : 10, 10 : 0,
796 : 4
76. 714 : 0, 631 : 6, 26 : 5, 373 : 1, 775 : 8, 906 : 13,
509 : 2, 2032 : 7, 42 : 4, 4 : 3, 136 : 9, 1028 : 10
79. During a search, if we stop the search at an empty cell, we
may not ﬁnd the item even if it is present. The cell may be
empty because an item was deleted. One solution is to mark
deleted cells and consider them nonempty during a search.
80. False. Take g = {(1, a), (2, b)} and f = {(a, z), (b, z)}.
83. True. Let z ∈Z. Since f is onto, there exists y ∈Y such
that f(y) = z. Since g is onto, there exists x ∈X such that
g(x) = y. Now f(g(x)) = f(y) = z. Therefore f ◦g is onto.
86. True. Suppose that g(x1) = g(x2). Then f(g(x1)) = f(g(x2)).
Since f ◦g is one-to-one, x1 = x2. Therefore, g is one-to-one.
88. g(S) = {a}, g(T) = {a, c}, g−1(U) = {1}, g−1(V) =
{1, 2, 3}
93. No. Let f(x) = x and g(x) = x2. Then
E1(f) = f(1) = 1 = g(1) = E1(g).
96. 101
99. Suppose that S(Y1) = s1s2s3 = S(Y2). Now a ∈Y1 if and
only if s1 = 1 if and only if a ∈Y2. Also b ∈Y1 if and only
if s2 = 1 if and only if b ∈Y2. Also c ∈Y1 if and only if
s3 = 1 if and only if c ∈Y2. It follows that Y1 = Y2 and S is
one-to-one.
101. If x ∈X ∩Y, CX ∩Y(x) = 1 = 1 · 1 = CX(x)CY(x). If x /∈
X ∩Y, then CX∩Y(x) = 0. Since either x /∈X or x /∈Y, either
CX(x) = 0 or CY(x) = 0. Thus CX(x)CY(x) = 0 = CX∩Y(x).
104. If x ∈X −Y, then
CX−Y(x) = 1 = 1 ·[1 −0] = CX(x)[1 −CY(x)].
If x /∈X −Y, then either x /∈X or x ∈Y. In case x /∈X,
CX−Y(x) = 0 = 0 ·[1 −CY(x)] = CX(x)[1 −CY(x)].
In case x ∈Y,
CX−Y(x) = 0 = CX(x)[1 −1] = CX(x)[1 −CY(x)].
Thus the equation holds for all x ∈U.
107. f is onto by deﬁnition. Suppose that f(X) = f(Y). Then
CX(x) = CY(x), for all x ∈U. Suppose that x ∈X. Then
CX(x) = 1. Thus CY(x) = 1. Therefore, x ∈Y. This argu-
ment shows that X ⊆Y. Similarly, Y ⊆X. Therefore X = Y
and f is one-to-one.
109. f is a commutative, binary operator.
112. f is not a binary operator since f(x, 0) is not deﬁned.
114. g(x) = −x
117. The statement is true. The least integer greater than or equal
to x is the unique integer k satisfying
k −1 < x ≤k.
Now
k + 2 < x + 3 ≤k + 3.
Thus, k + 3 is the least integer greater than or equal to x + 3.
Therefore, k + 3 = ⌈x + 3⌉. Since k = ⌈x⌉, we have
⌈x + 3⌉= k + 3 = ⌈x⌉+ 3.

<!-- pagina 21 -->
Hints and Solutions to Selected Exercises
653
120. If n is an odd integer, n = 2k + 1 for some integer k. Now
n2
4 = (2k + 1)2
4
= 4k2 + 4k + 1
4
= k2 + k + 1
4.
Since k2 + k is an integer,
'n2
4
(
= k2 + k.
The result now follows because
%n −1
2
& %n + 1
2
&
=
#(2k + 1) −1
2
$ #(2k + 1) + 1
2
$
= 2k(2k + 2)
4
= 4k2 + 4k
4
= k2 + k.
123. Let k = ⌈x⌉. Then k −1 < x ≤k and 2x ≤2k. Thus
⌈2x⌉≤2k = 2⌈x⌉. Now ⌈x⌉= k < x + 1. Therefore
2⌈x⌉< 2x + 2 ≤⌈2x⌉+ 2, so 2⌈x⌉−2 < ⌈2x⌉. Therefore
2⌈x⌉−1 ≤⌈2x⌉.
126. April, July
Section 3.2 Review
1. A sequence is a function in which the domain is a subset of
integers.
2. If sn denotes element n of the sequence, we call n the index
of the sequence.
3. A sequence s is increasing if for all i and j in the domain of
s, if i < j, then si < sj.
4. A sequence s is decreasing if for all i and j in the domain of
s, if i < j, then si > sj.
5. A sequence s is nonincreasing if for all i and j in the domain
of s, if i < j, then si ≥sj.
6. A sequence s is nondecreasing if for all i and j in the domain
of s, if i < j, then si ≤sj.
7. Let {sn} be a sequence deﬁned for n = m, m + 1, . . . , and let
n1, n2, . . . be an increasing sequence whose values are in the
set {m, m+1, . . .}. We call the sequence {snk} a subsequence
of {sn}.
8. am + am+1 + · · · + an
9. amam+1 · · · an
10. A string over X is a ﬁnite sequence of elements from X.
11. The null string is the string with no elements.
12. X∗is the set of all strings over X.
13. X+ is the set of all nonnull strings over X.
14. The length of a string α is the number of elements in α. It is
denoted |α|.
15. The concatenation of strings α and β is the string consisting
of α followed by β. It is denoted αβ.
16. A string β is a substring of the string α if there are strings γ
and δ with α = γβδ.
Section 3.2
1. c
2. c
3. cddcdc
5. Increasing, decreasing, nonincreasing, nondecreasing
8. None of (a)–(d)
31. 52
32. 52
33. No
34. No
35. No
36. Yes
45. 12
46. 23
47. 7
48. 46
49. 1
50. 3
51. 3
52. 21
53. No
54. No
55. No
56. Yes
73. 15
74. 155
75. 2n + 3(n −1)n/2
76. Yes
77. No
78. No
79. Yes
88. 2/9
91. z4 = a3 + a4 = 2/9 + 3/64 = 155/576
94. Yes. We must show that
an =
n −1
n2(n −2)2 >
n
(n + 1)2(n −1)2 = an+1
for all n ≥3.
The preceding inequality is equivalent, successively, to
(n −1)2(n + 1)2(n −1) > n3(n −2)2
(n2 −1)2(n −1) > n3(n −2)2
(n4 −2n2 + 1)(n −1) > n3(n2 −4n + 4)
3n4 + 2n2 + n −1 > 6n3.
Since 3n4 > 6n3 and 2n2 + n −1 > 0 for all n > 3,
3n4 + 2n2 + n −1 > 3n4 > 6n3
for all n > 3.
By plugging in n = 3 into the inequality 3n4 +2n2 +n−1 >
6n3, we can verify that the inequality also holds for n = 3.
Thus
3n4 + 2n2 + n −1 > 6n3
for all n ≥3
and hence the equivalent inequality an > an+1 also holds for
all n ≥3. Therefore a is decreasing.
97. Since ai > 0 for all i, zn+1 > zn for all n. Thus z is increasing.
100. Yes, z is nondecreasing. See the solution to Exercise 97.
101. We have n < 4n and n ·4n is a perfect square.
105. Since 6 = 2 ·3, the a-sequence must contain a multiple of 3.
The smallest multiple of 3 that can contribute to a perfect
square is 4 ·3 = 12. Since 6 < 8 < 12 and 6 ·8 ·12 is a
perfect square, s6 = 12.
109. 1, 3, 5, 7, 9, 11, 13
110. 1, 5, 9, 13, 17, 21, 25
111. nk = 2k −1
112. snk = 4k −3
117. 88
118. 1140
119. 48
120. 3168

<!-- pagina 22 -->
654
Hints and Solutions to Selected Exercises
137. b1 = 1, b2 = 2, b3 = 3, b4 = 4, b5 = 5, b6 = 126
140. Let s0 = 0. Then
n
)
k=1
akbk =
n
)
k=1
(sk −sk−1)bk
=
n
)
k=1
skbk −
n
)
k=1
sk−1bk
=
n
)
k=1
skbk −
n
)
k=1
skbk+1 + snbn+1
=
n
)
k=1
sk(bk −bk+1) + snbn+1.
143. 00, 01, 10, 11
146. 000, 010, 001, 011, 100, 110, 101, 111, 00, 01, 11, 10, 0,
1, λ
149. Basis Step (n = 1)
In this case, {1} is the only nonempty
subset of {1}, so the sum is
1
1 = 1 = n.
Inductive Step
Assume that the statement is true for n. We
divide the subsets of
{1, . . . , n, n + 1}
into two classes:
C1 = class of nonempty subsets that do not contain n + 1
C2 = class of subsets that contain n + 1.
By the inductive assumption,
)
C1
1
n1 · · · nk
= n.
Since a set in C2 consists of n + 1 together with a subset
(empty or nonempty) of {1, . . . , n},
)
C2
1
(n + 1)n1 · · · nk
=
1
n + 1 +
1
n + 1
)
C1
1
n1 · · · nk
.
[The term 1/(n + 1) results from the subset {n + 1}.] By the
inductive assumption,
1
n + 1 +
1
n + 1
)
C1
1
n1 · · · nk
=
1
n + 1 +
1
n + 1 ·n = 1.
Therefore,
)
C2
1
(n + 1)n1 · · · nk
= 1.
Finally,
)
C1∪C2
1
n1 · · · nk
=
)
C1
1
n1 · · · nk
+
)
C2
1
(n + 1)n1 · · · nk
= n+1.
151. Since x1 ≤x ≤xn, |x −x1| = x −x1 and |x −xn| = xn −x.
Thus
n
)
i=1
|x −xi| = |x −x1| +
n−1
)
i=2
|x −xi| + |x −xn|
= (x −x1) +
n−1
)
i=2
|x −xi| + (xn −x)
=
n−1
)
i=2
|x −xi| + (xn −x1).
154. Using Exercise 4, Section 2.4, we have
n
)
i=1
n
)
j=1
(i −j)2 =
n
)
i=1
n
)
j=1
(i2 −2ij + j2)
=
n
)
i=1
n
)
j=1
i2 −2
n
)
i=1
n
)
j=1
ij +
n
)
i=1
n
)
j=1
j2
=
n
)
j=1
n
)
i=1
i2 −2
n
)
i=1
i
n
)
j=1
j +
n
)
i=1
n
)
j=1
j2
=
n
)
j=1
n(n + 1)(2n + 1)
6
−2
#n(n + 1)
2
$2
+
n
)
i=1
n(n + 1)(2n + 1)
6
= n
#n(n + 1)(2n + 1)
6
$
−n2(n + 1)2
2
+ n
#n(n + 1)(2n + 1)
6
$
= 2n
#n(n + 1)(2n + 1)
6
$
−n2(n + 1)2
2
= n2(n + 1)[2(2n + 1) −3(n + 1)]
6
= n2(n + 1)[n −1]
6
= n2(n2 −1)
6
.
155. The function f is one-to-one. Suppose that f(α) = f(β). Then
αab = βab. Thus α = β.
The function f is not onto. Since |f(α)| ≥2 for all
α ∈X∗, f(α)̸ = λ for all α ∈X∗.
158. Let α = λ. Then α ∈L and the ﬁrst rule states that ab = aαb ∈
L. Now β = ab ∈L and the ﬁrst rule states that aabb = aβb ∈
L. Now γ = aabb
∈
L and the ﬁrst rule states that
aaabbb = aγ b ∈L.
161. We use strong induction on the length n of α to show that if
α ∈L, α has an equal number of a’s and b’s.
The Basis Step is n = 0. In this case, α is the null
string, which has an equal number of a’s and b’s.
We turn now to the Inductive Step. We assume any
string in L of length k < n has an equal number of a’s and
b’s. We must show that any string in L of length n has an
equal number of a’s and b’s. Let α ∈L and suppose that
|α| = n > 0. Now α is in L because of either rule 1 or rule 2.
Suppose that α is in L because of rule 1. In this case,
α = aβb or α = bβa, where β ∈L. Since |β| < n, by the

<!-- pagina 23 -->
Hints and Solutions to Selected Exercises
655
inductive hypothesis β has an equal number of a’s and b’s.
Since α = aβb or α = bβa, α also has an equal number of
a’s and b’s.
Suppose that α is in L because of rule 2. In this case,
α = βγ , where β ∈L and γ ∈L. Since |β| < n and |γ | < n,
by the inductive hypothesis β and γ each have equal numbers
of a’s and b’s. Since α = βγ , α also has an equal number of
a’s and b’s. The proof by induction is complete.
Section 3.3 Review
1. A binary relation from a set X to a set Y is a subset of the
Cartesian product X × Y.
2. In a digraph of a relation on X, vertices represent the elements
of X and directed edges from x to y represent the elements
(x, y) in the relation.
3. A relation R on a set X is reﬂexive if (x, x) ∈R for ev-
ery x ∈X. The relation {(1, 1), (2, 2)} is a reﬂexive relation
on {1, 2}. The relation {(1, 1)} is not a reﬂexive relation on
{1, 2}.
4. A relation R on a set X is symmetric if for all x, y ∈X, if
(x, y) ∈R, then (y, x) ∈R. The relation {(1, 2), (2, 1)} is
a symmetric relation on {1, 2}. The relation {(1, 2)} is not a
symmetric relation on {1, 2}.
5. A relation R on a set X is antisymmetric if for all x, y ∈
X, if (x, y) ∈R and (y, x) ∈R, then x = y. The re-
lation {(1, 2)} is an antisymmetric relation on {1, 2}. The
relation {(1, 2), (2, 1)} is not an antisymmetric relation
on {1, 2}.
6. A relation R on a set X is transitive if for all x, y, z ∈X, if
(x, y) and (y, z) ∈R, then (x, z) ∈R. The relation {(1, 2),
(2, 3), (1, 3)} is a transitive relation on {1, 2, 3}. The relation
{(1, 2), (2, 1)} is not a transitive relation on {1, 2}.
7. A relation R on a set X is a partial order if R is reﬂexive,
antisymmetric, and transitive. The relation
{(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)}
is a partial order on {1, 2, 3}.
8. If R is a relation from X to Y, the inverse of R is the relation
from Y to X:
R−1 = {(y, x) | (x, y) ∈R}.
The inverse of the relation {(1, 2), (1, 3)} is {(2, 1), (3, 1)}.
9. Let R1 be a relation from X to Y and R2 be a relation from Y
to Z. The composition of R1 and R2 is the relation from X to
Z
R2 ◦R1 = {(x, z) | (x, y) ∈R1 and (y, z) ∈R2 for some y ∈Y}.
The composition of the relations
R1 = {(1, 2), (1, 3), (2, 2)}
and
R2 = {(2, 1), (2, 3), (1, 4)}
is
R2 ◦R1 = {(1, 1), (1, 3), (2, 1), (2, 3)}.
Section 3.3
1. {(8840, Hammer), (9921, Pliers), (452, Paint), (2207,
Carpet)}
4. {(a, a), (b, b)}
5.
a
6
b
2
a
1
c
1
8.
Mercury
1
Venus
2
Earth
3
Mars
4
Jupiter
5
Saturn
6
Uranus
7
Neptune
8
9.
a
b
c
12.
2
1
4
3
13. {(a, b), (a, c), (b, a), (b, d), (c, c), (c, d)}
16. {(b, c), (c, b), (d, d)}
17. (Exercise 1) {(Hammer, 8840), (Pliers, 9921), (Paint, 452),
(Carpet, 2207)}
18. {(1, 1), (1, 4), (2, 2), (2, 5), (3, 3), (4, 1), (4, 4), (5, 2),
(5, 5)}
20. R = R−1 = {(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2),
(2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (5, 1)}
23. Antisymmetric
24. Symmetric, antisymmetric, transitive
27. Antisymmetric
30. Reﬂexive, symmetric, antisymmetric, transitive, partial order
33. Antisymmetric

<!-- pagina 24 -->
656
Hints and Solutions to Selected Exercises
35. Reﬂexive, antisymmetric, transitive, partial order
38. Reﬂexive: Suppose that (x1, x2) is in X1 × X2. Since Ri is
reﬂexive, x1R1x1 and x2R2x2. Thus (x1, x2)R(x1, x2).
Antisymmetric: Suppose that (x1, x2)R(x′
1, x′
2) and
(x′
1, x′
2)R(x1, x2). Then x1R1x′
1 and x′
1R1x1. Since R1 is anti-
symmetric, x1 = x′
1. Similarly, x2 = x′
2. Therefore (x1, x2) =
(x′
1, x′
2) and R is antisymmetric.
Transitivity is proved similarly.
40. {(1, 1), (2, 2), (3, 3), (4, 4), (1, 2), (2, 3), (2, 1), (3, 2)}
43. {(1, 1), (1, 2), (2, 1), (2, 2)}
45. True. Let (x, y), (y, z) ∈R−1. Then (z, y), (y, x) ∈R. Since
R is transitive, (z, x) ∈R. Thus (x, z) ∈R−1. Therefore, R−1
is transitive.
48. True. We must show that (x, x) ∈R ◦S for all x ∈X. Let
x ∈X. Since R and S are reﬂexive, (x, x) ∈R and (x, x) ∈S.
Therefore, (x, x) ∈R ◦S and R ◦S is reﬂexive.
51. True. Let (x, y) ∈R∩S. Then (x, y) ∈R and (x, y) ∈S. Since
R and S are symmetric, (y, x) ∈R and (y, x) ∈S. Therefore,
(y, x) ∈R ∩S and R ∩S is symmetric.
54. False. Let R = {(1, 2)}, S = {(2, 1)}.
57. True. Suppose that (x, y), (y, x) ∈R−1. Then (y, x), (x, y) ∈
R. Since R is antisymmetric, y = x. Therefore R−1 is anti-
symmetric.
59. R is reﬂexive and symmetric. R is not antisymmetric, not tran-
sitive, and not a partial order.
Section 3.4 Review
1. An equivalence relation is a relation that is reﬂexive, sym-
metric, and transitive. The relation
{(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}
is an equivalence relation on {1, 2, 3}. The relation
{(1, 1), (3, 3), (1, 2), (2, 1)}
is not an equivalence relation on {1, 2, 3}.
2. Let R be an equivalence relation on X. The equivalence
classes of X given by R are sets of the form
{x ∈X | xRa},
where a ∈X.
3. If R is an equivalence relation on X, the equivalence classes
partition X. Conversely, if S is a partition of X and we deﬁne
xRy to mean that for some S ∈S, both x and y belong to S,
then R is an equivalence relation.
Section 3.4
1. Equivalence relation: [1] = [3] = {1, 3}, [2] = {2}, [4] =
{4}, [5] = {5}
4. Equivalence relation: [1] = [3] = [5] = {1, 3, 5}, [2] =
{2}, [4] = {4}
7. Not
an
equivalence
relation
(neither
transitive
nor
reﬂexive)
10. Equivalence relation: [1] = [3] = [5] = {1, 3, 5}, [2] =
[4] = {2, 4}
11. The relation is an equivalence relation.
14. The relation is not an equivalence relation. It is neither re-
ﬂexive nor symmetric.
17. {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (3, 4), (4, 3), (4, 4)},
[1] = [2] = {1, 2}, [3] = [4] = {3, 4}
20. {(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2),
(3, 3), (4, 4)},
[1] = [2] = [3] = {1, 2, 3}, [4] = {4}
24. {1}, {1, 3}, {1, 4}, {1, 3, 4}
26. [Part (b)]
{San Francisco, San Diego, Los Angeles}, {Pittsburgh,
Philadelphia}, {Chicago}
28. R = {(x, x) | x ∈X}
31. Suppose that x R y. Since R is reﬂexive, y R y. Taking z = y in
the given condition, we have y R x. Therefore R is symmetric.
Now suppose that x R y and y R z. The given condition
tells us that z R x. Since R is symmetric, x R z. Therefore R is
transitive. Since R is reﬂexive, symmetric, and transitive, R
is an equivalence relation.
34. [Part (b)]
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
(1, 8), (1, 9), (1, 10), (2, 1), (3, 1), (4, 1), (5, 1),
(6, 1), (7, 1), (8, 1), (9, 1), (10, 1)
37. (a) We show symmetry only. Let (x, y) ∈R1 ∩R2. Then
(x, y) ∈R1 and (x, y) ∈R2. Since R1 and R2 are sym-
metric, (y, x) ∈R1 and (y, x) ∈R2. Thus (y, x) ∈R1∩R2
and, therefore, R1 ∩R2 is symmetric.
(b) A is an equivalence class of R1 ∩R2 if and only if there
are equivalence classes A1 of R1 and A2 of R2 such that
A = A1 ∩A2.
40. [Part (b)] Torus
43. If x ∈X, then x ∈f −1(f({x})). Thus ∪{S | S ∈S} = X.
Suppose that
a ∈f −1({y}) ∩f −1({z})
for some y, z ∈Y. Then f(a) = y and f(a) = z. Thus y = z.
Therefore, S is a partition of X. The equivalence relation that
generates this partition is given in Exercise 41.
46. Suppose, by way of contradiction, that a ∈[b]. Then (a, b) ∈
R. Since R is symmetric, (b, a) ∈R. Since R is transitive,
(b, b) ∈R, which is a contradiction. Therefore [b] = ∅.
49. Since R is not transitive, there exist (a, b), (b, c) ∈R, but
(a, c) /∈R. Then a ∈[b], b ∈[c], and a /∈[c]. Since R is
reﬂexive, b ∈[b]. Therefore [b] ∩[c]̸ = ∅, but [b]̸ = [c].
Thus the collection of pseudo equivalence classes does not
partition X.
53. ρ(R1) = {(1, 1), (2, 2), (3, 3), (4, 4), (1, 2), (3, 4), (4, 2)}
σ(R1) = {(1, 1), (2, 1), (1, 2), (3, 4), (4, 3), (4, 2), (2, 4)}
τ(R1) = {(1, 1), (1, 2), (3, 4), (4, 2), (3, 2)}
τ(σ(ρ(R1))) = {(x, y) | x, y ∈{1, 2, 3, 4}}

<!-- pagina 25 -->
Hints and Solutions to Selected Exercises
657
56. Let (x, y), (x, z) ∈τ(R). Then (x, y) ∈Rm and (y, z) ∈Rn.
Thus (x, z) ∈Rm+n. Therefore, (x, z) ∈τ(R) and τ(R) is
transitive.
59. Suppose that R is transitive. If (x, y) ∈τ(R) = ∪{Rn}, then
there exist x = x0, . . . , xn = y ∈X such that (xi−1, xi) ∈R
for i = 1, . . . , n. Since R is transitive, it follows that (x, y) ∈
R. Thus R ⊇τ(R). Since we always have R ⊆τ(R), it fol-
lows that R = τ(R).
Suppose that τ(R) = R. By Exercise 56, τ(R) is tran-
sitive. Therefore, R is transitive.
60. True. Let D = {(x, x) | x ∈X}. Then, by deﬁnition, ρ(R) =
R ∪D, where R is any relation on X. Now
ρ(R1 ∪R2) = (R1 ∪R2) ∪D = (R1 ∪D) ∪(R2 ∪D)
= ρ(R1) ∪ρ(R2).
63. False. Let R1 = {(1, 2), (2, 3)}, R2 = {(1, 3), (3, 4)}.
66. True. Using the notation and hint for Exercise 60,
ρ(τ(R1)) = τ(R1) ∪D
and
τ(ρ(R1)) = τ(R1 ∪D).
So we must show that τ(R1) ∪D = τ(R1 ∪D).
We ﬁrst note that if A ⊆B, then τ(A) ⊆τ(B).
Now R1 ⊆R1 ∪D. Therefore, τ(R1) ⊆τ(R1 ∪D). Also,
D ⊆R1 ∪D. Therefore, D = τ(D) ⊆τ(R1 ∪D). It follows
that τ(R1) ∪D ⊆τ(R1 ∪D).
Since R1 ⊆τ(R1), R1∪D ⊆τ(R1)∪D. By the note in
the preceding paragraph, we have τ(R1∪D) ⊆τ(τ(R1)∪D).
Since τ(R1) ∪D is transitive, τ(τ(R1) ∪D) = τ(R1) ∪D
(Exercise 59). Therefore, τ(R1 ∪D) ⊆τ(R1) ∪D.
67. A set is equivalent to itself by the identity function.
If X is equivalent to Y, there is a one-to-one, onto func-
tion f from X to Y. Now f −1 is a one-to-one, onto function
from Y to X.
If X is equivalent to Y, there is a one-to-one, onto func-
tion f from X to Y. If Y is equivalent to Z, there is a one-to-
one, onto function g from Y to Z. Now g ◦f is a one-to-one,
onto function from X to Z.
Section 3.5 Review
1. To obtain the matrix of a relation from X to Y, we label the
rows with the elements of X and the columns with the ele-
ments of Y. We then set the entry in row x and column y to 1
if xRy and to 0 otherwise.
2. A relation is reﬂexive if and only if its matrix has 1’s on the
main diagonal.
3. A relation is symmetric if and only if its matrix A satisﬁes the
following: For all i and j, the ijth entry of A is equal to the
jith entry of A.
4. See the paragraph following the proof of Theorem 3.5.6.
5. The matrix of the relation R2 ◦R1 is obtained by replacing
each nonzero term in A1A2 by 1.
Section 3.5
1.
⎛
⎝
α
β
+
δ
1
0
0
0
1
2
1
0
1
0
3
0
1
1
0
⎞
⎠
4.
⎛
⎜
⎜
⎜
⎜
⎝
1
2
3
4
5
1
0
1
0
0
0
2
0
0
1
0
0
3
0
0
0
1
0
4
0
0
0
0
1
5
0
0
0
0
0
⎞
⎟
⎟
⎟
⎟
⎠
8. R = {(a, w), (a, y), (c, y), (d, w), (d, x), (d, y), (d, z)}
11. The test is, whenever the ijth entry is 1, i̸ = j, then the jith
entry is not 1.
14. (For Exercise 8)
⎛
⎜
⎜
⎝
a
b
c
d
w
1
0
0
1
x
0
0
0
1
y
1
0
1
1
z
0
0
0
1
⎞
⎟
⎟
⎠
16. (a) A1 =
⎛
⎝
1
1
1
0
1
0
⎞
⎠
(b) A2 =
% 0
1
0
1
1
1
&
(c) A1A2 =
⎛
⎝
1
2
1
0
1
0
0
1
0
⎞
⎠
(d) We change each nonzero entry in part (c) to 1 to obtain
A1A2 =
⎛
⎝
1
1
1
0
1
0
0
1
0
⎞
⎠.
(e) {(1, b), (1, a), (1, c), (2, b), (3, b)}
19. Each column that contains 1 in row x corresponds to an ele-
ment of the equivalence class containing x.
21. Suppose that the ijth entry of A is 1. Then the ijth entry of
either A1 or A2 is 1. Thus either (i, j) ∈R1 or (i, j) ∈R2.
Therefore, (i, j) ∈R1 ∪R2. Now suppose that (i, j) ∈
R1 ∪R2. Then the ijth entry of either A1 or A2 is 1. There-
fore, the ijth entry of A is 1. It follows that A is the matrix of
R1 ∪R2.
25. Each row must contain exactly one 1 for the relation to be a
function.
Section 3.6 Review
1. An n-ary relation is a set of n-tuples.
2. A database management system is a program that helps users
access information in a database.
3. A relational database represents data as tables and provides
ways to manipulate the tables.

<!-- pagina 26 -->
658
Hints and Solutions to Selected Exercises
4. A single attribute or combination of attributes for a relation is
a key if the values of the attributes uniquely deﬁne an n-tuple.
5. A query is a request for information from a database.
6. The selection operator chooses certain n-tuples from a rela-
tion. The choices are made by giving conditions on the at-
tributes (see Example 3.6.3).
7. The project operator chooses speciﬁed columns from a re-
lation. In addition, duplicates are eliminated (see Example
3.6.4).
8. The join operation on relations R1 and R2 begins by examin-
ing all pairs of tuples, one from R1 and one from R2. If the
join condition is satisﬁed, the tuples are combined to form
a new tuple. The join condition speciﬁes a relationship be-
tween an attribute in R1 and an attribute in R2 (see Example
3.6.5).
Section 3.6
1. {(1089, Suzuki, Zamora), (5620, Kaminski, Jones), (9354,
Jones, Yu), (9551, Ryan, Washington), (3600, Beaulieu, Yu),
(0285, Schmidt, Jones), (6684, Manacotti, Jones)}
5. EMPLOYEE [Name]
Suzuki, Kaminski, Jones, Ryan, Beaulieu,
Schmidt, Manacotti
8. BUYER [Name]
United Supplies, ABC Unlimited, JCN Electronics,
Danny’s, Underhanded Sales, DePaul University
11. TEMP := BUYER [Part No = 20A8]
TEMP [Name]
Underhanded Sales, Danny’s, ABC Unlimited
14. TEMP1 := BUYER [Name = Danny’s]
TEMP2 := TEMP1 [Part No = Part No] SUPPLIER
TEMP2 [Dept]
04, 96
17. TEMP1 := BUYER [Name = JCN Electronics]
TEMP2 := TEMP1 [Part No = Part No] SUPPLIER
TEMP3 := TEMP2 [Dept = Dept] DEPARTMENT
TEMP4 := TEMP3 [Manager = Manager] EMPLOYEE
TEMP4 [Name]
Kaminski, Schmidt, Manacotti
22. Let R1 and R2 be two n-ary relations. Suppose that the set of
elements in the ith column of R1 and the set of elements in
the ith column of R2 come from a common domain for i =
1, . . . , n. The union of R1 and R2 is the n-ary relation R1∪R2.
TEMP1 := DEPARTMENT [Dept = 23]
TEMP2 := DEPARTMENT [Dept = 96]
TEMP3 := TEMP1 union TEMP2
TEMP4 := TEMP3 [Manager = Manager] EMPLOYEE
TEMP4 [Name]
Kaminski, Schmidt, Manacotti, Suzuki
Chapter 3 Self-Test
1. [Section 3.1] f is not one-to-one. f is onto.
2. [Section 3.2]
(a) b5 = 35, b10 = 120
(b) (n + 1)2 −1
(c) Yes
(d) No
3. [Section 3.3] Reﬂexive, symmetric, transitive
4. [Section 3.3] Symmetric
5. [Section 3.4] Yes. It is reﬂexive, symmetric, and transitive.
6. [Section 3.4] [3] = {3, 4}. There are two equivalence classes.
7. [Section 3.1] x = y = 2.3
8. [Section 3.2]
(a) 14
(b) 18
(c) 192
(d) ank = 4k
9. [Section 3.1] Deﬁne f from X = {1, 2} to {3} by f(1) =
f(2) = 3. Deﬁne g from {1} to X by g(1) = 1.
10. [Section 3.2]
(a) ccddccccdd
(b) cccddccddc
(c) 5
(d) 20
11. [Section 3.1] (a : b means “store item a in cell b.”) 1 : 1,
784 : 4, 18 : 5, 329 : 6, 43 : 7, 281 : 8, 620 : 9, 1141 : 10,
31 : 11, 684 : 12
12. [Section 3.4] {(a, a), (b, b), (b, d), (b, e), (d, b), (d, d), (d, e),
(e, b), (e, d), (e, e), (c, c)}
13. [Section 3.3] All counterexample relations are on {1, 2, 3}.
(a) False. R = {(1, 1)}.
(b) True
(c) True
(d) False. R = {(1, 1)}.
14. [Section 3.2]
n−2
)
k=−1
(n −k −2)rk+2
15. [Section 3.3] R = {(1, 1), (2, 2), (3, 3), (4, 4), (1, 2), (2, 1),
(2, 3)}
16. [Section 3.4]
(a) R is reﬂexive because any eight-bit string has the same
number of zeros as itself.
R is symmetric because, if s1 and s2 have the same
number of zeros, then s2 and s1 have the same number
of zeros.
To see that R is transitive, suppose that s1 and s2
have the same number of zeros and that s2 and s3 have
the same number of zeros. Then s1 and s3 have the same
number of zeros. Therefore, R is an equivalence relation.
(b) There are nine equivalence classes.

<!-- pagina 27 -->
Hints and Solutions to Selected Exercises
659
(c) 11111111, 01111111, 00111111, 00011111, 00001111,
00000111, 00000011, 00000001, 00000000
17. [Section 3.5]
⎛
⎝
1 0
1 1
0 1
⎞
⎠
18. [Section 3.5]
%1 1 0
1 0 1
&
19. [Section 3.5]
⎛
⎝
1 1 0
2 1 1
1 0 1
⎞
⎠
20. [Section 3.5]
⎛
⎝
1 1 0
1 1 1
1 0 1
⎞
⎠
21. [Section 3.6]
ASSIGNMENT [Team]
Blue Sox, Mutts, Jackalopes
22. [Section 3.6]
PLAYER [Name, Age]
Johnsonbaugh, 22; Glover, 24; Battey, 18; Cage, 30;
Homer, 37; Score, 22; Johnsonbaugh, 30; Singleton, 31
23. [Section 3.6]
TEMP1 := PLAYER [Position = p]
TEMP2 := TEMP1 [ID Number = PID] ASSIGNMENT
TEMP2 [Team]
Mutts, Jackalopes
24. [Section 3.6]
TEMP1 := PLAYER [Age ≥30]
TEMP2 := TEMP1 [ID Number = PID] ASSIGNMENT
TEMP2 [Team]
Blue Sox, Mutts
Section 4.1 Review
1. An algorithm is a step-by-step method of solving a problem.
2. Input—the algorithm receives input. Output—the algorithm
produces output. Precision—the steps are precisely stated.
Determinism—the intermediate results of each step of execu-
tion are unique and are determined only by the inputs and the
results of the preceding steps. Finiteness—the algorithm ter-
minates; that is, it stops after ﬁnitely many instructions have
been executed. Correctness—the output produced by the al-
gorithm is correct; that is, the algorithm correctly solves the
problem. Generality—the algorithm applies to a set of inputs.
3. A trace of an algorithm is a simulation of execution of the
algorithm.
4. The advantages of pseudocode over ordinary text are that
pseudocode has more precision, structure, and universality. It
is often readily converted to computer code.
5. An algorithm is made up of one or more pseudocode
functions.
Section 4.1
3. The algorithm does not receive input (but, logically, it needs
none). If some even number greater than 2 is not the sum of
two prime numbers, the algorithm will stop and output “no”.
If every even number greater than 2 is the sum of two prime
numbers, lines 2 and 3 become an inﬁnite loop—in this case,
the algorithm will not terminate and, therefore, will not pro-
duce output. The algorithm lacks precision; in order to execute
line 2, we need to know how to check whether n is the sum of
two primes. The algorithm does have the determinism prop-
erty. The algorithm may lack the ﬁniteness property. We have
already noted that if every even number greater than 2 is the
sum of two prime numbers (which is currently unsettled), the
algorithm will not terminate. The algorithm is not general; that
is, it does not apply to a set of inputs. Rather, it applies to one
set of inputs—namely, the empty set.
6.
Input:
s, n
Output:
small, the smallest value in the sequence s
min(s, n) {
small = s1
for i = 2 to n
if (si < small) // smaller value found
small = si
return small
}
9.
Input:
s, n
Output:
small (smallest), large (largest)
small large(s, n, small, large) {
small = large = s1
for i = 2 to n {
if (si < small)
small = si
if (si > large)
large = si
}
}
12.
Input:
s, n
Output:
sum
seq sum(s, n) {
sum = 0
for i = 1 to n
sum = sum + si
return sum
}
15.
Input:
s, n
Output:
s (in reverse)
reverse(s, n) {
i = 1
j = n
while (i < j) {

<!-- pagina 28 -->
660
Hints and Solutions to Selected Exercises
swap(si, sj)
i = i + 1
j = j −1
}
}
18.
Input:
A (an n × n matrix of a relation R), n
Output:
true, if R is reﬂexive; false, if R is not reﬂexive
is reﬂexive(A, n) {
for i = 1 to n
if (Aii == 0)
return false
return true
}
21.
Input:
A (an n × n matrix of a relation R), n
Output:
true, if R is antisymmetric; false, if R is not
antisymmetric
is reﬂexive(A, n) {
for i = 1 to n −1
for j = i + 1 to n
if (Aij == 1 ∧Aji == 1)
return false
return true
}
24.
Input:
A (an m×k matrix of a relation R1), B (a k×n matrix
of a relation R2), m, k, n
Output:
C (the m × n matrix of the relation R2 ◦R1)
comp relation(A, B, m, k, n, C) {
// ﬁrst compute the matrix product AB
for i = 1 to m
for j = 1 to n {
Cij = 0
for t = 1 to k
Cij = Cij + Ait Btj
}
// replace each nonzero entry in C by 1
for i = 1 to m
for j = 1 to n
if (Cij > 0)
Cij = 1
}
Section 4.2 Review
1. Finding web pages containing key words is a searching prob-
lem. The programs that perform the search are called search
engines. Finding medical records in a hospital is another
searching problem. Such a search may be carried out by peo-
ple or by a computer.
2. We are given text t and we want to ﬁnd the ﬁrst occurrence of
pattern p in t or determine that p does not occur in t.
3. We use the notation in the solution to Exercise 2. Determine
whether p is in t starting at index 1 in t. If so, stop. Otherwise,
determine whether p is in t starting at index 2 in t. If so, stop.
Continue in this way until ﬁnding p in t or determining that
p cannot be in t. In the latter case, the search can be termi-
nated when the index in t is so large that there are not enough
characters remaining in t to accommodate p.
4. Sorting a sequence s means to rearrange the data so that s is in
order (nonincreasing order or nondecreasing order).
5. The entries in a book’s index are sorted in increasing order,
thus making it easy to quickly locate an entry in the index.
6. To sort s1, . . . , sn using insertion sort, ﬁrst insert s2 in s1 so
that s1, s2 is sorted. Next, insert s3 in s1, s2 so that s1, s2, s3 is
sorted. Continue until inserting sn in s1, . . . , sn−1 so that the
entire sequence s1, . . . , sn is sorted.
7. The time required by an algorithm is the number of steps to ter-
mination. The space required by an algorithm is the amount of
storage required by the input, local variables, and so on.
8. Knowing or being able to estimate the time and space required
by an algorithm gives an indication of how the algorithm will
perform for input of various sizes when run on a computer.
Knowing or being able to estimate the time and space required
by two or more algorithms that solve the same problem makes
it possible to compare the algorithms.
9. Many practical problems are too diﬃcult to be solved eﬃ-
ciently, and compromises either in generality or correctness
are necessary.
10. When a randomized algorithm executes, at some points it
makes random choices.
11. The requirement that the intermediate results of each step of
execution be uniquely deﬁned and depend only on the inputs
and results of the preceding steps is violated.
12. To shuﬄe s1, . . . , sn, ﬁrst swap s1 and a randomly chosen
element in s1, . . . , sn. Next, swap s2 and a randomly chosen
element in s2, . . . , sn. Continue until swapping sn−1 and a ran-
domly chosen element in sn−1, sn.
13. We might generate random arrangements of sequences to use
as input to test or time a sorting program.
Section 4.2
1. First i and j are set to 1. The while loop then compares
t1 · · · t4 = “bala” with p = “bala”. Since the comparison suc-
ceeds, the algorithm returns i = 1 to indicate that p was found
in t starting at index 1 in t.
4. First 20 is inserted in
34
Since 20 < 34, 34 must move one position to the right
34
Now 20 is inserted
34
20

<!-- pagina 29 -->
Hints and Solutions to Selected Exercises
661
Since 144 > 34, it is immediately inserted to 34’s right
34
144
20
Since 55 < 144, 144 must move one position to the right
34
144
20
Since 55 > 34, 55 is now inserted
34
55
144
20
The sequence is now sorted.
7. Since each element is greater than or equal to the element to
its left, the element is always inserted in its original position.
8. We ﬁrst swap ai and aj, where i = 1 and j = rand(1, 5) = 5.
After the swap we have
57
72
101
34
135
i
j
We next swap ai and aj, where i = 2 and j = rand(2, 5) = 4.
After the swap we have
101
72
57
34
135
i
j
We next swap ai and aj, where i = 3 and j = rand(3, 5) = 3.
The sequence is unchanged.
We next swap ai and aj, where i
=
4 and j
=
rand(4, 5) = 5. After the swap we have
101
72
34
57
135
j
i
11. Yes. The following values for rand sort the input in increasing
order:
rand(1, 5) = 3,
rand(2, 5) = 2,
rand(3, 5) = 5,
rand(4, 5) = 5.
13. The while loop tests whether p occurs at index i in t. If p
does occur at index i in t, ti+j−1 will be equal to pj for all
j = 1, . . . , m. Thus j becomes m + 1 and the algorithm re-
turns i. If p does not occur at index i in t, ti+j−1 will not be
equal to pj for some j. In this case the while loop terminates
(without executing return i).
Now suppose that p occurs in t and its ﬁrst occurrence
is at index i in t. As noted in the previous paragraph, the al-
gorithm correctly returns i, the smallest index in t where p
occurs.
If p does not occur in t, then the while loop terminates
for every i and i increments in the for loop. Therefore, the for
loop runs to completion, and the algorithm correctly returns 0
to indicate that p was not found in t.
16.
Input:
s (the sequence s1, . . . , sn), n, and key
Output:
i (the index of the last occurrence of key in s, or 0 if
key is not in s)
reverse linear search(s, n, key) {
i = n
while (i ≥1) {
if (si == key)
return i
i = i −1
}
return 0
}
19. We measure the time of the algorithm by counting the number
of comparisons (ti+j−1 == pj) in the while loop.
No comparisons will be made if n −m + 1 ≤0. In the
remainder of this solution, we assume that n −m + 1 > 0.
If p is in t, m comparisons must be performed to verify
that p is, in fact, in t. We can guarantee that exactly m compar-
isons are performed if p is at index 1 in t.
If p is not in t, at least one comparison must be per-
formed for each i. We can guarantee that exactly one compar-
ison is performed for each i if the ﬁrst character in p does not
occur in t. In this case, n −m + 1 comparisons are made.
If m < n −m + 1, the best case is that p is at index 1 in
t. If n −m + 1 < m, the best case is that the ﬁrst character in
p does not occur in t. If m = n −m + 1, either situation is the
best case.
22.
Input:
s (the sequence s1, . . . , sn) and n
Output:
s (sorted in nondecreasing order)
selection sort(s, n) {
for i = 1 to n −1 {
// ﬁnd smallest in si, . . . , sn
small index = i
for j = i + 1 to n
if (sj < ssmall index)
small index = j
swap(si, ssmall index)
}
}
Section 4.3 Review
1. Analysis of algorithms refers to the process of deriving esti-
mates for the time and space needed to execute algorithms.
2. The worst-case time for input of size n of an algorithm is the
maximum time needed to execute the algorithm among all in-
puts of size n.
3. The best-case time for input of size n of an algorithm is the
minimum time needed to execute the algorithm among all in-
puts of size n.

<!-- pagina 30 -->
662
Hints and Solutions to Selected Exercises
4. The average-case time for input of size n of an algorithm is the
average time needed to execute the algorithm over some ﬁnite
set of inputs all of size n.
5. f(n) = O(g(n)) if there exists a positive constant C1 such that
|f(n)| ≤C1|g(n)| for all but ﬁnitely many positive integers n.
This notation is called the big oh notation.
6. Except for constants and a ﬁnite number of exceptions, f is
bounded above by g.
7. f(n) = ,(g(n)) if there exists a positive constant C2 such that
|f(n)| ≥C2|g(n)| for all but ﬁnitely many positive integers n.
This notation is called the omega notation.
8. Except for constants and a ﬁnite number of exceptions, f is
bounded below by g.
9. f(n) = -(g(n)) if f(n) = O(g(n)) and f(n) = ,(g(n)). This
notation is called the theta notation.
10. Except for constants and a ﬁnite number of exceptions, f is
bounded above and below by g.
Section 4.3
1. -(n)
4. -(n2)
7. -(n2)
10. -(n)
13. -(n lg n)
14. -(n2)
17. -(n)
20. -(n2)
23. -(n3)
26. -(n lg n)
29. -(1)
32. When n = 1, we obtain
1 = A + B + C.
When n = 2, we obtain
3 = 4A + 2B + C.
When n = 3, we obtain
6 = 9A + 3B + C.
Solving this system for A, B, C, we obtain
A = B = 1
2,
C = 0.
We obtain the formula
1 + 2 + · · · + n = n2
2 + n
2 + 0 = n(n + 1)
2
,
which can be proved using mathematical induction (see Sec-
tion 2.4).
34. n! = n(n −1) · · · 2 ·1 ≤n ·n · · · n = nn
37. Since n = 2lg n, nn+1 = (2lg n)n+1 = 2(n+1) lg n. Thus, it suf-
ﬁces to show that (n + 1) lg n ≤n2 for all n ≥1. A proof by
induction shows that n ≤2n−1 for all n ≥1. Thus, lg n ≤n−1
for all n ≥1. Therefore,
(n + 1) lg n ≤(n + 1)(n −1) = n2 −1 < n2
for all n ≥1.
40. Since f(n) = O(g(n)), there exist constants C′ > 0 and N
such that
f(n) ≤C′g(n)
for all n ≥N.
Let
C = max{C′, f(1)/g(1), f(2)/g(2), . . . , f(N)/g(N)}.
For n ≤N,
f(n)/g(n) ≤max{f(1)/g(1), f(2)/g(2), . . . , f(N)/g(N)}
≤C.
For n ≥N,
f(n) ≤C′g(n) ≤Cg(n).
Therefore, f(n) ≤Cg(n) for all n.
43. False. If the statement were true, we would have nn ≤C2n for
some constant C and for all suﬃciently large n. The preceding
inequality may be rewritten as
0n
2
1n
≤C
for some constant C and for all suﬃciently large n. Since
(n/2)n becomes arbitrarily large as n becomes large, we can-
not have nn ≤C2n for some constant C and for all suﬃciently
large n.
46. True
49. True
52. False. If n! ≥C(n + 1)! for all n ≥K, then, canceling n!,
1 ≥C(n + 1) for all n ≥K. But 1 ≥C(n + 1) is false if
n > max{1/C −1, K}.
54. True
57. True
60. True
62. False. A counterexample is f(n) = n and g(n) = 2n.
65. True
68. False. A counterexample is f(n) = 1 and g(n) = 1/n.
69. f(n)̸ = O(g(n)) means that for every positive constant C,
|f(n)| > C|g(n)| for inﬁnitely many positive integers n.
72. We ﬁrst ﬁnd nondecreasing positive functions f0 and g0
such that for inﬁnitely many n, f0(n) = n2 and g0(n) = n.
This implies that f0(n)̸ = O(g0(n)). Our functions also satisfy
f0(n) = n and g0(n) = n2 for inﬁnitely many n [obviously dif-
ferent n than those for which f0(n) = n2 and g0(n) = n]. This
implies that g0(n)̸ = O(f0(n)). If we then set f(n) = f0(n) + n
and g(n) = g0(n) + n, we obtain increasing positive functions
for which f(n)̸ = O(g(n)) and g(n)̸ = O(f(n)).
We begin by setting f0(2) = 2 and g0(2) = 22. Then
f0(n) = n,
g0(n) = n2,
if n = 2.
Because g0 is nondecreasing, the least n for which we may
have g0(n) = n is n = 22. So we deﬁne f0(22) = 24 and
g0(22) = 22. Then
f0(n) = n2,
g0(n) = n,
if n = 22.
The preceding discussion motivates deﬁning
f0(22k) =
2
22k
if k is even
22k+1
if k is odd

<!-- pagina 31 -->
Hints and Solutions to Selected Exercises
663
g0(22k) =
2
22k+1
if k is even
22k
if k is odd.
Suppose that n = 22k. If k is odd, f0(n) = n2 and g0(n) = n; if
k is even, f0(n) = n and g0(n) = n2. Now f0 and g0 are deﬁned
only for n = 22k, but they are nondecreasing on this domain.
To extend their domains to the set of positive integers, we may
simply deﬁne f0(1) = g0(1) = 1 and make them constant on
sets of the form {i | 22k ≤i < 22k+1}.
76. No
78. (a) The sum of the areas of the rectangles below the curve is
equal to
1
2 + 1
3 + · · · + 1
n.
This area is less than the area under the curve, which is
equal to
3 n
1
1
x dx = loge n.
The given inequality now follows immediately.
(b) The sum of the areas of the rectangles whose bases are on
the x-axis and whose tops are above the curve is equal to
1 + 1
2 + · · · +
1
n −1.
Since this area is greater than the area under the curve, the
given inequality follows immediately.
(c) Part (a) shows that
1 + 1
2 + · · · + 1
n = O(loge n).
Since loge n = -(lg n) (see Example 4.3.6),
1 + 1
2 + · · · + 1
n = O(lg n).
Similarly, we can conclude from part (b) that
1 + 1
2 + · · · + 1
n = ,(lg n).
Therefore,
1 + 1
2 + · · · + 1
n = -(lg n).
80. Replacing a by b in the sum yields
bn+1 −an+1
b −a
=
n
)
i=0
aibn−i <
n
)
i=0
bibn−i
=
n
)
i=0
bn = (n + 1)bn.
83. By Exercise 81, the sequence {(1 + 1/n)n}∞
n=1 is increasing.
Therefore
2 =
%
1 + 1
1
&1
≤
%
1 + 1
n
&n
for every positive integer n. Exercise 82 shows that
%
1 + 1
n
&n
< 4
for every positive integer n. Taking logs to the base 2, we
obtain
1 = lg 2 ≤lg
%
1 + 1
n
&n
< lg 4 = 2.
Since
lg
%
1 + 1
n
&n
= n lg
%
1 + 1
n
&
= n lg
%n + 1
n
&
= n[lg(n + 1) −lg n],
we have
1 ≤n[lg(n + 1) −lg n] < 2.
Dividing by n gives the desired inequality.
86. Replacing b by a in the sum yields
bn+1 −an+1
b −a
=
n
)
i=0
aibn−i >
n
)
i=0
aian−i
=
n
)
i=0
an = (n + 1)an.
89. By Exercise 88, the sequence {(1+1/n)n+1}∞
n=1 is decreasing.
Since (1 + 1/n)n+1 = 4, when n = 1,
4 ≥
%
1 + 1
n
&n+1
=
%n + 1
n
&n+1
.
Taking logs to the base 2, we obtain
2 = lg 4 ≥lg
%n + 1
n
&n+1
= (n + 1) lg
%n + 1
n
&
= (n + 1)[lg(n + 1) −lg n].
Dividing by n + 1 gives the desired inequality.
91. True. Since limn→∞f(n)/g(n) = 0, taking ε = 1, there exists
N such that
4444
f(n)
g(n)
4444 < 1,
for all n ≥N.
Therefore, for all n ≥N, |f(n)| < |g(n)| and f(n) = O(g(n)).
94. True. Let d = |c|. Since limn→∞|f(n)|/|g(n)| = d > 0, tak-
ing ε = d/2, there exists N such that
4444
|f(n)|
|g(n)| −d
4444 < d/2,
for all n ≥N.
This last inequality may be written
−d
2 < |f(n)|
|g(n)| −d < d
2,
for all n ≥N,
or
d
2 < |f(n)|
|g(n)| < 3d
2 ,
for all n ≥N,

<!-- pagina 32 -->
664
Hints and Solutions to Selected Exercises
or
d
2|g(n)| < |f(n)| < 3d
2 |g(n)|,
for all n ≥N.
Therefore, f(n) = -(g(n)).
99. Multiply both sides of the inequality in Exercise 98 by lg e and
use the change-of-base formula for logarithms.
Section 4.4 Review
1. An algorithm that contains a recursive function
2. A function that invokes itself
3.
factorial(n) {
if (n == 0)
return 1
return n ∗factorial(n −1)
}
4. The original problem is divided into two or more subproblems.
Solutions are then found for the subproblems (usually by fur-
ther subdivision). These solutions are then combined in order
to obtain a solution to the original problem.
5. In a base case, a solution is obtained directly, that is, without
a recursive call.
6. If a recursive function had no base case, it would continue to
call itself and never terminate.
7. f1 = 1, f2 = 1, fn = fn−1 + fn−2 for n ≥3
8. f1 = 1, f2 = 1, f3 = 2, f4 = 3
Section 4.4
1. (a) At line 2, since 4̸ = 0, we proceed to line 4. The algorithm
is invoked with input 3.
(b) At line 2, since 3̸ = 0, we proceed to line 4. The algorithm
is invoked with input 2.
(c) At line 2, since 2̸ = 0, we proceed to line 4. The algorithm
is invoked with input 1.
(d) At line 2, since 1̸ = 0, we proceed to line 4. The algorithm
is invoked with input 0.
(e) At lines 2 and 3, since 0 = 0, we return 1.
Execution resumes in part (d) at line 4 after computing
0! (= 1). We return 0! ·1 = 1.
Execution resumes in part (c) at line 4 after computing
1! (= 1). We return 1! ·2 = 2.
Execution resumes in part (b) at line 4 after computing
2! (= 2). We return 2! ·3 = 6.
Execution resumes in part (a) at line 4 after computing
3! (= 6). We return 3! ·4 = 24.
4. We use induction on i, where n = 2i. The Basis Step is i = 1.
In this case, the board is a tromino T. The algorithm correctly
tiles the board with T and returns. Thus the algorithm is correct
for i = 1.
Now assume that if n = 2i, the algorithm is cor-
rect. Let n = 2i+1. The algorithm divides the board into four
(n/2) × (n/2) subboards. It then places one right tromino in
the center as in Figure 2.4.6. It considers each of the squares
covered by the center tromino as missing. It then tiles the four
subboards, and, by the inductive assumption, these subboards
are correctly tiled. Therefore, the n×n board is correctly tiled.
The Inductive Step is complete. The algorithm is correct.
7. The proof is by strong induction on n. The Basis Steps
(n = 1, 2) are readily veriﬁed.
Assume that the algorithm is correct for all k < n. We
must show that the algorithm is correct for n > 2. Since n > 2,
the algorithm executes the return statement
return walk(n −1) + walk(n −2)
By the inductive assumption, the values of walk(n −1) and
walk(n −2) are correctly computed by the algorithm. Since
walk(n) = walk(n −1) + walk(n −2),
the algorithm returns the correct value of walk(n).
10. (a)
Input:
n
Output:
2 + 4 + · · · + 2n
1.
sum(s, n) {
2.
if (n == 1)
3.
return 2
4.
return sum(n −1) + 2n
5.
}
(b) Basis Step (n = 1) If n is equal to 1, we correctly re-
turn 2.
Inductive Step
Assume that the algorithm correctly
computes the sum when the input is n −1. Now suppose
that the input to this algorithm is n > 1. At line 2, since
n̸ = 1, we proceed to line 4, where we invoke this algo-
rithm with input n −1. By the inductive assumption, the
value returned, sum(n −1), is equal to
2 + · · · + 2(n −1).
At line 4, we then return
sum(n −1) + 2n = 2 + · · · + 2(n −1) + 2n,
which is the correct value.
13.
Input:
The sequence s1, . . . , sn and the length n of the
sequence
Output:
The maximum value in the sequence
ﬁnd max(s, n) {
if (n == 1)
return s1
x = ﬁnd max(s, n −1)
if (x > sn)
return x
else
return sn
}
We prove that the algorithm is correct using induction
on n. The base case is n = 1. If n = 1, the only item in the
sequence is s1 and the algorithm correctly returns it.

<!-- pagina 33 -->
Hints and Solutions to Selected Exercises
665
Assume that the algorithm computes the maximum for
input of size n −1, and suppose that the algorithm receives
input of size n. By assumption, the recursive call
x = ﬁnd max(s, n −1)
correctly computes x as the maximum value in the sequence
s1, . . . , sn−1. If x is greater than sn, the maximum value in the
sequence s1, . . . , sn is x—the value returned by the algorithm.
If x is not greater than sn, the maximum value in the sequence
s1, . . . , sn is sn—again, the value returned by the algorithm.
In either case, the algorithm correctly computes the maximum
value in the sequence. The Inductive Step is complete, and we
have proved that the algorithm is correct.
16. To list all of the ways that a robot can walk n meters, set s to
the null string and invoke this algorithm.
Input:
n, s (a string)
Output:
All the ways the robot can walk n meters. Each
method of walking n meters includes the extra
string s in the list.
list walk1(n, s) {
if (n == 1) {
println(s + “take one step of length 1”)
return
}
if (n == 2) {
println(s + “take two steps of length 1”)
println(s + “take one step of length 2”)
return
}
s′ = s + “take one step of length 2” // concatenation
list walk1(n −2, s′)
s′ = s + “take one step of length 1” // concatenation
list walk1(n −1, s′)
}
18. After one month, there is still just one pair because a pair
does not become productive until after one month. There-
fore, a1 = 1. After two months, the pair alive in the beginning
becomes productive and adds one additional pair. Therefore,
a2 = 2. The increase in pairs of rabbits an −an−1 from month
n −1 to month n is due to each pair alive in month n −2
producing an additional pair. That is, an −an−1 = an−2. Since
{an} satisﬁes the same recurrence relation as {fn}, a1 = f2, and
a2 = f3, an = fn+1, n ≥1.
21. Basis Step (n = 2)
f 2
2 = 1 = 1 ·2 −1 = f1f3 + (−1)3
Inductive Step
fnfn+2 + (−1)n+2 = fn(fn+1 + fn) + (−1)n+2
= fnfn+1 + f 2
n + (−1)n+2
= fnfn+1 + fn−1fn+1+ (−1)n+1+ (−1)n+2
= fn+1(fn + fn−1) = f 2
n+1
24. Basis Step (n = 1)
f 2
1 = 12 = 1 = 1 ·1 = f1f2
Inductive Step
n+1
)
k=1
f 2
k =
n
)
k=1
f 2
k + f 2
n+1 = fnfn+1 + f 2
n+1
= fn+1(fn + fn+1) = fn+1fn+2
27. We use strong induction.
Basis Steps (n = 6,7)
f6 = 8 > 7.59 = (3/2)5. f7 = 13 >
11.39 = (3/2)6.
Inductive Step
fn = fn−1 + fn−2 >
%3
2
&n−2
+
%3
2
&n−3
=
%3
2
&n−1 5%3
2
&−1
+
%3
2
&−26
=
%3
2
&n−1 #16
9
$
>
%3
2
&n−1
30. We use strong induction on n.
Basis Step (n = 1)
1 = f1
Inductive Step
Suppose that n > 2 and that every posi-
tive integer less than n can be expressed as the sum of distinct
Fibonacci numbers, no two of which are consecutive. Let fk1
be the largest Fibonacci number satisfying n ≥fk1. If n = fk1,
then n is trivially the sum of distinct Fibonacci numbers, no
two of which are consecutive. Suppose that n > fk1. By the
inductive assumption, n −fk1 can be expressed as the sum of
distinct Fibonacci numbers fk2 > fk3 > · · · > fkm, no two of
which are consecutive:
n −fk1 =
m
)
i=2
fki.
Now n is expressed as the sum of Fibonacci numbers:
n =
m
)
i=1
fki.
(∗)
We next show that fk1 > fk2, so that, in particular, n is the sum
of distinct Fibonacci numbers.
Notice that fk2 < n. Since fk1 is the largest Fibonacci
number satisfying n ≥fk1, fk2 ≤fk1. If fk2 = fk1,
n ≥fk1 + fk2 > fk1 + fk1−1 = fk1+1.
This last inequality contradicts the choice of fk1 as the largest
Fibonacci number satisfying n ≥fk1. Therefore fk1 > fk2.
The only Fibonacci numbers in the sum (∗) that might
be consecutive are fk1 and fk2. If they are consecutive, we may
also write (∗) as
n =
m
)
i=1
fki
= fk1 + fk2 +
m
)
i=3
fki

<!-- pagina 34 -->
666
Hints and Solutions to Selected Exercises
= fk1 + fk1−1 +
m
)
i=3
fki
= fk1+1 +
m
)
i=3
fki.
Now fk1+1 ≤n and fk1+1 > fk1. This contradicts the choice of
fk1 as the largest Fibonacci number satisfying n ≥fk1. The
inductive step is complete.
33. Using the formula fk fk+2 −f 2
k+1 = (−1)k+1 from Exercise 21,
we obtain
1 +
n
)
k=1
(−1)k+1
fk fk+1
= 1 +
n
)
k=1
fk fk+2 −f 2
k+1
fk fk+1
= 1 +
n
)
k=1
%fk+2
fk+1
−fk+1
fk
&
= 1 +
%f3
f2
−f2
f1
&
+
%f4
f3
−f3
f2
&
+ · · · +
%fn+2
fn+1
−fn+1
fn
&
= 1 + fn+2
fn+1
−f2
f1
= fn+2
fn+1
.
36. Basis Step (n = 4)
4
)
k=1
(−1)kkfk = −f1 + 2f2 −3f3 + 4f4 = −1 + 2 −6 + 12 = 7
and
(−1)4(4f3 + f1) −2 = 8 + 1 −2 = 7.
Inductive Step
n+1
)
k=1
(−1)kkfk =
n
)
k=1
(−1)kkfk + (−1)n+1(n + 1) fn+1
= (−1)n(nfn−1 + fn−3) −2 + (−1)n+1(n + 1) fn+1
= (−1)n+1[(n + 1)fn+1 −nfn−1 −fn−3] −2
= (−1)n+1[(n + 1)(fn + fn−1) −nfn−1 −fn−3] −2
= (−1)n+1[(n + 1)fn + fn−1 −fn−3] −2
= (−1)n+1[(n + 1)fn + fn−2] −2.
The last step is justiﬁed by the equality fn−1 = fn−2 + fn−3.
Chapter 4 Self-Test
1. [Section 4.1] At line 2, we set large to 12. At line 3, since
b > large (3 > 12) is false, we move to line 5. At line 5, since
c > large (0 > 12) is false, we move to line 7, where we return
large (12), the maximum of the given values.
2. [Section 4.1] If the set S is an inﬁnite set, the algorithm will not
terminate, so it lacks the ﬁniteness and output properties. Line
1 is not precisely stated since how to list the subsets of S and
their sums is not speciﬁed; thus the algorithm lacks the preci-
sion property. The order of the subsets listed in line 1 depends
on the method used to generate them, so the algorithm lacks
the determinism property. Since line 2 depends on the order
of the subsets generated in line 1, the determinism property is
lacking here as well.
3. [Section 4.2] The while loop ﬁrst tests whether “110” occurs
in t at index 1. Since “110” does not occur in t at index 1,
the algorithm next tests whether “110” occurs in t at index 2.
Since “110” does occur in t at index 2, the algorithm returns
the value 2.
4. [Section 4.2] First 64 is inserted in
44
Since 64 > 44, it is immediately inserted to 44’s right
44
64
Next 77 is inserted. Since 77 > 64, it is immediately inserted
to 64’s right
44
64
77
Next 15 is inserted. Since 15 < 77, 77 must move one position
to the right
44
64
77
Since 15 < 64, 64 must move one position to the right
44
64
77
Since 15 < 44, 44 must move one position to the right
44
64
77
Now 15 is inserted
44
15
64
77
Finally 3 is inserted. Since 3 < 77, 77 must move one position
to the right
44
15
64
77
Since 3 < 64, 64 must move one position to the right
44
15
64
77
Since 3 < 44, 44 must move one position to the right
44
15
64
77
Since 3 < 15, 15 must move one position to the right
44
15
64
77

<!-- pagina 35 -->
Hints and Solutions to Selected Exercises
667
Now 3 is inserted
44
15
3
64
77
The sequence is sorted.
5. [Section 4.2] We ﬁrst swap ai and aj, where i = 1 and
j = rand(1, 5) = 1. The sequence is unchanged.
We next swap ai and aj, where i
=
2 and j
=
rand(2, 5) = 3. After the swap we have
51
2
5
44
96
j
i
We next swap ai and aj, where i = 3 and j = rand(3, 5) = 5.
After the swap we have
96
2
5
44
51
i
j
We next swap ai and aj, where i = 4 and j = rand(4, 5) = 5.
After the swap we have
96
2
5
51
44
i
j
6. [Section 4.1]
sort(a, b, c, x, y, z) {
x = a
y = b
z = c
if (y < x)
swap(x, y)
if (z < x)
swap(x, z)
if (z < y)
swap(y, z)
}
7. [Section 4.2]
repeaters(s, n) {
i = 1
while (i < n) {
if (si == si+1)
println(si)
// skip to next element not equal to si
j = i
while (i < n ∧si == sj)
i = i + 1
}
}
8. [Section 4.1]
test distinct(a, b, c) {
if (a == b ∨a == c ∨b == c)
return false
return true
}
9. [Section 4.3]
Input:
A and B (n × n matrices) and n
Output:
true (if A = B); false (if A̸ = B)
equal matrices(A, B, n) {
for i = 1 to n
for j = 1 to n
if (Aij¬ = Bij)
return false
return true
}
The worst-case time is -(n2).
10. [Section 4.3] -(n3)
11. [Section 4.3] -(n4)
12. [Section 4.3] -(n2)
13. [Section 4.4] Since n̸ = 2, we proceed immediately to line 6,
where we divide the board into four 4×4 boards. At line 7, we
rotate the board so that the missing square is in the upper-left
quadrant. At line 8, we place one tromino in the center. We
then proceed to lines 9–12, where we call the algorithm to tile
the subboards. We obtain the tiling:
14. [Section 4.4] t4 = 3, t5 = 5
15. [Section 4.4]
Input:
n, an integer greater than or equal to 1
Output:
tn
tribonacci(n) {
1.
if (n == 1 ∨n == 2 ∨n == 3)
2.
return 1
3.
return tribonacci(n −1) + tribonacci(n −2)
+ tribonacci(n −3)
}
16. [Section 4.4] Basis Steps (n = 1, 2, 3)
If n = 1, 2, 3, at
lines 1 and 2 we return the correct value, 1. Therefore, the al-
gorithm is correct in these cases.

<!-- pagina 36 -->
668
Hints and Solutions to Selected Exercises
Inductive Step
Assume that n > 3 and that the algorithm
correctly computes tk, if k < n. Since n > 3, we proceed to
line 3. We then call this algorithm to compute tn−1, tn−2, and
tn−3. By the inductive assumption, the values computed are
correct. The algorithm then computes tn−1 + tn−2 + tn−3. But
the formula shows that this value is equal to tn. Therefore, the
algorithm returns the correct value for tn.
Section 5.1 Review
1. We say that d divides n if there exists an integer q satisfying
n = dq.
2. If d divides n, we say that d is a divisor of n.
3. If d divides n, n = dq, we call q the quotient.
4. An integer greater than 1 whose only positive divisors are itself
and 1 is called prime.
5. An integer greater than 1 that is not prime is called composite.
6. If n is composite, it must have a divisor d satisfying 2 ≤d ≤
⌊√n⌋(see Theorem 5.1.7).
7. Algorithm 5.1.8 does not run in time polynomial in the size of
the input.
8. Any integer greater than 1 can be written as a product of
primes. Moreover, if the primes are written in nondecreasing
order, the factorization is unique.
9. See the proof of Theorem 5.1.12.
10. A common divisor of m and n, not both zero, is an integer that
divides both m and n.
11. The greatest common divisor of m and n, not both zero, is the
largest common divisor of m and n.
12. See Theorem 5.1.17.
13. A common multiple of m and n is an integer that is divisible
by both m and n.
14. The least common multiple of m and n is the smallest positive
common multiple of m and n.
15. See Theorem 5.1.22.
16. gcd(m, n) ·lcm(m, n) = mn
Section 5.1
1. First d is set to 2. Since n mod d = 9 mod 2 = 1 is not equal
to 0, d is incremented and becomes 3.
Now n mod d = 9 mod 3 equals 0, so the algorithm re-
turns d = 3 to indicate that n = 9 is composite and 3 is a
divisor of 9.
4. When d is set to 2, . . . , 6, n mod d is not equal to zero. How-
ever, when d becomes 7, n mod d = 637 mod 7 equals 0, so
the algorithm returns d = 7 to indicate that n = 637 is com-
posite and 7 is a divisor of 637.
7. First d is set to 2. Since n mod d = 3738 mod 2 equals 0, the
algorithm returns d = 2 to indicate that n = 3738 is composite
and 2 is a divisor of 3738.
9. 47
12. 17
15. 1
18. 20
21. 13
24. 32 ·73 ·11
25. (For Exercise 14) 25
28. Since d divides m, there exists q such that m = dq. Multi-
plying by n gives mn = d(qn). Therefore, d divides mn (with
quotient qn).
31. Since a divides b, there exists q1 such that b = aq1. Since b
divides c, there exists q2 such that c = bq2. Now
c = bq2 = (aq1)q2 = a(q1q2).
Therefore, a divides c (with quotient q1q2).
36. Basis Step (n = 1)
70
i=0 Fi = F0 = 3 = 5 −2 = F1 −2.
Inductive Step
Assume true for n. Now
n
8
i=0
Fi = Fn
9n−1
8
i=0
Fi
:
= Fn(Fn −2)
= (22n + 1)(22n −1) = 22n+1 −1 = Fn+1 −2.
39. We use the identity
Cn −1 = (C −1)(Cn−1 + Cn−2 + · · · + C + 1).
Now suppose that m = ab, a > 1 and b > 1. Taking C = 2a
and n = b, we ﬁnd that
(2a)b −1 = (2a −1)((2a)b−1 + (2a)b−2 + · · · + 2a + 1).
Thus 2a −1 divides (2a)b −1 = 2m −1. Since a > 1,
2a −1 > 1. Therefore 2m −1 is composite.
40. Since 2 is not the product of two or more elements in E, it is
E-prime.
43. Since 12 = 2 ·6, it is E-composite.
46. Notice that 2 ·m, where m is odd, is E-prime since it is not the
product of two or more elements in E. It follows that the set of
E-primes is inﬁnite.
49. The E-prime 18 divides 6 ·6 (36 = 2 ·18), but 18 does not
divide 6.
Section 5.2 Review
1.
n
)
i=0
di10i
2.
n
)
i=0
bi2i
3.
n
)
i=0
hi16i
4. ⌊1 + lg n⌋
5. Perform the computation ;n
i=0 bi2i in decimal.
6. Divide the number to be converted to binary by 2. The remain-
der gives the 1’s bit. Divide the quotient by 2. The remainder
gives the 2’s bit. Continue.
7. Perform the computation ;n
i=0 hi16i in decimal.
8. Divide the number to be converted to hexadecimal by 16. The
remainder gives the number of 1’s. Divide the quotient by 16.
The remainder gives the number of 16’s. Continue.
9. Use the ordinary algorithm for adding decimal numbers to add
binary numbers—except replace the decimal addition table by
the binary addition table.
10. Use the ordinary algorithm for adding decimal numbers to add
hexadecimal numbers—except replace the decimal addition
table by the hexadecimal addition table.

<!-- pagina 37 -->
Hints and Solutions to Selected Exercises
669
11. Let
n =
m
)
i=0
bi2i
be the binary expansion of n. Using repeated squaring, com-
pute a1, a2, a4, a8, . . . , abm. Then
an = a+m
i=0bi2i =
m
8
i=0
abi2i.
12. Proceed as described in the solution to Exercise 11, only use
the formula
ab mod z = [(a mod z)(b mod z)] mod z.
Section 5.2
1. 6
4. 7
7. 1585
10. 163
11. 9
14. 32
17. 100010
20. 110010000
23. 11000
26. 1001000
29. 58
32. 2563
35. (For Exercise 11) 9
38. FE
41. 3DBF9
43. 2010 cannot represent a number in binary because 2 is an ille-
gal symbol in binary. 2010 could represent a number in either
decimal or hexadecimal.
45. 51
48. 4570
51. (For Exercise 11) 11
54. (For Exercise 45) 33
57. 9450 cannot represent a number in binary because 9, 4, and 5
are illegal symbols in binary. 9450 cannot represent a number
in octal because 9 is an illegal symbol in octal. 9450 represents
a number in either decimal or hexadecimal.
59. The algorithm begins by setting result to 1 and x to a. Since
n = 16 > 0, the body of the while loop executes. Since
n mod 2 is not equal to 1, result is not modiﬁed. x becomes
a2, and n becomes 8.
Since n = 8 > 0, the body of the while loop executes.
Since n mod 2 is not equal to 1, result is not modiﬁed. x be-
comes a4, and n becomes 4.
Since n = 4 > 0, the body of the while loop executes.
Since n mod 2 is not equal to 1, result is not modiﬁed. x be-
comes a8, and n becomes 2.
Since n = 2 > 0, the body of the while loop executes.
Since n mod 2 is not equal to 1, result is not modiﬁed. x be-
comes a16, and n becomes 1.
Since n = 1 > 0, the body of the while loop exe-
cutes. Since n mod 2 is equal to 1, result becomes result ∗x =
1 ∗a16 = a16. x becomes a32, and n becomes 0.
Since n = 0 is not greater than 0, the while loop termi-
nates. The algorithm returns result, which is equal to a16.
62. The algorithm begins by setting result to 1 and x to a mod z =
5 mod 21 = 5. Since n = 10 > 0, the body of the while loop
executes. Since n mod 2 is not equal to 1, result is not mod-
iﬁed. x is set to x ∗x mod z = 25 mod 21 = 4, and n is set
to 5.
Since n = 5 > 0, the body of the while loop executes.
Since n mod 2 is equal to 1, result is set to (result∗x) mod z =
4 mod 21 = 4. x is set to x ∗x mod z = 16 mod 21 = 16, and
n is set to 2.
Since n = 2 > 0, the body of the while loop executes.
Since n mod 2 is not equal to 1, result is not modiﬁed. x is set
to x ∗x mod z = 256 mod 21 = 4, and n is set to 1.
Since n = 1 > 0, the body of the while loop executes.
Since n mod 1 is equal to 1, result is set to (result∗x) mod z =
16 mod 21 = 16. x is set to x ∗x mod z = 16 mod 21 = 16,
and n is set to 0.
Since n = 0 is not greater than 0, the while loop
terminates. The algorithm returns result, which is equal to
an mod z = 510 mod 21 = 16.
65. If mk is the highest power of 2 that divides m, then m = 2mkp,
where p is odd. Similarly, if nk is the highest power of 2 that
divides n, then n = 2nkq, where q is odd. Now mn = 2mk+nkpq.
Since pq is odd, mk + nk is the highest power of 2 that divides
mn, and the result follows.
Section 5.3 Review
1. See Algorithm 5.3.3.
2. If a is a nonnegative integer, b is a positive integer, and r =
a mod b, then gcd(a, b) = gcd(b, r).
3. a ≥fn+2 and b ≥fn+1
4. log3/2 2m/3
5. Write the nonzero remainders as found by the Euclidean algo-
rithm in the form
r = n −dq
in the order in which the Euclidean algorithm computes them.
Substitute the formula for the next-to-last remainder into the
last equation. Call the resulting equation E1. Substitute the
second-to-last formula for the remainder into E1. Call the re-
sulting equation E2. Substitute the third-to-last formula for the
remainder into E2. Continue until the ﬁrst formula for the re-
mainder is substituted into the last Ek equation.
6. s is the inverse of n mod z if ns mod z = 1.
7. Find numbers s′ and t′ such that s′n + t′φ = 1. Set s =
s′ mod φ.
Section 5.3
1. 90 mod 60 = 30; 60 mod 30 = 0; so gcd(60, 90) = 30.
4. 825 mod 315
=
195; 315 mod 195
=
120; 195 mod
120
=
75; 120 mod 75 = 45; 75 mod 45 = 30; 45 mod
30 = 15; 30 mod 15 = 0; so gcd(825, 315) = 15.
7. 4807 mod 2091 = 625;
2091 mod 625 = 216;
625 mod
216 = 193; 216 mod 193 = 23; 193 mod 23 = 9; 23 mod
9 = 5;
9 mod 5 = 4;
5 mod 4 = 1;
4 mod 1 = 0;
so
gcd(2091, 4807) = 1.
10. 490256 mod 337 = 258; 337 mod 258 = 79; 258 mod 79 =
21; 79 mod 21 = 16; 21 mod 16 = 5; 16 mod 5 = 1; 5 mod
1 = 0; so gcd(490256, 337) = 1.

<!-- pagina 38 -->
670
Hints and Solutions to Selected Exercises
13. (For Exercise 10) The nonzero remainders in the order they
are computed by the Euclidean algorithm are
490256 mod 337 = 258
337 mod 258 = 79
258 mod 79 = 21
79 mod 21 = 16
21 mod 16 = 5
16 mod 5 = 1.
Writing these equations in the form r = n −dq, where r is the
remainder and q is the quotient, yields
258 = 490256 −337 ·1454
79 = 337 −258 ·1
21 = 258 −79 ·3
16 = 79 −21 ·3
5 = 21 −16 ·1
1 = 16 −5 ·3.
Substituting the next-to-last formula for 5 into the last equa-
tion yields
1 = 16 −(21 −16 ·1) ·3 = 16 ·4 −21 ·3.
Substituting the second-to-last formula for 16 into the previ-
ous equation yields
1 = (79 −21 ·3)4 −21 ·3 = 79 ·4 −21 ·15.
Substituting the third formula for 21 into the previous equation
yields
1 = 79 ·4 −(258 −79 ·3)15 = 79 ·49 −258 ·15.
Substituting the second formula for 79 into the previous equa-
tion yields
1 = (337 −258)49 −258 ·15 = 337 ·49 −258 ·64.
Finally, substituting the ﬁrst formula for 258 into the previous
equation yields
1 = 337 ·49 −(490256 −337 ·1454)64
= 337 ·93105 −490256 ·64.
Thus, if we set s = −64 and t = 93105,
s ·490256 + t ·337 = gcd(490256, 337) = 1.
16. gcd recurs(a, b) {
make a largest
if (a < b)
swap(a, b)
return gcd recurs1(a, b)
}
gcd recurs1(a, b) {
if (b == 0)
return a
r = a mod b
return gcd recurs1(b, r)
}
19.
gcd subtract(a, b) {
while (true) {
// make a largest
if (a < b)
swap(a, b)
if (b == 0)
return a
a = a −b
}
}
22. By Theorem 5.3.5, a pair a, b, a > b, would require n modu-
lus operations when input to the Euclidean Algorithm only if
a ≥fn+2 and b ≥fn+1. Now f29 = 514229, f30 = 832040,
and f31 = 1346269. Thus, no pair can require more than
28 modulus operations in the worst case because 29 modulus
operations would require one member of the pair to exceed
1000000. The pair 514229, 832040 itself requires 28 modulus
operations.
25. We prove the statement by induction on n.
Basis Step (n = 1)
gcd(f1, f2) = gcd(1, 1) = 1
Inductive Step
Assume that gcd(fn, fn+1) = 1. Now
gcd(fn+1, fn+2) = gcd(fn+1, fn+1 + fn) = gcd(fn+1, fn) = 1.
We use Exercise 18 with a = fn+1 + fn and b = fn+1 to justify
the second equality.
29. If m = 1, the result is immediate, so we assume that m > 1.
Suppose that f is one-to-one and onto. Since m > 1,
there exists x such that f(x) = nx mod m = 1. Thus there ex-
ists q such that
nx = mq + 1.
Let g be the greatest common divisor of m and n. Then g di-
vides both m and n and also nx −mq = 1. Therefore, g = 1.
Now suppose that gcd(m, n) = 1. By Theorem 5.3.7,
there exist s and t such that
1 = sm + tn.
Let k ∈X. Then
k = msk + ntk.
Therefore,
(ntk) mod m = (k −msk) mod m = k mod m = k.
We may argue as in the Computing an Inverse Modulo an In-
teger subsection that if we set x = tk mod m, then f(x) =
(ntk) mod m. Therefore, f is onto. Since f is a function from
X to X, f is also one-to-one.
30. If a̸ = 0, a = 1 ·a + 0 ·b > 0. In this case, a ∈X. Similarly,
if b̸ = 0, b ∈X.
33. Suppose that g does not divide a. Then a = qg+r, 0 < r < g.
Since g ∈X, there exist s and t such that g = sa + tb. Now
r = a −qg = a −q(sa + tb) = (1 −qs)a + (−qt)b.
Therefore r ∈X. Since g is the least element in X and 0 < r <
g, we have a contradiction. Therefore, g divides a. Similarly,
g divides b.
35. gcd(3, 2) = gcd(2, 1) = gcd(1, 0) = 1, s = 2

<!-- pagina 39 -->
Hints and Solutions to Selected Exercises
671
38. gcd(47, 11) = gcd(11, 3) = gcd(3, 2) = gcd(2, 1) = gcd(1, 0)
= 1, s = 30
41. gcd(243, 100) = gcd(100, 43) = gcd(43, 14) = gcd(14, 1) =
gcd(1, 0) = 1, s = 226
42. We argue by contradiction. Suppose that 6 has an inverse mod-
ulo 15; that is, suppose that there exists s such that 6s mod
15 = 1. Then there exists q such that
15 −6sq = 1.
Since 3 divides 15 and 3 divides 6sq, 3 divides 1. We have
obtained the desired contradiction. Thus, 6 does not have an
inverse modulo 15.
That 6 does not have an inverse modulo 15 does not con-
tradict the result preceding Example 5.3.9. In order to guar-
antee that n has an inverse modulo φ, the result preceding
Example 5.3.9 requires that gcd(n, φ) = 1. In this exercise,
gcd(6, 15) = 3.
Section 5.4 Review
1. Cryptology is the study of systems for secure communications.
2. A cryptosystem is a system for secure communications.
3. To encrypt a message is to transform the message so that only
an authorized recipient can reconstruct it.
4. To decrypt a message is to transform an encrypted message so
that it can be read.
5. Compute c = an mod z and send c.
6. Compute cs mod z. z is chosen as the product of primes p and
q. s satisﬁes ns mod (p −1)(q −1) = 1.
7. The security of the RSA encryption system relies mainly on
the fact that at present there is no eﬃcient algorithm known
for factoring integers.
Section 5.4
1. FKKGEJAIMWQ
4. BUSHWHACKED
7. 53
9. z = pq = 17 ·23 = 391
12. c = an mod z = 10131 mod 391 = 186
14. z = pq = 59 ·101 = 5959
17. c = an mod z = 58441 mod 5959 = 3237
Chapter 5 Self-Test
1. [Section 5.1] For d = 2, . . . , 6, 539 mod d is not equal to zero,
so d increments. When d = 7, 539 mod d equals zero, so the
algorithm returns d = 7 to indicate that 539 is composite and
7 is a divisor of 539.
2. [Section 5.2] 150
3. [Section 5.1] 539 = 72 ·11
4. [Section 5.3] gcd(480, 396) = gcd(396, 84) = gcd(84, 60) =
gcd(60, 24) = gcd(24, 12) = gcd(12, 0) = 12
5. [Section 5.1] 72 ·132
6. [Section 5.1] 2 ·52 ·74 ·134 ·17
7. [Section 5.2] 110101110, 1AE
8. [Section 5.3] Since
log3/2
2(100,000,000)
3
= log3/2 1004 + log3/2
2
3
= (4 log3/2 100) −1
= 4(11.357747) −1 = 44.430988,
an upper bound for the number of modulus operations re-
quired by the Euclidean algorithm for integers in the range 0
to 100,000,000 is 44.
9. [Section 5.2] The algorithm begins by setting result to 1 and
x to a. Since n = 30 > 0, the body of the while loop exe-
cutes. Since n mod 2 is not equal to 1, result is not modiﬁed.
x becomes a2, and n becomes 15.
Since n = 15 > 0, the body of the while loop executes.
Since n mod 2 is equal to 1, result becomes result ∗x =
1 ∗a2 = a2. x becomes a4, and n becomes 7.
Since n = 7 > 0, the body of the while loop executes.
Since n mod 2 is equal to 1, result becomes result ∗x = a2 ∗
a4 = a6. x becomes a8, and n becomes 3.
Since n = 3 > 0, the body of the while loop executes.
Since n mod 2 is equal to 1, result becomes result ∗x = a6 ∗
a8 = a14. x becomes a16, and n becomes 1.
Since n = 1 > 0, the body of the while loop executes.
Since n mod 2 is equal to 1, result becomes result ∗x =
a14 ∗a16 = a30. x becomes a32, and n becomes 0.
Since n = 0 is not greater than 0, the while loop
terminates. The algorithm returns result, which is equal
to a30.
10. [Section 5.2] The algorithm begins by setting result to 1 and x
to a mod z = 50 mod 11 = 6. Since n = 30 > 0, the body of
the while loop executes. Since n mod 2 is not equal to 1, result
is not modiﬁed. x is set to x ∗x mod z = 36 mod 11 = 3, and
n is set to 15.
Since n = 15 > 0, the body of the while loop executes.
Since n mod 2 is equal to 1, result is set to (result∗x) mod z =
3 mod 11 = 3. x is set to x ∗x mod z = 9 mod 11 = 9, and n
is set to 7.
Since n = 7 > 0, the body of the while loop executes.
Since n mod 2 is equal to 1, result is set to (result∗x) mod z =
27 mod 11 = 5. x is set to x ∗x mod z = 81 mod 11 = 4, and
n is set to 3.
Since n = 3 > 0, the body of the while loop executes.
Since n mod 2 is equal to 1, result is set to (result∗x) mod z =
20 mod 11 = 9. x is set to x ∗x mod z = 16 mod 11 = 5, and
n is set to 1.
Since n = 1 > 0, the body of the while loop executes.
Since n mod 2 is equal to 1, result is set to (result∗x) mod z =
45 mod 11 = 1. x is set to x ∗x mod z = 25 mod 11 = 3, and
n is set to 0.
Since n = 0 is not greater than 0, the while loop
terminates. The algorithm returns result, which is equal to
an mod z = 5030 mod 11 = 1.

<!-- pagina 40 -->
672
Hints and Solutions to Selected Exercises
11. [Section 5.3] The nonzero remainders in the order they are
computed by the Euclidean algorithm are
480 mod 396 = 84
396 mod 84 = 60
84 mod 60 = 24
60 mod 24 = 12.
Writing these equations in the form r = n −dq, where r is the
remainder and q is the quotient, yields
84 = 480 −396 ·1
60 = 396 −84 ·4
24 = 84 −60 ·1
12 = 60 −24 ·2.
Substituting the next-to-last formula for 24 into the last equa-
tion yields
12 = 60 −24 ·2 = 60 −(84 −60) ·2 = 3 ·60 −2 ·84.
Substituting the second formula for 60 into the previous equa-
tion yields
12 = 3 ·(396 −84 ·4) −2 ·84 = 3 ·396 −14 ·84.
Finally, substituting the ﬁrst formula for 84 into the previous
equation yields
12 = 3 ·396 −14 ·(480 −396) = 17 ·396 −14 ·480.
Thus, if we set s = 17 and t = −14,
s ·396 + t ·480 = gcd(396, 480) = 12.
12. [Section 5.3] The nonzero remainders in the order they are
computed by the Euclidean algorithm are
425 mod 196 = 33
196 mod 33 = 31
33 mod 31 = 2
31 mod 2 = 1.
Writing these equations in the form r = n −dq, where r is the
remainder and q is the quotient, yields
33 = 425 −196 ·2
31 = 196 −33 ·5
2 = 33 −31 ·1
1 = 31 −2 ·15.
Substituting the next-to-last formula for 2 into the last equa-
tion yields
1 = 31 −(33 −31) ·15 = 16 ·31 −15 ·33.
Substituting the second formula for 31 into the previous equa-
tion yields
1 = 16 ·(196 −33 ·5) −15 ·33 = 16 ·196 −95 ·33.
Finally, substituting the ﬁrst formula for 33 into the previous
equation yields
1 = 16 ·196 −95 ·(425 −196 ·2) = 206 ·196 −95 ·425.
Thus, if we set s′ = 206 and t′ = −95,
s′ ·196 + t′ ·425 = gcd(196, 425) = 1.
Thus s = s′ mod 425 = 206 mod 425 = 206.
13. [Section 5.4] z = pq = 13 ·17 = 221, φ = (p −1)(q −1) =
12 ·16 = 192
14. [Section 5.4] s = 91
15. [Section 5.4] c = an mod z = 14419 mod 221 = 53
16. [Section 5.4] a = cs mod z = 2891 mod 221 = 63
Section 6.1 Review
1. If an activity can be constructed in t successive steps and
step 1 can be done in n1 ways, step 2 can be done in n2 ways,
. . . , and step t can be done in nt ways, then the number of
diﬀerent possible activities is n1 ·n2 · · · nt. As an example, if
there are two choices for an appetizer and four choices for a
main dish, the total number of dinners is 2 ·4 = 8.
2. Suppose that X1, . . . , Xt are sets and that the ith set Xi has
ni elements. If {X1, . . . , Xt} is a pairwise disjoint family, the
number of possible elements that can be selected from X1 or
X2 or . . . or Xt is n1 + n2 + · · · + nt. As an example, suppose
that within a set of strings, two start with a and four start with
b. Then 2 + 4 = 6 start with either a or b.
3. |X ∪Y| = |X| + |Y| −|X ∩Y|. An example of the use of
the Inclusion-Exclusion Principle for two sets is provided by
Example 6.1.14.
Section 6.1
1. 2 ·4
4. 8 ·4 ·5
7. 62
10. 5 ·4 ·3
13. 6 + 12 + 9
16. m + n
19. 1 + 1
22. There are 5 ·4 ·3 strings that begin with AC and 5 ·4 ·3
strings that begin with DB. Thus the answer is 5 ·4 ·3 +
5 ·4 ·3.
25. Since there are three kinds of cabs, two kinds of cargo beds,
and ﬁve kinds of engines, the correct number of ways to per-
sonalize the big pickups is 3 · 2 · 5 = 30, not 32.
26. 3: (1, 3), (2, 2), (3, 1), where (b, r) means the blue die shows
b and the red die shows r.
29. 6: (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), where (b, r)
means the blue die shows b and the red die shows r.
32. Since each die can show any one of ﬁve values, by the Mul-
tiplication Principle there are 5 ·5 outcomes in which neither
die shows 2.
34. 10 ·5
37. 24
40. 8
43. 24. (Once the ﬁrst four bits are assigned values, the last four
bits are determined.)

<!-- pagina 41 -->
Hints and Solutions to Selected Exercises
717
23. False. Consider the ﬂow
a
b
z
1, 1
2, 1
and the cut P = {a, b}.
Section 10.4 Review
In the solutions to Exercises 1–5, G is a directed, bipartite graph
with disjoint vertex sets V and W in which the edges are directed
from V to W.
1. A matching for G is a set of edges with no vertices in common.
2. A maximal matching for G is a matching containing the max-
imum number of edges.
3. A complete matching for G is a matching E having the prop-
erty that if v ∈V, then (v, w) ∈E for some w ∈W.
4. Add a supersource a and edges from a to each vertex in V. Add
a supersink z and edges from each vertex in W to z. Assign all
edges capacity 1. We call the resulting network a matching
network. Then, a ﬂow in the matching network gives a match-
ing in G [v is matched with w if and only if the ﬂow in edge
(v, w) is 1]; a maximal ﬂow corresponds to a maximal match-
ing; and a ﬂow whose value is |V| corresponds to a complete
matching.
5. If S ⊆V, let
R(S) = {w ∈W | v ∈S and (v, w) is an edge in G}.
Hall’s Marriage Theorem states that there exists a complete
matching in G if and only if |S| ≤|R(S)| for all S ⊆V.
Section 10.4
1. P = {a, A, B, D, J2, J5}
3. Finding qualiﬁed persons for jobs
6. Finding qualiﬁed persons for all jobs
9. All unlabeled edges are 1, 0. There is no complete matching.
A
B
C
D
E
F
J1
1, 1
1, 1
1, 1
1, 1
1, 1
1, 1
1, 1
1, 1
1, 1
1, 1
1, 1
1, 1
1, 1
1, 1
1, 1
a
z
J2
J3
J4
J5
13. Each row and column has at most one label.
17. If δ(G) = 0, then |S| −|R(S)| ≤0, for all S ⊆V. By Theo-
rem 10.4.7, G has a complete matching.
If G has a complete matching, then |S| −|R(S)| ≤0,
for all S ⊆V, so δ(G) ≤0. If S = ∅, |S| −|R(S)| = 0, so
δ(G) = 0.
Chapter 10 Self-Test
1. [Section 10.1] In each edge, the ﬂow is less than or equal to
the capacity and, except for the source and sink, the ﬂow into
each vertex v is equal to the ﬂow out of v.
2. [Section 10.1] 3
3. [Section 10.1] 3
4. [Section 10.1] 3
5. [Section 10.2] (a, b, e, f, g, z)
6. [Section 10.2] Change the ﬂows to Fa,b = 2, Fe,b = 1,
Fe,f = 1, Ff,g = 1, Fg,z = 1.
7. [Section 10.2] Fa,b = 3, Fb,c = 3, Fc,d = 4, Fd,z = 4,
Fa,e = 2, Fe,f = 2, Ff,c = 2, Ff,g = 1, Fg,z = 1, and all
other edge ﬂows zero.
8. [Section 10.2] Fa,b = 0, Fb,c = 5, Fc,d = 5, Fd,z = 8,
Fe,b = 3, Fg,d = 3, Fa,e = 8, Fe,f = 3, Ff,g = 3, Fa,h = 4,
Fe,i = 2, Fj,z = 6, Fh,i = 4, Fi,j = 6, and all other edge ﬂows
zero.
9. [Section 10.3] a—True, b—False, c—False, d—True
10. [Section 10.3] 6
11. [Section 10.3] No. The capacity of (P, P) is 6, but the capacity
of (P′, P′), P′ = {a, b, c, e, f}, is 5.
12. [Section 10.3] P = {a, b, c, e, f, g, h, i}
13. [Section 10.4]
A
B
C
D
J1
a
z
J2
J3
J4
J5
14. [Section 10.4] See the solution to Exercise 13.
15. [Section 10.4] A −J2, B −J1, C −J3, D −J5 is a complete
matching.
16. [Section 10.4] P = {a}
Section 11.1 Review
1. A combinatorial circuit is a circuit in which the output is
uniquely deﬁned for every combination of inputs.
2. A sequential circuit is a circuit in which the output is a function
of the input and state of the system.
3. An AND gate receives input x1 and x2, where x1 and x2 are
bits, and produces output 1 if x1 and x2 are both 1, and 0 oth-
erwise.
4. An OR gate receives input x1 and x2, where x1 and x2 are bits,
and produces output 0 if x1 and x2 are both 0, and 1 otherwise.

<!-- pagina 42 -->
718
Hints and Solutions to Selected Exercises
5. A NOT gate receives input x, where x is a bit, and produces
output 1 if x is 0, and 0 if x is 1.
6. An inverter is a NOT gate.
7. A logic table of a combinatorial circuit lists all possible inputs
together with the resulting outputs.
8. Boolean expressions in the symbols x1, . . . , xn are deﬁned
recursively as follows. 0, 1, x1, . . . , xn are Boolean expres-
sions. If X1 and X2 are Boolean expressions, then (X1), X1,
X1 ∨X2, and X1 ∧X2 are Boolean expressions.
9. A literal is the symbol x or x that appears in a Boolean
expression.
Section 11.1
1. x1 ∧x2
x1
x2
x1 ∧x2
1
1
0
1
0
1
0
1
1
0
0
1
x1
x2
x1       x2
x1       x2
4.
x1
x2
x3
((x1 ∧x2) ∨(x1 ∧x3)) ∧x3
1
1
1
0
1
1
0
1
1
0
1
0
1
0
0
1
0
1
1
0
0
1
0
1
0
0
1
0
0
0
0
1
7. If x = 1, the output y is undetermined: Suppose that x = 1
and y = 0. Then the input to the AND gate is 1, 0. Thus the
output of the AND gate is 0. Since this is then NOTed, y = 1.
Contradiction. Similarly, if x = 1 and y = 1, we obtain a
contradiction.
10. 0
13. 1
16. Is a Boolean expression. x1, x2, and x3 are Boolean expres-
sions by (11.1.2). x2 ∨x3 is a Boolean expression by (11.1.3c).
(x2 ∨x3) is a Boolean expression by (11.1.3a). x1 ∧(x2 ∨x3)
is a Boolean expression by (11.1.3d).
19. Not a Boolean expression
22.
B
A
25. (A ∧B) ∨(C ∧A)
A
B
C
(A ∧B) ∨(C ∧A)
1
1
1
1
1
1
0
1
1
0
1
0
1
0
0
0
0
1
1
1
0
1
0
0
0
0
1
1
0
0
0
0
27. (A ∧(C ∨(D ∧C))) ∨(B ∧(D ∨(C ∧A) ∨C))
29.
A
B
(A ∨B) ∧A
1
1
1
1
0
1
0
1
0
0
0
0
A
A
B
32.
A
A
B
C
B
C
B
C
Section 11.2 Review
1. (a ∨b) ∨c = a ∨(b ∨c), (a ∧b) ∧c = a ∧(b ∧c)
2. a ∨b = b ∨a, a ∧b = b ∧a
3. a∧(b∨c) = (a∧b)∨(a∧c), a∨(b∧c) = (a∨b)∧(a∨c)
4. a ∨0 = a, a ∧1 = a
5. a ∨a = 1, a ∧a = 0
6. Boolean expressions are equal if they have the same values for
all possible assignments of bits to the literals.
7. Combinatorial circuits are equivalent if, whenever the circuits
receive the same inputs, they produce the same outputs.
8. Let C1 and C2 be combinatorial circuits represented, respec-
tively, by the Boolean expressions X1 and X2. Then C1 and C2
are equivalent if and only if X1 = X2.

<!-- pagina 43 -->
Hints and Solutions to Selected Exercises
719
Section 11.2
1.
x1
x2
x1 ∧x2
x1 ∨x2
1
1
0
0
1
0
1
1
0
1
1
1
0
0
1
1
4.
x1
x2
x3
x1 ∨(x2 ∨x3)
(x1 ∧x2) ∨x3
1
1
1
1
1
1
1
0
0
0
1
0
1
1
1
1
0
0
1
1
0
1
1
1
1
0
1
0
1
1
0
0
1
1
1
0
0
0
1
1
6.
x1
x1 ∨x1
1
1
0
0
9.
x1
x2
x3
x1 ∧(x2 ∧x3)
(x1 ∧x2) ∨(x1 ∧x3)
1
1
1
0
0
1
1
0
1
1
1
0
1
1
1
1
0
0
1
1
0
1
1
0
0
0
1
0
0
0
0
0
1
0
0
0
0
0
0
0
11.
x
x
1
1
0
0
14. False. Take x1 = 1, x2 = 1, x3 = 0.
16.
a
b
c
a ∨(b ∧c)
(a ∨b) ∧(a ∨c)
1
1
1
1
1
1
1
0
1
1
1
0
1
1
1
1
0
0
1
1
0
1
1
1
1
0
1
0
0
0
0
0
1
0
0
0
0
0
0
0
18. The Boolean expressions that represent the circuits are
(A ∧B) ∨(A ∧C) and A ∧(B ∨C). The expressions are equal
by Theorem 11.2.1(c). Therefore, the switching circuits are
equivalent.
21.
A
C
D
E
B
F
Section 11.3 Review
1. A Boolean algebra consists of a set S containing distinct ele-
ments 0 and 1, binary operators + and ·, and a unary opera-
tor ′ on S satisfying the associative, commutative, distributive,
identity, and complement laws.
2. x + x = x, xx = x
3. x + 1 = 1, x0 = 0
4. x + xy = x, x(x + y) = x
5. (x′)′ = x
6. 0′ = 1, 1′ = 0
7. (x + y)′ = x′y′, (xy)′ = x′ + y′
8. The dual of a Boolean expression is obtained by replacing 0
by 1, 1 by 0, + by ·, and · by +.
9. The dual of a theorem about Boolean algebras is also a theo-
rem.
Section 11.3
2. One can show that the associative and distributive laws hold
for lcm and gcd directly. The commutative law clearly holds.
To see that the identity laws hold, note that
lcm(x, 1) = x
and
gcd(x, 6) = x.
Since
lcm(x, 6/x) = 6
and
gcd(x, 6/x) = 1,
the complement laws hold. Therefore, (S, +, ·,′ , 1, 6) is a
Boolean algebra.
4. We show only
x ·(x + z) = (x ·y) + (x ·z)
for all x, y, z ∈Sn.
Now
x ·(y + z) = min{x, max{y, z}}
(x ·y) + (x ·z) = max{min{x, y}, min{x, z}}.
We assume that y ≤z. (The argument is similar if y > z.)
There are three cases to consider: x < y; y ≤x ≤z; and z < x.
If x < y, we obtain
x ·(y + z) = min{x, max{y, z}}
= min{x, z} = x = max{x, x}
= max{min{x, y}, min{x, z}}
= (x ·y) + (x ·z).

<!-- pagina 44 -->
720
Hints and Solutions to Selected Exercises
If y ≤x ≤z, we obtain
x ·(y + z) = min{x, max{y, z}}
= min{x, z} = x = max{y, x}
= max{min{x, y}, min{x, z}}
= (x ·y) + (x ·z).
If z < x, we obtain
x ·(y + z) = min{x, max{y, z}}
= min{x, z} = z = max{y, z}
= max{min{x, y}, min{x, z}}
= (x ·y) + (x ·z).
7. If X ∪Y = U and X ∩Y = ∅, then Y = X.
8. xy + x0 = x(x + y)y
11. x + y′ = 1 if and only if x + y = x.
14. x(x + y0) = x
15. (For Exercise 13)
0 = x + y = (x + x) + y
= x + (x + y) = x + 0 = x
Similarly, y = 0.
18. [For part (c)]
x(x + y) = (x + 0)(x + y)
= x + 0y = x + y0 = x + 0 = x
21. First, show that if ba = ca and ba′ = ca′, then b = c. Now
take a = x, b = x + (y + z), and c = (x + y) + z and use this
result.
23. If the prime p divides n, p2 does not divide n.
Section 11.4 Review
1. The exclusive-OR of x1 and x2 is 0 if x1 = x2, and 1 otherwise.
2. A Boolean function is a function of the form
f(x1, . . . , xn) = X(x1, . . . , xn),
where X is a Boolean expression.
3. A minterm is a Boolean expression of the form
y1 ∧y2 ∧· · · ∧yn,
where each yi is either xi or xi.
4. The disjunctive normal form of a not identically zero Boolean
function f is
f(x1, . . . , xn) = m1 ∨m2 ∨· · · ∨mk,
where each mi is a minterm.
5. Let A1, . . . , Ak denote the elements Ai of Zn
2 for which f(Ai) =
1. For each Ai = (a1, . . . , an), set mi = y1 ∧· · · ∧yn, where
yj = xj if aj = 1, and yj = xj if aj = 0. Then
f(x1, . . . , xn) = m1 ∨m2 ∨· · · ∨mk.
6. A maxterm is a Boolean expression of the form
y1 ∨y2 ∨· · · ∨yn,
where each yi is either xi or xi.
7. The conjunctive normal form of a not identically one Boolean
function f is
f(x1, . . . , xn) = m1 ∧m2 ∧· · · ∧mk,
where each mi is a maxterm.
Section 11.4
In these hints, a ∧b is written ab.
1. xy ∨xy ∨x y
4. xyz ∨xyz ∨xy z ∨xyz ∨xyz
7. xyz ∨xy z ∨x y z
10. wxyz ∨wxy z ∨wxyz ∨wxyz ∨wx y z
∨wxyz ∨wxyz ∨wxy z ∨w xyz ∨w x y z
11. xy ∨xy
14. xyz
17. xyz ∨xyz ∨xyz ∨xyz
20. 0
22. 22n
25. (For Exercise 3)
(x ∨y ∨z)(x ∨y ∨z)(x ∨y ∨z)
28. (For Exercise 3)
(x ∨y ∨z)(x ∨y ∨z)(x ∨y ∨z)(x ∨y ∨z)(x ∨y ∨z)
Section 11.5 Review
1. A gate is a function from Zn
2 into Z2.
2. A set of gates G is functionally complete if, given any posi-
tive integer n and a function f from Zn
2 into Z2, it is possible
to construct a combinatorial circuit that computes f using only
the gates in G.
3. {AND, OR, NOT}
4. A NAND gate receives input x1 and x2, where x1 and x2 are
bits, and produces output 0 if x1 and x2 are both 1, and 1 oth-
erwise.
5. Yes
6. The problem of ﬁnding the best circuit
7. Small components that are themselves entire circuits
8. See Figure 11.5.8.
9. See Figure 11.5.9.
Section 11.5
1. AND can be expressed in terms of OR and NOT: xy = x ∨y.
2. A combinatorial circuit consisting only of AND gates would
always output 0 when all inputs are 0.
5. We use induction on n to show that there is no n-gate com-
binatorial circuit consisting of only AND and OR gates that
computes f(x) = x.

<!-- pagina 45 -->
Hints and Solutions to Selected Exercises
721
If n = 0, the input x equals the output x, and so it is
impossible for a 0-gate circuit to compute f. The Basis Step is
proved.
Suppose that there is no n-gate combinatorial circuit
consisting of only AND and OR gates that computes f. Con-
sider an (n + 1)-gate combinatorial circuit consisting of only
AND and OR gates. The input x ﬁrst arrives at either an AND
or an OR gate. Suppose that x ﬁrst arrives at an AND gate.
(The argument is similar if x ﬁrst arrives at an OR gate and
is omitted.) Because the circuit is a combinatorial circuit, the
other input to the AND gate is either x itself, the constant 1,
or the constant 0. If both inputs to the AND gate are x itself,
then the output of the AND gate is equal to the input. In this
case, the behavior of the circuit is unchanged if we remove
the AND gate and connect x to what was the output line of
the AND gate. But we now have an equivalent n-gate circuit,
which, by the inductive hypothesis, cannot compute f. Thus
the (n + 1)-gate circuit cannot compute f.
If the other input to the AND gate is the constant 1, the
output of the AND gate is again equal to the input and we can
argue as in the previous case that the (n+1)-gate circuit cannot
compute f.
If the other input to the AND gate is the constant 0, the
AND gate always outputs 0 and, so, changing the value of x
does not aﬀect the output of the circuit. In this case, the cir-
cuit cannot compute f. The Inductive Step is complete. There-
fore, no n-gate combinatorial circuit consisting of only AND
and OR gates can compute f(x) = x. Thus {AND, OR} is not
functionally complete.
6.
x
y
9. y1 = x1x2 ∨(x2 ∨x3); y2 = x2 ∨x3
12. (For Exercise 3) The dnf may be simpliﬁed to xy∨xz∨x y and
then rewritten as x(y ∨z) ∨x y = (xyz) ∨x y = xyz x y, which
gives the circuit
x
y
z
15.
x
y
s
c
17. xy = (x ↓x) ↓(y ↓y)
x ∨y = (x ↓y) ↓(x ↓y) x = x ↓x
x ↑y = [(x ↓x) ↓(y ↓y)] ↓[(x ↓x) ↓(y ↓y)]
20. Since
x = x ↓x,
x ∨y = (x ↓y) ↓(x ↓y),
and {NOT, OR} is functionally complete, {NOR} is function-
ally complete.
23.
x
y
s
c
25. The logic table is
x
y
z
Output
1
1
1
1
1
1
0
1
1
0
1
1
1
0
0
0
0
1
1
1
0
1
0
0
0
0
1
0
0
0
0
0
27. The logic table is
b
FLAGIN
c
FLAGOUT
1
1
0
1
1
0
1
1
0
1
1
1
0
0
0
0
Thus c = b ⊕FLAGIN and FLAGOUT = b ∨FLAGIN. We
obtain the circuit
b
c
FLAGIN
FLAGOUT
28. 010100

<!-- pagina 46 -->
722
Hints and Solutions to Selected Exercises
31.
2's
b
c
2's
b
c
2's
b
c
FLAGIN FLAGOUT/FLAGIN
FLAGOUT/FLAGIN
0
y1
x1
y2
x2
y3
x3
module
module
module
34. Writing the truth tables shows that
x = x →0,
x ∨y = (x →0) →y.
Therefore a NOT gate can be replaced by one →gate, and an
OR gate can be replaced by two →gates. Since the set {NOT,
OR} is functionally complete, it follows that the set {→} is
functionally complete.
Chapter 11 Self-Test
1. [Section 11.1]
x
y
z
(x ∧y) ∨z
1
1
1
1
1
1
0
1
1
0
1
1
1
0
0
0
0
1
1
1
0
1
0
1
0
0
1
1
0
0
0
1
2. [Section 11.2] The circuits are equivalent. The logic table for
either circuit is
x
y
Output
1
1
0
1
0
1
0
1
0
0
0
0
3. [Section 11.2] The circuits are not equivalent. If x = 0, y = 1,
and z = 0, the output of circuit (a) is 1, but the output of circuit
(b) is 0.
4. [Section 11.3] Bound laws:
X ∪U = U,
X ∩∅= ∅
for all X ∈S.
Absorption laws:
X ∪(X ∩Y) = X,
X ∩(X ∪Y) = X
for all X, Y ∈S.
5. [Section 11.1] 1
6. [Section 11.1]
x1
x2
x3
7. [Section 11.2] The equation is true. The logic table for either
expression is
x
y
z
Value
1
1
1
1
1
1
0
1
1
0
1
0
1
0
0
0
0
1
1
1
0
1
0
1
0
0
1
1
0
0
0
0
8. [Section 11.2] The equation is false. If x = 1, y = 0, and
z = 1, then
(x ∧y ∧z) ∨(x ∨z) = 0,
but
(x ∧z) ∨(x ∧z) = 1.
9. [Section 11.1] Suppose that x is 1. Then the upper input to the
OR gate is 0. If y is 1, then the lower input to the OR gate is 0.
Since both inputs to the OR gate are 0, the output y of the OR
gate is 0, which is impossible. If y is 0, then the lower input to
the OR gate is 1. Since an input to the OR gate is 1, the output
y of the OR gate is 1, which is impossible. Therefore, if the
input to the circuit is 1, the output is not uniquely determined.
Thus the circuit is not a combinatorial circuit.
10. [Section 11.3] (x(x + y ·0))′ = (x(x + 0))′
(Bound law)
= (x ·x)′
(Identity law)
= x′
(Idempotent law)
11. [Section 11.3] Dual: (x + x(y + 1))′ = x′
(x + x(y + 1))′ = (x + x ·1)′
(Bound law)
= (x + x)′
(Identity law)
= x′
(Idempotent law)
12. [Section 11.3]
is not a unary operator on S. For example,
{1, 2} /∈S.
In Exercises 13–16, a ∧b is written ab.
13. [Section 11.4] x1x2x3
x1
x2
x3

<!-- pagina 47 -->
Hints and Solutions to Selected Exercises
723
14. [Section 11.4] x1x2x3 ∨x1x2x3
x1
x2
x3
15. [Section 11.4] x1x2x3 ∨x1x2x3 ∨x1x2x3
x1
x2
x3
16. [Section 11.4] x1x2x3 ∨x1x2x3 ∨x1x2x3 ∨x1x2x3
17. [Section 11.5]
x
y
z
Output
1
1
1
1
1
1
0
0
1
0
1
1
1
0
0
0
0
1
1
0
0
1
0
0
0
0
1
1
0
0
0
0
18. [Section 11.5] Disjunctive normal form: xyz∨xy z∨xyz∨x y z
(xyz ∨xy z) ∨xyz ∨x y z = xy ∨(xyz ∨x y z)
= xy ∨x z
x
y
z
19. [Section 11.5]
x
y
x ⊕y
20. [Section 11.5]
x
y
z
Half
adder
Half
adder
c9
s9
c99
s99
c
s
Section 12.1 Review
1. A unit time delay accepts as input a bit xt at time t and outputs
xt−1, the bit received as input at time t −1.
2. A serial adder inputs two binary numbers and outputs their
sum.
3. A ﬁnite-state machine consists of a ﬁnite set I of input sym-
bols, a ﬁnite set O of output symbols, a ﬁnite set S of states,
a next-state function f from S × I into S, an output function
g from S × I into O, and an initial state σ ∈S.
4. Let M = (I, O, S, f, g, σ) be a ﬁnite-state machine. The
transition diagram of M is a digraph G whose vertices
are the states. An arrow designates the initial state. A di-
rected edge (σ1, σ2) exists in G if there exists an input i with
f(σ1, i) = σ2. In this case, if g(σ1, i) = o, the edge (σ1, σ2) is
labeled i/o.
5. The SR ﬂip-ﬂop is deﬁned by the table
S
R
Q
1
1
Not allowed
1
0
1
0
1
0
0
0
2
1
ifSwaslastequalto1
0
ifRwaslastequalto1
Section 12.1
1.
a/0
a/1
b/1
b/1
0
1
4.
a/0
a/1
b/1
a/1
b/0
c/0
c/0
c/1
b/1
0
1
2
6. I = {a, b}; O = {0, 1}; S = {σ0, σ1}; initial state = σ0
I
a
b
a
b
S
σ0
σ1
σ0
0
1
σ1
σ1
σ1
1
1

<!-- pagina 48 -->
724
Hints and Solutions to Selected Exercises
9. I = {a, b}; O = {0, 1}; S = {σ0, σ1, σ2, σ3}; initial state = σ0
I
a
b
a
b
S
σ0
σ1
σ2
0
0
σ1
σ0
σ2
1
0
σ2
σ3
σ0
0
1
σ3
σ1
σ3
0
0
11. 1110
14. 001110
17. 20210
20. 020022201020
21.
E
O
1/0
1/1
0/0
0/1
24.
0/0
1/0
1/1
1/0
0/0
0/0
0
1
2
27. When γ is input, the machine outputs xn, xn−1, . . . until
xi
= 1. Thereafter, it outputs xi. However, according to
Algorithm 11.5.16, this is the 2’s complement of α.
Section 12.2 Review
1. A ﬁnite-state automaton consists of a ﬁnite set I of input sym-
bols, a ﬁnite set S of states, a next-state function f from S ×I
into S, a subset A of S of accepting states, and an initial state
σ ∈S.
2. A string is accepted by a ﬁnite-state automaton A if, when the
string is input to A, the last state reached is an accepting state.
3. Finite-state automata are equivalent if they accept precisely
the same strings.
24.
b
b
b
a
a
a
a
b
0
1
2
3
Section 12.2
1. All incoming edges to σ0 output 1 and all incoming edges to
σ1 output 0; hence the ﬁnite-state machine is a ﬁnite-state au-
tomaton.
a
b
b
a
0
1
4.
a/0
a/1
b/0
b/0
0
1
7.
b
a
b
a
a
b
0
1
2
10. (For Exercise 1) I = {a, b}; S = {σ0, σ1}; A = {σ0}; initial
state = σ0
I
a
b
S
σ0
σ0
σ1
σ1
σ1
σ0
13. Accepted
16. Accepted
18. No matter which state we are in, after an a we move to an
accepting state; however, after a b we move to a nonaccepting
state.
21.
b
Even
Odd
b
a
a

<!-- pagina 49 -->
Hints and Solutions to Selected Exercises
725
27.
a
b
a
a
b
a
b
a
b
b
0
1
2
3
4
30.
a
b
b
a
b
a
b
a
0
1
2
3
32. (For Exercise 1) This algorithm determines whether a string
over {a, b} is accepted by the ﬁnite-state automaton whose
transition diagram is given in Exercise 1.
Input:
n, the length of the string (n = 0 designates the
null string); s1 · · · sn, the string
Output:
“Accept” if the string is accepted
“Reject” if the string is not accepted
ex32(s, n) {
state = ‘σ0’
for i = 1 to n {
if (state == ‘σ0’ ∧si == ‘b’)
state = ‘σ1’
if (state == ‘σ1’ ∧si == ‘b’)
state = ‘σ0’
}
if (state == ‘σ0’)
return “Accept”
else
return “Reject”
}
35. Make each accepting state nonaccepting and each nonaccept-
ing state accepting.
38. Using the construction given in Exercises 36 and 37, we ob-
tain the following ﬁnite-state automaton that accepts L1 ∩L2.
(We designate the states in Exercise 6 with primes.)
The ﬁnite-state automaton that accepts L1 ∪L2 is the
same as the ﬁnite-state automaton that accepts L1 ∩L2 except
that the set of accepting states is
{(σ1, σ ′
0),
(σ1, σ ′
1),
(σ1, σ ′
2),
(σ0, σ ′
2)}.
b
a
a
a
a
b
b
b
a
a
b
b
h             j
0,
19
h             j
1,
19
h             j
1,
29
h             j
1,
09
h             j
0,
19
h             j
0,
29
41. Use the construction of Exercises 36 and 37.
Section 12.3 Review
1. A “natural language” refers to ordinary written and spoken
words and combinations of words. A “formal language” is
an artiﬁcial language consisting of a speciﬁed set of strings.
Formal languages are used to model natural languages and to
communicate with computers.
2. A phrase-structure grammar consists of a ﬁnite set N of
nonterminal symbols, a ﬁnite set T of terminal symbols where
N ∩T = ∅, a ﬁnite subset of [(N ∪T)∗−T∗] × (N ∪T)∗
called the set of productions, and a starting symbol in N.
3. If α →β is a production and xαy ∈(N ∪T)∗, we say that xβy
is directly derivable from xαy.
4. If αi ∈(N∪T)∗for i = 1, . . . , n, and αi+1 is directly derivable
from αi for i = 1, . . . , n −1, we say that αn is derivable from
α1 and write α1 ⇒αn.

<!-- pagina 50 -->
726
Hints and Solutions to Selected Exercises
5. We call α1 ⇒α2 ⇒· · · ⇒αn a derivation of αn from α1.
6. The language generated by a grammar consists of all strings
in terminals derivable from the start symbol.
7. Backus normal form (BNF) is a way to write the productions
of a grammar. In BNF the nonterminal symbols typically begin
with “⟨” and end with “⟩”. Also the arrow →is replaced with
::=. Productions with the same left-hand side are combined
using the bar “|”. An example is
⟨signed integer⟩::=
+ ⟨unsigned integer⟩| −⟨unsigned integer⟩
8. In a context-sensitive grammar, every production is of the form
αAβ →αδβ, where α, β ∈(N ∪T)∗, A ∈N, and δ ∈
(N ∪T)∗−{λ}.
9. In a context-free grammar, every production is of the form
A →δ, where A ∈N and δ ∈(N ∪T)∗.
10. In a regular grammar, every production is of the form A →a,
A →aB, or A →λ, where A, B ∈N and a ∈T.
11. A context-sensitive grammar
12. A context-free grammar
13. A regular grammar
14. A language is context-sensitive if there is a context-sensitive
grammar that generates it.
15. A language is context-free if there is a context-free grammar
that generates it.
16. A language is regular if there is a regular grammar that gener-
ates it.
17. A context-free, interactive Lindenmayer grammar consists of
a ﬁnite set N of nonterminal symbols; a ﬁnite set T of terminal
symbols where N ∩T = ∅; a ﬁnite set of productions A →B,
where A ∈N ∪T and B ∈(N ∪T)∗; and a starting symbol
in N.
18. The von Koch snowﬂake is generated by the context-free, in-
teractive Lindenmayer grammar
N = {D}
T = {d, +, −}
P = {D →D −D + + D −D, D →d, + →+,
−→−}.
d means “draw a straight line of a ﬁxed length in the current
direction,” + means “turn right by 60◦,” and −means “turn
left by 60◦.”
19. Fractal curves are characterized by having a part of the whole
curve resemble the whole.
Section 12.3
1. Regular, context-free, context-sensitive
4. Context-free, context-sensitive
7. σ ⇒bσ ⇒bbσ ⇒bbaA ⇒bbabA ⇒bbabbA ⇒
bbabbaσ ⇒bbabbab
10. σ ⇒ABA ⇒ABBA ⇒ABBAA
⇒ABBaAA ⇒abBBaAA ⇒abbBaAA
⇒abbbaAA ⇒abbbaabA ⇒abbbaabab
12. (For Exercise 1)
<σ > ::= b<σ > | a<A> | b
< A > ::= a<σ > | b<A> | a
15. S →aA, A →aA, A →bA, A →a,
A →b, S →a
18. S →aA, S →bS, S →λ, A →aA,
A →bB, A →λ, B →aA, B →bS
21. <exp number> ::= <integer> E <integer> |
<ﬂoat number> |
<ﬂoat number> E <integer>
24. S →aSa, S →bSb, S →a, S →b, S →λ
25. If a derivation begins S ⇒aSb, the resulting string begins with
a and ends with b. Similarly, if a derivation begins S ⇒bSa,
the resulting string begins with b and ends with a. Therefore,
the grammar does not generate the string abba.
28. If a derivation begins S ⇒abS, the resulting string begins
ab. If a derivation begins S ⇒baS, the resulting string begins
ba. If a derivation begins S ⇒aSb, the resulting string starts
with a and ends with b. If a derivation begins S ⇒bSa, the
resulting string begins with b and ends with a. Therefore, the
grammar does not generate the string aabbabba.
31. The grammar does generate L, the set of all strings over {a, b}
with equal numbers of a’s and b’s.
Any string generated by the grammar has equal num-
bers of a’s and b’s since whenever any of the productions are
used in a derivation, equal numbers of a’s and b’s are added to
the string.
To prove the converse, we consider an arbitrary string α
in L, and we use induction on the length |α| of α to show that
α is generated by the grammar. The Basis Step is |α| = 0. In
this case, α is the null string, and S ⇒λ is a derivation of α.
Let α be a nonnull string, and suppose that any string in
L whose length is less than |α| is generated by the grammar.
We ﬁrst consider the case that α starts with a. Then α can be
written α = aα1bα2, where α1 and α2 have equal numbers of
a’s and b’s. By the inductive hypothesis, there are derivations
S ⇒α1 and S ⇒α2 of α1 and α2. But now
S ⇒aSbS ⇒aα1bα2
is a derivation of α. Similarly, if α starts with b, there is a
derivation of α. The Inductive Step is ﬁnished, and the proof
is complete.
32. Replace each production
A →x1 · · · xnB,
where n > 1, xi ∈T, and B ∈N, with the productions
A →x1A1
A1 →x2A2
...
An−1 →xnB,
where A1, . . . , An−1 are additional nonterminal symbols.

<!-- pagina 51 -->
Hints and Solutions to Selected Exercises
727
35. S ⇒D + D + D + D ⇒d + d + d + d
S ⇒D + D + D + D
⇒D + D −D −DD + D + D −D
+ D + D −D −DD + D + D −D
+ D + D −D −DD + D + D −D
+ D + D −D −DD + D + D −D
⇒d + d −d −dd + d + d −d
+ d + d −d −dd + d + d −d
+ d + d −d −dd + d + d −d
+ d + d −d −dd + d + d −d
START
Section 12.4 Review
1. Let σ be the start state, let T be the set of input symbols, and let
N be the set of states. Let P be the set of productions S →xS′,
if there is an edge labeled x from S to S′, and S →λ if S is
an accepting state. Let G be the regular grammar (N, T, P, σ).
Then the set of strings accepted by A is equal to L(G).
2. A nondeterministic ﬁnite-state automaton consists of a ﬁnite
set I of input symbols, a ﬁnite set S of states, a next-state
function f from S ×I into P(S), a subset A of S of accepting
states, and an initial state σ ∈S.
3. A string α is accepted by a nondeterministic ﬁnite-state
automaton A if there is some path representing α in the tran-
sition diagram of A beginning at the initial state and ending in
an accepting state.
4. Nondeterministic ﬁnite-state automata are equivalent if they
accept precisely the same strings.
5. Let G = (N, T, P, σ) be a regular grammar. The ﬁnite-state
automaton A is constructed as follows. The set of input sym-
bols is T. The set of states is N together with an additional
state F /∈N ∪T. The next-state function f is deﬁned as
f(S, x) = {S′ | S →xS′ ∈P} ∪{F | S →x ∈P}.
The set of accepting states is F together with all S for which
S →λ is a production. Then A accepts precisely the strings
L(G).
Section 12.4
1.
a
a
b
b
b
b
0
1
2
4.
a
b
a
c
a
c
b
c
a
a
0
1
2
6.
I = {a, b}; S = {σ0, σ1, σ2}; A = {σ1, σ2};
initial state = σ0
I
a
b
S
σ0
{σ1, σ2}
∅
σ1
{σ1}
{σ0, σ2}
σ2
∅
∅
9. I = {a, b}; S = {σ0, σ1, σ2, σ3}; A = {σ3};
initial state = σ0
I
a
b
S
σ0
{σ0}
{σ0, σ1}
σ1
{σ2}
∅
σ2
∅
{σ3}
σ3
{σ3}
{σ3}
11. (For Exercise 6) N = {σ0, σ1, σ2}, T = {a, b},
σ0 →aσ1,
σ0 →bσ0,
σ1 →aσ0,
σ1 →bσ2,
σ2 →bσ1,
σ2 →aσ0,
σ2 →λ
14. No. For the ﬁrst three characters, bba, the moves are deter-
mined and we end at C. From C, no edge contains an a; there-
fore, bbabab is not accepted.
17. Yes. The path (σ, σ, σ, σ, C, C), which represents the string
aaaab, ends at C, which is an accepting state.

<!-- pagina 52 -->
728
Hints and Solutions to Selected Exercises
21.
a
a
b
b
b
b
a
0
1
2
3
4
24.
a
a
b
b
b
a
a
b
b
a
b
b
b
b
b
b
b
b
b
b
a
b
a
b
a
b
1
0
2
3
4
5
6
7
8
9
10
15
14
13
12
11
27.
a
a
a
b
b
b
a
b
b
a
0
1
2
3
4
5
30. (For Exercise 21) σ0 →aσ1, σ0 →bσ4, σ1 →bσ2,
σ2 →bσ3, σ3 →aσ3, σ3 →bσ3, σ4 →aσ3, σ3 →λ
Section 12.5 Review
1. Let A = (I, S, f, A, σ) be a nondeterministic ﬁnite-state au-
tomaton. An equivalent deterministic ﬁnite-state automaton
can be constructed as follows. The set of states is the power
set of S. The set of input symbols is I (unchanged). The start
symbol is {σ} (essentially unchanged). The set of accepting
states consists of all subsets of S that contain at least one ac-
cepting state of A. The next state function is deﬁned by the
rule
f ′(X, x) =
2
∅
ifX = ∅
F
S∈X f(S, x)
ifX̸ = ∅.
2. A language L is regular if and only if there exists a ﬁnite-state
automaton that accepts precisely the strings in L.

<!-- pagina 53 -->
Hints and Solutions to Selected Exercises
729
Section 12.5
1. (For Exercise 1)
a
a
b
b
a
a
a
a
a
b
b
b
b
b
0
2
,
0
2
,
0
1
,
1
2
,
0
1,
2
2.
   , F
A
a
a
b
b
a
b
5.
SBCF
BC
SAF
SACF
SABCF
AC
S
C
A
a
a
b
a
b
b
a
b
b
b
b
a
a
a
b
b
b
a
a
a

<!-- pagina 54 -->
730
Hints and Solutions to Selected Exercises
7. (For Exercise 21)
a
a
b
b
b
b
a
a
a
b
b
a
0
1
2
3
4
5
10. Figure 12.5.7 accepts the string ban, n ≥1, and strings that
end b2 or aban, n ≥1. Using Example 12.5.8, we see that Fig-
ure 12.5.9 accepts the string anb, n ≥1, and strings that start
b2 or anba, n ≥1.
11.
b
a
b
a
0
1
14.
a
a
b
a
b
0
1
17.
b
b
b
a
b
a
b
b
a
a
a
a
1
2
4
3
20.
b
a
b
a
a
a
b
b
a
a
b
a
b
b
a
a
b
b
b
a
0
1
2
3
09
19
29
39
22. σ0 →aσ1, σ0 →bσ2, σ0 →a, σ1 →aσ0,
σ1 →aσ2, σ1 →bσ1, σ1 →b, σ2 →bσ0
25. Suppose that L is regular. Then there exists a ﬁnite-state au-
tomaton A with L = Ac(A). Suppose that A has k states. Con-
sider the string akbbak and argue as in Example 12.5.6.
28. The statement is false. Consider the regular language L =
{anb
|
n
≥
0}, which is accepted by the ﬁnite-state
automaton

<!-- pagina 55 -->
Hints and Solutions to Selected Exercises
731
A
B
a
b
b
S
a
a
b
The language
L′ = {un | u ∈L, n ∈{1, 2, . . . }}
is not regular. Suppose that L′ is regular. Then there is a ﬁnite-
state automaton A that accepts L′. In particular, A accepts anb
for every n. It follows that for suﬃciently large n, the path rep-
resenting anb contains a cycle of length k < n. Since A accepts
anbanb, A also accepts an+kbanb, which is a contradiction.
Chapter 12 Self-Test
1. [Section 12.1]
a/0
a/1
b/0
b/1
0
1
2. [Section 12.1] 1101
3. [Section 12.2]
A
B
1
0
S
0
0
1
1
4. [Section 12.2] Yes
5. [Section 12.3] Context-free
6. [Section 12.3] S
⇒
aSb
⇒
aaSbb
⇒
aaaSbbb
⇒
aaaAbbbb ⇒aaaaAbbbb ⇒aaaabbbb
7. [Section 12.3] aibj, j ≤2 + i, j ≥1, i ≥0
8. [Section 12.4]
a
b
a
b
b
a
a
0
1
2
9. [Section 12.5]
a
b
a
a
b
b
h     j
0
h     j
2
h           j
0,
1
10. [Section 12.1] I = {a, b}; O = {0, 1}; S = {S, A, B}; initial
state = S
f
g
I
a
b
a
b
S
S
A
A
0
0
A
S
B
1
1
B
A
B
1
0
11. [Section 12.1]
S
A
0/1
1/1
1/1
B
C
0/0
0/1
1/0
0/1
1/0
12. [Section 12.2]
S
A
B
C
0
0
0
0
1
1
1
1
13. [Section 12.2] Every 0 is followed by a 1.
14. [Section 12.3] S →ASB, S →AB, AB →BA, BA →AB,
A →a, B →b
15. [Section 12.4] I = {a, b}; S = {σ0, σ1, σ2}; A = {σ0}; initial
state = σ0
I
a
b
S
σ0
{σ0, σ1}
∅
σ1
∅
{σ2}
σ2
{σ0, σ2}
{σ2}
16. [Section 12.4] Yes, since the path
(σ0, σ0, σ1, σ2, σ2, σ2, σ2, σ0)
represents aabaaba and σ0 is an accepting state.

<!-- pagina 56 -->
732
Hints and Solutions to Selected Exercises
17. [Section 12.4]
1
1
0
0
1
0
1
1
0
1
s0
s1
s2
s3
s4
s5
18. [Section 12.5]
a
b
b
a
b
a
b
a
a
b
a
b
h     j
0
h     j
2
h           j
0,
1
h           j
0,
2
h                 j
0,
1,
2
19. [Section 12.5] Combine the nondeterministic ﬁnite-state
automata that accept L1 and L2 in the following way. Let S
be the start state of L2. For each edge of the form (S1, S2)
labeled a in L1 where S2 is an accepting state, add an edge
(S1, S) labeled a. The start state of the nondeterministic ﬁnite-
state automaton is the start state of L1. The accepting states of
the nondeterministic ﬁnite-state automaton are the accepting
states of L2.
20. [Section 12.5] Let A′ be a nondeterministic ﬁnite-state
automaton that accepts a regular language that does not con-
tain the null string. Add a state F. For each edge, (σ, σ ′)
labeled a in A′ where σ ′ is accepting, add the edge (σ, F)
labeled a. Make F the only accepting state. The resulting non-
deterministic ﬁnite-state automaton A has one accepting state.
We claim that Ac(A) = Ac(A′).
We show that Ac(A) ⊆Ac(A′). [The argument that
Ac(A′) ⊆Ac(A) is similar and omitted.] Suppose that
α ∈Ac(A). There is a path
(σ0, σ1, . . . , σn−1, σn)
that represents α in A, with σn an accepting state. Since α̸ = λ,
there is a last symbol a in α. Thus the edge (σn−1, σn) is
labeled a. Now the path
(σ0, σ1, . . . , σn−1, F)
represents α in A′ and terminates in an accepting state. There-
fore, α ∈Ac(A′).
To see that the statement is false for an arbitrary regular
language, consider the regular language
L = {λ} ∪{0i | i is odd }
and a nondeterministic ﬁnite-state automaton A with start
state S that accepts L. Since λ ∈L, S is an accepting state. If
S has a loop labeled 0, then A accepts all strings of 0’s; there-
fore, there is no loop at S labeled 0. Since 0 ∈L and there is no
loop at S, there is an edge from S to an accepting state S′̸ = S,
which is a contradiction. Therefore, A has at least two accept-
ing states.
Appendix A
1. ⎛
⎝
2 + a
4 + b 1 + c
6 + d
9 + e 3 + f
1 + g −1 + h 6 + i
⎞
⎠
2. % 5
7
7
−7 10 −1
&
5. %3 18 27
0 12 −6
&
8. %−2 −35 −56
−7 −18
13
&
9. ⎛
⎝
18 10
14 −6
23
1
⎞
⎠
12. (−4)
14. (a) 2 × 3, 3 × 3, 3 × 2
(b)
AB =
%33 18 47
8
9 43
&
AC =
%16 56
14 63
&
CA =
⎛
⎝
4 18 38
0
0
0
2 17 75
⎞
⎠
AB2 =
%177 215 531
80
93 323
&
BC =
⎛
⎝
18 65
34 25
12 54
⎞
⎠
