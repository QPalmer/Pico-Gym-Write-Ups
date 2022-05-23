# MiniRSA
* **Points:** 300
* **Category:** Cryptography
* **Challenge Year:** 2019

## Description
> Let's decrypt this: <a href="https://jupiter.challenges.picoctf.org/static/ee7e2388b45f521b285334abb5a63771/ciphertext">ciphertext</a>? Something seems a bit small.
>
>**Hint1:** RSA <a href="https://en.wikipedia.org/wiki/RSA_(cryptosystem)">tutorial</a><br>
>**Hint2:** How could having too small an e affect the security of this 2048 bit key?<br>
>**Hint3:** Make sure you don't lose precision, the numbers are pretty big (besides the e value)<br>

## Solution
I struggled a bit with with one at first because a didn't follow the hints. I assumed we needed to find `d` to decrypt the normal way here. But we dont' need `d`, because plaintext^e is less than `n`. A lot less than `n` in fact. That's not good. In order to encrypt or decrypt in RSA, `n` needs to be greater than your text to the power of `d` or `e`. 
<br>
This is because smaller number % greater number always equals the smaller number. <a href="https://www.sololearn.com/Discuss/1127838/how-does-modulo-works-when-first-number-is-smaller-than-the-second">The smaller number is not divisible by the larger, so the smaller number IS the remainder.</a> 


```
>>> 9 % 100
9
>>> 3 % 14
3
>>> 3 % 92837483920293874290472013984720234982374
3
```

So with that proven, we just need to find the cubed root of the ciphertext value `c` and that should get us our plaintext value! Finding the cube root of a `c` value this big was pretty difficult without losing precision however. I grabbed the <https://pypi.org/project/gmpy2">gmpy2 python module</a> to help with this, which has an 'iroot' method that can take the nth root of a number.r 
<br>

```python
import gmpy2   # Documentation here: https://gmpy2.readthedocs.io/en/latest/mpz.html

# provided variables
n = 29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673
e = 3
c = 2205316413931134031074603746928247799030155221252519872649649212867614751848436763801274360463406171277838056821437115883619169702963504606017565783537203207707757768473109845162808575425972525116337319108047893250549462147185741761825125 


# We just have to find the cubed root of C 
cube_check =  gmpy2.iroot(c,3)
if True in cube_check:
    print(f"{c} is a perfect cube!")
    print(f"The cubed root is {cube_check[0]} \n")
    plaintext = cube_check[0]
else:
    print(f"{c} is not a perfect cube.")


# convert to hex, then convert to string
hexstring = hex(plaintext)
hexstring = hexstring[2:]
bytes_object = bytes.fromhex(hexstring)
ascii_string = bytes_object.decode("ASCII")
print(f"FLAG:{ascii_string}")
```

Run the script! 
<br>

```
$ python3 minirsa_crack.py 
2205316413931134031074603746928247799030155221252519872649649212867614751848436763801274360463406171277838056821437115883619169702963504606017565783537203207707757768473109845162808575425972525116337319108047893250549462147185741761825125 is a perfect cube!
The cubed root is 13016382529449106065894479374027604750406953699090365388202874238148389207291005 

FLAG:picoCTF{n33d_a_lArg3r_e_606ce004}
```

:black_flag: **flag:**`picoCTF{n33d_a_lArg3r_e_606ce004}`