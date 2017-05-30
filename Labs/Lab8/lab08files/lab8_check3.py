def get_words(description):
    description = description.split()
    words = []
    for i in description:
        i = i.lower()
        i = i.replace('\"',"")
        i = i.replace(".","") 
        i = i.replace(",","")
        i = i.replace("(","")
        i = i.replace(")","")
        if len(i)>=4 and i.isalpha() == True:
            words.append(i)
    words = set(words)
    return words
club1 = open("csa.txt")
club1 = club1.read()
club1 = club1.split("|")
club1descrip = get_words(club1[1])
club2 = open("allclubs.txt")
clubnames = []
for all_clubs in club2:
    all_clubs = all_clubs.split("|")
    if all_clubs[0] != club1[0]:
        allclubdescrip = get_words(all_clubs[1])
        common = allclubdescrip & club1descrip
        if len(common) > 1:
            clubtuple = len(common),all_clubs[0]
            clubnames.append(clubtuple)

clubnames.sort(reverse=True)
print clubnames[0:5]


            
        
        

        
        
        