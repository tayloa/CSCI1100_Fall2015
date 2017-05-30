'''
Start to the Date class for Lab 9.  This code will not run in Python
until three methods are added:
    __init__,
    __str__
    same_day_in_year
'''

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',\
                    'September', 'October', 'November', 'December' ]

class Date(object):      
    def __init__(self,y=1900,m=1,d=1):
        self.d = d    ##you must define the objects variables
        self.m = m
        self.y = y
    def __str__(self):
        day = str(self.d)
        day1 = day.rjust(2,'0')
        month = str(self.m)
        month1 = month.rjust(2,'0')            
        return "%s/%s/%s" %(self.y,month1,day1)            
    def same_day_in_year(self,other):
        if self.y == other.y:
            if self.d == other.d:   ##if day of year1 = day of year2
                return True
            else:
                return False
        else:  
            return False
    def is_leap_year(self):
        if self.y%4 == 0:
            if self.y%100 == 0 and self.y%400 == 0:
                return True
            else:
                return False
        else:
            return False
    def __lt__(self, other):
        if self.y < other.y:
            return True
        if self.y == other.y:
            if self.m < other.m:
                return True
            else:
                return False
            if self.m == other.m:
                if self.d < other.d:
                    return True
                else:
                    return False
                
        
        
        
        
if __name__ == "__main__":
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1996, 4, 13)
    d4 = Date(1998, 4, 11)  
    print "d1: " + str(d1)
    print "d2: " + str(d2)
    print "d3: " + str(d3)
    print "d1.same_day_in_year(d2)", d1.same_day_in_year(d2) 
    print "d2.same_day_in_year(d3)", d2.same_day_in_year(d3) 
    print "d1.is_leap_year()", d1.is_leap_year()
    print "d2.is_leap_year()", d2.is_leap_year()
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1998, 5, 13)
    d4 = Date(1998, 4, 11)
    
    print "d1 < d2",d1<d2
    print "d2 < d3",d2<d3
    print "d3 < d4",d3<d4