def st1(L):
    L1 = list(L)
    L1.sort()
    min1,min2 = L1[0],L1[1]
    i1 = L.index(min1)
    i2 = L.index(min2, i1+1)
    return i1,i2
def st2(L):
    if L[0] < L[1]:
        i1,i2 = 0,1
    else:
        i1,i2 = 1,0
    for i in range[2,len(L)]:
        if L[i] < L[i1]:
            i1, i2 = i, i1
        elif L[i] < L[i2]:
            i2 = i
    return i1,i2
            
if __name__ == "__main__":
    print "Test Cases"