# Description:
AES-ECB is bad, so I rolled my own cipher block chaining mechanism - Addition Block Chaining! 

You can find the source here: aes-abc.py. 

The AES-ABC flag is body.enc.ppm

# Hints:
You probably want to figure out what the flag looks like in ECB form...

# Journey

After some research of ECB and ppm decryption, I found decrypt.py script and changed BLOCK_SIZE = 16 as it is in aes-abc.py .

So let's run it!

<code>python3 decrypt.py</code>

And when it finish,we open the new .ppm file and see the flag!

Flag: picoCTF{d0Nt_r0ll_yoUr_0wN_aES}
