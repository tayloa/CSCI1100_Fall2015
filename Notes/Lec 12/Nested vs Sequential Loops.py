# Version 1 #nested loop
sum = 0
for i in range(10):
    for j in range(10):
        sum += 1
print sum #100


# Version 2 #nested loop
sum = 0
for i in range(10):
    for j in range(i+1,10):
        sum += 1
print sum #45

# Version 3 #sequential loop
sum = 0
for i in range(10):
    sum += 1
for j in range(10):
    sum += 1
print sum #20