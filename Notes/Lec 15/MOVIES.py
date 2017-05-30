#For each actor,find how many movies they were in

def parse_line(line):
    m = line.strip().split("|")
    actor = m[0].strip()
    movie = m[1].strip()
    year = int(m[2])
    return actor,movie,year
def find_actor(nummovies,a):
    for i in range(len(nummovies)):
        if nummovies[i][0] == actor:
            return i
nummovies = []
f = open("hanks.txt")
for line in f:
    a,m,y = parse_line(line)
    print a
    print num
    idx = find-actor(nummovies, a)
    nummovies[idx][1] += 1
name = raw_inpu(nummovies, name)
print "%s starred in %d movies)" %(name, nummovies[idx][1])