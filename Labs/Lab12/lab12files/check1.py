def add(m,n):
    if n == 0:
        return m
    else:
        #print "m:",m,"n:",n,"add:",add(m,n-1) + 1
        return add(m,n-1) + 1
    
#def mult(m,n):
    #if n == 0:
        #return m-m
    #else:
        #if add(m,n) == m+n:
            #return mult(m,n-1) + m
def mult(m,n):
    if n == 0:
        return n
    else:
        return add(mult(m,n-1),m)  ##each time mult runs,add will run, and the nult in the add will run until n == 0
    
def power(m,n):
    if n == 0:
        return 1
    else:
        return mult(power(m,n-1),m)

print add(5,3)           
print mult(5,4)
print power(5,2)

