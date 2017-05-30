from Date import *

##how to use month names and compare 
def birthday(filename):
    b = open(filename)
    line = b.read()
    line = line.strip().split()
    return line
if __name__ == '__main__':
    b = birthday('birthdays.txt')
    birthdays = []
    months = []
    i = 0
    while i < len(b):
        birthday = Date(int(b[i]),int(b[i+1]),int(b[i+2]))
        birthdays.append(birthday)
        months.append(b[i+1])
        i += 3
    months.sort()
    month_count = []
    for i in months:
        count = months.count(i),str(i)    #count consists of the month(number) and number of birthdays in that month
        month_count.append(count)
    month_count = list(set(month_count))
    month_count.sort(reverse=True)
    print month_count
    
    earliestbirthday = birthdays[0]    #finding earliest and latest birthday
    latestbirthday = birthdays[0]
    i = 1
    while i < len(birthdays):
        if (earliestbirthday < birthdays[i]) == True:      
            earlistbirthday = birthdays[i]
        if (latestbirthday < birthdays[i]) == True:
            latestbirthday = birthdays[i]
        i += 1
    print "earliest birthday:",earliestbirthday
    print "latest birthday:",latestbirthday
    highcount = int(month_count[0][1])
    print "Month with most birthdays:",month_names[highcount]