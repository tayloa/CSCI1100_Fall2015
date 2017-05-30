def bpop_new(bpop,fpop):
    bpop_next = int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop)
    return bpop_next
def fpop_new(fpop,bpop):
    fpop_next = int(0.4 * fpop + 0.02 * fpop * bpop)
    return fpop_next
    
bpop = int(raw_input("Number of bunnies ==> "))
fpop = int(raw_input("Number of foxes ==> "))
new_b = int(bpop_new(bpop,fpop))
new_f = int(fpop_new(fpop,bpop))
print fpop
print "Year 1:",bpop,fpop
bpop = bpop_new(new_b,new_f)
fpop = fpop_new(new_f,new_b)
print "Year 2:",new_b,new_f
bpop = bpop_new(new_b,new_f)
fpop = fpop_new(new_f,new_b)
print "Year 3:",bpop,fpop
new_b = bpop_new(bpop,fpop)
new_f = fpop_new(fpop,bpop)
print "Year 4:",new_b,new_f
bpop = bpop_new(new_b,new_f)
fpop = fpop_new(new_f,new_b)
print "Year 5:",bpop,fpop