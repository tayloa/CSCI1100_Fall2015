'''
Time Complexity

Constant Time,O(1)
    does not depend on the size of the data
    (list/dictionary/set)
Linear Time, 0(n)
    depends linearly on the data, twice the size
    of the data,the program wil take twice the length
    
    value in list
    
Quadratic Time, 0(n^2)
    some sort of double loop, scales 2
    quadratically,twice the data,4 times slower the program
    
    double loop
'''

#dictionary: where
#keys: name
#value: set of hobbies for that person

characters = {}
characters['Gru'] = set(['World domination','dancing'])
characters['Minion'] = set(['Floating','dancing'])
characters['Margo'] = set(['dancing','World domination'])

for person in sorted(characters.keys()):
    print "%s: " %person.capitalize(),
    for hobby in characters[person]:
        print "%s," %hobby,
    print characters[person]
    
hobbies = {}
#key: a hobby from characters dictionary
#value: set of names with that hobby
all = set()   #find all hobbies

for key in characters:
    all = all | characters[key]
print all
for hobby in all: #initialize hobbies with these keys
    hobbies[hobby] = set()
for name in characters: #add stuff from caracters
    for hobby in hobbies:
        hobbies[hobby].add(name)
print hobbies #now each hobby is a key and they are assigned to each character with that hobby
 