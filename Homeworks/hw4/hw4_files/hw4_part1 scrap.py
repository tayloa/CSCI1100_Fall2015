word = raw_input("Enter a word => ")
v = ['a','e','i','o','u']
print word
if len(word) >= 8:
    print "The word \'"+word+"\' is alternating"
else:
    print "The word \'"+word+"\' is not alternating"
    

def is_alternating(word):
    word = word.lower()
    i = 0
    while i == 0:
        if word[i] in v is True:
            value = True
        else:
            value = False
    while 0 < i <= len(word):        
            if word[i-1] < word[i]: 
                value = True
                if i%2 != 0 and word[i] in v == true:
                    value = False
                else:
                    value = True
            else:
                value = False
    i += 1
    return value
if is_alternating(word) == True:
    print "The word \'"+word+"\' is alternating"

        
        
        
    