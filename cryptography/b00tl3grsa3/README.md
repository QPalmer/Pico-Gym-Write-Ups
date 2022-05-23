# b00tl3gRSA3
* **Points:** 450
* **Category:** Cryptography
* **Challenge Year:** 2019

## Description
> Why use p and q when I can use more? Connect with nc jupiter.challenges.picoctf.org 51575.
>
> **HINT:** There's more prime factors than p and q, finding d is going to be different.

## Solution
This is pretty easy once you follow the hint and realize that the provided `n` value has more than two prime factors. 
I used this <a href="https://www.alpertron.com.ar/ECM.HTM">Intiger Factorization Calculator</a> to get all of the factors of N. I'm not sure how this is done, but I suspect that if `n` has more than two prime factors, finding those factors becomes mathematically a lot easier. For instance, I copyed an `n` value from a previous challenge that I knew had two prime factors into the Calculator and it ran for ten minutes before I forced it to quit. Some numbers are harder to factorize than others (apparently) so choosing a good `p` and `q` to make `n` is very important. All your factorizable RSA keys are belong to us. <br>
<br>
I put all of the factors of `n` into a file called `factorsofn.txt` and called that file in a python script. Since I'd had to drill all of the different RSA algorithms in previous challenges, solving for `d` wasn't that difficult! <br>
1. **Find phi_n:** This can be done by looping through all of the factors of `n`, subtracting 1, and then getting the product of all those numbers. `n = (q-1)(p-1)(r-1)(s-1)...`
2. **Find d:** we know that (de)%phi_n = 1
3. **Decrypt!: We know that plaintext = (ciphertext^d) % n


```python
# variables from 'ciphertext' file
c = 4725700440175387717370663253604604880318977580857149666291272539172288303932689486045287647583877000834540029030829082601006869125508472437228237891351252433038789618310503168468180702210742342899035752797961587148588383132514048859101029372165510825579895554852746991478738688747706720189042659472810442136495933747631402389888108872017586962
n = 11311153245717614406268293978551632656858701908973163136232191617400359805267566477740313683855090494016382101981418917068338700928663455074639156114590670116023165540170442391924518431788587345155342816303143106725405225683195911520848674721490863896312295335465267552866491456948826839796456138127758206399188124954384820069868034278296405229
e = 65537

def is_factor(f):
    try:
        n % int(f) == 0
    except:
        print(f"{f} is not a factor of N!")

# determine phi_n 
product = 1
with open('factorsofn.txt') as n_factors:
    for factor in n_factors:
        # convert to int
        factor = int(factor)

        # check if really a factor of N
        is_factor(factor)

        # subtract 1
        factor = factor - 1

        # find product (phi_n) (p-1)(q-1)(r-1)(s-1)...
        product = product * factor
        
phi_n = product        
print(f"phi_n:\n {phi_n}")

# d = (e ** -1) % phi
d = pow(e, -1, phi_n)

print(f"d: \n {d}")

# pt = (ct ** d) % n
plaintext = pow(c, d, n)
print(plaintext)

# convert to hex, then convert to string
hexstring = hex(plaintext)
hexstring = hexstring[2:]
bytes_object = bytes.fromhex(hexstring)
ascii_string = bytes_object.decode("ASCII")
print(f"FLAG:\n {ascii_string}")
```

Let's run the script!
<br>

```
$ python3 bootlegrsa3.py 
phi_n:
 11311153213842653351787056560784936078242906833851869481080973403708925574444786727012972254783778700670601572415530883493035796147137818009309132306627949337550116185786638930693643731455465156358337655985354591211953187402916657320013164919691634782598468237014373204400772312373616192129659427084787574958269763146227800616416051200000000000
d: 
 6978752158349141527373996857276635951046766526188265292392223622975882411503043338980568734030884717970242375766696542015058706031852505778513126399110443435980269892919766622863382276903149878654033341772858276937536462343972641999706003075022220309662771612427730602864721126246657166619814439693202093373783326560839237650865664132810473473
13016382529449106065933618925167173598170118383294989999418818439562860648542589
FLAG:
 picoCTF{too_many_fact0rs_0731311}
```

:black_flag: **flag:**`picoCTF{too_many_fact0rs_0731311}`
