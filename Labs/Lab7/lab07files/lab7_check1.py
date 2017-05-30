def parse_line(line):
    if line.count("/")<3:
        return None
    else:
        line = line.split("/",3) #split can have a max
        if (line[0].isdigit() == False)  or (line[1].isdigit()==False) or (line[2].isdigit()==False):
            return None
        else:
            line = (int(line[0]),int(line[1]),int(line[2]),line[3])
            return line        

f = open("example.txt")
lines = f.readline()
print parse_line("12/12/12/    Again some spaces\n")
print parse_line("12/32/4 Here is some spaces ")
print parse_line("12/a/412/3/4/Here is some random text, like 5/4=3")
print parse_line("as12/3/4/Here is some random text, like 5/4=3")
