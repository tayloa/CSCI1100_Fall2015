""" Testing the infinite loop

"""



n = int(raw_input("Enter a positive integer => "))
sum = 0
i = 0


while i != n:
    sum += 1

    #print "**i:%d" %(i,sum)
    
    i +=1
    
print 'Sum is',sum