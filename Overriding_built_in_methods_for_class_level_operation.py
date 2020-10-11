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
    
    def __add__(self, addPoint):
        return Point(self.x + addPoint.x, self.y + addPoint.y)
    
    def __sub__(self, subPoint):
        return Point(self.x - subPoint.x, self.y - subPoint.y)

    def __str__(self):
        return "x= {} , y= {}".format(self.x, self.y)
        
        
p=Point(5,10)
q=Point(10,15)
print(p + q)
print(p - q)
