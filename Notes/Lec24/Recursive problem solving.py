"""
Recursive function:
1.Stopping condition
  n = 0?
  n = 1?
  n = 2?
2.What is the recursive part of the function?
 
  fact(n) = fact(n-1) * n
  fib(n) = fib(n-1) + fib(n-2)
  merge_sort(L):
     merge_sort(left half of L)
     merge_sort(right half of L)
     merge them both in a sorted order, and return
     
"""
"""
Problem: Find the value that occurs the most in the list

Refine requirements:
1.How do I break ties or return all value that occur most frequently?
2.What should I return for empty list?
3.What are the diferent values and is there a limited number of them?
  Expected number of distinct values in the list: m
  Is m constant?
  Do we expect m to be as big as n (#items in list)
4.What are the values? Any floats?
  Which values are considerded the same?
  
___________________
Version 1.
 A list of integers, m is not fixed
 I am looking for the value that occurs the most
 Return None if list is empty
 
 List solution: O(n logn)
  Sort a copy of the list, and keep track of # times an item was 
  seen and keep track of the most frequent item
  Conmplexity: sort list = O(n),sort copy of list = O(n logn),going through list and
 Set solution: O(n * m)
  Find the set(L): O(n) => m distinct values
  For each distinct value(set(L)):
    count how many times value occurs in list L
    and keep track of the max
 
 Dictionary solution: O(n+m)
  Use a dictionary D,where key = value in list,
  and a key's value = count of that values
  For each item in list: O(n)
   update counts in D
  For each key in the dictionary: O(m)
   check the count
   and keep track of the max
"""

def mode_list(L):
    L1  = l[:]
    L1.sort()
    lastval = L1[0]
    lastcount = 1
    maxval = 0
    maxcount = 0
    for i in range(1,len(L1)):
        val = L1[i]
        if val == lastval:
            lastcount += 1
        else:
            if lastcount > maxcount:
                maxcount = lastcount
                maxval = lastval
            lastval = val
            lastcount = 1
        if lastcount > maxcount:
            maxcount = lastcount
            maxval = lastval
        return maxval
     
def mode_set(L):
    L1  = l[:]
    L1 = set(L1)

def mode_dictionary(L):
    D = {}
    for item in L:
        if item not in D:
            D[item] = 1
        else:
            D[item] += 1
    maxval = None
    maxcount = 0
    for key in D:
        cnt = D[key]
        if cnt > maxcount:
            
if __name__ == "__main__":
    vals = [1,2,3,3,3,5,6,7,23,55,222,56,56,7,33,5,5,6,6,6,6,6,]