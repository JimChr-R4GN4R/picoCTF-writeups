import codecs

c = 'cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}' # cipher text

rot13 = lambda s: codecs.decode(s, 'rot13')
decrypted_message = rot13(c)


print(decrypted_message)


############ Useful script sources ############
#https://stackoverflow.com/questions/42788831/encrypt-decrypt-with-rot13-using-a-lambda
