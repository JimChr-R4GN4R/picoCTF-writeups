#Description:
The numbers... what do they mean?

# Hint:
The flag is in the format PICOCTF{}

#File:
42 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }


# Journey

So when read the file, I realized that every number is an alphabet's letter.
That means a = 1, b = 2 ,..., z = 26

So I made a quick python3 script.
So let's run it!
<code>python3 script.py</code>

Flag: picoctf{thenumbersmason}

I tried it,but it did not work...So checked hint and I realized that it wants all the letters in uppercase.
So I added in script Upper_case_convert.

Final Flag: PICOCTF{THENUMBERSMASON}
