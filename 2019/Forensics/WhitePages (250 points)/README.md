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

Flag : picoCTF{not_all_spaces_are_created_equal_dd5c2e2f77f89f3051c82bfee7d996ef}
