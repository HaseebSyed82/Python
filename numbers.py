# This program reads integers, determine how many 
# positives and negatives values have beeen inserted.
# The program stop reading after the zero has been inserted.
# It also displays average and total of the numbers.
#
# Creator: Haseeb Syed
# Class: CIS-1400
# Homework 4

numbers = int(input("Enter an integer, the input ends if it is 0: "))
positive = 0
negative = 0
sum_number = 0
total = 0
average = 0

if (numbers != 0):
    while (numbers != 0):
        numbers = int(input("Enter an integer, the inout ends if it is 0: "))
        if (numbers > 0):
            total += numbers
            positive += 1
            sum_number += 1
        elif (numbers < 0):
            total += numbers
            negative += 1
            sum_number += 1
        sum_number += 1
        total = positive + negative
        average = sum_number / total
    print ("The number of positives is ", positive)
    print ("The number of negatives is ", negative)
    print ("The total is", sum_number)
    print ("The avearge is ", average)
else :
    print ("You didn't enter any number")
    

    
    
    
        
         
    
        
