# extensions
* **Points:** 150
* **Category:** Forensics
* **Challenge Year:** 2019

## Description
> This is a really weird text file <a href="https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt">TXT</a>? Can you find the flag?
>
> Hint 1: How do operating systems know what kind of file it is? (It's not just the ending!)
> 

## Solution
<p>The header of a file is a good place to start. Lo and behold, are those the letters PNG?!</p>

![binary file screenshot](https://raw.githubusercontent.com/QPalmer/Pico-Gym-Write-Ups/master/forensics/extensions/pngmaybe.png)

</p>I changed the extenstion of the .txt file to .png to see if that would get it to open as an image. It's amazing when stuff 'just works'. The file was an image all along that contains the flag.</p>

:black_flag: **flag:**`picoCTF{now_you_know_about_extensions}`
