# ptx-fun

Playing around with `ptx`, the permuted index tool used to make concordances
for the Unix system reference manual "back in the day" (apparently).

## Requirements

- Python 3
- `num2words`
  - Run `pip install num2words`

## Demos

- `python -c "import string; print(' '.join(string.ascii_uppercase))" | ptx`

```
   R S T U V W X Y Z                   A B C D E F G H I J K L M N O P Q
   S T U V W X Y Z                 A   B C D E F G H I J K L M N O P Q R
   T U V W X Y Z                 A B   C D E F G H I J K L M N O P Q R S
   U V W X Y Z                 A B C   D E F G H I J K L M N O P Q R S T
   V W X Y Z                 A B C D   E F G H I J K L M N O P Q R S T U
   W X Y Z                 A B C D E   F G H I J K L M N O P Q R S T U V
   X Y Z                 A B C D E F   G H I J K L M N O P Q R S T U V W
   Y Z                 A B C D E F G   H I J K L M N O P Q R S T U V W X
   Z                 A B C D E F G H   I J K L M N O P Q R S T U V W X Y
                   A B C D E F G H I   J K L M N O P Q R S T U V W X Y Z
                 A B C D E F G H I J   K L M N O P Q R S T U V W X Y Z
               A B C D E F G H I J K   L M N O P Q R S T U V W X Y Z
             A B C D E F G H I J K L   M N O P Q R S T U V W X Y Z
           A B C D E F G H I J K L M   N O P Q R S T U V W X Y Z
         A B C D E F G H I J K L M N   O P Q R S T U V W X Y Z
       A B C D E F G H I J K L M N O   P Q R S T U V W X Y Z
     A B C D E F G H I J K L M N O P   Q R S T U V W X Y Z
     B C D E F G H I J K L M N O P Q   R S T U V W X Y Z                  A
     C D E F G H I J K L M N O P Q R   S T U V W X Y Z                  A B
     D E F G H I J K L M N O P Q R S   T U V W X Y Z                   /B C
     E F G H I J K L M N O P Q R S T   U V W X Y Z                     /C D
     F G H I J K L M N O P Q R S T U   V W X Y Z                       /D E
     G H I J K L M N O P Q R S T U V   W X Y Z                         /E F
     H I J K L M N O P Q R S T U V W   X Y Z                           /F G
     I J K L M N O P Q R S T U V W X   Y Z                             /G H
     J K L M N O P Q R S T U V W X Y   Z                               /H I
```

> A permuted index from the alphabet (from `string.acii_uppercase`) that shows
> clearly what `ptx` does in terms of the sequence of letters of the alphabet.

- `python -c "import string; print(' '.join(reversed(string.ascii_uppercase)))" | ptx`

```
     Q P O N M L K J I H G F E D C B   A                               /S R
     R Q P O N M L K J I H G F E D C   B A                             /T S
     S R Q P O N M L K J I H G F E D   C B A                           /U T
     T S R Q P O N M L K J I H G F E   D C B A                         /V U
     U T S R Q P O N M L K J I H G F   E D C B A                       /W V
     V U T S R Q P O N M L K J I H G   F E D C B A                     /X W
     W V U T S R Q P O N M L K J I H   G F E D C B A                   /Y X
     X W V U T S R Q P O N M L K J I   H G F E D C B A                  Z Y
     Y X W V U T S R Q P O N M L K J   I H G F E D C B A                  Z
     Z Y X W V U T S R Q P O N M L K   J I H G F E D C B A
       Z Y X W V U T S R Q P O N M L   K J I H G F E D C B A
         Z Y X W V U T S R Q P O N M   L K J I H G F E D C B A
           Z Y X W V U T S R Q P O N   M L K J I H G F E D C B A
             Z Y X W V U T S R Q P O   N M L K J I H G F E D C B A
               Z Y X W V U T S R Q P   O N M L K J I H G F E D C B A
                 Z Y X W V U T S R Q   P O N M L K J I H G F E D C B A
                   Z Y X W V U T S R   Q P O N M L K J I H G F E D C B A
   A                 Z Y X W V U T S   R Q P O N M L K J I H G F E D C B
   B A                 Z Y X W V U T   S R Q P O N M L K J I H G F E D C
   C B A                 Z Y X W V U   T S R Q P O N M L K J I H G F E D
   D C B A                 Z Y X W V   U T S R Q P O N M L K J I H G F E
   E D C B A                 Z Y X W   V U T S R Q P O N M L K J I H G F
   F E D C B A                 Z Y X   W V U T S R Q P O N M L K J I H G
   G F E D C B A                 Z Y   X W V U T S R Q P O N M L K J I H
   H G F E D C B A                 Z   Y X W V U T S R Q P O N M L K J I
   I H G F E D C B A                   Z Y X W V U T S R Q P O N M L K J
```

