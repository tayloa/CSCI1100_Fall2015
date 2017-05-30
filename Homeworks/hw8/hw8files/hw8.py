import math
from Board import *
from Ricks import*
##line 83 out of range
def fileinfo(filename,type_): ##converts text file to dictionary
       ##each board.txt file contains different boards or universes
       fileobject = open(filename)    ##takes user input boardfile
       allinfo = []
       for line in fileobject:  ##for every universe in the boardfile
              info = {}    ##the information for that universe will be stored in its own dictionary
              for i in line:  
                     i = line.replace("\n","").split("|")
              if type_ == "board":
                     info["name"] = i[0]
                     info["gravity"] = i[1]
                     info["portal"] = i[2],i[3]
                     info["right"] = i[4]
                     info["up"] = i[5]
                     info["left"] = i[6]
                     info["down"] = i[7]
                     if len(i) > 7:
                            obs = i[8::]
                            points = []
                            n = 1
                            while n != len(obs)+1:
                                   point = int(obs[n-1]),int(obs[n])
                                   points.append(point)
                                   n +=2
                     info["obstacle"] = points
                     allinfo.append(info)
              if type_ == "rick":  
                     info["boardname"] = i[0]
                     info["x,y"] = i[1],i[2]
                     info["length"] = i[3]
                     info["dy,dx"] = i[4],i[5] 
                     allinfo.append(info)
       return allinfo

if __name__ == "__main__":
       ##user input
       boardname = raw_input("Board file name => ")
       print boardname
       rickname = raw_input("Rick file name => ")
       print rickname
       
       ##calling the function to get board and rick information
       boardinfo = fileinfo(boardname,"board") 
       rickinfo = fileinfo(rickname,"rick")
       
       ##printing the information of all the board's universes information and printing the rick information
       i = 0
       alluniverses = []
       for dictionary in boardinfo:
              alluniverses.append(board(boardinfo[i])) ##now each universe object is in a list
              print board(boardinfo[i]) 
              i += 1
       print 
     
       i = 0
       allricks = []
       print "All Ricks"
       for dictionary in rickinfo:
              allricks.append(ricks(rickinfo[i]))   ##now each rick object is in a list
              print "Time 0:",ricks(rickinfo[i])
              i += 1
       print "-"*70," \n"
       for i in range(-1,101,1):
              caughtricks = []   ##list of captured Ricks after simulation has ended
              if len(allricks) == 0:  ##loop will break if all Ricks are captured
                     break
              else:
                     n = 0
                     for n in range(len(allricks)):    ##moving the ricks and checking speed and collisions
                            movement = allricks[n].move(alluniverses)
                            grav = movement[1]    ##puling out the gravity for use in slowcheck function)
                            slowcheck = allricks[n].speedcheck(grav)
                            collisioncheck = allricks[n].collision(alluniverses)
                            edgecheck = allricks[n].edge(alluniverses)
                            if slowcheck[0] != False:    ##Removing captured Ricks from allricks list
                                   caughtricks.append(allricks[n])
                                   allricks.remove(allricks[n])
                            if len(allricks) > 0:
                                   for j in range(len(allricks)):    ###checking Rick on Rick collisions
                                          if allricks[n] != allricks[j]:     ######OUT OF RANGE HER
                                                 sameboard = allricks[n].sameboard(allricks[j])
                                                 if sameboard != False:
                                                        print "Time",str(i)+":",sameboard[1]
                                                        print allricks[n]," \n",allricks[j]
                                                        print 
                                   else:
                                          continue
                            if collisioncheck != False:    ##printing the collision
                                   print "\nTime",str(i)+":",collisioncheck[1]
                                   print 
                            if edgecheck != False:    ##printing board change 
                                   print "\n","Time",str(i)+":",edgecheck[1]
                                   print "   Past Location:",
                                   print "   Current Location:",allricks[n]
                                   print
                            n +=1
                     if (i > 0) and (i in range(0,100,10)):
                            print "-"*70
                            print "End of time %s: all free Ricks" %(i-1) 
                            for rick in allricks:   ##will print the time and rick's location
                                   if rick == allricks[-1]:
                                          print "Time",str(i-1)+":",rick
                                          print "-"*70
                                   else:
                                          print "Time",str(i-1)+":",rick
                     if i == 100:     ##when the simulation is over,it will show you
                            print "-"*70,"\nTime %s: simulation ended" %(i)
      
       ###Printing the remaining Ricks
       if len(allricks) != 0:    ##printing whatever Ricks are left
              print "The following Ricks are alive"
              for rick in allricks:
                     print "        %s" %(rick)
              print
       if len(caughtricks) == 0:    ##if the length of caughtricks is 0,print this
              print "No Ricks were caught by the Transdimensional Council of Ricks"
              print "-"*70
       else:
              print "The following Ricks were caught by Transdimensional Council of Ricks:"  ##printing caught Ricks
              for rick in caughtricks:
                     print "        %s" %(rick)
              print "-"*70
              
       


       
       