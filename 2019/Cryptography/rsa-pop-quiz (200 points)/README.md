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

After a bit, I found that n = q*p

So type 'y' and write the n

n = q*p = 60413*76753 = 4636878989

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
