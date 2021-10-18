# First Grep
* **Points:** 100
* **Category:** General Skills
* **Challenge Year:** 2019

## Description
> Can you find the flag in <a href="https://jupiter.challenges.picoctf.org/static/315d3325dc668ab7f1af9194f2de7e7a/file">file</a>? 
>
> This would be really tedious to look through manually, something tells me there is a better way.
>

## Solution
Not my first grep. What **is** grep? <br>

The genesis of has to do with early text editors using regular expressions with those text editors. <br>

Where GREP Came From:<br>
https://www.youtube.com/watch?v=NTfOnGZUZDk

* g/re/p
* **g**lobal/**re**gex/**p**rint 


Was able to solve this challenge by downloading the file and "grepping?" for the beginning of the flag: 

```
s0ren$ grep picoCTF{ file
picoCTF{grep_is_good_to_find_things_f77e0797}
```

- :black_flag: **flag:**
`picoCTF{grep_is_good_to_find_things_f77e0797}`
