class board(object):
    def __init__(self,info):
        self.name = info['name']
        self.gravity = info['gravity']
        self.portal = info['portal']
        self.right = info['right']
        self.up = info['up']
        self.left = info['left']
        self.down = info['down']
        self.obstacles = info['obstacles']
    def __str__(self):
        return "Board %s: Portal location: (%s,%s), Gravity: %s\n    Obstacles at: %s\n    Portals to: right: %s, up: %s, left: %s, down: %s" %(self.name,self.portal[0],self.portal[1] \
        ,self.gravity,self.obstacles,self.right,self.up,self.left,self.down)
        