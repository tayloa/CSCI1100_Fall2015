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
    return words

x = open("wrpi.txt")
x = x.read().split("|")
x = get_words(x[1])

y = open("kendo.txt")
y = y.read().split("|")
y = get_words(y[1])

common = x & y
print common
unique = x - y
print unique
unique2 = y - x
print unique2
