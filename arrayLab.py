# This python program converts
# power to current. Program also calculates
# the total of each columm.
# Creator:Haseeb syed
# Lab array 1
# Class: CIS 1400

# Values
resistance = [16, 27, 39,56,81]
current = []
power = []
total1  = 0
total2 = 0
total3 = 0

# Current values
for i  in range (5):
    x = eval(input("Enter the value for current: "))
    current.append(x)
    
# Formula for power
print ("Resistance  Current Power")
for i in range (5):
    power = ((resistance [i]) * (current [i]**2))
    print(resistance [i],"        ", current [i],"     ",power)
    
# Calculating the power
for i in range(len(resistance) and len(current)):
    total1 += resistance [i]
    total2 += current [i]
    total3 += power

print("Total:", total1," Total:",total2,"Total:",total3)
