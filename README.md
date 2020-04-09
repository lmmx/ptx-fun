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

- `python -c "import string; print(' '.join(reversd(string.ascii_uppercase)))" | ptx`

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
> and after the index word (here each word is a capital letter)

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

If you have any other ideas, feel free to fork this repo, this was just a
little experiment to play around with the `ptx` tool.

Run `man ptx` and `info ptx` for more info on it, and see these resources:

- [StackExchange: Unix & Linux – "`/usr/bin/ptx`: Can you provide a use case or two?"](https://unix.stackexchange.com/questions/92730/usr-bin-ptx-can-you-provide-a-use-case-or-two)
- [Reading a Permuted Index | Unearthed Arcana](http://blog.corvus.net/2012/01/reading-permuted-index-permuted-index.html)
- [Wikipedia: Key Word in Context](https://en.wikipedia.org/wiki/Key_Word_in_Context)
  - "_A KWIC index is a special case of a permuted index._"
- [Unix Power Tools – Reading a Permuted Index](https://docstore.mik.ua/orelly/unix/upt/ch50_09.htm)
  - "_The first time that people new to UNIX take a look at the front of the system's UNIX Reference Manual,_
    _they are likely to be surprised by the most unlikely looking document: the ubiquitous permuted index._"
