# Data Types
name = "Laya" #This is a string
myAge = 45 #This is an integer
myHeight = 159.5 #This is a decimal number (float/real)
isAnOnlyChild = True #This is a boolean (True/False)

#Casting (Changing from one data type to another)
age = input("Enter age:")
print(age)
print(age + "10") #concatenate two strings together (join them up)
ageAsanInt = int(age)
print(ageAsanInt + 10) # add teo integers together (maths addition)
print ("Your age is " + str(ageAsanInt))

# Data types - more examples
stillanInteger = -4
myNumber = "0787822873" # always store as a string 

#Arithmetic operators 
add = 10 + 10
subtract = 10 - 10
multiply = 10 * 10
division = 10 / 10 #Will output as a float
Integerdivision = 11 // 10 # Forces output to be n integer
print (add, subtract, multiply, division)
print (Integerdivision)
modulo = 5 % 4 #Remainder of division
print (modulo)
exponent = 2 ** 3 #To the power of
print(exponent)

# Activity 1 - take two inputs, multiply them together and outut answer

number1 = input(" Enter a number:")
number2 = input(" Enter another number:")
multiply = int(number1) * int(number2)
print(multiply)


# Activity 1 - input user's age, output times 7
# Activity 1 - take radius as input, output volume of sphere (v = 4/3 x pi x r^3)