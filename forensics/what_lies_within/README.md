# What Lies Within
* **Points:** 150
* **Category:** Forensics
* **Challenge Year:** 2019

## Description
> There's something in the <a href="https://jupiter.challenges.picoctf.org/static/011955b303f293d60c8116e6a4c5c84f/buildings.png">building</a>. Can you retrieve the flag?
>
> Hint: There is data encoded somewhere... there might be an online decoder.

![photo of church buildings](https://raw.githubusercontent.com/QPalmer/Pico-Gym-Write-Ups/master/forensics/what_lies_within/buildings.png)

## Solution
<p> The hint was very useful for this problem. I opened buildings.png in an hex editor but didn't get anywhere. Web searched for 'online decoder for hidden messages in png' and this site was the first result https://stylesuxx.github.io/steganography/. The I uploaded the buildings.png to the site and was given the flag.</p>

<p> That's a neat trick, but how does it work? What is 'Steganography'? Is it time to go down another rabbit hole? </p>

<p> <a href="https://portswigger.net/daily-swig/what-is-steganography-a-complete-guide-to-the-ancient-art-of-concealing-messages">Steganography</a> (not to be confused with stenography) is way of *hiding* a message or data (or a malicious payload) in another file. In this case, the flag was hidden in a .png file. How it was hidden is a little fuzzy to me, but my understanding is that you can manipulate the least significant bits of a file and hide parts of a full message across the entire file. This is called 'LSB Steganography' and works great with PNG files because of there are four channels of data in a PNG (r,g,b,a) and you can manipulate each one somewhat significantly without affecting the human-readibilty of the image. </p>


:black_flag: **flag:**`picoCTF{picoCTF{h1d1ng_1n_th3_b1t5}}`
