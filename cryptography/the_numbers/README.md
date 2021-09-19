# The Numbers
* **Points:** 50
* **Category:** Cryptography

### Description
> The <a href ="https://github.com/QPalmer/Pico-Gym-Write-Ups/blob/master/cryptography/the_numbers/the_numbers.png">numbers...</a> what do they mean?

### Solution

We need to find the flag in this image: 
![Image of numbers in MS Paint](https://raw.githubusercontent.com/QPalmer/Pico-Gym-Write-Ups/master/cryptography/the_numbers/the_numbers.png)

Ok so I got a little ahead of myself here. The brackets in the .png image give away that the numbers are in flag format. I started building a little table to decode the numbers assuming that 16, 9, 3, 15 mapped to the letters p, i, c, 0. 

| numbers| 16 | 9 | 3 | 15 | 3 | 20 | 6 | 
| -- | -- | --| --| --| --| --| -- | 
| flag | p | i | c | o | C | T | F | 

This is a 'rot 0' caeser cipher. "P" is the 16th letter of the alphabet so it is represented as "16" 

So now all we have to do is convert the rest of the numbers into their cooresponding letters. 

PicoCTF
{
20
8 
5
14
21
13
2
5
18
19
13
1
19
15
14
}

It probably wasn't necessary to write a script to do transpose the numbers into letters but I did it anyway. Good practice for more difficult challenges. 

I hard coded the numbers above into this script: <a href= "https://github.com/QPalmer/Pico-Gym-Write-Ups/blob/master/cryptography/the_numbers/my_caesar_cipher.py#L35">my_caesar_cipher.py</a></b> which returns a the following string: 
thenumbersmason

**flag:**
`picoCTF{thenumbersmason}`