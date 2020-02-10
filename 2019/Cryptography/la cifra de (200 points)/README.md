# Description:
I found this cipher in an old book. Can you figure out what it says? Connect with <code>nc 2019shell1.picoctf.com 61559</code>.

# Hints:
- There are tools that make this easy.
- Perhaps looking at history will help

# Journey

When we execute the command in terminal,we get this text:
########################################################################################

  Ne iy nytkwpsznyg nth it mtsztcy vjzprj zfzjy rkhpibj nrkitt ltc tnnygy ysee itd tte cxjltk

Ifrosr tnj noawde uk siyyzre, yse Bnretèwp Cousex mls hjpn xjtnbjytki xatd eisjd

Iz bls lfwskqj azycihzeej yz Brftsk ip Volpnèxj ls oy hay tcimnyarqj dkxnrogpd os 1553 my Mnzvgs Mazytszf Merqlsu ny hox moup Wa inqrg ipl. Ynr. Gotgat Gltzndtg Gplrfdo 

Ltc tnj tmvqpmkseaznzn uk ehox nivmpr g ylbrj ts ltcmki my yqtdosr tnj wocjc hgqq ol fy oxitngwj arusahje fuw ln guaaxjytrd catizm tzxbkw zf vqlckx hizm ceyupcz yz tnj fpvjc hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3xg6ndl651}

Yse lncsz bplr-izcarpnzjo dkxnroueius zf g uzlefwpnfmeznn cousex mzwkapr, cfd mgip axtfnj 1467 gj Lkty Bgyeiyyl Argprzn.

Ehk Atgksèce Inahkw ts zmprkkzrk xzmkytmkx narqpd zmp Argprzn Oiyh zr Gqmexyt Cousex.

Ny 1508, Jumlntjd Txnehkrtuy nyvkseej yse yt-narqpd zfmurf ceiyl (a sferoc zf ymtfzjo arusahjes) zmlt ctflj qltkw me g hciznnar hzmvtyety zf zmp Volpnèxj Nivmpr.

Hjwlgxz’s yjnoti moupwez fapkfcej ny 1555 ay f notytnafeius zf zmp fowdt. Zmp lubpr nfwvkx zf zmp arusahjes gwp nub dhokeej wpgaqlrrd, muz yse gqahggpty fyd zmp itipx rjetkwd axj xidjo be rpatx zf g ryestyii ppy vmcayj, hhohs cgs me jnqfkwpnz bttn jlcn hzrxjdpusoety.

########################################################################################

So let's begin.
- First of all here we see the flag encrypted:
hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3xg6ndl651}

- Second,we know that numbers are not encrypted cause of '1553', '1467' and '1555'

- From the title, we see Italian

Let's try caecar cipher!

Tried it with no luck...

Let's check the dates...1553

So let's duckduckgo (we hate google) '1553 encryption'!

The first result is 'Vigenère cipher' which was made from Leon Battista Alberti who was Italian !

So let's try decrypt the flag with Vigenère decryptor!

I used https://www.guballa.de/vigenere-solver and pasted all the text to decrypt it.

It finds that the encryption key was "flag" and we see at flag's place 'halfpicoCTF{b311a50_0r_v1gn3r3_c1ph3rb6cdf651}'

Flag: picoCTF{b311a50_0r_v1gn3r3_c1ph3rb6cdf651}
