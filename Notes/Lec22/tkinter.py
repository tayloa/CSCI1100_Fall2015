from Tkinter import * ### (1)import everything from Tkinter


#root = Tk() ### (1)object of type Tk
#root.mainloop() ### (2)
#print "Hello" ### (3)
## ^ Creates an empty window waiting for a command,after window is closed,main loop ends, then 'Hello' is printed

#root = Tk()
#main_frame = Frame(root)
#main_frame.pack()  ##makes interface apart of GUI

#top_frame = Frame(main_frame)  ##creates new frame inside main_frame
#top_frame.pack(side=TOP)

#bottom_frame = Frame(main_frame)  ##creates new frame inside main_frame
#bottom_frame.pack(side=BOTTOM)   

#button = Button(top_frame, text="LEFT")  ##creates button
#button.pack(side=LEFT)  ##side can be adjusted for button location

#button2 = Button(bottom_frame, text="RIGHT")
#button2.pack(side=RIGHT)

##canvas = Canvas(top_frame,height = 200, width = 200) ##creates canvas,takes location,height ,and width 
##canvas.pack()
#root.mainloop()

#print 'Hello'