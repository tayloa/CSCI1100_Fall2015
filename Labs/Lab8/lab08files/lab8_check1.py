def get_words(description):
    description = description.split()
    words = []
    for i in description:
        i = i.lower()
        i = i.replace('\"',"")
        i = i.replace(".","") #replace needs to be set equal to variable
        i = i.replace(",","")
        i = i.replace("(","")
        i = i.replace(")","")
        if len(i)>=4 and i.isalpha() == True:
            words.append(i)
    words = set(words)
    return words,len(words)

files = open("wrpi.txt")    
files = files.read()
files = files.split("|") #split into 2 parts,description is element 1 of the string
x = get_words(files[1])
print x

