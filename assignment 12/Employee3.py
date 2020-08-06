# This is the object for Employee 3
# Assignment 12
# Haseeb Syed
# CIS 1400


class Employee3:
    def __init__(self,name = "Joy Rogers",idnumber = 81774,department = "Manufacturing",position = "Engineer"):
        self.name  = "Joy Rogers"
        self.idnumber = 81774
        self.department = "Manufacturing"
        self.position = "Engineer"

    def getName(self):
        return self.name
    
    def getIDNumber(self):
        return self.idnumber
    
    def getDepartment(self):
        return self.department
    
    def getPosition(self):
        return self.position
