# Day 3: Control Flow and Logical Operators
# conditional statements
# logical operators
# code blocks and scope

#===============================================================================================================
#Control Flow with if, elif, and else statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
#if height == 120:
#if height != 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry! you have to grow taller before you can ride.")

# = IS ASSIGNMENT OPERATOR
# == IS COMPARISON OPERATOR (EQUAL TO)
#!= IS COMPARISON OPERATOR (NOT EQUAL TO)
#> IS COMPARISON OPERATOR (GREATER THAN)
#< IS COMPARISON OPERATOR (LESS THAN)
#>= IS COMPARISON OPERATOR (GREATER THAN OR EQUAL TO)
#<= IS COMPARISON OPERATOR (LESS THAN OR EQUAL TO)

#===============================================================================================================
#Modulo Operator
#The modulo operator % gives the remainder of a division operation.
print(7 % 2)  # Output: 1
print(10 % 3)  # Output: 1
print(10 % 2)  # Output: 0
print(156 % 4)  # Output: 0
print(156 % 5)  # Output: 1


print("Welcome to the Even Number Finder!")
Number = int(input("Please enter a number: "))
if Number % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd!")

#================================================================================================================
#Nested if statements and elif statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay 7$")
    else:
        print("Please pay 12$")
else:
    print("Sorry you have to grow taller before you can ride.")


################################

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay 5$")
    elif age <= 18:
        print("Please pay 7$")
    else:
        print("Please pay 12$")
else:
    print("Sorry you have to grow taller before you can ride.")

#================================================================================================================
#Multiple if statements

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Would you like to see the picture? (y/n)")
    if wants_photo == "y":
        #add 3$ if user wants photo
        bill += 3
    print(f"Your total bill is: {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

#=================================================================================================================

#Python Pizza Exercise

# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1

# Example Interaction
# Welcome to Python Pizza Deliveries!
# What size pizza do you want? S, M or L: L
# Do you want pepperoni on your pizza? Y or N: Y
# Do you want extra cheese? Y or N: N
# Your final bill is: $28.


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print ("Please enter correct input")

#addon pepperoni
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

#addon extra_cheese
if extra_cheese == "Y":
    bill += 1

print (f"Your final bill is: ${bill}.")


#=================================================================================================================

# Logical Operators
# Logical operators are used to combine conditional statements.
# The three main logical operators in Python are:
# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Returns True if the statement is false


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    # and operator example
    elif age >= 45 and age <=55:
        print("Youth tickets are free.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

#=================================================================================================================

#Project: Treasure Island


print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

inputA = input('You\'re at a cross road. Where do you want to go? '
               'Type "left" or "right"\n').lower()
if inputA == "left":
    inputB = input('You\'ve come to a lake. There is an island in the middle of the lake.\n '
                   'Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()
    if inputB == "wait":
        inputC = input('You arrive at the island unharmed. '
                       'There is a house with 3 doors \n One red, one yellow and one blue. '
                       'Which colour do you choose?\n').lower()
        if inputC == "yellow":
            print("You found the treasure! You Win!")
        elif inputC == "blue":
            print("Beasts! killed you. Game Over. You Lose.")
        elif inputC == "red":
            print("Full of Fire. Game Over. You Lose.")
        else:
            print("Game Over. You Lose.")

    else:
        print("You have eaten by Crocodile. You Lose.")


else:
    print("Game Over. You Lose.")


