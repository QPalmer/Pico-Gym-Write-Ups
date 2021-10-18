# Easy1
* **Points:** 100
* **Category:** Cryptography
* **Challenge Year:** 2019

## Description
> The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? 
> We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. 
> Can you use this table to solve it?.
> 


```
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
   +----------------------------------------------------
A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
```


## Solution

This is called a <a href="https://www.youtube.com/watch?v=SkJcmCaHqS0">Vigenère Cipher</a>. You can use a key and the above table to encrypt/decrypt text.
The cipher text is just the letter by letter interseciton of the plaintext one axis of the table and the key on the other. 
So to decrypt, we start with key on one column and stop on the row with that contains the cipher text. 

Very easy to search for a site that does this automatically, even without knowing the key. But in the spirit of learning I decided to manually decipher (most) of the text. 

Key: `SOLVECRYPTO` <br>
Cipher Text: `UFJKXQZQUNB`

|Key|CT|PT|
|--|--|--|
|S|U|C| 
|O|F|R|
|L|J|Y|
|V|K|P| 
|E|X|T|
|C|Q|O| 
|R|Z|I| 
|Y|Q|S|
|P|U|F| 
|T|N|U|
|O|B|N|

Plain Text: `CRYPTOISFUN`

 :black_flag: **flag:**`picoCTF{CRYPTOISFUN}`