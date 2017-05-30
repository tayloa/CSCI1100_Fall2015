import json
def find_dictionary(month,lists,stat,sort):    #month = user input,lists = opened file'sdata,stat = key,sort = min or max
    stats = []    #will be a list of lists of stats and years
    if stat == "MNTM":    #when the stat is MNTM(average of mean tempertures) the list format will be [year,stat]
        for dictionary in lists:
            if dictionary["month"] == month:
                for key in dictionary:
                    if key == stat:
                        if (dictionary[key] != -9999) and (dictionary[key] != 0):    #keys with values -9999 or 0 won't be added to the list
                            statslist = [dictionary["year"],float(dictionary[stat])]    #list is made up of year,and stat  
                            stats.append(statslist)
    else:
        for dictionary in lists:
            if dictionary["month"] == month:    #if the key isn't MNTM create the list of lists in [stat,year] format
                for key in dictionary:
                    if key == stat:
                        if (dictionary[key] != -9999) and (dictionary[key] != 0):  #keys with values -9999 or 0 won't be added to the list
                            statslist = [float(dictionary[stat]),dictionary["year"]]    #list is made up of stat and year  
                            stats.append(statslist)  
    if sort == "min":    #if sort keyword = "min", sort the list low to high
        stats.sort()
    elif sort == "max":    #if sort keyword = "max", sort the list high to low
        stats.sort(reverse=True)
    return stats    #returns list of requested stats and years(in list format) [[year,stat],[year,stat]]

def top3years(stats,name):  #takes the previpus function's value as an input along with a name from the list name(data set titles)
    if len(stats) == 0:    #if the stats set is empty,print not enough data
        print name,"Not enough data"
    else:
        stats = stats[:3]   #limit's the list to only look at the first 3 values
        for i in stats:
            if i == stats[0]:
                print name,"%s: %.1f," %(i[1],i[0]), 
            elif i == stats[1]:
                print "%s: %.1f," %(i[1],i[0]),
            elif i == stats[2]:
                print "%s: %.1f" %(i[1],i[0])
                
def average(stats,name):
    temps = [] #creates list of temperatures from each year's requested month
    if stats == "MNTMhightolow":
        for i in stats:
            temps.append(i[0])        #will look at value 0 instead because of how the list is formatted
        average = round((sum(temps)/len(temps)),2)  
    else:
        for i in stats:
            temps.append(i[1])
        average = round((sum(temps)/len(temps)),1)
    print name,average

def histogram(stats):   #takes stats(in a certain range) as input and a name from list
    temps = []
    years = []    #will be a list of years, taken from stats
    for i in stats:
        temps.append(i[1])
        years.append(i[0])
    average = int(sum(temps)/len(temps))  #computes average in range ten years similar to the previous function 
    print str(years[0])+"-"+str(years[-1])+":","*"*average
    
if __name__ == '__main__':
    name = ["Highest max value =>","Lowest min value =>",'Highest days with max >= 90 =>','Highest days with max <= 32 =>','Highest total =>'\
            ,'Lowest total =>','Highest snow depth =>','Lowest snow depth =>','Overall:','First 10 years:','Last 10 years:']    #list of data set titles
    data = json.loads(open("tempdata.json").read())
    month = int(raw_input("Enter a month (1-12) => "))  #User input month
    print month
    print "Temperatures\n","-"*50
    EMXT = top3years(find_dictionary(month,data,"EMXT","max"),name[0]) 
    EMNT = top3years(find_dictionary(month,data,"EMNT","min"),name[1])
    DT90 = top3years(find_dictionary(month,data,"DT90","max"),name[2])
    DX32 = top3years(find_dictionary(month,data,"DX32","max"),name[3])
    print "\nPrecipitation\n","-"*50
    TPCP_HIGH = top3years(find_dictionary(month,data,"TPCP","max"),name[4])
    TPCP_LOW = top3years(find_dictionary(month,data,"TPCP","min"),name[5])
    TSNW_HIGH = top3years(find_dictionary(month,data,"TSNW","max"),name[6])
    TSNW_LOW = top3years(find_dictionary(month,data,"TSNW","min"),name[7])
    print "\nAverage temperatures\n","-"*50
    MNTMlowtohigh = find_dictionary(month,data,"MNTM","min")
    MNTMhightolow = find_dictionary(month,data,"MNTM","max")
    MNTMover = average(MNTMlowtohigh,name[8])
    MNTMfirst10 = average(MNTMlowtohigh[0:10],name[9])
    MNTMlast10 = average(MNTMhightolow[0:10],name[10])
    print 
    yearset1 = histogram(MNTMlowtohigh[0:10])   #so the list created by MNTMlowtohigh is now an input for the histogram
    yearset2 = histogram(MNTMlowtohigh[10:20])
    yearset3 = histogram(MNTMlowtohigh[20:30])
    yearset4 = histogram(MNTMlowtohigh[30:40])
    yearset5 = histogram(MNTMlowtohigh[40:50])
    yearset6 = histogram(MNTMlowtohigh[50:])
    
    
    
    
    
    