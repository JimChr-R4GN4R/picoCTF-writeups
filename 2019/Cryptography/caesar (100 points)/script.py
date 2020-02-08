plainText = 'rgdhhxcviwtgjqxrdcdydkefyh'


for shift in range(1,26):

	def caesar(plainText, shift): 
		cipherText = ""
		for ch in plainText:
			if ch.isalpha():
				stayInAlphabet = ord(ch) + shift 
				if stayInAlphabet > ord('z'):
					stayInAlphabet -= 26
				finalLetter = chr(stayInAlphabet)
				cipherText += finalLetter
		return cipherText
	
	print('shift = +',shift,' decrypted text: ',caesar(plainText, shift),'\n')


########### Useful sources for the script ###########
https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python
