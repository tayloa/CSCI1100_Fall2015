'''Classes

Dictionary = Structured Data
'''
class Point2d(object):
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0
        
    def length(self):
        return (self.x**2 + self.y**2)**(0.5)
    def __str__(self):
        return "(%d, %d)" %(self.x, self.y)
    def distance(self, other):
        d = (self.x-other.x)**2 +(self.y-other.y)**2
        d = d**(0.5)
        return d
    def __add__(self, other):
        new = Point2d(self.x, self.y)
        new.x += other.x
        new.y += other.y
        return new

if __name__ == "__main__":
    pt1 = Point2d(10,20)
    pt2 = Point2d(30,40)
    print pt1.x, pt1.y
    print pt2.x, pt2.y
    
    print "Length of pt is:", pt1.length()