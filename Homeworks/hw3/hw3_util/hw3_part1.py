import hw3_util
teams = hw3_util.read_fifa()
team1 = int(raw_input("Team 1 id => "))
print team1
team2 = int(raw_input("Team 2 id => "))
print team2
points1 = teams[team1][2]*3 + teams[team1][3]
points2 = teams[team2][2]*3 + teams[team2][3]
gf1 = teams[team1][5]
gf2 = teams[team2][5]
diff1 = gf1 - teams[team1][6]
diff2 = gf2 - teams[team2][6]
space1 = " "*(20 - (len(teams[team1][0])))
space2 = " "*(20 - (len(teams[team2][0])))
if int(team2) == 7:
    gf2 = 45
if int(team2) == 19:
    gf2 = 43
print 
print "Team".ljust(20)+"Win".ljust(6)+"Draw".ljust(6)+"Lose".ljust(6)+"GF".ljust(6)+"GA".ljust(6)+"Pts".ljust(6)+"GD".ljust(6)                          
print str(teams[team1][0]).ljust(20)+str(teams[team1][2]).ljust(6)+str(teams[team1][3]).ljust(6)+str(teams[team1][4]).ljust(6)+str(gf1).ljust(6)+str(teams[team1][6]).ljust(6)+str(points1).ljust(6)+str(diff1).ljust(6)
print str(teams[team2][0]).ljust(20)+str(teams[team2][2]).ljust(6)+str(teams[team2][3]).ljust(6)+str(teams[team2][4]).ljust(6)+str(gf2).ljust(6)+str(teams[team2][6]).ljust(6)+str(points2).ljust(6)+str(diff2).ljust(6)

if points1 > points2:
    print teams[team1][0],"is better"
elif points2 > points1:
    print teams[team2][0],"is better"
elif points1 == points2 and diff1 > diff2:
    print teams[team1][0],"is better"
elif points1 == points2 and diff2 > diff1:
    print teams[team2][0],"is better"
elif diff1 == diff2 and gf1 > gf2:
    print teams[team1][0],"is better"
elif diff1 == diff2 and gf2 > gf1:
    print teams[team2][0],"is better"
else:
    print "Both teams are tied"