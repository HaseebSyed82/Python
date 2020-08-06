def cylvol(radius, length):
	result = 3.14 * radius**2 *length
	return result
def surface(volume, radius):
    result = 2 * 3.14 * radius * length
    return result
def main():
    Volume = eval(input(" Enter the radius: "))
    Surface = eval(input("Enter the length: "))
    print ("volume of the given measurment is %.2f" % cylvol(radius, length), "cm^2")
    print ("Surface of the given measurment is %.2f" % surface(volume, radius), "cm^2") 

main()
