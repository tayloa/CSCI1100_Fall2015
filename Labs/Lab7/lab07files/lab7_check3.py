def parse_line(line):
    if line.count("/")<3:
        return None
    else:
        line = line.split("/",3) #split can have a max
        if (line[0].isdigit() == False)  or (line[1].isdigit()==False) or (line[2].isdigit()==False):
            return None
        else:
            line = (int(line[0]),int(line[1]),int(line[2]),line[3])
            return line        
    
 
def get_line(fname,parno,lineno):
    files = open(fname+".txt")
    whitespace = 1
    lno = -1
    skip = False
    for i in files:                             #checking each line in the file
        if i.strip() == '' and skip == False:   #if the line is a blank space,increment whitespace by 1
            whitespace += 1
            skip = True             
        elif i.strip() == '' and skip == True:  #if there is a blank space
            continue                            #continue says "go back to the start of the loop",so keep incrementing whitespace
        else:
            skip = False                        #if the line ("i") is not a blankspace, skip = False, so stop the loop
        if whitespace == parno:                 #all ifs always get evaluated, elifs get evaluated if the above is false
            lno += 1                            #when we have found the paragraph number,start looking at lines
            if lno == lineno:                 
                return i
            
filename = raw_input("Please enter file name => ")
parnum = int(raw_input("Please enter paragraph number => "))
linenum = int(raw_input("Please enter line number => "))

getline = get_line(filename,parnum,linenum)
python = open("program.py",'w')

while getline != "0/0/0/END\n":    #while loop doesn't depend on i here,it depends on this condition,so no incrementing needed  
    x = parse_line(getline)
    filename = str(x[0])     #at this point,you are changing the input for the next time it loops
    parnum = x[1]
    linenum = x[2]
    string = x[3] 
    python.write(string)            #writing it to the python file
    getline = get_line(filename,parnum,linenum)     #returns line
python.close()
    

    

