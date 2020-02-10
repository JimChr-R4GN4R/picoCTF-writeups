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

First step is done!

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

Second step is done!

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
