cord0 = [200,200]
direct0 = "right"
print "Turtle: ("+str(cord0[0])+","+str(cord0[1])+") facing:",direct0

def move(cord,direction,amount):
    if direction == "up":
        cord[0] = cord[0]
        cord[1] = cord[1] - amount
    elif direction == "down":
        cord[0] = cord[0]
        cord[1] = cord[1] + amount
    elif direction == "left":
        cord[1] = cord[1]
        cord[0] = cord[0] - amount
    elif direction == "right":
        cord[1] = cord[1]
        cord[0] = cord[0] + amount
    print "Turtle:","("+str(cord[0])+","+str(cord[1])+") facing:",direction

def turn(direct):
    if direct == "left":
        direct = "down"
    elif direct == "right":
        direct = "up"
    elif direct == "up":
        direct = "left"
    elif direct == "down":
        direct = "right"
    return direct

def jump(cord,direct):
    if direct == "left":
        cord[0] = cord[0] - 50
    elif direct == "right":
        cord[0] = cord[0] + 50
    elif direct == "up":
        cord[1] = cord[1] + 50
    elif direct == "down":
        cord[1] = cord[1] + 50
    return cord


commands = [ ]
i = 0
while i < 5:
    cmd = raw_input("Command (move,jump,turn) => ")
    print cmd
    if i == 5:
        print "Turtle:","("+str(cord0[0])+","+str(cord0[1])+") facing:",direct0
    if cmd.lower() == "jump":
        jump(cord0,direct0)        
        print "Turtle:","("+str(cord0[0])+","+str(cord0[1])+") facing:",direct0
        commands.append(cmd)
    elif cmd.lower() == "move":
        move(cord0,direct0,20)
        commands.append(cmd)
    elif cmd.lower() == "turn":
        direct0 = turn(direct0)
        print "Turtle:","("+str(cord0[0])+","+str(cord0[1])+") facing:",direct0
        commands.append(cmd)
    else: 
        print "Turtle:","("+str(cord0[0])+","+str(cord0[1])+") facing:",direct0
        commands.append(cmd)
   
    i += 1
print   
print "All commands entered",commands
print "Sorted commands",sorted(commands)


        
    
    
    
    
    
    
    
    