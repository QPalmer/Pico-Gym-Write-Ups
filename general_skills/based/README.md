# Based
* **Points:** 200
* **Category:** General Skills
* **Challenge Year:** 2019

## Description
> To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. 
> Can you get the flag from this program to prove you are on the way to becoming 1337? 
> Connect with nc jupiter.challenges.picoctf.org 15130.</p>
>
> HINT: I hear python can convert things.
>


## Solution
It turns out Python CAN convert things. You can pass two arguments (a string and a base value) to `int()` to convert anything from binary to base32 into ascii text. Like most of the scripts in this write up this one can probably use a complete refactor, but it works for the purpose of solving this challenge. 

```python
def all_your_base(str, base):
    # change base input into integer
    base_val = int(base)

    # split string 
    words = str.split()

    text = [ ]

    for word in words:
        decimal = (int(word, base_val))
        text.append(chr(decimal))

    final_text = "".join(text)  
    print(final_text)

def run_program():
    while True:
        string = input(f"Enter String:\n")
        if string == "q":
            exit(0)
        else:
            base = input(f"Enter Base \n")
            all_your_base(string, base)


run_program()
```

<p>With the above script I was able to copy the strings from the webshell into my script and copy the outputs back into the webshell. There is probably a sexier way to do this but in this case it got the job done and was WAY more fun than doing the same exact thing with an online converter. Fun, after all, is why we're here! :nerd_face: </p>


```
s0ren$ python3 based.py 
Enter String:
01110000 01100101 01100001 01110010
Enter Base 
2
pear
Enter String:
155 141 160
Enter Base 
8
map
Enter String:
01110100 01100001 01100010 01101100 01100101
Enter Base 
2
table
Enter String:
163 165 142 155 141 162 151 156 145
Enter Base 
8
submarine
Enter String:
63 6f 6e 74 61 69 6e 65 72
Enter Base 
16
container
```


pasted inputs from the script above. For the hexidecimal piece I had to manually type out each hex letter individually. A little annoying because the first two questions (binary and octal) had each character separated with a space which I was able to separate (to convert each letter) using `.split()` in python.

```
s0ren-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 15130
Let us see how data is stored
table
Please give the 01110100 01100001 01100010 01101100 01100101 as a word.
...
you have 45 seconds.....

Input:
table
Please give me the  163 165 142 155 141 162 151 156 145 as a word.
Input:
submarine
Please give me the 636f6e7461696e6572 as a word.
Input:
container
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_02167de8}
```

...And there it is!

:black_flag: **flag:**`picoCTF{learning_about_converting_values_02167de8}`