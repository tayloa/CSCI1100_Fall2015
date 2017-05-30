import Points ##this will be for longitute and latitude
from Points import Point2d

class business(object):
    def __init__(self,name,lat, lon, address,url,category,scores):
        self.name = name
        self.loc = Point2d(lon,lat)
        #self.lat = lat
        #self.lon = lon
        self.address = address
        self.url = url
        self.category = category
        self.scores = scores
        ##convert scores into integers
        for i in range(len(scores)):
            scores[i] = int(scores[i])
        self.score = scores
    def avgscore(self):
        if len(self.score) < 3:
            return sum(self.scores)/float(len(self.scores))
        else:
            s = list(self.scores)
            s.sort()
            return (sum(s[1:-1])/float(len(s)-2))
    def __str__(self):
        return "%s\n\t%s\n\tLocation: %s\nAvg Score %1f" %(self.name, self.address,self.loc,self.avgscore())

if __name__ == '__main__':
    f = open('yelp.txt')
    line = f.readline()
    m = line.strip().split('|')
    b = business(m[0],m[1],m[2],m[3],m[4],m[5],m[6:])
    print b

