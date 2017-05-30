'''
Find index of value if value is in list
of if it is not,return the index of where value would be inserted to 
keep the list sorted
'''

def search(L,val):
    for i in range(len(L)):
        if L[i] >= val:
            return i
    return len(L)

if __name__ == '__main__':
    
    print search([2,4,8],10)