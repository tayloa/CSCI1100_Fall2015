import hw4_util
import math

#Input
c1 = raw_input("First country => ")
print c1
c2 = raw_input("Second country => ")
print c2


#Country Data
c1data = hw4_util.read_flu(c1)
c2data = hw4_util.read_flu(c2)
a = True
if (len(c1data)) == 0:
    print "I could not find country",c1    
if (len(c2data)) == 0:
    print "I could not find country",c2
if (len(c1data)) == 0 or (len(c2data)) == 0:
    a = False

    
if a == True:    
    #Mean
    i = 0
    c1total = 0
    while i < len(c1data):
        c1total += c1data[i]
        i += 1
    i = 0
    c2total = 0
    while i < len(c2data):
        c2total += c2data[i]
        i += 1
        
    #Cutoff
    c1mean = c1total /len(c1data)
    c2mean = c2total /len(c2data)
    c1cutoff = (c1mean + max(c1data)) /2
    c2cutoff = (c2mean + max(c2data)) /2
    
    #Conversion to + and -
    #Use for loops / range to find values in data below cutoff
    country1 = ""
    country2 = ""
    i = 0
    for n in c1data:
        if n < c1cutoff:
            country1 = country1+"-"
        elif n >= c1cutoff:
            country1 = country1+"+"
        i += 1
    for n in c2data:
        if n < c2cutoff:
            country2 = country2+"-"
        elif n >= c2cutoff:
            country2 = country2+"+"
        i += 1    
    
    #Final Results
    print "".ljust(12)+"1".ljust(4)+"2".ljust(4)+"3".ljust(4)+"4".ljust(4)+"5".ljust(4)+"6".ljust(4)+"7".ljust(4) \
          +"8".ljust(4)+"9".ljust(4)+"10".ljust(4)+"11".ljust(4)+"12".ljust(4)
    print c1.ljust(12)+country1
    print c2.ljust(12)+country2

