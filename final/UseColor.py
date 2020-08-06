# This is the main function of the class 
# it displays what happen when you mix two 
# different colors.
# Haseeb Syed
# CIS 1400
# Final Lab


from Color import Color

def main():
    print ("Red, Blue, yellow are primary color because")
    print ("the cannot be made by mixing others colors")
    print ("find out what happen when you mix these")
    print ("    ")
    color1 = Color("red", "blue")
    print (color1.getPurple())
    print ("  ")
    color2 = Color("red", "Yellow")
    print (color2.getOrange())
    print ("   ")
    color3 = Color("blue", "yellow")
    print (color3.getGreen())

main()