> A permuted index for the alphabet in reverse now, that shows how `ptx`
> sorts the index and makes a concordance entry giving the context before
> and after the index word (here each word is a capital letter).
> 
> Notice how the direction of the gap shows the 'cyclic' structure of the
> permutation index. After squinting at it for a while, I think you can
> see this as an alphabetic form of a _circulant matrix_ which is then
> sorted by the middle value (or alternatively, sorted by the first value,
> and then rows rotated by `n // 2`). I'll revisit this below.

- `python -c "from ptx import a2i; txt='''$(python -c "import string; print(' '.join(string.ascii_uppercase))" | ptx)'''; print(a2i(txt))"`

```
   17 18 19 20 21 22 23 24 25                   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
   18 19 20 21 22 23 24 25                 0   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
   19 20 21 22 23 24 25                 0 1   2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
   20 21 22 23 24 25                 0 1 2   3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
   21 22 23 24 25                 0 1 2 3   4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
   22 23 24 25                 0 1 2 3 4   5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
   23 24 25                 0 1 2 3 4 5   6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
   24 25                 0 1 2 3 4 5 6   7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
   25                 0 1 2 3 4 5 6 7   8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
                   0 1 2 3 4 5 6 7 8   9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
                 0 1 2 3 4 5 6 7 8 9   10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
               0 1 2 3 4 5 6 7 8 9 10   11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
             0 1 2 3 4 5 6 7 8 9 10 11   12 13 14 15 16 17 18 19 20 21 22 23 24 25
           0 1 2 3 4 5 6 7 8 9 10 11 12   13 14 15 16 17 18 19 20 21 22 23 24 25
         0 1 2 3 4 5 6 7 8 9 10 11 12 13   14 15 16 17 18 19 20 21 22 23 24 25
       0 1 2 3 4 5 6 7 8 9 10 11 12 13 14   15 16 17 18 19 20 21 22 23 24 25
     0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15   16 17 18 19 20 21 22 23 24 25
     1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16   17 18 19 20 21 22 23 24 25                  0
     2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17   18 19 20 21 22 23 24 25                  0 1
     3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18   19 20 21 22 23 24 25                   /1 2
     4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19   20 21 22 23 24 25                     /2 3
     5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20   21 22 23 24 25                       /3 4
     6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21   22 23 24 25                         /4 5
     7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22   23 24 25                           /5 6
     8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23   24 25                             /6 7
     9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24   25                               /7 8
```

> Since numbers are the universal language, index the alphabet against the list
> of letters it was generated from (again using `string.ascii_uppercase`), and
> replace each letter in the `ptx` output string with its index number.
>
> This notably distorts the straight line that made the alphabetic concordance
> from `ptx` clearly readable.

- `python -c "from ptx import a2c; txt='''$(python -c "import string; print(' '.join(string.ascii_uppercase))" | ptx)'''; print(a2c(txt))"`

