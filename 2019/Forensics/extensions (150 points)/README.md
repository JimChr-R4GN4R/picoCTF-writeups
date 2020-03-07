# Description:
This is a really weird text file flag.txt? Can you find the flag?

# Hints:
- How do operating systems know what kind of file it is? (It's not just the ending!
- Make sure to submit the flag as picoCTF{XXXXX}


# Journey:
So I downloaded the .txt file and tried to open it,but text editor could not open it.

So I wanted to analyze the real type of file by opening the terminal and typing <code>binwalk flag.txt</code>

and I got this:

////////////////////////////////////////////////////////////////////////////////////

0             0x0             PNG image, 1697 x 608, 8-bit/color RGB, non-interlaced

91            0x5B            Zlib compressed data, compressed

////////////////////////////////////////////////////////////////////////////////////

Here we see that it's actually a .png file . So I renamed it from flag.txt to flag.png and opened it and got the flag!

Flag: picoCTF{now_you_know_about_extensions}
