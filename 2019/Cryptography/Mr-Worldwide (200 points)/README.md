# Description:
A musician left us a message.txt. What's it mean?

message.txt = (35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)

# Hints:
None
  
# Journey
We see in text file that it has coordinates.So I thinked at first that I will put the first letter of every country the cord is,but didn't work. So after that tried the first letter of the city these cords are.
I made a script to do the work fast.
So let's try it!

<code>python3 script.py</code> (it needs reverse_geocoder module.If you do not have it,then it will install it for you.
If something goes wrong,then try in your terminal type <code>pip3 install reverse_geocoder</code> and then run the script).

When finish,we copy the first letter of every name and we get this:

K from Kamigyo-ku

O from Odessa

D from Dayton

I from Istanbul (Name says 'Eminoeunue',but at Admin1 says Istanbul and chose to use this one.)

A from Abu Dhabi

K from Kuala Lumpur

A from Addis Ababa

L from Loja

A from Amsterdam

S from Sleepy Hollow

K from Kodiak

A from Alexandria

So we have KODIAKALASKA, but if we read message text,we see that it has a '_' , so let's add it to it's right place.
So we have KODIAK_ALASKA !


Flag: picoCTF{KODIAK_ALASKA}
