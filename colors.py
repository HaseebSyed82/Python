#
##

print ("Red, Blue, and Yellow are primary colors because they cannot be made by mixing two different colors.")
print ("Type two of those color name to find out what color you get.")

colorOne = input("name of the color 1 = ")
colorTwo = input("name of the color 1 = ")

# Color you get by mixing red and blue    
if ((colorOne.lower() == "red".lower()) and (colorTwo.lower() == "blue".lower())):
    print ("If you mix those colors you get PURLE")
if ((colorOne.lower() == "blue".lower()) and (colorTwo.lower() == "red".lower())):
    print ("If you mix those colors you get PURLE")

# Color you get by mixing red and yellow
if ((colorOne.lower() == "red".lower()) and (colorTwo.lower() == "yellow".lower())):
    print ("If you mix those colors you get ORANGE")
if ((colorOne.lower() == "yellow".lower()) and (colorTwo.lower() == "red".lower())):
    print ("If you mix those colors you get ORANGE")

# Color you get by mixing blue and yellow
if ((colorOne.lower() == "blue".lower()) and (colorTwo.lower() == "yellow".lower())):
    print ("If you mix those colors you get GREEN")    
if ((colorOne.lower() == "yellow".lower()) and (colorTwo.lower() == "blue".lower())):
    print ("If you mix those colors you get GREEN")
    
