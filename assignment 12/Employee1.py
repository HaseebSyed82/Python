# This is the object for Employee 1
# Assignment 12
# Haseeb Syed
# CIS 1400

class Employee1:
    def __init__(self,name = "Susan Meyers",idnumber = 47899,department = "Accounting",position = "Vice President"):
        self.name  = "Susan Meyers"
        self.idnumber = 47899
        self.department = "Accounting"
        self.position = "Vice President"

    def getName(self):
        return self.name
    
    def getIDNumber(self):
        return self.idnumber
    
    def getDepartment(self):
        return self.department
    
    def getPosition(self):
        return self.position
