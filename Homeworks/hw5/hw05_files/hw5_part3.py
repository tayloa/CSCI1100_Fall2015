''' Author: Aaron Taylor Email:tayloa5@rpi.edu

     Purpose:This program reads baby names from a list
     and returns the most popular names.
'''

if __name__ == "__main__":
    filename = raw_input("File name => ")
    print filename
    k = int(raw_input("How many names to display? => "))
    print k
    print 
    
    #MALE and FEMALE lists
    
    files = open(filename)
    files = files.readlines()
    male = []
    female = []
    
    for i in files:
        names = []
        names = i.split(",")
        if names[1] == 'M':
            n = names[2].strip("\n")
            n = int(n)
            males = n,names[0],names[1]
            male.append(males)            
        elif names[1] == 'F':
            names = i.split(",") #remove the '' from each, sort each based on
            n = names[2].strip("\n")
            n = int(n)
            females = n,names[0],names[1]
            female.append(females)
    
    #sorting
    print male
    male.sort(reverse=True)
    print male
    female.sort(reverse=True)
    
    #printing names based on cutoff
    
    print "Top female names"        
    for i in range(k):
        if (k != 0) and (i%2 == 0) and i != 0:
            print female[i][1],"("+str(female[i][0])+")"
        else:
            print female[i][1],"("+str(female[i][0])+")",

    
    
       
    #print "\nTop male names"        
    #for i in range(k):
        #if (k != 0) and (i%2 == 0) and i != 0:
            #print female[i][1],"("+str(female[i][0])+")"
        #else:
            #print male[i][1],"("+str(male[i][0])+")",
       
            