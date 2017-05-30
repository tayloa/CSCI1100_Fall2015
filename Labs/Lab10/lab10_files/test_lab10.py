'''
This is code to test your functions in this lab.  It is driven by a
Python module called nose, which has been imported here.  

We assume your program is called lab10.py, and we import all the
function in your program here. Make sure any other code in lab10.py
is under the 

     if __name__ == "__main__":

line.

Nose testing module is actually relative simple.

To understand it, start by looking at the main code at the bottom of
the file.  The function call nose.runmodule() causes nose to scan back
up through the preceeding code and find all functions that start with
test_.  Nose runs these functions in turn.  Each function must end
with an 'assert' statement followed by a boolean condition.  If the
boolean condition evaluate to True, nose does not say anything.  If a
condition evaluates to False, the "assert" is said to "fail".  Nose
detects these failures and tells you about them.  To see the behavior
of Nose, change some of the assert statements (for example, try == 3 for 
any test) and see what happens.

'''

import nose
import random
import time
from lab10_check1 import *

def test_closest1():
    assert closest1(L1) == (4.3, 5.4)

def test_closest2():
    assert closest2(L1) == (4.3, 5.4)


if __name__ == "__main__":
    #nose.runmodule()
    L2 = []
    for i in range(3000):
        rand = random.uniform(0.0,3000)
        L2.append(rand)
   
    start1 = time.time()
    closest1(L2)
    end1 = time.time()
    print end1-start1,"seconds (run time)"
    
    start2 = time.time()
    closest2(L2)
    end2 = time.time()
    print end2-start2,"seconds (run time)"
    
      