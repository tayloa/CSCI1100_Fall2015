"""Author: Aaron Taylor,tayloa5@rpi.edu

   Purpose: This program computes the changing Bunny and Fox
   population over a cretain set of years
"""
def next_pop(bpop, fpop):
    bpop_next = int(max(0,round((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop)))
    fpop_next = int(max(0,round(0.4 * fpop + 0.02 * fpop * bpop)))
    return (bpop_next, fpop_next)

def check_convergence(bpop, fpop):
    i = 0
    a = False
    while i < 100:
        i += 1
        population = next_pop(bpop,fpop)
        if population[0] == 0 or population[1] == 0:
            a = True
            break   
        if bpop == population[0] and fpop == population[1]:
            a = True
            break
        bpop = population[0]
        fpop = population[1]        
    bpop = population[0]
    fpop = population[1]
    
    return (bpop,fpop,i,a)

if __name__ == '__main__':

    bpop =int(raw_input("Please enter the starting bunny population ==> "))
    print bpop
    fpop =int(raw_input("Please enter the starting fox population ==> "))
    print fpop
    newpop = check_convergence(bpop,fpop)
    print "(Bunny, Fox):","Start","("+str(bpop)+",",str(fpop)+")","End:","("+str(newpop[0])+",",str(newpop[1])+")"+",","Converged:",newpop[3],"in",newpop[2],"generations"