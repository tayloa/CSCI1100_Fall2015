from ball import *
from random import *
from Tkinter import *
if __name__ == '__main__': 
    root = Tk()   
    root.title("Tkinter: Lab 11")       
    colorList = ["blue", "red", "green", "yellow", "magenta", "orange"]
    color = choice(colorList)
    x = randint(10,390)
    y = randint(10,390)
    dx = randint(-8,8)
    dy = randint(-8,8)
    radius = randint(5,10)
    balls = []
    for i in range(10):
        balls.append(Ball(x,y,dx,dy,radius,color,root))
    for ball in balls:
        ball.draw_ball()
        
        