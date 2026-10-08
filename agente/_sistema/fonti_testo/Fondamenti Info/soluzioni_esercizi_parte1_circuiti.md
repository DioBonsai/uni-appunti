# soluzioni_esercizi_parte1_circuiti

<!-- pagina 1 -->
587
a p p e n d i x
Answers to Questions & Exercises
Chapter 1
Section 1.1
	 1.	 One and only one of the upper two inputs must be 1, and the lowest input 
must be 1.
	 2.	 The 1 on the lower input is negated to 0 by the NOT gate, causing the out-
put of the AND gate to become 0. Thus both inputs to the OR gate are 0 
(remember that the upper input to the flip-flop is held at 0) so the output 
of the OR gate becomes 0. This means that the output of the AND gate will 
remain 0 after the lower input to the flip-flop returns to 0.
	 3.	 The output of the upper OR gate will become 1, causing the upper NOT 
gate to produce an output of 0. This will cause the lower OR gate to pro-
duce a 0, causing the lower NOT gate to produce a 1. This 1 is seen as the 
output of the flip-flop as well as being fed back to the upper OR gate, where 
it holds the output of that gate at 1, even after the flip-flop’s input has 
returned to 0.
	 4.	 a.  The entire circuit is equivalent to a single OR gate.
	
	 b.  This entire circuit is also equivalent to a single XOR gate.
	 5.	 a.  6AF2        b.  E85517        c.  48
	 6.	 a.  01011111110110010111
	
	 b.  0110000100001010
	
	 c.  101010 1111001101
	
	 d.  0000000100000000
Section 1.2
	 1.	 In the first case, memory cell number 6 ends up containing the value 5. In 
the second case, it ends up with the value 8.
	 2.	 Step 1 erases the original value in cell number 3 when the new value is 
written there. Consequently, Step 2 does not place the original value from 
cell number 3 in cell number 2. The result is that both cells end up with 
F

<!-- pagina 2 -->
588
Appendixes
the value that was originally in cell number 2. A correct procedure is the 
following:
Step 1.  Move the contents of cell number 2 to cell number 1.
Step 2.  Move the contents of cell number 3 to cell number 2.
Step 3.  Move the contents of cell number 1 to cell number 3.
	 3.	 32768 bits
Section 1.3
	 1.	 Faster retrieval of data and higher transfer rates
	 2.	 The point to remember here is that the slowness of mechanical motion 
compared with the speed of the internal functioning of the computer 
dictates that we minimize the number of times we must move the read/
write heads. If we fill a complete surface before starting the next, we must 
move the read/write head each time we finish with a track. The number of 
moves therefore is approximately the same as the total number of tracks on 
the two surfaces. If, however, we alternate between surfaces by electroni-
cally switching between the read/write heads, we must move the read/
write heads only after each cylinder has been filled.
	 3.	 In this application, information must be retrieved from mass storage in 
a random manner, which would be time consuming in the context of the 
­spiral system used on CDs and DVDs. (Moreover, current technology does 
not allow individual portions of data to be updated on a CD or DVD.)
	 4.	 CD, DVD, and Blu-ray disks are all the same physical size and use the same 
spiral track layout for placing data on the platter. A player equipped with 
multiple lasers is able to read all three types of optical disk.
	 5.	 Flash drives do not require physical motion so they have shorter response 
times and do not suffer from physical wear.
	 6.	 Magnetic hard disks are faster and have higher capacities than other 
forms of magnetic media, such as floppy disks and magnetic tape. Speed, 
­capacity, and rewriting ability compare favorably to optical media. Price 
per units of storage on magnetic disks continues to be lower than solid-state 
disks, although this advantage has steadily eroded in recent years.
Section 1.4
	 1.	 Computer Science
	 2.	 The two patterns are the same, except that the sixth bit from the low-order 
end is always 0 for uppercase and 1 for lowercase.
	 3.	 a.	 00100010	
01010011	
01110100	
01101111
	
	 	
01110000	
00100001	
00100010	
00100000
	
	 	
01000011	
01101000	
01100101	
01110010
	
	 	
01111001	
01101100	
00100000	
01110011
	
	 	
01101000	
01101111	
01110101	
01110100
	
	 	
01100101	
01110100	
00101110

<!-- pagina 3 -->
589
Appendix F
	
	 b.	 01000100	
01101111	
01100101	
01110011
	
	 	
00100000	
00110010	
00100000	
00101011
	
	 	
00100000	
00110011	
00100000	
00111101
	
	 	
00100000	
00110101	
00111111
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
	 4.	
