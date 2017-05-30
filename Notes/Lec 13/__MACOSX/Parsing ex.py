#PARSING

if __name__=="__main__":
    
    f = open("film.txt")
    i = 0
    for line in f:
        m = line.strip().split("\t")    #each line is separated by Tab
        i += 1
        if m[0].startswith("Albany"):
            print "%s: Population: %s" %(m[0],m[1])
