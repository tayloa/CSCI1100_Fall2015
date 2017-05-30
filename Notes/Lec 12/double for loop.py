import math



#PRINTING A MULTIPLICATION TABLE WITH A DOUBLE FOUR LOOP
#digits = range(10)
#for i in digits:
    #for j in digits:
        #print "%d x %d = %d " %(i,j,i*j)

def find_distance(p1,p2): #distance formula for problem below (functions before main code!)
    x1,y1 = p1
    x2,y2 = p2
    distance = math.sqrt( (y2-y1)**2 + (x2-x1)**2 )
    return distance



#(x,y)        
points = [ (1,5), (13.5, 9), (10, 5), (8, 2), (16,3) ]

#Find the min distance b/w each point, those points are closest together

#distance = []  #for storing the distances
min_distance = 5000
closest_points = []
for p in points:
    for q in points:
        if p != q:              #as long as theyre not the same,calculate the distance
            dist = find_distance(p,q)
            if dist < min_distance:
                min_distance = dist
                closest_points = (p,q)
        #print "%s -> %f" % ((p,q), dist)
        
print "Minimum distance is:%.2f between poinrs %s%" %(min_distances,closest_points)