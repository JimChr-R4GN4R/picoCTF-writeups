c = '42 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }' # numbered string /// 16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }

c = c.split(' ')



decrypted_message = "" # character converted variable

Num_of_letters = len(c) # num of characters c contains (24 characters in this example)

for i in range (0 , Num_of_letters):

  ###################################
  try:                             ##
    while int(c[i]) > 26:          #### if number is 27,alphabet has 26 letters,so 27 is 'a'
      c[i] = str(int(c[i]) - 26)   ##
  except:                          ##
    pass                           ##
  ###################################

  ##################################################
  if c[i] == "1":                                 ##
    decrypted_letter = "a"                        ##
  elif c[i] == "2":
    decrypted_letter = "b"
  elif c[i] == "3":
    decrypted_letter = "c"
  elif c[i] == "4":
    decrypted_letter = "d"
  elif c[i] == "5": 
    decrypted_letter = "e"
  elif c[i] == "6":
    decrypted_letter = "f"
  elif c[i] == "7":
    decrypted_letter = "g"
  elif c[i] == "8": 
    decrypted_letter = "h"
  elif c[i] == "9":
    decrypted_letter = "i"
  elif c[i] == "10":
    decrypted_letter = "j"
  elif c[i] == "11": 
    decrypted_letter = "k"
  elif c[i] == "12":
    decrypted_letter = "l"
  elif c[i] == "13":
    decrypted_letter = "m"
  elif c[i] == "14":
    decrypted_letter = "n"
  elif c[i] == "15": 
    decrypted_letter = "o"
  elif c[i] == "16":
    decrypted_letter = "p"
  elif c[i] == "17":
    decrypted_letter = "q"
  elif c[i] == "18": 
    decrypted_letter = "r"
  elif c[i] == "19":
    decrypted_letter = "s"
  elif c[i] == "20":
    decrypted_letter = "t"
  elif c[i] == "21": 
    decrypted_letter = "u"
  elif c[i] == "22":
    decrypted_letter = "v"
  elif c[i] == "23": 
    decrypted_letter = "w"
  elif c[i] == "24":
    decrypted_letter = "x"
  elif c[i] == "25":
    decrypted_letter = "y"
  elif c[i] == "26": 
    decrypted_letter = "z"
  else:                                           ##
    decrypted_letter = str(c[i])                  ##
  ##################################################
  
  decrypted_message = str(decrypted_message + decrypted_letter) # add number's character in our $a variable

Upper_case_convert = 1 # Do you want decrypted message in upper case? (yes = 1/ no = 0)

if Upper_case_convert == 1:
  decrypted_message = decrypted_message.upper()
  
print(decrypted_message)
