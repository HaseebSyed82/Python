# This program  tests four generators by measuring their
# output voltages at three different times.
# Program also computes average of each generator.
# Program also computes average for all the generators.
# HomeWork: 5
# Creator: Haaseeb Syed

print ("Enter the test results for each generator three different times.")
print ("Program will display and calculate the average of each generator.")
num = 3
numTwo = 4
# 1st Generator
vOne, vTwo, vThree = eval(input("Generator one results: "))
generatorOneAvg = ((vOne + vTwo + vThree) / num)

# 2nd Generator
vFour, vFive, vSix = eval(input("Generator one results: "))
generatorTwoAvg = ((vFour + vFive + vSix) / num)

# 3rd Generator
vSeven, vEight, vNine = eval(input("Generator one results: "))
generatorThreeAvg = ((vSeven + vEight + vNine) / num)

# 4th Generator
vTen, vEleven, vTweleve = eval(input("Generator one results: "))
generatorFourAvg = ((vTen + vEleven + vTweleve) / num)

# Results
print ("1st generator:", vOne, vTwo, vThree)
print ("2nd generator:", vFour, vFive, vSix)
print ("3rd generator:", vSeven, vEight, vNine)
print ("4th generatoe:", vTen, vEleven, vTweleve)

# Average of each generator
print ("The avearge of the generator one is =", generatorOneAvg)
print ("The avearge of the generator two is =", generatorTwoAvg)
print ("The avearge of the generator three is =", generatorThreeAvg)
print ("The avearge of the generator four is =", generatorFourAvg)

# Average of All generators
AvgOfAllGenerators = (
    (generatorOneAvg + generatorTwoAvg + generatorThreeAvg + generatorFourAvg) / numTwo)
print ("The average of all genrators is:", AvgOfAllGenerators)
    
