"""Author: <your name and email>

   Purpose: This program reads a word from user input and prints whether
   the word is at least 8 characters long, starts with a vowel, 
   alternates vowels and consonants and the consonants are in 
   increasing alphabetical order.

"""

######### Put all your function definitions here
######### I am putting in a template to get you started

def is_alternating(word):
    word = word.lower()
    v = ['a','e','i','o','u']
    a = True
    if len(word) < 8: #if the word is less than 8 letters, return false
        return False
    elif word[0] not in v: #if the first letter isnt a vowel, return false
        a = False
        return False
    elif a == True: #if the first letter ia a vowel
        i = 1
        while i < len(word): #for the length of the word
            if (word[i] in v) == False: # if the letter is not a vowel, move to the next letter
                i += 1
                if i < len(word): # if we are still in range, check if the next letter is a vowel
                    if (word[i] in v) == True: # if it is a vowel, move to the next one
                        i += 1
            else:   
                return False # if 2 letters in a row arent vowels, the word isnt alternating
        i = 3  # since we know the word is alternating, check if 
        while i < len(word): # check if the CONSANANTS are in increasing alphabetical order
            if (word[i-2] >= word[i]): # if the pr
                return False 
            i += 2
        return True
    else:
        return True

######## This is the main body of your program
######## All code should be below the if statement

######## This if statement is executed when we run the program
######## but not when we import it as a module

#######  Keep the body of your program small, put main
#######  functions in a function, but each function should do
#######  something simple

if __name__ == "__main__":
    word = raw_input("Enter a word => ")
    print word
    ## now call your function here and check its output
is_alternating(word)

if is_alternating(word) is True:
    print "The word \'"+word.lower()+"\' is alternating"

else:
    print "The word \'"+word.lower()+"\' is not alternating"


        
    
        