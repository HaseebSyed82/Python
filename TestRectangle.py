# main function
# This program imports rectangle object and displays
# height, width, area and perimeter.
# Object Lab
# haseeb Syed
# CIS 1400

from Rectangle import Rectangle

def main ():
    rectangle1 = Rectangle(4,40)
    print ("The height of the rectangle is:", rectangle1.getHeight())
    print ("The width of the rectangle is:", rectangle1.getWidth())
    print ("The perimeter of the rectangle is:", "%.2f" %rectangle1.getPerimeter())
    print ("The Area of the rectangle is:", "%.2f" %rectangle1.getArea())

    print ("    ")
    print ("Values for Rectangle 2")

    # Rectangle 2
    rectangle2 = Rectangle (3.5, 35.7)
    print ("The height of the rectangle is:", rectangle2.getHeight())
    print ("The width of the rectangle is:", rectangle2.getWidth())
    print ("The perimeter of the rectangle is:", "%.2f" %rectangle2.getPerimeter())
    print ("The Area of the rectangle is:", "%.2f" %rectangle2.getArea())

    
main()