```
   ⑰ ⑱ ⑲ ⑳ ㉑ ㉒ ㉓ ㉔ ㉕                   ⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯
   ⑱ ⑲ ⑳ ㉑ ㉒ ㉓ ㉔ ㉕                 ⓪   ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰
   ⑲ ⑳ ㉑ ㉒ ㉓ ㉔ ㉕                 ⓪ ①   ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱
   ⑳ ㉑ ㉒ ㉓ ㉔ ㉕                 ⓪ ① ②   ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲
   ㉑ ㉒ ㉓ ㉔ ㉕                 ⓪ ① ② ③   ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳
   ㉒ ㉓ ㉔ ㉕                 ⓪ ① ② ③ ④   ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑
   ㉓ ㉔ ㉕                 ⓪ ① ② ③ ④ ⑤   ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑ ㉒
   ㉔ ㉕                 ⓪ ① ② ③ ④ ⑤ ⑥   ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑ ㉒ ㉓
   ㉕                 ⓪ ① ② ③ ④ ⑤ ⑥ ⑦   ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑ ㉒ ㉓ ㉔
                   ⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧   ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑ ㉒ ㉓ ㉔ ㉕
                 ⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨   ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑ ㉒ ㉓ ㉔ ㉕
               ⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩   ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑ ㉒ ㉓ ㉔ ㉕
             ⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪   ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑ ㉒ ㉓ ㉔ ㉕
           ⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫   ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑ ㉒ ㉓ ㉔ ㉕
         ⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬   ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑ ㉒ ㉓ ㉔ ㉕
       ⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭   ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑ ㉒ ㉓ ㉔ ㉕
     ⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮   ⑯ ⑰ ⑱ ⑲ ⑳ ㉑ ㉒ ㉓ ㉔ ㉕
     ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯   ⑰ ⑱ ⑲ ⑳ ㉑ ㉒ ㉓ ㉔ ㉕                  ⓪
     ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰   ⑱ ⑲ ⑳ ㉑ ㉒ ㉓ ㉔ ㉕                  ⓪ ①
     ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱   ⑲ ⑳ ㉑ ㉒ ㉓ ㉔ ㉕                   /① ②
     ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲   ⑳ ㉑ ㉒ ㉓ ㉔ ㉕                     /② ③
     ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳   ㉑ ㉒ ㉓ ㉔ ㉕                       /③ ④
     ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑   ㉒ ㉓ ㉔ ㉕                         /④ ⑤
     ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑ ㉒   ㉓ ㉔ ㉕                           /⑤ ⑥
     ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑ ㉒ ㉓   ㉔ ㉕                             /⑥ ⑦
     ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑ ㉒ ㉓ ㉔   ㉕                               /⑦ ⑧
```

> To try and remove the distortion, use the `num2words` package's function
> `num2words()` to transcribe the name of each integer in the previous step
> into what will hopefully be a monospace character. On my system it's not,
> but it's a little better than before.

---

## The permuted index as a circulant matrix

I may well have missed something obvious here (I still haven't finished reading
_Matrix Analysis_ by Horn & Johnson) but from the concepts I know in matrix
algebra, this is a circulant matrix formed either as:

- the product of the sequence `[A, ..., Z]` (i.e. the vector `a`) with the reversal
  matrix which has zeroes everywhere except along the main antidiagonal,
