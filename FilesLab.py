# This python program calls scores.txt
# and calculates the number of scores
# and calculate their average.
# Files I/O lab
# Haseeb Syed

# Importing OS
import os

# Main function
def main():
    # Prompt the user to enter filenames
    f1 = input("Enter a filename: ").strip()
    if os.path.isfile(f1):
        # Open files for input
        infile = open(f1, "r")
    s = infile.read() # Read all from the file
    
    scores = [eval(x) for x in s.split()]
    print(scores)
    print("There are ", len(scores), " scores")
    print("The total is ", sum(scores))
    
    # Calculating Average
    average = (sum(scores) / len (scores))
    print("The average is ","%.2f" % average)

main()
