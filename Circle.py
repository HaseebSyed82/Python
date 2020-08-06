# This is objec of a circle 

import math

class Circle:
    def __init__(self,radius=1):
        self.__radius = radius # This is the circle constructor

     # function returns perimeter of a circle   
    def getPerimeter(self):
        return 2*self.radius *math.pi

    #turn area of a circle
    def getArea(self):
        return self.radius*self.radius*math.pi

    # Change the value of the radius
    def setRadius (self, radius):
        self.radius = radius

    # get the radius value
    def getRadius(self):
        return self.radius
