#Write a Python program to extract the first and last characters of a string entered by the user. 
# userInput = (input("Enter a phrase:"))
# print(userInput[5])

#Write a Python program to reverse a string entered by the user. 
# userInput = (input("Enter a character:"))
# for character in userInput:
#     print(character)

# myString = (input("Enter a phrase:"))
# reverseString = ""
# for character in myString:
#     reverseString = character + reverseString
# print(reverseString)

#Generate and print one random integer from 1 to 6. 
# import random
# myRandomNumber = random.randint (1, 6)
# print(myRandomNumber)

#Roll two dice (1–6) and print both values and their total using + string concatenation. 
# import random
# myRandomNumber1 = random.randint (1, 6)
# print("You have rolled", myRandomNumber1)
# myRandomNumber2 = random.randint (1, 6)
# print("You have rolled", myRandomNumber2)

# print("your total is ", myRandomNumber1 + myRandomNumber2)

import random
myRandomNumber1 = random.randint (1, 6)
myRandomNumber2 = random.randint (1, 6)
print(str(myRandomNumber1) + "+" + str(myRandomNumber2) + "=")
print(str(myRandomNumber1 + myRandomNumber2))