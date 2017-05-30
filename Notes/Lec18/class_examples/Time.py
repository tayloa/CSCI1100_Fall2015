''' Class for storing Time(militaty time)
'''

class Time(object):                 ##if you are defining time, you need hours,minutes,seconds
    def __init__(self,hr,mi,ss):    ##self,hour,min,secs
        self.seconds = ss + mi*60 + hr*60*60
    def __convert(hr,mi,ss):
        hr = self.second/3600
        mi = (self.seconds - hr*3600) / 60
        ss = self.seconds = hr*3600 - min*60
        return hr, mi, sec
    def __str__(self):
        hr, mi, ss = self.convert()
        return '%2d:%2d:%2d' \
               %(hr,mi,ss)
    def __add__(self, other):
        total =(self.seconds + other.seconds)
        hr = self.second/3600
        mi = (self.seconds - hr*3600) / 60
        ss = total - hr*3600 - mi*60    
        return Time(hr, mi, ss)
    def __sub__(self, other):
        total =(self.seconds - other.seconds)
        hr = total/3600
        mi = (total - hr*3600) / 60
        ss = total - hr*3600 - mi*60    
        return Time(hr, mi, ss)        
        
        
