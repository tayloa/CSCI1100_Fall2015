def splitinfo(files): #separates villain info into a lists within a list
    info = []
    for allinfo in files:
        allinfo = allinfo.strip("\n").split('\t')
        info.append(allinfo)
    return info

def comparison(userinput,villainstuff):
    commonstory = []
    split = []
    for villain in villainstuff:
        if userinput == villain[1]:
            split = villain[2].split(",")               #list of userinput villain's stories
    for i in range(len(split)):
        split[i] = split[i].strip()
    solostories = set(split)
    for villain in villainstuff:                  #loop for getting the stories for every other villain
        villainsolostory = []                   
        newsplit = villain[2].split(",")
        for i in range(len(newsplit)):
            newsplit[i] = newsplit[i].strip()
        villainsolostory = set(newsplit)
        if len(villainsolostory & solostories) > 0:
            for story in (villainsolostory & solostories):
                commonstory.append(story)      #adds story to list if it contains more than one villain,we want it to add the same story multiple times for the end count
        commonstory.sort()
        commonset = set(commonstory)
        solostory = list(solostories - commonset)   #adds the story without any other villains,so count for thiswill e 1
    allstory = commonstory+solostory
    allstory.sort()
    counts = []
    for i in allstory:
            storycount = i,allstory.count(i)
            counts.append(storycount)
    countz = list(set(counts)) 
    
    return counts

if __name__ == "__main__":
    name = raw_input("Enter name of villain => ")
    print name
    who = open('DrWhoVillains.tsv')
    who.readline()        
    villaininfo = splitinfo(who)  #info for each villain is given in a list within the list of allvillain info
    villainstuff = []  #top ten list
    for villain in villaininfo:
        name_stories = []   #at each append adding a villains story count,name,and stories into name_stories
        name_stories.append(int(villain[6]))
        name_stories.append(villain[0].strip())
        name_stories.append(villain[8].strip()) 
        villainstuff.append(name_stories)
    villainstuff.sort(reverse=True)   #now sorting the list within a list by storynumber 
    comparison = comparison(name,villainstuff)  #calling the comparison function
    
    if len(comparison) == 0:
        print "\nSorry this character does not exist."
    else:
        line = "\nStories featuring \"%s\"" %(name)   #printing the final output
        print line
        print "-" * (len(line)-2)
        newcomparison = list(set(comparison))
        newcomparison.sort()
        for i in newcomparison:
            print i[0]+":","*"*i[1]