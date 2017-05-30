import lab06_util
import math

#Functions
def ok_to_add(row,column,number,bd):    
    r = bd[row]
    if number in r == True:
        return False
    for r in range(9):
        if bd[r][column] == number:
            return False
    rindex = math.trunc(row/3)
    cindex = math.trunc(column/3)
    rowshift = 3*rindex
    cshift = 3*cindex
    for r in range(3):
        for c in range(3):
            if bd[r+rowshift][c+cshift] == number:
                return False
    return True

def verify_board(bd):
    for r in range(9):
        for c in range(9):
            if bd[r][c] == "."and (ok_to_add(r,c,bd[r][c],bd)) == False:
                return False
    return True



#Getting the board
bd = open("easy.txt")
bd = bd.read()
bd = bd.split("\n")
l =[]
for i in bd:
    l.append(i.split(" "))
l.pop()
bd = l

z = verify_board(bd)   


#Printing the board
while z == False:
    i = 0
    print "-"*25
    while i < 9:
        for j in range(9):
            if j == 0:
                print "|",
            row = bd[i][j]
            print row,
            j += 1                  
            if (j%3) == 0:
                print "|",
        if ((i+1)%3) == 0:
            print
            print "-"*25, 
        print
        i += 1
    rownum = int(raw_input("Enter a row number => "))-1
    columnnum = int(raw_input("Enter a column number => "))-1
    number = raw_input("Which number will be entered => ")
    y = ok_to_add(rownum,columnnum,number,bd) 
    x = True
    if bd[rownum][columnnum] != ".":
        x = False
    if y == True and x == True:
        bd[rownum][columnnum] = number
        z = verify_board(bd)
        print "good number"
    else:
        print "bad number"


i = 0
print "-"*25
while i < 9:
    for j in range(9):
        if j == 0:
            print "|",
        row = bd[i][j]
        print row,
        j += 1                  
        if (j%3) == 0:
            print "|",
    if ((i+1)%3) == 0:
        print
        print "-"*25, 
    print
    i += 1
print "board solved"