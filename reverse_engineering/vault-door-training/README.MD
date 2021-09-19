# vault-door-training
* **Points:** 50
* **Category:** Reverse Engineering

### Description
> Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: <a href="https://jupiter.challenges.picoctf.org/static/a4a1ca9c54d8fac9404f9cbc50d9751a/VaultDoorTraining.java">Vaultdoortraining.java</a>


### Solution
The password is hardcoded into the .java file on line 24
`return password.equals("w4rm1ng_Up_w1tH_jAv4_be8d9806f18");`

It looks like this is just a simple cautionary tale against putting plaintext passwords into source code. Anyone with eyes and access to a text editor can lift the password. 

**flag:**
`picoCTF{w4rm1ng_Up_w1tH_jAv4_be8d9806f18}`