# This python program reads unspecified 
# number of scores and calculate their
# averages, number of list, sum, below,
# and above averages.
# CIS 1400
# Haseeb Syed
# List Homework 2


# Importing Random
import random

# Inputing the rndom scores
scores = 50
aboveAvgScore = 0 
belowAvgScore = 0
scores = [random.randint(0,100)]
scores = eval(input("Enter number of scores: "))
aboveAvgScore >= scores
belowAvgScore <= scores

# Sum  and length of scores
print (scores)
print("The total of the scores is",sum(scores))
print ("The length of the scores is",len(scores))

# Average
average = (scores)
average = (sum(scores) / len(scores))
print ("The average of the scores is"," %.2f" %average,"%")

# Below and above averages
average = (sum(scores) / len(scores))
print ("The above average scores are: ",aboveAvgScore)
print ("The below average scores are: ",belowAvgScore)
