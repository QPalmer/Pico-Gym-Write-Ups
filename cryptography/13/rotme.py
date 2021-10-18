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