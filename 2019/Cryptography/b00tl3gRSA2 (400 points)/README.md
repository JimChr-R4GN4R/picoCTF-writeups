# Description:
In RSA d is alot bigger than e, why dont we use d to encrypt instead of e? Connect with <code>nc 2019shell1.picoctf.com 40480</code>.

# Hints:
What is e generally?

# Journey
If I execute the command in terminal,I get this:

c: 9441946045928195698424166861038874800891230754558616936927685072387020518657466893007961139270325566877072507834117473429708511884926359454570074234067039611730178722581043591649511496711348194779282970917930042762828783121511514879026068271836725651947542260791351749786373786688590901505154178092904646949

n: 62743718931425333804618406703154373253092695913040000425664036426022555057655138605389986137910184400944235359564279036228044138030300121985362609500158688691579900066964565727147899701324571953234127326087835288791473039142931654744765464973804859904116047918276135383956149092554835750073641916703160094989

e: 8338767290121834344541653148366183850869545163839943905084666024850946099946232773134973820302999925724770587329369217473278673760530907159200273566784900744898309874013485957680858296561895130643632676950395689843962722149791878091276462966288632483283350628233708969670587879748274434835566651347350142273

At the first tried to find <code>d = ( e^(-1) )MOD phi</code> by trying to factor n and from there find phi , but n is very big number...

After some hours of searching I could not find something intresting...

Then I checked the hint and what variables it gives me again... For some reason e took my attention and thinked to put e as 65537 (cause of the hint) and d as e...Why? Because I can (-_-) ...

So let's try it (^_^)!

I have this in my mind:
<code>plaintext = ( ciphertext ^ d )MOD n</code>

So made a script which has c and n as they are and d = e an e = 65537 .

<code>python3 script.py</code>

Then I took this result:

<code>21080685081069964473082305196627941617916360794538080598701001685774196707802021420599447319326438641309183316151500199397018050465310263386685754092586122949472119359718409454263607539312233937774479046689650192679866322996028947025390436621034818643291374760370590905271397655813455314797251907586367434783</code>

Then converted from decimal to hex :

<code>1E0517A4D88182029618A4478F41E3C3CE116EAF8448163E16D4D4AA55591A3B31AC71F22550DD2B6B5B39261E2EA2B5E10A4D54544946528454276C64C0B65C46A22D1F40A4459A226CDB90AC949545A118470A1AD9A9F86CE48B61D3EBF52BF2D68C8609E2910BBBAB6E3E0319672ABDD8FD45D6974BE1395E2FB25B3C301F</code>

and then from hex to ascii:

<code>¤Ø¤GAãÃÎn¯H>ÔÔªUY;1¬qò%PÝ+k[9&.¢µá
MTTIFRT'ldÀ¶\F¢-@¤E"lÛ¬E¡G
Ù©øläaÓëõ+òÖ	â»«n>g*½ØýEÖKá9^/²[<0</code>
  
And I see that this is not the flag... Yeyyy  \\-_-/

Then tried to switch e with d, so <code>plaintext = pow(c,e,n)</code> , and followed the same steps.

And guess... For some reason it worked (^_^') . One of CTFs' part is luck ;)

Flag: picoCTF{bad_1d3a5_9093280}