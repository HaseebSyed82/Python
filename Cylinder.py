# Object for cylinder
# lab12 Orientation
# CIS 1400
# Haseeb Syed

# Importing Math
import math

# CLass
class Cylinder:
    def __init__(self, radius, length):
        self.__radius = radius
        self.__length = length
        
    # Get radius
    def getRadius(self):
        return self.__radius

    # Get length
    def getLength(self):
        return self.__length

    # Get volume
    def getVolume(self):
        return (math.pi * (self.__radius ^2) * self.__length)

    # Get radius
    def getSurface(self):
        return (2 * math.pi * self.__radius * self.__length)
    
    
