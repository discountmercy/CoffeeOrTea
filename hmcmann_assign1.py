# Henry McMann
# Coffee or Tea? v5.0
# A program for ordering a piping hot cup of joe or a cuppa tea.
# October 4th, 2018

# Initializing Variables
originalPrice = 0.00
taxMultiplier = 1.13
invalidInput = "Sorry, that input was invalid. Please try again."

# Initial Inputs
customerName = input("What is your name? >")
drinkType = input("Coffee or Tea? >")

# if block to validate drinkType input
# this if block is important because if the drinkType input was invalid it would not be checked until the flavour block.
if drinkType.lower() == "coffee" or drinkType.lower() == "c":
    drinkType = "coffee"
elif drinkType.lower() == "tea" or drinkType.lower() == "t":
    drinkType = "tea"
else:
    print(invalidInput)
    exit()

# input for drinkSize
drinkSize = input("Small, Medium, or Large? >")

# if block to validate drinkSize input and change originalPrice variable
if drinkSize.lower() == "small" or drinkSize.lower() == "s":
    originalPrice += 1.50
    drinkSize = "small"
elif drinkSize.lower() == "medium" or drinkSize.lower() == "m":
    originalPrice += 2.50
    drinkSize = "medium"
elif drinkSize.lower() == "large" or drinkSize.lower() == "l":
    originalPrice += 3.25
    drinkSize = "large"
else:
    print(invalidInput)
    exit()

# if block to prompt for flavour depending on the choice of coffee or tea and to change originalPrice variable further
if drinkType.lower() == "coffee":
    drinkFlavour = input("Vanilla, Chocolate, or none? >")
    if drinkFlavour.lower() == "vanilla" or drinkFlavour.lower() == "v":
        originalPrice += 0.25
        drinkFlavour = "vanilla"
    elif drinkFlavour.lower() == "chocolate" or drinkFlavour.lower() == "c":
        originalPrice += 0.75
        drinkFlavour = "chocolate"
    elif drinkFlavour.lower() == "none" or drinkFlavour.lower() == "":
        originalPrice += 0
        drinkFlavour = "nothing"
    else:
        print(invalidInput)
        exit()
elif drinkType.lower() == "tea":
    drinkFlavour = input("Mint, Lemon, or none? >")
    if drinkFlavour.lower() == "mint" or drinkFlavour.lower() == "m":
        originalPrice += 0.50
        drinkFlavour = "mint"
    elif drinkFlavour.lower() == "lemon" or drinkFlavour.lower() == "l":
        originalPrice += 0.25
        drinkFlavour = "lemon"
    elif drinkFlavour.lower() == "nothing" or drinkFlavour.lower() == "":
        originalPrice += 0
        drinkFlavour = "nothing"
    else:
        print(invalidInput)
        exit()
else:
    print(invalidInput)
    exit()

# final variable created for the originalPrice multiplied by tax
finalPrice = originalPrice * taxMultiplier

# all relevant information is printed here.
print("For",customerName, "a", drinkSize, drinkType, "with", drinkFlavour, "$ %.2f" % float(finalPrice))
