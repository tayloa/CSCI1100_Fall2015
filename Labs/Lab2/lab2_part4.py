fname = raw_input("Please enter your first name:")
lname = raw_input("Please enter your last name:")+"!"
greet = "Hello,"
longest = (max(len(fname),len(lname),len(greet)))
top = "*"*(longest+6)
space = (longest-len(greet))
print space
space_f =(longest-len(fname))
print space_f
space_l =(longest-len(lname))
print space_l
print top
print "**"+" ",greet+" "*space+"**"
print "**"+" ",fname+" "*space_f+"**"
print "**"+" ",lname+" "*space_l+"**"
print top
 