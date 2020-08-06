# This phython program calculates the colume and
# side surface of a cylnder.
# program asks you to enter length and radius
# of the cylinder.
# Creator: Haseeb Syed
# Class: CIS 1400
# Homework: Lab function

# Calculating volume
def volume (radius,length):
    result = (3.14 * radius**2 * length)
    return result

# Calculating surface
def sideSurface (radius,length):
    result = (2 * 3.14 * radius *length)
    return result

# Result
def main():
    radius = eval(input("Enter radius:"))
    length = eval(input("Enter length:"))
    print ("The volume is %.2f" % volume(radius,length), "centimeters^3")
    print ("The Surface Area is %.2f" % sideSurface(radius, length), "m^2")
    
main()

