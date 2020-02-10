# Description:
Class, take your seats! It's PRIME-time for a quiz... <code>nc 2019shell1.picoctf.com 61751</code>

# Hints:
https://simple.wikipedia.org/wiki/RSA_algorithm

# Jounrey

We see clearly that the challegne has to do with RSA encryption.Let's begin!

So if we execute the command in temrinal, we get this at first:

#############################################################################################

Good morning class! It's me Ms. Adleman-Shamir-Rivest
Today we will be taking a pop quiz, so I hope you studied. Cramming just will not do!
You will need to tell me if each example is possible, given your extensive crypto knowledge.
Inputs and outputs are in decimal. No hex here!
#### NEW PROBLEM ####
q : 60413

p : 76753
##### PRODUCE THE FOLLOWING ####
n

IS THIS POSSIBLE and FEASIBLE? (Y/N):

#############################################################################################

It want us to find n variable.

After a bit, I found that n = q * p

So type 'y' and write the n

n = q * p = 60413 * 76753 = 4636878989

So write '4636878989'


Next it says this:

#############################################################################################

#### NEW PROBLEM ####
p : 54269

n : 5051846941
##### PRODUCE THE FOLLOWING ####
q

IS THIS POSSIBLE and FEASIBLE? (Y/N):

#############################################################################################

From the previous step,we see that q = n/p = 5051846941/54269 = 93089

So type 'Y' and write '93089'


Next step say:

#############################################################################################

#### NEW PROBLEM ####
e : 3

n : 12738162802910546503821920886905393316386362759567480839428456525224226445173031635306683726182522494910808518920409019414034814409330094245825749680913204566832337704700165993198897029795786969124232138869784626202501366135975223827287812326250577148625360887698930625504334325804587329905617936581116392784684334664204309771430814449606147221349888320403451637882447709796221706470239625292297988766493746209684880843111138170600039888112404411310974758532603998608057008811836384597579147244737606088756299939654265086899096359070667266167754944587948695842171915048619846282873769413489072243477764350071787327913
##### PRODUCE THE FOLLOWING ####
q

p

IS THIS POSSIBLE and FEASIBLE? (Y/N):

#############################################################################################

Now we have e and n and need to find q and p which is not possible, so type 'n' and continue.

Next step says:

#### NEW PROBLEM ####
q : 66347

p : 12611
##### PRODUCE THE FOLLOWING ####
totient(n)

IS THIS POSSIBLE and FEASIBLE? (Y/N):

#############################################################################################

We have p and q and we need to find totient(n) [or φ(n) or phi(n) ]

phi(n) = (p - 1) * (q - 1)

phi(n) = (12611 - 1) * (66347 - 1)

phi(n) = 12610*66346

phi(n) = 836623060

So type 'y' and write '836623060'

Next step says:

#############################################################################################

#### NEW PROBLEM ####
plaintext : 6357294171489311547190987615544575133581967886499484091352661406414044440475205342882841236357665973431462491355089413710392273380203038793241564304774271529108729717

e : 3

n : 29129463609326322559521123136222078780585451208149138547799121083622333250646678767769126248182207478527881025116332742616201890576280859777513414460842754045651093593251726785499360828237897586278068419875517543013545369871704159718105354690802726645710699029936754265654381929650494383622583174075805797766685192325859982797796060391271817578087472948205626257717479858369754502615173773514087437504532994142632207906501079835037052797306690891600559321673928943158514646572885986881016569647357891598545880304236145548059520898133142087545369179876065657214225826997676844000054327141666320553082128424707948750331
##### PRODUCE THE FOLLOWING ####
ciphertext

IS THIS POSSIBLE and FEASIBLE? (Y/N):

#############################################################################################

Now it starts to get ap bit harder. It want's us to encrypt the plaintext with e and n.

After some research I found that <code> c = m ^ e mod n </code> ( c = ciphertext , m = plaintext message )

Now cause of the really big numbers we need finally the help of python3 !!!!

I made a script after some time to calculate ciphertext,so let's run it!
<code>python3 pl-e-n_ciphertext.py</code>
