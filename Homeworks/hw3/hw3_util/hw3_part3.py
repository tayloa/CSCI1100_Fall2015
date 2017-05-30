backchar = raw_input("Background char => ")
print backchar
forechar = raw_input("Foreground char => ")
print forechar
h = raw_input("Height => ")
print h

if len(backchar) == 1 and len(forechar) == 1 and h.isdigit() == True :
    
    i = 0
    l = 2*int(h) + 2 + len(str(h))
    
    while i < int(h)/2:
        if i == 0:
            line2 = str(i+1)+backchar*(int(h)-i)+forechar*(2)+backchar*(int(h)-i)
        elif i == 2: 
            line2 = str(i+1)+backchar*(int(h)-i)+forechar+backchar*(i*2)+'o'+backchar*(int(h)-i)    
        else:
            line2 = str(i+1)+backchar*(int(h)-i)+forechar+backchar*(i*2)+forechar+backchar*(int(h)-i)
        
        print line2.rjust(l)
        i += 1
    while i < int(h):
        if i == int(h):
            line2 = str(i+1)+backchar*(i+1)+forechar+forechar+backchar*(i+1)
        else:
            line2 = str(i+1)+backchar*(i+1)+forechar+backchar*(2*(int(h))-2*i-2)+forechar+backchar*(i+1)
        print line2.rjust(l)
        i += 1
elif h.isdigit() == False:
    print "Please enter a number for height"
elif len(backchar) != 1:
    print "Please enter one character for background"
elif len(forechar) != 1:
    print "Please enter one character for the foreground"