# This is the object of a rectangle
# Object Lab
# haseeb Syed
# CIS 1400

import math

class Rectangle:
    def __init__(self,width=2, height=1):
        self.width = width
        self.height = height
        
    # Return perimeter of the rectangle
    def getPerimeter(self):
        return 2*(self.height + self.width)

    # Return Area of the rectangle
    def getArea(self):
        return (self.height*self.width)
         
    def setHeight (self, height):
        self.height = height
        
    def getHeight(self):
        return self.height

    def setWidth (self, width):
        self.width = width
        
    def getWidth(self):
        return self.width
        
        
