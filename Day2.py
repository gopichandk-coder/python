#Day2
#Data Types, Numbers, Operations, Type Conversion, F-Strings

#Data Types-Strings, Integers, Floats, Booleans

print(len("Hello"))
#Subscripting
print("Hello"[0])
print("Hello"[4])
print("Hello"[-1])

#String
print("123" +"345")

#Integer = Whole Number
print(123 + 10)

#123,456,789 In python we can replace commas with underscores,#computer removes the undersocre and make it as one number
# Large Integers
print (123_456_789)



#Float = Decimal Number
#Float = Floating Point Number
print(3.14159)

#Boolean #true #false
print(True)
print(False)

#===============================================================================================================
#type is used check the data type of a variable or value
print(type(123))
print(type("Hello"))
print(type(123.12))
print(type(False))


#Type Conversion (covert one data type to another with rules)
print("123" + "456")
print(int("123") + int("456"))
print(float("123.12") + float("456.45"))
print(str(123) + str(456))
print(bool(1)) #True
print(bool(0)) #False

#print(int("abc") + int("456")) #this will give an error because abc is not a number

#Make this line of code run without errors
#print("Number of letters in your name: " + len(input("Enter your name")))
print("Number of letters in your name: " + str(len(input("Enter your name"))))


#===============================================================================================================

#Mathematical Operations

print("My age: " + str(12))
print(123+456)
print(7-3)
print(3*3)
print(6/2) #provide float

print(6//2) #provide integer for complete division
print(5//2) #provides 2 but its wrong, need to very careful with this operator
print(5/2) #provides 2.5 which is correct

print(2**3) # 2 to the power of 3

#PEMDAS
#Parenthesis, Exponents, Multiplication, Division, Addition, Subtraction
print(3*3+3/3-3)
print(3/3*3+3-3)
#left to right rule for same precedence operators

print(3*(3+3)/3-3)
#===============================================================================================================

#Number Manipulation
bmi = 84 / 1.65 ** 2
print(bmi) #provide floating with a lot of decimals after .
print(int(bmi)) #it gives lowest whole number

print(round(bmi)) #near whole number #flooring
print(round(3.3)) #3
print(round(3.7)) #4

print(round(bmi, 2)) #whole number and next two decimal places
print(round(bmi, 3)) #whole number and next three decimal places
#example of round function with 2 decimal places
print(round(8/3, 2)) #2.67


#=============================================================================================================

#Assignment operators
score = 0

#score = score + 1 #instead of this we can use below one
score += 1
#score = score - 1 #instead of this we can use below one
score -= 1
#score = score * 2 #instead of this we can use below one
score *= 2
#score = score / 2 #instead of this we can use below one
score /= 2

print(score)

#F-Strings
#F-Strings allow you to embed expressions inside string literals using curly braces {}
#example of f-string with variables
name = "Alice"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")

#example of f-string with variables
score = 0
height = 1.8
is_win = False
print(f"Your score is {score} , your height is {height}. Your winning condition is {is_win}")



#===========================================================================

#Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
print (f"Each person should pay: ${round((bill * (1 + tip / 100)) / people, 2)}")
