import lab05_util
import webbrowser
def print_info(restaurant):
    print restaurant[0],"("+restaurant[5]+")"
    street = restaurants[id_][3]
    street = street.split("+")
    address1 = street.pop(0)
    print ' '*7,address1
    print ' '*7,street[0]
    mean = 0
    i = 0
    while i < (len(restaurants[id_][6])):
        value1 = restaurants[id_][6][i]
        mean += value1
        i += 1
        if len(restaurants[id_][6]) > 3:
                    mean - min(restaurants[id_][6]) - max(restaurants[id_][6])        
    average = mean/float((len(restaurants[id_][6])))
    rev_num = len(restaurants[id_][6])
    print "Average Score: %.2f" %(average)
    print 
    print "Score     Output"
    print "_"*71
    if 0 < average < 2:
        print "%.2f" %(average),"      This restaurant is rated bad,based on",rev_num,"reviews." 
    elif 2 < average < 3:
        print "%.2f" %(average),"     This restaurant is rated average,based on",rev_num,"reviews." 
    elif 3 < average < 4:
        print "%.2f" %(average),"     This restaurant is rated above average,based on",rev_num,"reviews." 
    elif 4 < average < 5:
        print "%.2f" %(average),"     This restaurant is rated very good,based on",rev_num,"reviews." 
    
    
restaurants = lab05_util.read_yelp('yelp.txt')
print restaurants[0]
id_ = int(raw_input("Enter Restaurant ID => "))
if id_ < 1 or id_ > 155:
    print "Warning! Invalid input."
else:
    restaurant_info = print_info(restaurants[id_])
print
print "What would you like to do next?\n1. Visit the homepage\n2. Show on Google Maps\n3. Show directions to this restaurant"
choice = int(raw_input("Your choice (1-3)? ==> "))
RPI = '110th 8th Street, Troy NY'
if choice == 1:
    webbrowser.open(restaurants[id_][4])
elif choice == 2:
    webbrowser.open('http://www.google.com/maps/place/'+restaurants[id_][3])
elif choice == 3:
    webbrowser.open('http://www.google.com/maps/dir/'+RPI+'/'+restaurants[id_][3])
    