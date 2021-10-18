# Caesar    
* **Points:** 100
* **Category:** Cryptography
* **Challenge Year:** 2019

## Description
> Decrypt this <a href= "https://jupiter.challenges.picoctf.org/static/49f31c8f17817dc2d367428c9e5ab0bc/ciphertext">message</a>. 
>
>

## Solution
The file we downloaded from the link above contains the following ciphertext: 
PicoCTF{ynkooejcpdanqxeykjrbdofgkq}

Since the first part of the flag is not encrypted, we don't know how many places our ciphertext is shitfed by. 

I decided to write a little python script that would brute force through rot values 0 - 26 

```python
#create a list of letters in the alphabet
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

ciphertext = "ynkooejcpdanqxeykjrbdofgkq"
string = ciphertext.lower()      

'''
Loop through each rot (1-26). For each Rot value:
    loop through the ciphertext string. For each letter: 
        get the alphabet.index of the letter: 
        add rot to the index
        use new index to get decoded letter from alphabet
        add decoded letter to an array
        join arrary into string
        print string
'''

# decode the ciphertext based a given rot value
def decode_string(string, rot):
    decoded = []
    for letter in string:
        # get new index based on the rot 
        index_value = alphabet.index(letter) + rot
        if index_value > 25:
            index_value -= 26
        else:
            index_value
        # get letter from new index value
        l = alphabet[index_value]
        # add letter to decoded array
        decoded.append(l)
    # join and print
    decoded_text = "".join(decoded)
    print(f"rot-{rot}:{decoded_text}")


rot = 0 
while rot < 26:
    decode_string(ciphertext, rot)
    rot += 1
```

This script returned decoded cipher text 26 times (rot 0 - rot 25)

```
s0ren$ python3 brute_caesar.py
rot-0:ynkooejcpdanqxeykjrbdofgkq
rot-1:zolppfkdqeboryfzlkscepghlr
rot-2:apmqqglerfcpszgamltdfqhims
rot-3:bqnrrhmfsgdqtahbnmuegrijnt
rot-4:crossingtherubiconvfhsjkou
rot-5:dspttjohuifsvcjdpowgitklpv
rot-6:etquukpivjgtwdkeqpxhjulmqw
rot-7:furvvlqjwkhuxelfrqyikvmnrx
rot-8:gvswwmrkxlivyfmgsrzjlwnosy
rot-9:hwtxxnslymjwzgnhtsakmxoptz
rot-10:ixuyyotmznkxahoiutblnypqua
rot-11:jyvzzpunaolybipjvucmozqrvb
rot-12:kzwaaqvobpmzcjqkwvdnparswc
rot-13:laxbbrwpcqnadkrlxweoqbstxd
rot-14:mbyccsxqdrobelsmyxfprctuye
rot-15:nczddtyrespcfmtnzygqsduvzf
rot-16:odaeeuzsftqdgnuoazhrtevwag
rot-17:pebffvatgurehovpbaisufwxbh
rot-18:qfcggwbuhvsfipwqcbjtvgxyci
rot-19:rgdhhxcviwtgjqxrdckuwhyzdj
rot-20:sheiiydwjxuhkrysedlvxizaek
rot-21:tifjjzexkyvilsztfemwyjabfl
rot-22:ujgkkafylzwjmtaugfnxzkbcgm
rot-23:vkhllbgzmaxknubvhgoyalcdhn
rot-24:wlimmchanbylovcwihpzbmdeio
rot-25:xmjnndiboczmpwdxjiqacnefjp
```

From here, it was easy to grab the string that was actually human readable. 

There we likely much easier ways to solve this (existing tools online), but this way I have more own caesar cipher decrypter script that I can use on other projects. 

Very cool. :sunglasses:

- :black_flag: **flag:**`picoCTF{crossingtherubiconvfhsjkou}`