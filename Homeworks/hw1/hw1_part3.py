name = raw_input("Please enter a name ==> ") 
print name
count_a = int(raw_input("Count in 1970 => ")) 
print count_a
count_b = int(raw_input("Count in 1980 => "))
print count_b
count_c = int(raw_input("Count in 1990 => "))
print count_c
count_d = int(raw_input("Count in 2000 => "))
print count_d
change_a =100*((float(count_b-count_a))/count_a)
change_b =100*((float(count_c-count_b))/count_b)
change_c =100*((float(count_d-count_c))/count_c)
average = ((change_a + change_b + change_c))/3
print
print "Babies named",name
print "*"*(int(len("Babies named"+name))+1)
print
print "Year / Total / % change from previous decade" 
print "1970 /",count_a
print "1980 /",count_b,"/ %% %.2f" %change_a
print "1990 /",count_c,"/ %% %.2f" %change_b
print "2000 /",count_d,"/ %% %.2f" %change_c
print "Average change: %% %.2f" %average