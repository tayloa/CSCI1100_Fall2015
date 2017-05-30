def decipher(cipher_text):
    new_sentence = cipher_text.replace('uq','an') 
    new_sentnece = new_sentence.replace('vw','he')
    new_sentence = new_sentence.replace('aige','th')
    new_sentence = new_sentence.replace('rxr',' a')
    new_sentence = new_sentence.replace('az az','e')
    new_sentence = new_sentence.replace('yyy','u')
    new_sentence = new_sentence.replace('tzzt','o')
    new_sentence = new_sentence.replace('eie','y')
    new_sentence = new_sentence.replace('vw','he')
    return new_sentence
cipher_text = raw_input("Enter cipher text ==> ") 
print cipher_text
print
print "Deciphered as ==>",decipher(cipher_text)
print "Difference in length ==>",abs(len(cipher_text)-len(decipher(cipher_text)))
print
def encrypted(regular_text):
    new_cipher = regular_text.replace(' a','rxr')
    new_cipher = new_cipher.replace('e','az az')
    new_cipher = new_cipher.replace('y','eie')
    new_cipher = new_cipher.replace('u','yyy')
    new_cipher = new_cipher.replace('an','uq')
    new_cipher = new_cipher.replace('he','vw')
    new_cipher = new_cipher.replace('th','aige')
    new_cipher = new_cipher.replace('o','tzzt')
    return new_cipher
regular_text = raw_input("Enter regular text ==> ")
print regular_text
print
print "Encrypted as ==>",encrypted(regular_text)
print "Difference in length ==>",abs(len(encrypted(regular_text))-len(regular_text))


                                     