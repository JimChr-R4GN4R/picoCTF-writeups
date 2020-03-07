# Description:
Theres something in the building.png. Can you retrieve the flag?

# Hints:
There is data encoded somewhere, there might be an online decoder

# Journey:
At first I opened terminal and wanted to check if there is hidden text in the image by typing <code>strings building.png</code>.

Didn't found something...

Then checked it's metadata by typing <code>exiftool building.png</code> but still nothing...

Then checked the hint and checked for stegano-hidden data in the png.

So typed <code>zsteg building.png</code> (you can download it from here https://github.com/zed-0xff/zsteg)

and got this:

////////////////////////////////////////////////////////////////////

b1,r,lsb,xy         .. text: "^5>R5YZrG"

b1,rgb,lsb,xy       .. text: "<code>picoCTF{h1d1ng_1n_th3_b1t5}</code>"

b1,abgr,msb,xy      .. file: PGP\011Secret Sub-key -

b2,b,lsb,xy         .. text: "XuH}p#8Iy="

b3,abgr,msb,xy      .. text: "t@Wp-_tH_v\r"

b4,r,lsb,xy         .. text: "fdD\"\"\"\" "

b4,r,msb,xy         .. text: "%Q#gpSv0c05"

b4,g,lsb,xy         .. text: "fDfffDD\"\""

b4,g,msb,xy         .. text: "f\"fff\"\"DD"

b4,b,lsb,xy         .. text: "\"$BDDDDf"

b4,b,msb,xy         .. text: "wwBDDDfUU53w"

b4,rgb,msb,xy       .. text: "dUcv%F#A`"

b4,bgr,msb,xy       .. text: " V\"c7Ga4"

b4,abgr,msb,xy      .. text: "gOC_$_@o"

////////////////////////////////////////////////////////////////////

Flag: picoCTF{h1d1ng_1n_th3_b1t5}
