''' 
Read the length of a platform
Put the drunk in the middle of the platform
Print the platform with the man in it

while the drunk is still in the platform:
randomly move the drunk 
print the platform
'''

#import statements
import random

#funtion definitions here
def print_platform(iteration,location, length):
    left = location-1
    right = length - location
    print ("%4d " %iteration) +\
          "-"*left + "X" + "-"*right,
    raw_input("  <enter>  ")
    
    
if __name__ == "__main__":
    
    n = int(raw_input("Enter the length of platform => "))
    
    location = n/2
    iteration = 1
    while location > 0 and location <= n:
        print_platform(iteration,location, n)
        next = random.random()
        if next > 0.5:
            location += 1
        else:
            location -+ 1
        iteration += 1