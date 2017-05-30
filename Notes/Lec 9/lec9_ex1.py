"""
Get list of Farmer's Markets, each market has the 
following fields:

County	Market Name	Location	
Address Line 1	City	State	Zip	Contact	Phone	
Market Link	Operation Hours	Operation Season	
FMNP	Operating Months	
Latitude	Longitude	EBT/SNAP	
Location Points

"""


def get_markets():
    markets = []
    i = 0
    for line in open('Farmers_Markets.csv'):
        i += 1
        if i == 1:
            continue
        m = line.strip().split(",")
        markets.append(m)
    return markets

#Market is a list of lists
markets = get_markets()
print markets[0]

#Find and print market names/ address in Rensselaer county
county = raw_input("Which county => ")
couty = county.capitalize()
i = 0
cnt = 0
while i < len(markets):
    if markets[i][0] == county:
        print markets[i][1]
        cnt +=1
    i += 1
print "%d markets found in Rensselaer" %(cnt, county)




months = ['jan','feb','march','april','may','jun','july','aug','sep','oct','nov','dec']
agents = ['caulson','fitz','smith','simmons','hunter','mack','morse','skye','triplett','deathlok','koeing','gonzales']

#Capitalize the values in agents
i = 0
while i < len(agents):
    agents[i] = agents[i].capitalize()
    i += 1

#Check if capitalized
print 
print agents

#Find if there are any agents with F in their name
i = 0
cnt = 0
found = False               #Booleans
while i < len(agents):
    if agents[i][0] == 'F':
        found = True
    i += 1
if found:
    print 'Yes'
else:
    print "No"