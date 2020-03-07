# Description:
Find the flag in this pico_img.jpg. You can also find the file in /problems/so-meta_6_8d7541b8d04bd65a01336fdb8db6db24.

# Hints:
- What does meta mean in the context of files?
- Ever hear of metadata?

# Journey:
When read the title of the challenge I right away thinked to look at image's metadata.

So I opened terminal and typed <code>exiftool pico_img.png</code> and got this:

/////////////////////////////////////////////////////////////////////////////

ExifTool Version Number         : 11.16
File Name                       : pico_img.png
Directory                       : .
File Size                       : 106 kB
File Modification Date/Time     : 2020:03:07 22:52:13+00:00
File Access Date/Time           : 2020:03:07 22:52:15+00:00
File Inode Change Date/Time     : 2020:03:07 22:52:15+00:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 600
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Software                        : Adobe ImageReady
XMP Toolkit                     : Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27
Creator Tool                    : Adobe Photoshop CS6 (Windows)
Instance ID                     : xmp.iid:A5566E73B2B811E8BC7F9A4303DF1F9B
Document ID                     : xmp.did:A5566E74B2B811E8BC7F9A4303DF1F9B
Derived From Instance ID        : xmp.iid:A5566E71B2B811E8BC7F9A4303DF1F9B
Derived From Document ID        : xmp.did:A5566E72B2B811E8BC7F9A4303DF1F9B
Artist                          : picoCTF{s0_m3ta_505fdd8b}
Image Size                      : 600x600
Megapixels                      : 0.360

/////////////////////////////////////////////////////////////////////////////


Flag: picoCTF{s0_m3ta_505fdd8b}
