import math

class ricks(object):                 
    def __init__(self,info):
        self.board = info["boardname"]
        self.x0 = int(info["x,y"][0])
        self.y0 = int(info["x,y"][1])
        self.originalpoint =  int(info["x,y"][0]),int(info["x,y"][1])
        self.length =  int(info["length"])
        self.dx = float(info["dy,dx"][0])
        self.dy = float(info["dy,dx"][1])
        self.current = info["boardname"]
    def __str__(self):
        return "Rick of %s is in %s board at (%s,%s) with speed (%s,%s)" %(self.board,self.current,self.x0,self.y0,self.dx,self.dy)
    def move(self,board):    ##moving Rick
        for universe in board:
            if self.current == universe.name:
                self.x0 += int(self.dx/float(universe.grav))
                self.y0 += int(self.dy/float(universe.grav))
        return True,universe.grav
    def collision(self,board):    #takes self and board(list of objects) as inputs and checks for object collisions
        for universe in board:    #looking at the universes(objects)
            if self.current == universe.name:    ##if the universe and current rickboard have the same name,check for collisions
                for obstacle in universe.obstacle:
                    if (obstacle[0] in range(int(self.x0),int(self.x0+self.length))) and (obstacle[1] in range(int(self.y0),int(self.y0+self.length))):    ##collision check
                        collisionobject = obstacle[0],obstacle[1]    ##saving collision coordinates
                        self.dx = 0.5*float(-self.dx)  ##changing Rick's speed and direction
                        self.dy = -self.dy 
                        collisionstatement = "Rick of %s crashed into object at (%s,%s) in %s board. \n   New speed is (%s,%s)" %(self.board,collisionobject[0],collisionobject[1],self.current,self.dx,self.dy)
                        return True,collisionstatement    ##if there is a collision,True and a print statement will be returned
                    else:
                        return False
            else:
                return False
    def edge(self,board):  ##takes self and board(list of objects) as inputs,checks to see if Rick hits an edge
        for universe in board:
            if self.current == universe.name:
                if (self.x0 <= 0) or ((self.x0,self.y0) == (0,0)):    ##if Rick exits the board to the left
                    originalpos = self.x0,self.y0  ##saving final postiion before board change
                    originalboard = self.board    ##saving each specific Rick's original board
                    self.x0 = int(universe.portal[0])  ##changing Rick's postition
                    self.y0 = int(universe.portal[1])
                    self.current = universe.left
                    self.time = 0
                    statement = "Rick of %s moved from %s board to %s board" %(originalboard,originalboard,universe.left)
                    return True,statement
                elif (self.x0 + self.length) >= 1000:    ##right
                    originalpos = self.x0,self.y0
                    originalboard = self.board
                    self.x0 = int(universe.portal[0])
                    self.y0 = int(universe.portal[1])
                    self.current = universe.right
                    self.time = 0
                    statement = "Rick of %s moved from %s board to %s board" %(originalboard,originalboard,universe.right)
                    return True,statement                    
                elif (self.y0 <= 0) or ((self.x0,self.y0) == (0,0)):    ##down
                    originalpos = self.x0,self.y0
                    originalboard = self.board
                    self.x0 = int(universe.portal[0])
                    self.y0 = int(universe.portal[1])
                    self.current = universe.down
                    self.time = 0
                    statement = "Rick of %s moved from %s board to %s board" %(originalboard,originalboard,universe.down)
                    return True,statement                    
                elif (self.y0 + self.length) >= 1000:    ##up
                    originalpos = self.x0,self.y0
                    originalboard = self.board
                    self.x0 = int(universe.portal[0])
                    self.y0 = int(universe.portal[1])                      
                    self.current = universe.up
                    self.time = 0
                    statement = "Rick of %s moved from %s board to %s board" %(originalboard,originalboard,universe.up)
                    return True,statement   
        return False
    def sameboard(self,other):    ##checking for Rick on Rick collisions (sameboard)
        print self.current ,other.current
        if self.current == other.current:
            ##changing current Rick's properties
            self.current = self.board
            self.x0 = self.originalpoint[0]
            self.y0 = self.originalpoint[1]
            ##changing other Rick's properties
            other.current = other.board
            other.x0 = other.originalpoint[0]
            other.y0 = other.originalpoint[1]
            statement = "Rick of %s and Rick of %s have collided in %s" %(self.board,other.board,self.current)
            return True,statement
        else:
            return False
    def speedcheck(self,gravity):    ##checking if Rick is too slow(resulting in capture)
        self.dx = self.dx/gravity
        self.dy = self.dy/gravity
        if (math.sqrt((self.dx**2 + self.dy**2))) <= (2*self.length):
            stoppingspeed = math.sqrt(self.dx**2 + self.dy**2)
            statement = "Rick of %s in %s board location (%s,%s) with speed magnitude %s stops." %(self.board,self.current,self.x0,self.y0,stoppingspeed)
            return True,statement
        else: 
            return False,''