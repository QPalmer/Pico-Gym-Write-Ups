# What's a net cat?
* **Points:** 100
* **Category:** General Skills

## Description
> Using netcat (nc) is going to be pretty important. Can you connect to jupiter.challenges.picoctf.org at port 25103 to get the flag?

## Solution

PicoCTF has a webshell that can be used to solve challenges. Firing that up, it was easy to use nc to call the url and port to get the flag. 

```
s0ren-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 25103
You're on your way to becoming the net cat master
picoCTF{nEtCat_Mast3ry_d0c64587}
```

I have a lot of questions about what net cat is actually used for. Most of the tutorials I've run into sofar online present this tool in a nefarious context as a means to set up a <a href="https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md">reverse shell</a>. However, this security company blog outlines use by network admins and has a handy 'cheat sheet' that I'll likely need to reference in future challenges. 

https://www.varonis.com/blog/netcat-commands/


:black_flag: **flag:**
`picoCTF{nEtCat_Mast3ry_d0c64587}`
