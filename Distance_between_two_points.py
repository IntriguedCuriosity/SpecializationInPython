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
    
    def dist_two_points(self,point1):
        xdiff= point1.getX() - self.getX()
        ydiff= point1.getY() - self.getY()
        return ((xdiff ** 2) + (ydiff ** 2)) ** 0.5

def dist_two_points(point1, point2):
    xdiff = point2.getX()- point1.getX()
    ydiff = point2.getY() - point1.getY()
    
    return ((xdiff ** 2) + (ydiff ** 2)) ** 0.5
        
p=Point(5,10)
q=Point(10,15)
print(dist_two_points(p,q))
print(p.dist_two_points(q))