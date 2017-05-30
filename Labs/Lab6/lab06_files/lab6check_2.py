import math


rownum = int(raw_input("Enter a row number => "))-1
columnnum = int(raw_input("Enter a column number => "))-1
number = raw_input("Which number will be entered => ")




bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

num = [2,5,8]
num2 = [3,6,9]
i = 0
print "-"*25
while i < 9:
    for j in range(0,9,1):
        if j == 0:
            print "|",
        row = bd[i][j]
        print row,
        j += 1                  #Why is a counter needed for j here?
        if (j%3) == 0:
            print "|",
        if j == 0:
            print "|"
    if ((i+1)%3) == 0:
        print
        print "-"*25, 
    print
    i += 1

def ok_to_add(row,column,number):
    bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
           [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
           [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
           [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
           [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
           [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
           [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
           [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
           [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]    
    r = bd[int(row)]
    if number in r == True:
        return False
    for r in range(9):
        if bd[r][column] == number:
            return False
    rindex = math.trunc(int(row)/3)
    cindex = math.trunc(int(column)/3)
    rowshift = 3*rindex
    cshift = 3*cindex
    for r in range(3):
        for c in range(3):
            if bd[r+rowshift][c+cshift] == number:
                return False
    return True




y = ok_to_add(rownum,columnnum,number)

a = True
if bd[int(rownum)][int(columnnum)] != ".":
    a = False
if a == True and y == True:
    print "Success"
    
else:
    print "This number cannot be added."