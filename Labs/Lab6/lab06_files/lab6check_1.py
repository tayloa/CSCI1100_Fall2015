from random import randint

i = 0
print "-"*41
for i in range(-1,8):
    if i == 2 or i == 5 or i == 8:
        print "-"*41
    i += 1
    j = 0
    for j in range(0,9):
        print str(i)+","+str(j),
        if j == 2 or j == 5 or j == 8:
            print "|",
            if j == 8:
                print "\n",
    j += 1
print "-"*41