- _or_ as the circulant matrix formed from this same vector `a`, and which is then
  'rotated' (in the sense of a [circular shift](https://en.wikipedia.org/wiki/Circular_shift))
  by a number of rows equal to half the length of (`a` + extension) where for `ptx`
  this extension seems to be 8 (for purposes of computation, any numbers not in
  `range(26)` are to be replaced with whitespace).
  - specifically this type of circulant matrix is a Toeplitz matrix, and it can be
    recreated in Sage

I went with the latter approach, the program for which is stored in `toeplitz.py`,
which can be run by `sage-ipython` (I'm not sure if this is how you're supposed to
run programs with sage, I usually use it interactively), and the wrapper shell script
`run_sage_toeplitz.sh` takes care of this (removing the welcome and goodbye greetings
that for some reason aren't printed to STDERR).

The output is:

```
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z _ _ _ _ _ _ _ _
B C D E F G H I J K L M N O P Q R S T U V W X Y Z _ _ _ _ _ _ _ _ A
C D E F G H I J K L M N O P Q R S T U V W X Y Z _ _ _ _ _ _ _ _ A B
D E F G H I J K L M N O P Q R S T U V W X Y Z _ _ _ _ _ _ _ _ A B C
E F G H I J K L M N O P Q R S T U V W X Y Z _ _ _ _ _ _ _ _ A B C D
F G H I J K L M N O P Q R S T U V W X Y Z _ _ _ _ _ _ _ _ A B C D E
G H I J K L M N O P Q R S T U V W X Y Z _ _ _ _ _ _ _ _ A B C D E F
H I J K L M N O P Q R S T U V W X Y Z _ _ _ _ _ _ _ _ A B C D E F G
I J K L M N O P Q R S T U V W X Y Z _ _ _ _ _ _ _ _ A B C D E F G H
J K L M N O P Q R S T U V W X Y Z _ _ _ _ _ _ _ _ A B C D E F G H I
K L M N O P Q R S T U V W X Y Z _ _ _ _ _ _ _ _ A B C D E F G H I J
L M N O P Q R S T U V W X Y Z _ _ _ _ _ _ _ _ A B C D E F G H I J K
M N O P Q R S T U V W X Y Z _ _ _ _ _ _ _ _ A B C D E F G H I J K L
N O P Q R S T U V W X Y Z _ _ _ _ _ _ _ _ A B C D E F G H I J K L M
O P Q R S T U V W X Y Z _ _ _ _ _ _ _ _ A B C D E F G H I J K L M N
P Q R S T U V W X Y Z _ _ _ _ _ _ _ _ A B C D E F G H I J K L M N O
Q R S T U V W X Y Z _ _ _ _ _ _ _ _ A B C D E F G H I J K L M N O P
R S T U V W X Y Z _ _ _ _ _ _ _ _ A B C D E F G H I J K L M N O P Q
S T U V W X Y Z _ _ _ _ _ _ _ _ A B C D E F G H I J K L M N O P Q R
T U V W X Y Z _ _ _ _ _ _ _ _ A B C D E F G H I J K L M N O P Q R S
U V W X Y Z _ _ _ _ _ _ _ _ A B C D E F G H I J K L M N O P Q R S T
V W X Y Z _ _ _ _ _ _ _ _ A B C D E F G H I J K L M N O P Q R S T U
W X Y Z _ _ _ _ _ _ _ _ A B C D E F G H I J K L M N O P Q R S T U V
X Y Z _ _ _ _ _ _ _ _ A B C D E F G H I J K L M N O P Q R S T U V W
Y Z _ _ _ _ _ _ _ _ A B C D E F G H I J K L M N O P Q R S T U V W X
Z _ _ _ _ _ _ _ _ A B C D E F G H I J K L M N O P Q R S T U V W X Y
```

Clearly this is only half the way to the 'permuted index' you see from
`ptx` (the underscores are just to make the whitespace visible when it's
at the end of the line while developing this).

- To start with, the permuted index has a gap in the middle, which corresponds to
  a gap at the end of each row of the Toeplitz matrix obtained above.
  - Achieve this by adding a column vector to the left of the Toeplitz matrix
- Secondly, shift each row by twice the length of the whitespace extension
  (2\*8=16), by a permutation matrix formed from the circulant matrix
  of a vector: `{ 0` (16 + 1 = 17 times)`, 1` (once)`, 0` (26 - 8 - 1 = 17 times) `}`
  - A permutation matrix, `P`, must right-multiply to permute the
    columns of a matrix, `A`, which it acts on, i.e. `A * P`
  - This means the permutation matrix must share the number of columns
    of A, which here means `P` must be (26 + 8 + 1 = 35) rows in height
    (a circulant matrix is square, and its width [17 + 1 + 17 = 35] matches)
    

```
R S T U V W X Y Z _ _ _ _ _ _ _ _ _ A B C D E F G H I J K L M N O P Q
S T U V W X Y Z _ _ _ _ _ _ _ _ A _ B C D E F G H I J K L M N O P Q R
T U V W X Y Z _ _ _ _ _ _ _ _ A B _ C D E F G H I J K L M N O P Q R S
U V W X Y Z _ _ _ _ _ _ _ _ A B C _ D E F G H I J K L M N O P Q R S T
V W X Y Z _ _ _ _ _ _ _ _ A B C D _ E F G H I J K L M N O P Q R S T U
W X Y Z _ _ _ _ _ _ _ _ A B C D E _ F G H I J K L M N O P Q R S T U V
X Y Z _ _ _ _ _ _ _ _ A B C D E F _ G H I J K L M N O P Q R S T U V W
Y Z _ _ _ _ _ _ _ _ A B C D E F G _ H I J K L M N O P Q R S T U V W X
Z _ _ _ _ _ _ _ _ A B C D E F G H _ I J K L M N O P Q R S T U V W X Y
_ _ _ _ _ _ _ _ A B C D E F G H I _ J K L M N O P Q R S T U V W X Y Z
_ _ _ _ _ _ _ A B C D E F G H I J _ K L M N O P Q R S T U V W X Y Z _
_ _ _ _ _ _ A B C D E F G H I J K _ L M N O P Q R S T U V W X Y Z _ _
_ _ _ _ _ A B C D E F G H I J K L _ M N O P Q R S T U V W X Y Z _ _ _
_ _ _ _ A B C D E F G H I J K L M _ N O P Q R S T U V W X Y Z _ _ _ _
_ _ _ A B C D E F G H I J K L M N _ O P Q R S T U V W X Y Z _ _ _ _ _
_ _ A B C D E F G H I J K L M N O _ P Q R S T U V W X Y Z _ _ _ _ _ _
_ A B C D E F G H I J K L M N O P _ Q R S T U V W X Y Z _ _ _ _ _ _ _
A B C D E F G H I J K L M N O P Q _ R S T U V W X Y Z _ _ _ _ _ _ _ _
B C D E F G H I J K L M N O P Q R _ S T U V W X Y Z _ _ _ _ _ _ _ _ A
C D E F G H I J K L M N O P Q R S _ T U V W X Y Z _ _ _ _ _ _ _ _ A B
D E F G H I J K L M N O P Q R S T _ U V W X Y Z _ _ _ _ _ _ _ _ A B C
E F G H I J K L M N O P Q R S T U _ V W X Y Z _ _ _ _ _ _ _ _ A B C D
F G H I J K L M N O P Q R S T U V _ W X Y Z _ _ _ _ _ _ _ _ A B C D E
G H I J K L M N O P Q R S T U V W _ X Y Z _ _ _ _ _ _ _ _ A B C D E F
H I J K L M N O P Q R S T U V W X _ Y Z _ _ _ _ _ _ _ _ A B C D E F G
I J K L M N O P Q R S T U V W X Y _ Z _ _ _ _ _ _ _ _ A B C D E F G H
```

_Et voilà_, that is the same as the first output from `ptx` above (except
you may notice the bottom right corner in the `ptx` output is shortened
so as not to repeat the sequence's beginning beyond 2 words, instead
placing a `/` at the start of the first word it shows to indicate the
abbreviation.

Big love to Sage for making this kind of exploration so easy and fun.
It really felt like numerical matrices were the easier and more elegant
option here (as opposed to just taking the first Toeplitz matrix output
and reading that in, working with numbers and just converting to
letters at the end was something I've not done much of but really
helped build my intuition for how all these matrices really work,
which would have been lost if it was 'just another list').

---

## Two little post-scripts

- You may notice in the above calculations that the runs of zeroes in the circular permutation
  came out to be the same length (16 + 1 = 17) and (26 - 8 - 1 = 17). I did double check the program
  with a different value of `ext` (length of the spacing at the end of the alphabet) and confirmed
  that I do have this the right way round. If you switched them you'd do a "negative" or reversed
  circular shift (I've not looked up what the convention is, but since the A moves forward I call
  the one here a 'forward' shift. I think in cryptography it's a _rotation_ (as in `ROT13` and Caesar
  cipher). There are also 'circular permutation proteins' whose sequences get shifted in this way,
  and over in `numpy` it's called "rolling" a vector.

- I don't really like to use Jupyter notebooks, I find they can get quite unreproducible at times
  if you're not deliberately writing scripts to save specific units of output, but Sage only works
  on my machine in the IPython console so I ended up coding as done when submitting jobs to a server,
  writing shell scripts to run discrete units of work and save the standard output in text files
  named in reference to the script that they came from.

  - The final result here is in `sage_concordance.stdout.txt` which was created by
    `run_sage_concordance.sh` which executed `concordance.py` non-interactively (I was
    running the program to STDOUT to see results of changes I made). This isn't my usual
    development style but it worked nicely here (where the README is the main product more
    so than a software package etc.)
  - I'm leaving the lines that overwrite the output files commented out in the versioned code repo,
    so you can try running this yourself without losing the local reference to compare to.

---

If you have any other ideas, feel free to fork this repo (this was just a
little experiment to play around with the `ptx` tool) or hit my line on Twitter,
[@permutans](https://twitter.com/permutans).

---

Run `man ptx` and `info ptx` for more info on it, and see these resources:

- [StackExchange: Unix & Linux – "`/usr/bin/ptx`: Can you provide a use case or two?"](https://unix.stackexchange.com/questions/92730/usr-bin-ptx-can-you-provide-a-use-case-or-two)
- [Reading a Permuted Index | Unearthed Arcana](http://blog.corvus.net/2012/01/reading-permuted-index-permuted-index.html)
- [Wikipedia: Key Word in Context](https://en.wikipedia.org/wiki/Key_Word_in_Context)
  - "_A KWIC index is a special case of a permuted index._"
- [Unix Power Tools – Reading a Permuted Index](https://docstore.mik.ua/orelly/unix/upt/ch50_09.htm)
  - "_The first time that people new to UNIX take a look at the front of the system's UNIX Reference Manual,_
    _they are likely to be surprised by the most unlikely looking document: the ubiquitous permuted index._"
