# Description:
Decrypt this message.txt. You can find the ciphertext in /problems/caesar_6_238b8f4604d91ecb59cda5b4f0e66fc8 on the shell server.

message.txt = picoCTF{rgdhhxcviwtgjqxrdcdydkefyh}

# Hints:
caesar cipher tutorial --> https://learncryptography.com/classical-encryption/caesar-cipher

# Journey

So from the title we realize that it's caecar cipher which is really easy to break it.

Let's run caecar's bruteforce script!

<code>python3 script.py</code>

We see at +11 shift a nice plaintext...
crossingtherubiconojovpqjs

So let's try it!

Aaaand it's correct!

Flag: picoCTF{crossingtherubiconojovpqjs}
