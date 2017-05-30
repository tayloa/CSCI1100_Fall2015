## Process results for Germany
def stats(country,wins,losses,draws,goals_for,goals_against):
     print country
     print'Wins:',wins,'Lose:',losses,'Draws:',draws
     print'Total number of points:',wins* 3+draws,'Goal advantage:',goals_for - goals_against
     return " "



print stats("Germany",2,1,0,7,2)
print stats("USA",1,1,1,4,4)
print stats("Argentina",3,0,0,6,3)
print stats("England",0,2,1,4,2)