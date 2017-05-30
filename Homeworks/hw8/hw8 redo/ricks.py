import math
class rick(object):
    def __init__(self,rick):  ##initialization
        self.name = rick['name']
        self.x = rick['x,y'][0]
        self.y = rick['x,y'][1]
        self.x0 = rick['x,y'][0]
        self.y0 = rick['x,y'][1]
        self.length = rick['length']
        self.dx = rick['dx,dy'][0]
        self.dy = rick['dx,dy'][1]
        self.currentboard = rick['name']
    def __str__(self):  ##string representation of the object
        return "Rick of %s is in %s board at (%s,%s) with speed (%s,%s)" %(self.name,self.currentboard,self.x,self.y,self.dx,self.dy)
    def move(self,board):  ##moving rick
        for universe in board: ##universe is a key while board is a dictionary
            if self.currentboard == universe:  ##matching up Rick's current location and the board object so information is correct
                self.x += int(self.dx/board[universe].gravity)  ##moving rick by his given speed affected by the gravity of the universe
                self.y += int(self.dy/board[universe].gravity)
    def obstaclecheck(self,board,i):  ##checking to see if Rick hits an obstacle on a board
        for universe in board: ##universe is a key while board is a dictionary
            if self.currentboard == universe:
                for coordinates in board[universe].obstacles:
                    if (coordinates[0] in range(self.x,(self.x+self.length))) and (coordinates[1] in range(self.y,(self.y+self.length))):
                        self.dx = -(self.dx/2)
                        self.dy = -self.dy
                        print "\nTime %s: Rick of %s crashed into object at (%s,%s) in %s board\n   New speed is (%s,%s)" %(i,self.name,coordinates[0],coordinates[1],self.currentboard, \
                        self.dx,self.dy)
    def edgecheck(self,board,i):  ##checking to see if rick runs off the edge of the board,if so he is teleported to a new board
        for universe in board:
            if self.currentboard == universe:
                if (self.x <= 0) or (self.x,self.y) == (0,0): ##left exit
                    print "\nTime %s: Rick of %s moved from %s board to %s board" %(i,self.name,self.currentboard,board[universe].left)
                    print "      Past location: Rick of %s is in %s board at (%s,%s) with speed (%s,%s)" %(self.name,self.currentboard,self.x,self.y,self.dx,self.dy)
                    self.currentboard= board[universe].left
                    self.x = board[self.currentboard].portal[0]
                    self.y = board[self.currentboard].portal[1]
                    print "      Current location: Rick of %s is in %s board at (%s,%s) with speed (%s,%s)" %(self.name,self.currentboard,self.x,self.y,self.dx,self.dy)
                elif (self.x +self.length >=1000):  ##right exit
                    print "\nTime %s: Rick of %s moved from %s board to %s board" %(i,self.name,self.currentboard,board[universe].right)
                    print "      Past location: Rick of %s is in %s board at (%s,%s) with speed (%s,%s)" %(self.name,self.currentboard,self.x,self.y,self.dx,self.dy)
                    self.currentboard= board[universe].right
                    self.x = board[self.currentboard].portal[0]
                    self.y = board[self.currentboard].portal[1] 
                    print "      Current location: Rick of %s is in %s board at (%s,%s) with speed (%s,%s)" %(self.name,self.currentboard,self.x,self.y,self.dx,self.dy)
                elif (self.y <= 0) or (self.x,self.y) == (0,0): ##up exit
                    print "\nTime %s: Rick of %s moved from %s board to %s board" %(i,self.name,self.currentboard,board[universe].up)
                    print "      Past location: Rick of %s is in %s board at (%s,%s) with speed (%s,%s)" %(self.name,self.currentboard,self.x,self.y,self.dx,self.dy)
                    self.currentboard= board[universe].up
                    self.x = board[self.currentboard].portal[0]
                    self.y = board[self.currentboard].portal[1]   
                    print "      Current location: Rick of %s is in %s board at (%s,%s) with speed (%s,%s)" %(self.name,self.currentboard,self.x,self.y,self.dx,self.dy)
                elif (self.y +self.length >= 1000): ##down exit
                    print "\nTime %s: Rick of %s moved from %s board to %s board" %(i,self.name,self.currentboard,board[universe].down)
                    print "      Past location: Rick of %s is in %s board at (%s,%s) with speed (%s,%s)" %(self.name,self.currentboard,self.x,self.y,self.dx,self.dy)
                    self.currentboard= board[universe].down
                    self.x = board[self.currentboard].portal[0]
                    self.y = board[self.currentboard].portal[1]   
                    print "      Current location: Rick of %s is in %s board at (%s,%s) with speed (%s,%s)" %(self.name,self.currentboard,self.x,self.y,self.dx,self.dy)
    def rickcheck(self,other,i):  ##checks to see if ricks are on the same board,if they are, it changes them to the portal locations on their original boards
        if self.currentboard == other.currentboard and (self.name != other.name):
            if (self.x in range(other.x,other.x+other.length)) or (self.y in range(other.y,other.y+other.length)) \
               or (other.x in range(self.x,self.x+self.length)) or (other.y in range(self.y,self.y+self.length)):
                print '\nTime %s: Rick of %s and Rick of %s have collided in %s board.' %(i,self.name,other.name,self.currentboard)
                self.currentboard = self.name
                self.x = self.x0
                self.y = self.y0
                self.dx = int(self.dx)/2
                self.dy = int(self.dy)/2
                print '   Rick of %s is in %s board at (%s,%s) with speed (%s,%s)' %(self.name,self.currentboard,self.x,self.y,self.dx,self.dy)
                other.currentboard = other.name
                other.x = other.x0
                other.y = other.y0
                other.dx = other.dx/2
                other.dy = other.dy/2             
                print '   Rick of %s is in %s board at (%s,%s) with speed (%s,%s)' %(other.name,other.currentboard,other.x,other.y,other.dx,other.dy)
    def speedcheck(self):
        if math.sqrt(self.dx**2+self.dy**2) < 2*self.length:
            return True
        else:
            return False
