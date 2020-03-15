# Description:
I stopped using YellowPages and moved onto WhitePages... but the page they gave me is all blank!

whitepages.txt:

```
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
```

# Journey:

So as you can see the .txt file has only spaces...

Then I checked the file with hex editor. 

`hexyl whitepages.txt`

and got this:

```
┌────────┬─────────────────────────┬─────────────────────────┬────────┬────────┐
│00000000│ e2 80 83 e2 80 83 e2 80 ┊ 83 e2 80 83 20 e2 80 83 │××××××××┊×××× ×××│
│00000010│ 20 e2 80 83 e2 80 83 e2 ┊ 80 83 e2 80 83 e2 80 83 │ ×××××××┊××××××××│
│00000020│ 20 e2 80 83 e2 80 83 20 ┊ e2 80 83 e2 80 83 e2 80 │ ×××××× ┊××××××××│
│00000030│ 83 e2 80 83 20 e2 80 83 ┊ e2 80 83 20 e2 80 83 20 │×××× ×××┊××× ××× │
│00000040│ 20 20 e2 80 83 e2 80 83 ┊ e2 80 83 e2 80 83 e2 80 │  ××××××┊××××××××│
│00000050│ 83 20 20 e2 80 83 20 e2 ┊ 80 83 e2 80 83 20 e2 80 │×  ××× ×┊××××× ××│
│00000060│ 83 20 20 e2 80 83 e2 80 ┊ 83 e2 80 83 20 20 e2 80 │×  ×××××┊××××  ××│
│00000070│ 83 20 20 e2 80 83 20 20 ┊ 20 20 e2 80 83 20 e2 80 │×  ×××  ┊  ××× ××│
│00000080│ 83 e2 80 83 e2 80 83 e2 ┊ 80 83 20 20 e2 80 83 20 │××××××××┊××  ××× │
│00000090│ e2 80 83 20 e2 80 83 20 ┊ e2 80 83 e2 80 83 e2 80 │××× ××× ┊××××××××│
etc....
```
Here if we check cearfully,we can see that there is a pattern of `e2 80 83` and `20`

From the table which is right,we can see that where is `20` there is a space.

So I confirmed it by converting `20` from hex to ascii with this site:

https://www.rapidtables.com/convert/number/hex-to-ascii.html

Then I was curious about `e2 80 83`

I tried to convert it with the same site but It was unsupported characters...

So I searched on duckduckgo and found this page:

https://www.utf8-chartable.de/unicode-utf8-table.pl?start=8192&number=128

It says that `e2 80 83` is `EM SPACE` ...

Then I checked once again the table with `×`s and space and was thinking that he may uses hidden binary code...

Then I converted `×` to `1` and `space` to `0` but no luck...

Then tried to switch them but still no luck...

Then I decided to convert `e2 80 83` to `1` and `20` to `0` ...

I made this python3 script to do that:
```
import binascii


############################################################################# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):      #### Convert from binary to ascii
    n = int(bits, 2)                                                     ##
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)                                                  ##
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))             ##
###########################################################################


with open('whitepages.txt', 'rb') as f:
    data = f.read()
  
  
data = str(data)
data = data.replace('\\xe2\\x80\\x83','0').replace(' ','1') # replace \xe2\x80\x83 with 0 and the space with 1
data = data.replace("'","").replace('b','') # remove everything else except 0 and 1
data = ''.join(('0b',data)) # add at the beginning 0b to convert binary to ascii
  
print(text_from_bits(data))
```

And I got this text:
```
		picoCTF

		SEE PUBLIC RECORDS & BACKGROUND REPORT
		5000 Forbes Ave, Pittsburgh, PA 15213
		picoCTF{not_all_spaces_are_created_equal_dd5c2e2f77f89f3051c82bfee7d996ef}
```


Flag : picoCTF{not_all_spaces_are_created_equal_dd5c2e2f77f89f3051c82bfee7d996ef}
