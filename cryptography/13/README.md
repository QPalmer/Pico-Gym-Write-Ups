# 13
* **Points:** 100
* **Category:** Cryptography
* **Challenge Year:** 2019

## Description

> Cryptography can be easy, do you know what ROT13 is? 
>
> cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}

## Solution

A ROT13 cipher substitues a letter of plaintext with a letter 13 places away from it in the A-Z alphabet. 
Because of this, it works the same both forwards and backwards. 

```
A + 13 = N
N + 13 = A 
```

A ROT26 Cipher would do nothing: 

```
A + 26 = A
```

This challenge can be solved easily by going here: 
- https://rot13.com/

But why do that we when can write some bad code that does the same thing? <br>
I'm using Python's maketrans method below to compare my rot0 string with my rot13 string. <br>
There is probably a much better way to do this. But it was more fun than just going to someone else's site to decipher. 

```python
rot0 = "abcdefghijklmnopqrstuvwxyz"
rot1 = "bcdefghijklmnopqrstuvwxyza"
rot13 = "nopqrstuvwxyzabcdefghijklm"

flag = []
ciphertext = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
string = ciphertext.lower()
print(string)

rot_table = ciphertext.maketrans(rot13, rot0)
print(rot_table)

no_decode = ["_","}","{"]

for letter in string:
    if letter in no_decode:
        flag.append(letter)
    else:
        letter = ord(letter)
        flag.append(chr(rot_table[letter]))

final_flag = "".join(flag)
print(final_flag)
```

:black_flag: :black_flag: :black_flag: :black_flag: :black_flag: **flag:**
`picoCTF{not_too_bad_of_a_problem}`
