import lab05_util
import math
def print_info(restaurant):
    print restaurant[0],"("+restaurant[5]+")"
    street = restaurants[0][3]
    street = street.split("+")
    address1 = street.pop(0)
    print ' '*7,address1
    print ' '*7,street[0]
    mean = 0
    i = 0
    while i < (len(restaurants[0][6])):
        value1 = restaurants[0][6][i]
        mean += value1
        i += 1
    average = mean/float((len(restaurants[0][6])))
    print "Average Score: %.2f" %(average)

restaurants = lab05_util.read_yelp('yelp.txt')
print_info(restaurants[0])