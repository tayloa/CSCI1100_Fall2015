word = 'bookkeeper'

#Check for single double letter
i = 0
found = False
while i < len(word)-1:
    if word[i] == word[i+1]:
        found = True
    i += 1
    
if found:
    print "The word has a single double letter."
    
#Checks for a oduble double letter
i = 0
found = False
while i < len(word)-1:
    if word[i] == word[i+1] and word[i+2] == word[i+3]:
        found = True
    i += 1

if found:
    print "The word has a double double letter."