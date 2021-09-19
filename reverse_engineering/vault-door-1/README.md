# vault-door-1
* **Points:** 100
* **Category:** Reverse Engineering

### Description
> This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: <a href="https://jupiter.challenges.picoctf.org/static/ff2585f7afd21b81f69d2fbe37c081ae/VaultDoor1.java">VaultDoor1.java</a>

### Solution

Checking the java source code we find: 

```java
    // I came up with a more secure way to check the password without putting
    // the password itself in the source code. I think this is going to be
    // UNHACKABLE!! I hope Dr. Evil agrees...
    //
    // -Minion #8728
    public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '9' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '5' &&
               password.charAt(30) == '2' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '0' &&
               password.charAt(26) == '7' &&
               password.charAt(31) == 'e';
    }
```

.charAt() will return a letter in a string with the index value as an argument. There's probably something in Java that will let me rebuild the password by joining everything. But let's use python and then we can come back and see if anyone else approached this a differnet way. Manually going through lists like this reminds me too much of data entry work and I'd much rather get in the habit of using scripts. 

Using a little `ctrl+shift+l` and `opt_shift+i` magic in VScode, I created this little python dictionary based on the source code above. 

```python
letters = {
0:'d',
29:'9',
4:'r',
2:'5',
23:'r',
3:'c',
17:'4',
1:'3',
7:'b',
10:'_',
5:'4',
9:'3',
11:'t',
15:'c',
8:'l',
12:'H',
20:'c',
14:'_',
6:'m',
24:'5',
18:'r',
13:'3',
19:'4',
21:'T',
16:'H',
27:'5',
30:'2',
25:'_',
22:'3',
28:'0',
26:'7',
31:'e'
}
```   
Now we just have to loop through the dictionary in the correct order to build a list of letters. Then use `.join` to print out the flag just like we did in the first cryptography challenge. 

```python
# array of flag letters in the right order
sorted_letters = []

# range 
for i in range(32):
    #print(letters[i])
    sorted_letters.append(letters[i])

# join and print flag
flag = "".join(sorted_letters)
print(flag)
```


**flag:**
`picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}`