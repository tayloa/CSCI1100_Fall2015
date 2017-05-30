

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


#CONTINUE        
mylist = range(-10, 11) #range always returns a list!

for item in mylist:
    if item < 0: #continue tells the loop to skip over negatives in the list and keep printing items > 0
        continue 
    print item

i = 0
while i < len(mylist):
    if mylist[i] < 0:
        i += 1
        continue
    print mylist[i]
    i += 1
        