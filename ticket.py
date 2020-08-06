# This python program creates a file ticket.txt and reads it.
# program also reads output.txt file and gives user general info.
# Haseeb Syed
# CIS 1400
# FILES I/O HOMEWORK


# CREATING TEXT FILE AND READING IT.
import os
text = open ("C:\\TEMP\\ticket.txt", "w")
text.write ("Below is the content of file ticket.txt file:.\n")
text.write ("Ticket Price.\n")
text.write ("A31   149.99.\n")
text.write ("B31   49.99\n")
text.write ("A41   179.99\n")
text.write ("F31   169.99\n")
text.write ("A35   179.99\n")
text.write ("A44   169.99\n")
text.close()
textResult = open ("C:\\TEMP\\ticket.txt", "r")
test = textResult.readline()


# LOOPING 
while test:
    print (test)
    test = textResult.readline()
textResult.close()



# READING OUTPUT.TXT FILE
print ("*******************************************")
print ("                 TICKET REPORT             ")
print ("*******************************************")

import os

def main():
    output = input("Below is the content of the (Enter the file name):").strip()
    if os.path.isfile(output):
        infile = open(output, "r")
        s = infile.read() 
        ticket = [ eval(x) for x in s.split() ]

        # GENREAL INFOROMATION
        print("There are ", len(ticket), " tickets in the database.")
        print("Maximun Ticket price is $", max(ticket))
        print("Minimum Ticket price is $", min(ticket))

        # CALCULATING AVERGAE
        average = (sum(ticket) / len (ticket))
        print("Average Ticket Price is ", "%.2f" % average)
        print ("*******************************************")
        infile.close()
main()