5.	 a.  5	
b.  9	
c.  11	
d.  6	
e.  16	
f.  18
	 6.	 a.  110	
b.  1101	
c.  1011	
d.  10010	
e.  11011	
f.  100
	 7.	 In 24 bits, we can store three symbols using ASCII. Thus we can store 
­values as large as 999. However, if we use the bits as binary digits, we can 
store values up to 16,777,215.
	 8.	 a.  15.15        b.  51.0.128        c.  10.160
	 9.	 Geometric representations are more conducive to changes in scale than 
images encoded as bit maps. However, geometric representations do not 
typically provide the same photographic quality that bit maps produce. 
Indeed, as discussed in Section 1.9, JPEG representations of bit maps are 
very popular in photography.
	10.	 With a sample rate of 44,100 samples per second, one hour of stereo music 
would require 635,040,000 bytes of storage. Thus, it would just about fill a 
CD whose capacity is slightly more than 600MB.
Section 1.5
	 1.	 a.  42	
b.  33	
c.  23	
d.  6	
e.  31
	 2.	 a.  100000	
b.  1000000	
c.  1100000	
d.  1111	
e.  11011
	 3.	 a.  31⁄4	
b.  57⁄8	
c.  21⁄2	
d.  63⁄8	
e.  5⁄8
	 4.	 a.  100.1	
b.  10.11	
c.  1.001	
d.  0.0101	
e.  101.101
	 5.	 a.  100111	
b.  1011.110	
c.  100000	
d.  1000.00
Section 1.6
	 1.	 a.  3        b.  15        c.  -4        d.  -6        e.  0        f.  -16
	 2.	 a.  00000110	
b.  11111010	
c.  11101111 
d.  00001101	
e.  11111111	
f.  00000000
	 3.	 a.  11111111	
b.  10101011	
c.  00000100 
d.  00000010	
e.  00000000	
f.  10000001
	 4.	 a.  With 4 bits the largest value is 7 and the smallest is -8.
	
	 b.  With 6 bits the largest value is 31 and the smallest is -32.
	
	 c.  With 8 bits the largest value is 127 and the smallest is -128.
	 5.	 a.  0111 (5 + 2 = 7)        b.  0100 (3 + 1 = 4)        c.  1111 (5 + (-6) = -1) 
d.  0001 (-2 + 3 = 1)     e.  1000 (-6 + (-2) = -8)

<!-- pagina 4 -->
590
Appendixes
	 6.	 a.  0111	
b.  1011 (overflow)	
c.  0100 (overflow) 
d.  0001	
e.  1000 (overflow)
	 7.	 a.  0110
+ 0001
0111
	
b.  0011
+ 1110
0001
	
c.  0100
+ 1010
1110
	
d.  0010
+ 0100
0110
	
e.  0001
+1011
1100
	 8.	 No. Overflow occurs when an attempt is made to store a number that is too 
large for the system being used. When adding a positive value to a negative 
value, the result must be between the values being added. Therefore the 
result will be small enough to be stored without error.
	 9.	 a.  6 because 1110 → 14 - 8
	
	 b.  -1 because 0111 → 7 - 8
	
	 c.  0 because 1000 → 8 - 8
	
	 d.  -6 because 0010 → 2 - 8
	
	 e.  -8 because 0000 → 0 - 8
	
	 f.  1 because 1001 → 9 - 8
	10.	 a.  1101 because 5 + 8 = 13 → 1101
	
	 b.  0011 because -5 + 8 = 3 → 0011
	
	 c.  1011 because 3 + 8 = 11 → 1011
	
	 d.  1000 because 0 + 8 = 8 → 1000
	
	 e.  1111 because 7 + 8 = 15 → 1111
	
	 f.  0000 because -8 + 8 = 0 → 0000
	11.	 No. The largest value that can be stored in excess eight notation is 7, 
represented by 1111. To represent a larger value, at least excess 16 (which 
uses patterns of 5 bits) must be used. Similarly, 6 cannot be represented in 
excess four notation. (The largest value that can be represented in excess 
four notation is 3.)
Section 1.7
	 1.	 a.  5⁄8        b.  31⁄4        c.  9⁄32        d.  -11⁄2        e.  -(11⁄64)
	 2.	 a.  01101011        b.  01111010 (truncation error) 
c.  01001100        d.  11101110        e.  11111000 (truncation error)
	 3.	 01001001 (9⁄16) is larger than 00111101 (13⁄32). The following is a simple way 
