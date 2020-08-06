# This is the object for Employee 2
# Assignment 12
# Haseeb Syed
# CIS 1400

class Employee2:
    def __init__(self,name = "Mark Jones",idnumber = 39119,department = "IT",position = "Programmer"):
        self.name  = "Mark Jones"
        self.idnumber = 39119
        self.department = "IT"
        self.position = "Programmer"

    def getName(self):
        return self.name
    
    def getIDNumber(self):
        return self.idnumber
    
    def getDepartment(self):
        return self.department
    
    def getPosition(self):
        return self.position
