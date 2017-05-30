''' Author: Aaron Taylor Email:tayloa5@rpi.edu

    Purpose:This program asks the user for a top ten Doctor Who villain, then returns
    a list of other villains that appear in the same story arch as said villain.If the 
    top ten villain appears in their own story arc alone,that story will be returned 
    aswell.
'''

import textwrap
def splitinfo(files): #separates villain info into a lists within a list
    info = []
    for allinfo in files:
        allinfo = allinfo.strip("\n").split('\t')
        info.append(allinfo)
    return info

def stories(villaininfo):  #creates a master list of all Dr.Who villain appearances
    stories = []
    story = []
    for info in villaininfo:
        stories.append(info[8])
        for titles in stories:
            story.append(titles)
    story = set(story)
    return story 

def comparison(userinput,storylist,villainstuff):
    userinput = int(userinput)-1 #user will never input 0
    commonstory = []
    split = villainstuff[userinput][2].split(",") #splitting ths 3rd element of the tuple (story string)
    for i in range(len(split)):
        split[i] = split[i].strip()
    solostories = set(split)
    villainname = []                               #list of villains who appear in the same story arc as the given top ten villain
    for villain in villainstuff:                  #loop for getting the stories for every other villain
        if villain == villainstuff[userinput]:      #if the villain index is the same as the user input,skip it
            continue
        villainsolostory = []                   
        newsplit = villain[2].split(",")
        for i in range(len(newsplit)):
            newsplit[i] = newsplit[i].strip()
        villainsolostory = set(newsplit)
        if len(villainsolostory & solostories) > 0:
            villainname.append(villain[1])
            for story in (villainsolostory & solostories):
                commonstory.append(story)
    commonstory = set(commonstory)
    solostory = list(solostories - commonstory) #list of stories that top ten villain appears in alone
    villainname.sort()
    return villainstuff[userinput][1],len(commonstory),villainname,solostory

if __name__ == '__main__':
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
    for n in range(10):               #printing the top ten list
        print str(n+1)+".",villainstuff[n][1]
    
    print "Please enter a number between 1 and 10, or -1 to end"
    requested_villain = raw_input("Enter a villain ==> ")    #asking user which top ten vilain they want info on
    print requested_villain
    
    i = 0 #loop for asking user input
    while requested_villain != "-1":
        print
        villainstuff = [] #top ten list loop
        for villain in villaininfo:
            name_episodes = int(villain[5]),villain[0],villain[8]
            villainstuff.append(name_episodes)
        villainstuff.sort(reverse=True)
        for n in range(10):
            print str(n+1)+".",villainstuff[n][1]
        print
        masterlist_stories = stories(villaininfo)  #variable for master set of stories
        compared = comparison(requested_villain,masterlist_stories,villainstuff)  #variable for story comparison
        print compared[0],"in",compared[1],"stories, with the following other villains:\n","="*50
        print ', '.join(compared[2]),"\n"
        print "The stories that only features",compared[0],"are:\n","="*50
        print ', '.join(compared[3]),"\n"
        print
        villainstuff = [] #top ten list loop
        for villain in villaininfo:
            name_episodes = int(villain[5]),villain[0],villain[8]
            villainstuff.append(name_episodes)
        villainstuff.sort(reverse=True)
        for n in range(10):
            print str(n+1)+".",villainstuff[n][1]   
        print "Please enter a number between 1 and 10, or -1 to end"
        requested_villain = raw_input("Enter a villain ==> ")
        print requested_villain
        i += 1


        