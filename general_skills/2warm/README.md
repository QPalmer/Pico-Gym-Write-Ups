# 2 Warm
* **Points:** 50
* **Category:** General Skills
* **Challenge Year:** 2019

## Description
> Can you convert the number 42 (base 10) to binary (base 2)?

## Solution

As previously discovered, it's much easier to convert to binary from hexidecimal (base 16) rather than decimal (base 10).

Using our handy (but ugly) table at https://www.asciitable.com/ we can convert 42 to '2A' in base 16. 

Again, we're in a situation where I *could* just use an online tool to convert '2A' to binary, but I want to understand a little more about how this conversion actually happens.  

https://owlcation.com/stem/How-to-Convert-Hex-to-Binary-and-Binary-to-Hexadecimal

|Hex|Binary|
|--|--|
|0|0|
|1|0|
|2|10|
|3|11|
|4|100|
|5|101|
|6|110|
|7|111|
|8|1000|
|9|1001|
|A|1010|
|B|1011|
|C|1100|
|D|1101|
|E|1110|
|F|1111|

> Hex is very easy to convert to binary.

> 1. Write down the hex number and represent each hex digit by its binary equivalent number from the table above.
> 2. Use 4 digits and add insignificant leading zeros if the binary number has less than 4 digits. E.g. Write 102 (2 decimal) as 00102.
> 3. Then concatenate or string all the digits together.
> 4. Discard any leading zeros at the left of the binary number.

So using the table 
2 = 10
A = 1010

|Base 10|Base 16|Base 2|
|------|-----|-----|
|42|2A|101010|


*Someone* should write up a beautiful conversion table for personal use. Good idea for a project moving forward. 

:black_flag: **flag:**
`picoCTF{101010}`
