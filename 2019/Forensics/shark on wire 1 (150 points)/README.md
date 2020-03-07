# Description:
We found this capture.pcap . Recover the flag. 

You can also find the file in /problems/shark-on-wire-1_0_13d709ec13952807e477ba1b5404e620.

# Hints:
- Try using a tool like Wireshark
- What are streams?

# Journey:
So I downloaded the .pcap file and opened it with wireshark.

After a while of search, I found this UDP packet:

55	58.468655	10.0.0.6	10.0.0.11	UDP	60	5000 → 9999 Len=4[Malformed Packet]

which contains this data:

//////////////////////////////////////////////////////////////////////////

0000   ff ff ff ff ff ff 00 0c 29 b9 02 a9 08 00 45 00   ÿÿÿÿÿÿ..)¹.©..E.

0010   00 20 00 01 00 00 40 11 66 bc 0a 00 00 06 0a 00   . ....\@.f¼......

0020   00 0b 13 88 27 0f 00 0c dd 55 70 69 63 6f 00 00   ....'...ÝU<code>pico</code>..

0030   00 00 00 00 00 00 00 00 00 00 00 00               ............

//////////////////////////////////////////////////////////////////////////

So I thinked to type in the filter 'udp',but I checked the hints and decided to type 'udp.stream'

(I do not know if there is any diference but I thought that it was a good idea. :P)

So I continued from that point and found these two packets:

63	66.623328	10.0.0.2	10.0.0.12	UDP	60	5000 → 8888 Len=1

65	68.664355	10.0.0.2	10.0.0.13	UDP	60	5000 → 8888 Len=1

which contain the same data:

//////////////////////////////////////////////////////////////////////////

0000   ff ff ff ff ff ff 00 0c 29 b9 02 a9 08 00 45 00   ÿÿÿÿÿÿ..)¹.©..E.
0010   00 1d 00 01 00 00 40 11 66 c2 0a 00 00 02 0a 00   ......@.fÂ......
0020   00 0c 13 88 22 b8 00 09 45 8e 70 00 00 00 00 00   ...."¸..E.<code>p</code>.....
0030   00 00 00 00 00 00 00 00 00 00 00 00               ............

//////////////////////////////////////////////////////////////////////////

I thinked that the 'p' is the beginning of the flag 'pico' .

So I tried to follow it's stream by right clicking on it, then go to 'follow' and then 'udp stream'.

And just like that,I found the flag!

Flag: picoCTF{StaT31355_636f6e6e}
