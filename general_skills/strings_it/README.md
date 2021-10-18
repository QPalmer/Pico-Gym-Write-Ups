# strings it
* **Points:** 100
* **Category:** General Skills

### Description
> Can you find the flag in <a href="https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings">file</a> without running it?

### Solution
grep is a neat way to find things in files. Let's try 

```
$ grep picoCTF strings
Binary file strings matches
```

Huh. So that wasn't completely useless. We know that the string "picoCTF" exists in the file right? 
I greped for different text and nothing was returned. Looks like "Binary file strings matches" is a common grep error when a file begins with non-text data. 

https://unix.stackexchange.com/questions/335716/grep-returns-binary-file-standard-input-matches-when-trying-to-find-a-string

Opening the strings file in a text editor and doing a ctrl+f for "pico" returned the flag. 

**flag:**
`picoCTF{5tRIng5_1T_d66c7bb7}`