def closest1(listf):
    if len(listf)<2:
        return "(None,None)"
    elif len(listf) == 2:
        return listf[0],listf[1]
    else:
        differences = []
        i = 0
        for i in range(len(listf)):
            for j in range(len(listf)):
                difference = abs(listf[i] - listf[j]) 
                point = difference,listf[i],listf[j]
                if difference != 0:
                    differences.append(point)
    lowest = min(differences)  
    return lowest[1],lowest[2]

def closest2(listf):
    listf.sort()
    lowest = 2000
    i = 1
    for i in range(len(listf)-1):
        difference = abs(listf[i]-listf[i+1])
        if difference < lowest:
            lowest = difference
            lowestdifference = listf[i],listf[i+1]
    return lowestdifference
            
L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ] 
t1 = [1,2]
t2 = [1,5,2,2,7]
t3 = [7,2,5,3]
t4 = [30,15,47,38,63,57]
print L1
print closest1(L1) 
print closest2(L1)," \n"
print t1
print closest1(t1)
print closest2(t1)," \n"
print t2
print closest1(t2) 
print closest2(t2)," \n"
print t3
print closest1(t3)
print closest2(t3)," \n"
print t4
print closest1(t4)
print closest2(t4)," \n"

    