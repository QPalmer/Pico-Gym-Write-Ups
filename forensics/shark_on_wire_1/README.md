# shark on wire 1
* **Points:** 150
* **Category:** Forensics
* **Challenge Year:** 2019

## Description
> We found this <a href="https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap">packet capture</a>. Recover the flag.
>
>
> Hint 1: Try using a tool like Wireshark 
>
> Hint 2: What are streams? 

## Solution

<p>I'd have been completely lost of not for the hints here. </p> 

<p>I grabbed wireshark and opened up the .pcap file. My first instinct was to just control+F for the the string 'picoCTF{' and while I got some partial matches within different packets, I wasn't getting a full flag either. I figured I should pursue the hint about 'streams' rather than manually cobble together the flag (or write a script) and I'm glad a did. Thank you hints. </p>

<p>This is my first exposure to Wireshark and I really like the documentation they offer. I found an article under 'Advanced Topics'(wow really throwing this noob into the deep end of the pool eh Pico?) called 'Following Protocol Streams'
https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowStreamSection.html </p>

<p>I was able to find some control+f matches under the UDP packets so I followed the directions from the article to look at the UDP stream. Protocol streams help you look at packets in the same way an application might. I was able to move through the UDP stream with Wireshark until the flag was returned</p>

![wireshark screenshot](https://raw.githubusercontent.com/QPalmer/Pico-Gym-Write-Ups/master/forensics/shark_on_wire_1/flag.png)


:black_flag: **flag:**`picoCTF{StaT31355_636f6e6e}`