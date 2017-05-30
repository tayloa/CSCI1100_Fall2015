from boards import *
from ricks import *
import math

def getinfo(filename,filetype):  ##function for splitting the info in the file,takes as parameters a user input filename and a file type('board' or 'rick')
    f = open(filename)
    rickinfolist = []  ##list of dictionaries made up of each rick's information
    boardinfolist = []  ##list of dictionaries made up of each board's information
    if filetype == "rick":
        for line in f:  ##splitting the info for each rick, then adding each dictionary to rickinfolst
            infolist = line.strip().split("|")
            ricktionary = {} ##new dicionary for a rick's info
            ricktionary['name'] = infolist[0]
            ricktionary['x,y'] = int(infolist[1]),int(infolist[2])
            ricktionary['length'] = int(infolist[3])
            ricktionary['dx,dy'] = float(infolist[4]),float(infolist[5])
            rickinfolist.append(ricktionary)
        return rickinfolist
    if filetype == 'board':
        for line in f:
            infolist = line.strip().split("|")
            boarddictionary = {} ##new dicionary for a board's info
            boarddictionary['name'] = infolist[0]
            boarddictionary['gravity'] = int(infolist[1])
            boarddictionary['portal'] = int(infolist[2]),int(infolist[3])
            boarddictionary['right'] = infolist[4]
            boarddictionary['up'] = infolist[5]
            boarddictionary['left'] = infolist[6]
            boarddictionary['down'] = infolist[7]
            boarddictionary['obstacles'] = []
            if len(infolist) > 8:
                obstacles = infolist[8::]
                i = 0
                while i != len(obstacles):
                    coordinates = int(obstacles[i]),int(obstacles[i+1])
                    boarddictionary['obstacles'].append(coordinates)
                    i += 2
            boardinfolist.append(boarddictionary)
        return boardinfolist
            
if __name__ == "__main__":
    rickfile = raw_input("Rick file name => ")
    print rickfile
    boardfile = raw_input("Board file name => ")
    print boardfile
    
    allrickinfo = getinfo(rickfile,"rick")  ##list of dicionaries containing each rick's info
    allboardinfo = getinfo(boardfile,"board")  ##list of dictionary containing the board info
    allrickobjects = []
    allboardobjects = {}
    
    for boardinfo in allboardinfo:  ##creating boards,adding them to a list,and printing their infomation
        newobject = board(boardinfo)
        print newobject
        allboardobjects[newobject.name] = newobject
    print "All Ricks"  ##printing each ricks information
    for rickinfo in allrickinfo:  ##creating the objects and putting them in the list,"allrickobjects"
        newobject = rick(rickinfo)
        print "Time 0:",newobject
        allrickobjects.append(newobject)
    print "-"*75
    
    i = 1  ##represnts time
    alivericks = []
    fallenricks = []
    while i != 101:  ##running the simulation 100 times
        j = 0
        if len(allrickobjects) == len(fallenricks):
            print '-'*75
            print '\nTime %s: Simulation ended\n' %(i)
            break        
        if (i != 0) and i%10 == 0:
            print "-"*75
            print "Time %s: All Free Ricks" %(i)
            for rickobject in allrickobjects:
                if rickobject not in fallenricks:
                    print rickobject        
        for rickobject in allrickobjects:  ##calling hte functions on all the rick objects
            if rickobject in fallenricks:
                continue     
            if rickobject.speedcheck() == True:
                fallenricks.append(rickobject)
                continue
            elif (i == 100) and (rickobject not in fallenricks):
                alivericks.append(rickobject)
            elif rickobject not in fallenricks:
                rickobject.move(allboardobjects)  
                rickobject.obstaclecheck(allboardobjects,i)  
                rickobject.edgecheck(allboardobjects,i)
                rickobject.rickcheck(allrickobjects[j],i)
                rickobject.speedcheck()
            j += 1
        if i == 100:
            print '-'*75
            print 'Time 100: Simulation ended\n'        
        i += 1
    if len(alivericks) == len(allrickobjects):
        print 'The following Ricks are alive:'
        for rick in alivericks:
            print rick
        print "\nNo Ricks were caught by Transdimensional Council of Ricks"
        print "-"*75
    else:
        print 'The following Ricks are alive:'
        for rick in alivericks:
            print rick        
        print '\nThe following Ricks were caught by Transdimensional Council of Ricks:'
        for rick in fallenricks:
            print 'Rick of',rick.name