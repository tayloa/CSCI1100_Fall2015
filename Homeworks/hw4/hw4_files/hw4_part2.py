import hw4_util

if __name__ ==  "__main__":
    legos = hw4_util.read_legos()
    print "Current legos",legos
    name = raw_input("Type of lego wanted => ")
    print name
    quantity = raw_input("Quantity wanted => ")
    print quantity
    am1 = legos.count("1x1")
    am2 = legos.count("2x1")
    am3 = legos.count("2x2")
    
    
    #Conditions
    #Loops need to remove the amount of each piece from the list
    if name == "1x1":
        if int(quantity) <= am1:
            print "I can use",quantity,"1x1 legos for this"
            i = 1
            while i <= int(quantity):
                del legos[0]
                i += 1
            print "Remaining legos",legos    
        else:
            print "I don't have",quantity,"1x1 legos"
    if name == "2x1":
        if int(quantity) <= am2:
            print "I can use",quantity,"2x1 legos for this"
            i = 1
            while i <= int(quantity):
                del legos[am1]
                i += 1
            print "Remaining legos",legos         
        elif int(quantity)*2 <= am1:
            i = 1
            while i <= int(quantity)*2:
                del legos[0]
                i += 1
            print "Remaining legos",legos        
            print "I can use",int(quantity)*2,"1x1 legos for this"
        else:
            print "I don't have",quantity,"2x1 legos"
    if name == "2x2":
        if int(quantity) <= am3:
            print "I can use",quantity,"2x1 legos for this"
            i = 1
            while i <= int(quantity):
                del legos[am1+am2]
                i += 1
            print "Remaining legos",legos                 
        elif int(quantity)*2 <= am2:
            print "I can use",quantity,"2x1 legos for this"
            i = 1
            while i <= int(quantity)*2:
                del legos[am1]
                i += 1
            print "Remaining legos",legos         
        elif int(quantity)*4 <= am1:
            print "I can use",int(quantity)*4,"1x1 legos for this"
            i = 1
            while i <= int(quantity)*4:
                del legos[0]
                i += 1
            print "Remaining legos",legos         
        else:
            print "I don't have",quantity,"2x2 legos"
    
    
