# This python program displays smallast, largest,
# sum, and average of the random numbers inputed in the list.
# Class CIS 1400
# Array LAB 2
# Creator: Haseeb Syed

numbers = []
avgNumber = 20

for i in range (20):
    x = eval(input("Enter numbers: "))
    numbers.append(x)
    
average = (sum(numbers)/ avgNumber)
    
print ("The smallest number in list is:", min(numbers))
print ("The largest number in the list is:", max(numbers))
print ("The sum number of the list is: " ,"%.2f" % sum(numbers))
print ("The average of the numbers is: ", "%.2f" % average)
