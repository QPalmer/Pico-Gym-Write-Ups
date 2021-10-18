#create a list of letters in the alphabet
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

ciphertext = "ynkooejcpdanqxeykjrbdofgkq"
string = ciphertext.lower()      
no_decode = [" ", "_"]
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
        if letter in no_decode:
            decoded.append(letter)
        else:
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



