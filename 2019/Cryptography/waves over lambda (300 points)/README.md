# Description:
We made alot of substitutions to encrypt this. Can you decrypt it? Connect with <code>nc 2019shell1.picoctf.com 49935</code>.

# Hints:
Flag is not in the usual flag format

# Journey
When executed the command in terminal, I got this:

########################################################################################

-------------------------------------------------------------------------------
oikfmvgx jymy px diam bcvf - bmynaykod_px_o_irym_cvqhtv_btpppmahmv
-------------------------------------------------------------------------------
uy uymy kig qaoj qimy gjvk v navmgym ib vk jiam iag ib iam xjpe gpcc uy xvu jym xpkz, vkt gjyk p aktymxgiit bim gjy bpmxg gpqy ujvg uvx qyvkg hd v xjpe biaktympkf pk gjy xyv.  p qaxg vozkiucytfy p jvt jvmtcd ydyx gi ciiz ae ujyk gjy xyvqyk gict qy xjy uvx xpkzpkf; bim bmiq gjy qiqykg gjvg gjyd mvgjym eag qy pkgi gjy hivg gjvk gjvg p qpfjg hy xvpt gi fi pk, qd jyvmg uvx, vx pg uymy, tyvt upgjpk qy, evmgcd upgj bmpfjg, evmgcd upgj jimmim ib qpkt, vkt gjy gjiafjgx ib ujvg uvx dyg hybimy qy.

########################################################################################


We will use a very good site (and I think one of my favourites)!
https://www.boxentriq.com/code-breaking/cipher-identifier

If we paste the ciphertext in it,it recognise it as Monoalphabetic Substitution Cipher.
So it has a decryptor for this cipher.


We paste it here:

https://www.boxentriq.com/code-breaking/cryptogram

and execute auto decrypt.

When it's done, it gives this result first:

oikfmvgx jymy px diam bcvf - bmynaykod_px_o_irym_cvqhtv_btpppmahmv = congrats here is your flag frequency is c over lambda fdiiirubra

So we fix it like this:
frequency_is_c_over_lambda_fdiiirubra


Flag: picoCTF{frequency_is_c_over_lambda_fdiiirubra}
