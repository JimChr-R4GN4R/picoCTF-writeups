# Description:
We found this packet capture.pcap and picopico.key. 

Recover the flag. 

You can also find the file in /problems/webnet1_0_d63b267c607b8fedbae100068e010422.

# Hints:
- Try using a tool like Wireshark
- How can you decrypt the TLS stream?

# Journey:

(This challenge is like WebNet0)

So as like WebNet0 challenge, we open the pcap file with wireshark, then we insert the key from picopico.key in `Edit > Preferences > Protocols > SSL` and then analyze the packets.

So at the beginning I found this packet:
```
45	0.341085	172.31.22.220	128.237.140.23	HTTP	581	HTTP/1.1 200 OK  (text/css)
```
And decided to look deeper in this.

So `right click > Follow > SSL Stream` 

At first I checked this:
```
HTTP/1.1 200 OK
Date: Fri, 23 Aug 2019 16:27:04 GMT
Server: Apache/2.4.29 (Ubuntu)
Last-Modified: Mon, 12 Aug 2019 16:47:05 GMT
ETag: "62-58fee462bf227-gzip"
Accept-Ranges: bytes
Vary: Accept-Encoding
Content-Encoding: gzip
Pico-Flag: picoCTF{this.is.not.your.flag.anymore}
Content-Length: 100
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/css
```
But this is obviously not our flag,So I scroll more down...

```
.....JFIF..............Exif..MM.*.................J...........R.(...........;.........Z................................picoCTF{honey.roasted.peanuts}......ICC_PROFILE.......lcms....mntrRGB XYZ .........).9acspAPPL...................................-lcms...............................................
desc.......^cprt...\....wtpt...h....bkpt...|....rXYZ........gXYZ........bXYZ........rTRC.......@gTRC.......@bTRC.......@desc........c2..................................................................................text....FB..XYZ ...............-XYZ ...........3....XYZ ......o...8.....XYZ ......b.........XYZ ......$.........curv...............c...k...?.Q.4!.).2.;.F.Qw].kpz....|.i.}...0.....C.................
		
...
```

Hello there...

I tried this flag and guess what!!!

Flag: picoCTF{honey.roasted.peanuts}
