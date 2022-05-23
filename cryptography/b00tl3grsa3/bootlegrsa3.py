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



        

        







    
    