of determining which of two patterns represents the larger value:
Case 1.  If the sign bits are different, the larger is the one with 0 sign bit.
Case 2.  If the sign bits are both 0, scan the remaining portions of the 
patterns from left to right until a bit position is found where the 
two patterns differ. The pattern containing the 1 in this position 
represents the larger value.
Case 3.  If the sign bits are both 1, scan the remaining portions of the 
patterns from left to right until a bit position is found where the 
two patterns differ. The pattern containing the 0 in this position 
represents the larger value. The simplicity of this comparison 
process is one of the reasons for representing the exponent in 
floating-point systems with an excess notation rather than with 
two’s complement.

<!-- pagina 5 -->
591
Appendix F
	 4.	 The largest value would be 71⁄2, which is represented by the pattern 
01111111. As for the smallest positive value, you could argue that there are 
two “correct” answers. First, if you stick to the coding process described 
in the text, which requires the most significant bit of the mantissa to be 1 
(called normalized form), the answer is 1⁄32, which is represented by the pat-
tern 00001000. However, most machines do not impose this restriction for 
values close to 0. For such a machine, the correct answer is 1⁄256 represented 
by 00000001.
Section 1.8
	 1.	 Python is considered an interpreted language because users can type 
­program fragments interactively at a prompt, rather than having to save the 
script, invoke a compiler, and then execute the program.
	 2.	 a.  print('Computer Science Rocks' + '!')
	
	 b.  print(42)
	
	 c.  print(3.1416)
	 3.	 a.  rockstar = 'programmer'
	
	 b.  seconds_per_hour = 60 * 60
	
	     or
	 		
seconds_per_hour = 3600
	
	 c.  bodyTemp = 98.6
	 4.	 metricBodyTemp = (bodyTemp - 32)/1.8
Section 1.9
	 1.	 Run-length encoding, frequency-dependent encoding, relative encoding, 
and dictionary encoding
	 2.	 121321112343535
	 3.	 Color cartoons consist of blocks of solid color with sharp edges. Moreover, 
the number of colors involved is limited.
	 4.	 No. Both GIF and JPEG are lossy compression systems, meaning that 
details in the image will be lost.
	 5.	 JPEG’s baseline standard takes advantage of the fact that the human eye is 
not as sensitive to changes in color as it is to changes in brightness. Thus 
it reduces the number of bits used to represent color information without 
noticeable loss in image quality.
	 6.	 Temporal masking and frequency masking
	 7.	 When encoding information, approximations are made. In the case of 
numeric data, these approximations are compounded when computa-
tions are performed, which can lead to erroneous results. Approximations 
are not as critical in the cases of images and sound because the encoded 
data are normally only stored, transferred, and reproduced. If, however, 
images or sound were repeatedly reproduced, rerecorded, and then reen-
coded, these approximations could compound and ultimately lead to 
worthless data.

<!-- pagina 6 -->
592
Appendixes
Section 1.10
	 1.	 b, c, and e
	 2.	 Yes. If an even number of errors occurs in one byte, the parity technique 
does not detect them.
	 3.	 In this case, errors occur in bytes a and d of Question 1. The answer to 
Question 2 remains the same.
	 4.	 a.  100100010
101010011
101110100
b.  101000100
101101111
101100101
	 5.	 a.  BED	
b.  CAB	
c.  HEAD
	 6.	 One solution is the following:
A  00000
B  11100
C  01111
D  10011
Chapter 2
Section 2.1
	 1.	 On some machines this is a two-step process consisting of first reading the 
contents from the first cell into a register and then writing it from the regis-
ter into the destination cell. On most machines, this is accomplished as one 
activity without using an intermediate register.
	 2.	 The value to be written, the address of the cell in which to write, and the 
command to write
	 3.	 General-purpose registers are used to hold the data immediately applicable 
to the operation at hand; main memory is used to hold data that will be 
needed in the near future; and mass storage is used to hold data that will 
likely not be needed in the near future.
Section 2.2
	 1.	 The term move often carries the connotation of removing from one location 
and placing in another, thus leaving a hole behind. In most cases within a 
machine, this removal does not take place. Rather, the object being moved 
is most often copied (or cloned) into the new location.
101101111
100100010
001101000
001111001
001110011
001110101
001100100
001110000
000100000
101100101
101101100
001101000
101110100
100100001
001000011
101110010
000100000
101101111
101100101
100101110
001110011
000100000
100110011
000100000
100100000
100101011
000100000
100110101
000110010
000100000
000111101
100111111
