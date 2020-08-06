# This phython program prompts user to enter the answer for driving exam.
# It calculates your result and record your result.
# It displays the score and wrong and right answer.
# Class CIS1400
# Creator: Haseeb Syed
# Array homework

print ("Welcome to your driving license exam ")
print ("you need atleast 15 points to pass this exam")
print ("Use upper case letters only")

result = []
answers =  []
score = 0
rightAnswers =0
wrongAnswers =0
percentage =0

for i in range (20):
    print ("Question:", i)
    x = input("Enter answer: ")
    result.append(x)
    
print ("Correct Answers     Your Answers")


answers =  []
answers = ['B','D','A','A','C','A','B','A','C','D','B','C','D','A','D','C','C','B','D','A']
for i in range (20):
    print (answers[i],"                 ",result[i])
    
if (result [i] == answers [i]):
    score = rightAnswers

    print ("your score is", score "/20")
    print ("Congratulations!!! you got 100.00")

else (result [i] != answers [i]):
    score = rightAnswers
    percentage = rightAnswers / 20
    print ("your score is", score "/20")
    print ("Your percentage ", "%.2f" % percentage)
    
    if (percentage < 75):
        print ("You passed the exam")
        else:
            print ("Good luck next time")
