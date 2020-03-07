# Description:
This .tar file got tarred alot. Also available at /problems/like1000_0_369bbdba2af17750ddf10cc415672f1c.

# Hints:
Try and script this, it'll save you alot of time

# Journey:
So I downloaded the file with name '1000.tar' and inside it it has:

- 999.tar
- filler.txt (Inside it it has this: <code>alkfdslkjf;lkjfdsa;lkjfdsa</code>)

So I ingonred the filler.txt and opened the 999.tar .

Inside it, it has these files:

- 998.tar
- filler.txt (with the same thing inside it)

So now I realized I should make a script to extract the tar with name from 1000 to 1.

I decided to make it in python3.

So just run <code>python3 multi_tar_extractor.py</code>

And when finished I opened the final tar with name '1.tar' .
And it had the filler.txt and a file called 'flag.png'.

I opened the png file and got the flag!

Flag: picoCTF{l0t5_0f_TAR5}
