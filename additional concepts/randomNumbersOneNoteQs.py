# #question1a
# import random 

# myRandomNumber = random.randint(1, 3)
# print("Your challenge is", myRandomNumber)

#question1b
# import random 

# myRandomNumber = random.randint(1, 3)
# if myRandomNumber == 1 :
#     print("walk 10km")
# elif myRandomNumber == 2:
#     print("run 5k")
# elif myRandomNumber == 3:
#     print("swim 1km")

#question2
# counterA = 0
# while counterA < 3:
#     randomWord = input("Enter a word: ")
#     counterA = 0
#     for letter in randomWord: 
#         if letter == "a" or letter == "A":
#             counterA + 1

counterA = 0
while counterA < 3:
    randomWord = input("Enter a word: ")
    
    for letter in randomWord: 
        if letter == "a" or letter == "A":
           counterA=  counterA + 1
print("this word has", counterA, "a in it")

