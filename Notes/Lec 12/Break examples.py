

#BREAK
#sum = 0
#while True:
    #x = int(raw_input("Enter an integerto add (0 to stop)"))
    #if x == 0:
        #break   #Tells python to stop immediately and go outsied the loop
    #sum += x
    
#print sum

#for i in range(10):
    #print i
    #if i == 5: #when i == 5, stop the funtion and go outside of it
        #break
        
mylist = range(-10, 11)

for item in mylist:
    if item < 0:
        continue 
    print item
        