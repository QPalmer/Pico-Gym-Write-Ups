# First Grep
* **Points:** 100
* **Category:** General Skills

### Description
> Can you find the flag in <a href="https://jupiter.challenges.picoctf.org/static/315d3325dc668ab7f1af9194f2de7e7a/file">file</a>? This would be really tedious to look through manually, something tells me there is a better way.

### Solution
Not my first grep. What **is** grep? What a funny name right? 

g/re/p




Was able to solve this challenge by downloading the file and "grepping?" for the beginning of the flag: 

```
$ grep picoCTF{ file
picoCTF{grep_is_good_to_find_things_f77e0797}
```

**flag:**
`picoCTF{grep_is_good_to_find_things_f77e0797}`
