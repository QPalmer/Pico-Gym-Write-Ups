# La Cifra De
* **Points:** 200
* **Category:** Cryptography
* **Challenge Year:** 2019

## Description
> I found this cipher in an old book. Can you figure out what it says? <br>
> Connect with nc jupiter.challenges.picoctf.org 58295.
>

```
nc jupiter.challenges.picoctf.org 58295
Encrypted message:
Ne iy nytkwpsznyg nth it mtsztcy vjzprj zfzjy rkhpibj nrkitt ltc tnnygy ysee itd tte cxjltk

Ifrosr tnj noawde uk siyyzre, yse Bnretèwp Cousex mls hjpn xjtnbjytki xatd eisjd

Iz bls lfwskqj azycihzeej yz Brftsk ip Volpnèxj ls oy hay tcimnyarqj dkxnrogpd os 1553 my Mnzvgs Mazytszf Merqlsu ny hox moup Wa inqrg ipl. Ynr. Gotgat Gltzndtg Gplrfdo 

Ltc tnj tmvqpmkseaznzn uk ehox nivmpr g ylbrj ts ltcmki my yqtdosr tnj wocjc hgqq ol fy oxitngwj arusahje fuw ln guaaxjytrd catizm tzxbkw zf vqlckx hizm ceyupcz yz tnj fpvjc hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3xf966878l}

Tnj qixxe wkqw-duhfmkseej ipsiwtpznzn uk l puqjarusahjeii htpnjc hubpvkw, hay rldk fcoaso 1467 be Qpot Gltzndtg Fwbkwei.

Zmp Volpnèxj Nivmpr ox ehkwpfuwp surptorps ifwlki ehk Fwbkwei Jndc uw Llhjcto Htpnjc.

It 1508, Ozhgsyey Ycizmpmozd itapnzjo tnj do-ifwlki eahzwa xjntg (f xazwtx uk dhokeej fwpnfmezx) ehgy hoaqo lgypr hj l cxneiifw curaotjyt uk ehk Atgksèce Inahkw.

Merqlsu’x deityd htzkrje avupaxjo it 1555 fd a itytosfaznzn uk ehk ktryy. Ehk qzwkw saraps uk ehk fwpnfmezx lrk szw ymtfzjo rklflgwwy, hze tnj llvmlbkyd ati ehk nydkc wezypry fce sniej gj mkfys uk l mtjxotnn kkd ahxfde, cmtcn hln hj oilkprkse woys eghs cuwceyuznjjyt.
```

## Solution
<p> Hints suggested that there are "online tools that make this very easy". There certainly are. Most of the write ups I see are just folks that copied and pasted the encrypted text here: https://cryptii.com/pipes/vigenere-cipher. I guess that would get the job done but I want to know a little more. </p>

</p>So thanks to other write ups, I know this text was encrpyted using a Vigenère Cipher. What IS a Vigenère Cipher? Unlike a Caesar Cipher, where all the text is transposed by X number of letters, a Vigenere Cipher encrypts text using a key. Each letter in the key encryptes one letter in the plaintext by that many spaces. E.g. If the first letter in my plaintext is "A" and the first letter in my key is "L", I'm transposing "A" by "L" spaces and getting "L" for the first letter of my encrypted text. This is a lot easier to visualize for most people as a table of letters as explained in this video: https://www.youtube.com/watch?v=SkJcmCaHqS0&t=13s </p>

<p> Without using an online tool, where would I begin to make an attempt to find the flag here? Let's look at the part of the text that is in the same format as the flag: hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3xf966878l}. We found what is probably the flag here, but it is encrypted.</p>

<p>Knowing "pohzCZK{" = "picoCTF{", we might be able to extrapolate what the key is and use it to decrypt the rest of the flag. By referencing the vingenere matrix, we can map each encrypted character to each decrypted character to find the key.</p>

| plaintext | encrypted text |  key |
| ---- | ---- | ---- | 
|P | P | A |
|I | O | G |
|C | H | F |
|O | Z | L |
|C | C | A | 
|T | Z | G | 
|F | K | F | 

<p>It looks like the the key is 'FLAG'. How appropriate. Instead of manually applying this to the rest of the text, we can write a little <a href="https://github.com/QPalmer/Pico-Gym-Write-Ups/tree/master/cryptography/la_cifra_de/vigenere.py">python script</a> that can decrypt the text using a key.</p>

<p>Using that script we're able to decrypt all of the text including the flag.</p>
'''
$ python3 vigenere.py 
Enter Key: 
FLAG
Decrypted Text: IT IS INTERESTING HOW IN HISTORY PEOPLE OFTEN RECEIVE CREDIT FOR THINGS THEY DID NOT CREATE

DURING THE COURSE OF HISTORY, THE VIGENÈRE CIPHER HAS BEEN REINVENTED MANY TIMES

IT WAS FALSELY ATTRIBUTED TO BLAISE DE VIGENÈRE AS IT WAS ORIGINALLY DESCRIBED IN 1553 BY GIOVAN BATTISTA BELLASO IN HIS BOOK LA CIFRA DEL. SIG. GIOVAN BATTISTA BELLASO 

FOR THE IMPLEMENTATION OF THIS CIPHER A TABLE IS FORMED BY SLIDING THE LOWER HALF OF AN ORDINARY ALPHABET FOR AN APPARENTLY RANDOM NUMBER OF PLACES WITH RESPECT TO THE UPPER HALFPICOCTF{B311A50_0R_V1GN3R3_C1PH3RA966878A}

THE FIRST WELL-DOCUMENTED DESCRIPTION OF A POLYALPHABETIC CIPHER HOWEVER, WAS MADE AROUND 1467 BY LEON BATTISTA ALBERTI.

THE VIGENÈRE CIPHER IS THEREFORE SOMETIMES CALLED THE ALBERTI DISC OR ALBERTI CIPHER.

IN 1508, JOHANNES TRITHEMIUS INVENTED THE SO-CALLED TABULA RECTA (A MATRIX OF SHIFTED ALPHABETS) THAT WOULD LATER BE A CRITICAL COMPONENT OF THE VIGENÈRE CIPHER.

BELLASO’S SECOND BOOKLET APPEARED IN 1555 AS A CONTINUATION OF THE FIRST. THE LOWER HALVES OF THE ALPHABETS ARE NOW SHIFTED REGULARLY, BUT THE ALPHABETS AND THE INDEX LETTERS ARE MIXED BY MEANS OF A MNEMONIC KEY PHRASE, WHICH CAN BE DIFFERENT WITH EACH CORRESPONDENT.
'''

<p>Yes there are easier ways. The easy way is less fun.</p>


:black_flag: **flag:**`picoCTF{B311A50_0R_V1GN3R3_C1PH3RA966878A}`