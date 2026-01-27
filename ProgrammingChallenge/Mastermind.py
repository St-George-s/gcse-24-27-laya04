# import random
# # RandomNumber = str(random.randint (1000, 9999))
# RandomNumber = "1234"
# print(RandomNumber)
# counter=0
# userNumber = ""
# while counter != 4:
#     userNumber = input("Enter a random number: ")
#     for index in range(len(RandomNumber)):
#         for indexTwo in range(len(userNumber)):
#             if RandomNumber[index] == userNumber[indexTwo]:
#                 print(RandomNumber[index], "==", userNumber[indexTwo])
#                 counter = counter + 1
#                 print(counter, "numbers common")


# import random
# # RandomNumber = str(random.randint (1000, 9999))
# RandomNumber = "1234"
# print(RandomNumber)
# counter=0
# userNumber = ""
# while counter != 4:
#     userNumber = input("Enter a random number: ")
#     for index in range(RandomNumber[0]):
#         for indexTwo in range(len(userNumber)):
#             if RandomNumber[0] == userNumber[indexTwo]:
#                 counter = counter + 1
#                 print(counter, "numbers common")


# import random
# RandomNumber = str(random.randint (1000, 9999))
# counter=0
# numbersGuessed = []
# userNumber = ""
# while counter != 4:
#     userNumber = input("Enter a random number: ")
#     for index in range(len(RandomNumber)):
#         for indexTwo in range(len(userNumber)):
#             if RandomNumber[index] == userNumber[indexTwo] and userNumber[indexTwo] not in numbersGuessed:
#                 print(RandomNumber[index], "==", userNumber[indexTwo])
#                 numbersGuessed.append(userNumber[indexTwo])
#                 counter = counter + 1
#                 print(counter, "numbers common")
#                 print(numbersGuessed)
# print("You have found the number!")


import random
RandomNumber = str(random.randint (1000, 9999))
print(RandomNumber)
counter=0
numbersGuessed = []
userNumber = ""
guesses=0
while userNumber != RandomNumber:
    counter = 0
    userNumber = input("Enter a random number: ")
    guesses= guesses + 1
    # thats 1 to gues so can print total number of gueses at the end
    for index in range(len(RandomNumber)):
        for indexTwo in range(len(userNumber)):
            # checks the position of one number against the another number
            if RandomNumber[index] == userNumber[indexTwo] and userNumber[indexTwo] not in numbersGuessed:
                #only adds new numbers in common into array
                numbersGuessed.append(userNumber[indexTwo])
                counter = counter + 1
    print(counter, "numbers common")
    # print(numbersGuessed)
print("You have found the number in", guesses,"guesses" )