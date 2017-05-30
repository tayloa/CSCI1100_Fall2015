'''Recurrsion 
'''
def blast(n):
    if n <= 0:  ##basis step
        print  "Blast off!"
        
    else:  ##recursive step
        print n
        blast(n-1)
'''
5
4
3
2
1
Blast off!
'''
def factorial(n):
    if n ==1:
        return 1
    else:
        x = factorial(n-1)
        return x*n
if __name__ == '__main__':
    #blast(5)
    val = int(raw_input("Number => "))
    print "Factorial of %d is %d" %(val,factorial(val))
