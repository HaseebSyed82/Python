# This is the object for Color
# Haseeb Syed
# CIS 1400
# Final Lab

class Color:
    def __init__(self,colorOne,colorTwo):
        self.__colorOne = colorOne
        self.__colorTwo = colorTwo

    def getPurple(self):
        if ((self.__colorOne.lower() == "red".lower()) and (self.__colorTwo.lower() == "blue".lower())):
            print ("If you mix red and blue colors you get PURLE")
        if ((self.__colorOne.lower() == "blue".lower()) and (self.__colorTwo.lower() == "red".lower())):
            print ("If you mix blue and yellow colors you get PURLE")
           

    def getOrange(self):
        if ((self.__colorOne.lower() == "red".lower()) and (self.__colorTwo.lower() == "yellow".lower())):
            print ("If you mix red and yellow colors you get ORANGE")
        if ((self.__colorOne.lower() == "yellow".lower()) and (self.__colorTwo.lower() == "red".lower())):
            print ("If you mix yellow and red colors you get ORANGE")
            
    
    def getGreen(self):
        if ((self.__colorOne.lower() == "blue".lower()) and (self.__colorTwo.lower() == "yellow".lower())):
            print ("If you mix blue and yellow colors you get GREEN")    
        if ((self.__colorOne.lower() == "yellow".lower()) and (self.__colorTwo.lower() == "blue".lower())):
            print ("If you mix blue and yellow colors you get GREEN")
            
    


        
