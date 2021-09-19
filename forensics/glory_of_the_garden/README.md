# Glory of the Garden
* **Points:** 50
* **Category:** Forensics

### Description
> This garden contains more than it seems.

> *hint:* What is a hex editor?

### Solution
Had to use a hint after opening the file in VS code wasn't getting me anywhere. 

Opened garden.jpg in iHex

Did a crtl+f for 'pico' which took me to the plaintext version of the flag. 
`Here is a flag "picoCTF{more_than_m33ts_the_3y3eBdBd2cc}"`

In Hexidecimal: 
`48657265 20697320 6120666C 61672022 7069636F 4354467B 6D6F7265 5F746861 6E5F6D33 3374735F 7468655F 33793365 42644264 3263637D 220A' 

For future referrence "picoCTF{" in Hexidecimal is 
`70 69 63 6F 43 54 46 7B`
This might come in handy to find flags when these challenges start getting difficult. 


**flag:**
`picoCTF{more_than_m33ts_the_3y3eBdBd2cc}`
