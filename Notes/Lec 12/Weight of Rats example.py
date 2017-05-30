#WEIGHTS OF 2 RATS
l1 = [3.7,4.1,4.9,5.4,6.0]
l2 = [4.5,4.7,5.1,5.3,5.9]

i = 0
while i < len(l1) and i < len(l2):
    if l1[i] > l2[i]:
        print "On day %d, Rat 1 (%.1f) is heavier than rat 2 (%.1f)" % (i,l1[i],l2[i])
        break           #WHEN WEIGHT 1 IS GREATER THAN WEIGHT 2, GO OUTSIDE THE LOOP AND PRINT "Outside the loop"
    i += 1
print "\nOUTSIDE THE LOOP"