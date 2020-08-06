# main program that implements object circle

from Circle import Circle

def main():
    circle1 = Circle()
    print ("The area of the circle of the radius", circle1.getRadius(), "is %.2f" % circle1.getArea())
    
    circle2 = Circle(5.53)
    print ("The area of the circle of the radius", circle2.getRadius(), "is %.2f" %circle2.getArea())
    print ("The perimeter of the circle of the radius of", circle2.getRadius(), "is %.2f" %circle2.getPerimeter())
    
    circle2.setRadius (3.3)
    print ("The area of the circle of the radius", circle2.getRadius(), "is %.2f" %circle2.getArea())
    print ("The perimeter of the circle of the radius of", circle2.getRadius(), "is %.2f" %circle2.getPerimeter())

main()
