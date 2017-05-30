''' Author: Aaron Taylor   Email:tayloa5@rpi.edu

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

def stories(villaininfo):  #creates a master list of all Dr.Who villain stories
    stories = []
    story = []
    for info in villaininfo:
        stories.append(info[8])
        for titles in stories:
            story.append(titles)
    story = set(story)
    return story 

def comparison(userinput,storylist,villainstuff):
    userinput = int(userinput)-1 #indicie starts at 0, so when user says 1 (Dalek),it will go
    commonstory = []             #COMMONSTORY will be a list of shared stories between the userinput villain and all others
    split = villainstuff[userinput][2].split(",") #splitting ths 3rd element of the tuple (story string)
    for i in range(len(split)):   #taking out whitespace for the string in the lisr of individual stories made by the split function   
        split[i] = split[i].strip()   
    solostories = set(split)      #SOLOSTORIES will be the userinput villain's stories
    villainname = []              #VILLAINNAME will be a list of villains who appear in the same story arc as the user input villain        
    for villain in villainstuff:                  #loop for getting the stories for every other villain
        if villain == villainstuff[userinput]:    #if the villain tuple is the same as the user input villain tuple,skip it
            continue                  
        newsplit = villain[2].split(",")        
        for i in range(len(newsplit)):
            newsplit[i] = newsplit[i].strip()
        villainsolostory = set(newsplit)    #VILLAINSOLOSTORY is a list of all other individual villain stories (changes each time because of loop)

        if (villainsolostory & solostories):   #comparing the sets(user input villain stories and all other villain stories)
            villainname.append(villain[1])     #if something is shared, the villain's name will be added to the list VILLAINNAME
            for story in (villainsolostory & solostories):
                commonstory.append(story)    #stories in which solo villain and all others share
    commonstory = set(commonstory)             #all shared stories between solo villain and other villains
    solostory = list(solostories - commonstory)#list of stories that top ten villain appears in alone(original list-commonlist),cancels out shared
    solostory.sort()
    length_of_common_stories = len(commonstory) + len(solostory)
    villainname.sort()
    return villainstuff[userinput][1],length_of_common_stories,villainname,solostory #userinput villain name,number of common stories,all other villain names,and user input villain solo stories

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
    print
    for n in range(10):                                          #printing the top ten list
        print str(n+1)+".",villainstuff[n][1]    
    print "Please enter a number between 1 and 10, or -1 to end"
    requested_villain = raw_input("Enter a villain ==> ")        #asking user which top ten vilain they want info on
    print requested_villain
    
    i = 0
    while requested_villain != "-1":        
        if requested_villain.isdigit() == False or int(requested_villain) < 1: #if the input isn't a digit,or is an integer less than 1,reprint the top ten list and ask for the input again
            print
            villainstuff = []  #top ten list
            for villain in villaininfo:
                name_stories = []   #at each append adding a villains story count,name,and stories into name_stories
                name_stories.append(int(villain[6]))
                name_stories.append(villain[0].strip())
                name_stories.append(villain[8].strip()) 
                villainstuff.append(name_stories)
            villainstuff.sort(reverse=True)   #now sorting the list within a list by number of stories
            for n in range(10):               #printing the top ten list
                print str(n+1)+".",villainstuff[n][1]        
            print "Please enter a number between 1 and 10, or -1 to end"
            requested_villain = raw_input("Enter a villain ==> ")
            if requested_villain == "-1":    #if the user inputs -1,the loop will stop and print exiting
                print requested_villain
                print "Exiting" 
            else:
                print requested_villain            
            continue
        elif requested_villain.isdigit() == True:       
            masterlist_stories = stories(villaininfo)  #variable for master set of stories
            compared = comparison(requested_villain,masterlist_stories,villainstuff)  #variable for story comparison
            print compared[0],"in",compared[1],"stories, with the following other villains:\n","="*50
            for line in textwrap.wrap(', '.join(compared[2]),68): #.join() turns the list of compared villain names into a single string,looping it will print 
                print "\t"+line
            print " \n"
            if len(compared[3]) == 0:        #if the villain has no solo storys,print the statement stastement
                print "There are no stories with only this vilain"
                print "="*50
            else:
                print "The stories that only features",compared[0],"are:\n","="*50
                for line in textwrap.wrap(', '.join(compared[3]),68): 
                    print "\t"+line
            print "\n\n\n"
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
        requested_villain = raw_input("Enter a villain ==> ")
        if requested_villain == "-1":
            print requested_villain
            print "Exiting" 
        else:
            print requested_villain
        i += 1



        