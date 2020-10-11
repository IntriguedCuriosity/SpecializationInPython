class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initializeX, initializeY):
        """ Create a new point at the origin """
        self.x = initializeX
        self.y = initializeY
    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def __str__(self):
        return "x= {} , y= {}".format(self.x, self.y)
        
        
p=Point(5,10)
print(str(p))