'''Author: Aaron Taylor,tayloa5@rpi.edu

   Purpose:Compute future election results
'''
import math

if __name__ == '__main__':
    
    #VARIABLES
    candidate1_stats = raw_input("Enter candidate 1 stats ==> ")
    print candidate1_stats
    candidate1_stats = candidate1_stats.split(",")
    name1 = candidate1_stats[0]
    w1 = int(candidate1_stats[1])
    t1 = int(candidate1_stats[2])
    reps1 = int(candidate1_stats[3])
    stand1 = (w1*5)+(t1*2)+math.trunc(reps1/2)
    
    candidate2_stats = raw_input("Enter candidate 2 stats ==> ")
    print candidate2_stats
    candidate2_stats = candidate2_stats.split(",")
    name2 = candidate2_stats[0]
    w2 = int(candidate2_stats[1])
    t2 = int(candidate2_stats[2])
    reps2 = int(candidate2_stats[3])
    stand2 = (w2*5)+(t2*2)+math.trunc(reps2/2)
    
    
    #Standing
    a = True
    if stand1 < stand2:
        a = False
    else:
        a = True
        
        
    
    #First 3 lines    
    print "Columns are",name1+"'s votes,","rows are",name2+"'s votes"
    print "Votes"+"|"," 0   "+"1    "+"2    "+"3    4  "
    print ("-"*5)+"|"+("-"*25)
    
    newwin1 = 0
    newwin2 = 0
    newties1 = 0
    newties2 = 0
    for j in range(5):
        print str(j).rjust(3),"|".rjust(2)+" ",
        for i in range(5):
            if j > i:
                newwin1 = w1 
                newwin2 = w2 + 1
                newties1 = t1 
                newties2 = t2            
            elif i > j:
                newwin2 = w2 
                newwin1 = w1 + 1
                newties1 = t1 
                newties2 = t2            
            elif i == j:
                newties1 = t1 + 1
                newties2 = t2 + 1
                newwin1 = w1 
                newwin2 = w2            
            newreps1 = reps1 + i
            newreps2 = reps2 + j
            stand1 = (newwin1*5)+(newties1*2)+math.trunc(newreps1/2)
            stand2 = (newwin2*5)+(newties2*2)+math.trunc(newreps2/2)
            if stand1 > stand2:
                print name1[0]+"   ",
            elif stand2 > stand1:
                print name2[0]+"   ",
            elif stand1 == stand2:
                print "-   ",
            
        print
        
                