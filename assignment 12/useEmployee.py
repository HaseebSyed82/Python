# This is main function of the program
# program reads 3 different objects and displays
# name, id number, department, position.
# Assignment 12
# Haseeb Syed
# CIS 1400

from Employee1 import Employee1
from Employee2 import Employee2
from Employee3 import Employee3

def main():
    employee1 = Employee1(" ", 0, "  ", " ") 
    employee2 = Employee2(" ", 0, "  ", " ")
    employee3 = Employee3(" ", 0, "  ", " ")
    print ("Name         ID Number        Department      Position")
    print (employee1.getName(),employee1.getIDNumber(),"          ",employee1.getDepartment(),"    ",employee1.getPosition())
    print (employee2.getName()," ", employee2.getIDNumber(),"          ",employee2.getDepartment(),"            ",employee2.getPosition())
    print (employee3.getName()," ",employee3.getIDNumber(),"          ",employee3.getDepartment()," ",employee3.getPosition())
    
main ()
    
