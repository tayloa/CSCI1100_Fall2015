''' Boolean Practice

'''
import math

def is_intersect(x0,y0,r1,x1,y1,r2):
    dist = math.sqrt( (x0-x1)**2 + (y0-y1)**2 )
    if dist <= r1+r2:
        return True
    else:
        return False
    
def is_bigger(sem1, sem2):
    s1, y1 = sem1
    s2, y2 = sem2
    if y1 < y2:
        return sem2
    elif y2 < y1:
        return sem1
    elif s1 == 'Fall' and s2 == 'Spring':
        return sem1
    elif s2 == 'Fall' and s1 == 'Spring':
        return sem2
    else:
        return s1
    
print is_bigger( ('Fall', 2013), ('Spring', 2014))


'''
abc
acb

bac
bca

cab
cba
'''

def find_ordering(a,b,c):
    if a<= b and b<=c:
        print "a,b,c"
    elif a <= c and c<=b:
        print "a,c,b"
    ##....

def find_ordering2(a,b,c):
    ## a is the smallest value
    if a == min(a,b,c):
        if b<=c:
            print "a,b,c"
        else:
            print "a,c,b"
    elif b == min(a,b,c):
        if a <= c:
            print "a,c,b"
        else:
            print "c,a,b"
    else:
        if a
    ##....