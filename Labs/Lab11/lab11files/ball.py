from Tkinter import *
from random import *

class Ball(object):
    def __init__(self,x,y,dx,dy,radius,color):
        self.x,self.y =x,y
        self.dx,self.dy = dx,dy
        self.rad = radius
        self.color = color
    def position(self):
        return self.x,self.y
    def move(self):
        self.x += self.dx
        self.y += self.dy
    def bounding_box(self):
        return self.x-self.rad,self.y-self.rad,self.x+self.rad,self.y+self.rad
    def get_color(self):
        return self.color
    def some_inside(self,maxx,maxy):
        if (0< self.x+self.rad < maxx) and (0<self.x-self.rad<maxx) and \
           (0< self.y+self.rad < maxy) and (0<self.y-self.rad<maxy):
            return True
        else:
            return False
    def check_and_reverse(self,maxx,maxy):
        if (self.x - self.rad <= 0) or (self.x+self.rad >= maxx):
            self.dx = -self.dx
        if (self.y - self.rad <= 0) or (self.y+self.rad >= maxy):
            self.dy = -self.dy
    
