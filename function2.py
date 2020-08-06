# This phython program converts feet to meters 
# and vice versa.
# Hw function lab 2
# Class : CIS 1400
# creator = Haseeb Syed

value = 0.305
# Converts from feet to meters
feet = 0
def feetToMeter(feet):
    for feet in range (1, 11):
        meter = (feet / value)
        
# Converts from meters to feet
meter = 0
def meterToFeet(meter):
    for meter in range (20,74, 6):
        feet = (meter * value)
        print (feet,"    ", "%.1f" %meter,"   ",meter, "    ", "%.1f" %feet)
# Main function
def main():
    print ("Feet  Meter | Meter Feet")
    print(feetToMeter(feet),meterToFeet(meter))
main()


