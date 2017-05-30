f = open("rpi.txt") #opens file
print f
lines = f.read()    #reads file
print lines         #prints text in the file
f.close()           #closes file

#Writing to a new file
fout = open("mylines.txt","w")
fout.write("This is my first file!\n")
fout.write("Hopefully not my last!\n")
fout.close  #always close the file to save the changes

#part 1 exercise
#1
f = open("census_data.txt")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
f.close()
f = open("census_data.txt")
line4 = f.readline()
f.close()

#print line1,"line1"
#print line2,"line2"
#print line3,"line3"
#print line4,"line4"


#FOR loop with lines
y = open("census.txt")
lines = []
for line in y:
    print line
    lines.append(line)
    
print lines

