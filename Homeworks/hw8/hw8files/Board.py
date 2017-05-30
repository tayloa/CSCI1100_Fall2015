class board(object):
    def __init__(self,info):
        self.name = info["name"]
        self.grav = int(info["gravity"])
        self.portal = int(info["portal"][0]),int(info["portal"][1])
        self.right = info["right"]
        self.left = info["left"]
        self.up = info["up"]
        self.down = info["down"]
        self.obstacle = info["obstacle"]
    def __str__(self):
            return "Board %s: Portal location: %s, Gravity: %s \n    Obstacles at %s \
            \n    Portals to: right: %s, up: %s, left: %s, down: %s" %(self.name,self.portal,self.grav,\
            self.obstacle,self.right,self.up,self.left,self.down)
        