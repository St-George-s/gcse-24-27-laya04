# import random 
# num = random.randint(1,10)
# userGuess = int(input("guess the number"))
# if num == userGuess:
#     print("Correct")
# else:
#     print("Wrong, the number was ", num)


# largest = float('-inf')
# smallest = float('inf')

# for i in range(10):
#     num = int(input("Enter a number: "))

#     if num > largest:
#         largest = num

#     if num < smallest:
#         smallest = num

# print("Largest:", largest)
# print("Smallest:", smallest)
 
# for i in range(1,13):
#     result = 8*i
#     print("8 x", i, "=", result)

# total = 0
# for i in range(1,11):
#     age = int(input("Enter your age"))
#     total = total + age
# print("total ages =", total)

# userage = int(input("Enter user's age: "))
# if userage >= 18:
#     print("You can watch the 18 rated movies!")
# else:
#     print("you are too young, please select another option")

# usergenre = input("What's your favourite genre?: ")
# if usergenre == "romance":
#     print("You might like: 10 things I hate about you")
# elif usergenre == "horror":
#     print("You might like: Scream")
# elif usergenre == "comedy":
#     print("You might like: murder mystery")

# userage = int(input("Enter your age"))
# while userage < 14:
#     print("your age is not valid as it is too low, please increase")
#     userage = int(input("Enter another age"))
# print("age accepted")

# def IsEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# print(IsEven(6))
 
# numbers = []
# for i in range(1,11):
#     userNumber = int(input("enter a number"))
#     numbers = numbers.append(userNumber)
# userguess = int(input("enter a number to see if it is in the list"))
# found = False

# while userguess == numbers[]:
#     if userguess == numbers:
#         found = True
#         print("number is found")

# numbers = [5, 8, 12, 20, 7]
# found = False
# usernumber =12
# for i in range(len(numbers)):
#     if usernumber != numbers[i]:
#         found = False
#     else:
#         print("12 is in list")

# names = ["Ali", "Ben", "Chloe", "Dana", "Ethan"]
# found = False
# name = "Dana"
# for i in range(len(names)):
#     if name != names[i]:
#         found = False
#     else:
#         print("Dana is in the list")
# # num = [10, 15, 20, 25, 30]
# found = False
# usernum = 25
# for i in range(len(num)):
#     if usernum != num[i]:
#         found = False 
#     else:
#         print("25 is in list")

# userguess=""
# password = "admin123"
# while userguess != password:
#     userguess = input("enter a password: ")
# print("logged in")

# usernum=int(input("enter a number"))
# while usernum >0:
#     print(usernum)
#     usernum=int(input("enter a number"))
# print("invalid number")
# usernum = int(input("Enter a number: "))

# while usernum < 1 or usernum > 10:
#     usernum = int(input("Enter a number: "))

# print("Num accepted")
#Create a list of 5 exam scores and print the highest score.
# scores =[45,46,47,48,50]
# highest = scores[0]

# for i in scores:
#     if i >highest:
#         highest = i
# print("highest score is", highest)

#Store 4 colours in a list and print each one using a loop.
# colours= ["yellow","red","green","purple"]
# for i in colours:
#     print(i)
#Write a function called add_numbers that takes two numbers and returns their sum.
# def add_number(a,b):
#     return a + b
# print(add_number(5,3))

# #Write a function that takes a number and returns "Positive" or "Negative".
# def num(number):
#     if number>0:
#         return "positive"
#     else:
#         return "negative"
# print(num(12))

#1.Ask the user for their first and last name, then concatenate them into one full name.
# username = input("Enter your name: ")
# userlastname = input("Enter you last name: ")
# full_name = username + " " + userlastname
# print(full_name)

#2.Take a word as input and print it in uppercase.
# word = input("enter a word: ")
# word = word.upper()
# print(word)
#3.Take a sentence and print the first 5 characters.
# sentence = "A plane from Spain filled with osmotised rain"
# print(sentence[:5])
#4.Print the last 3 characters of a word.
#word = input("word")
#print(word[-3:])
#5.Count how many characters are in a string (without using len()).
# long_word = input("Enter a long word: ")
# count = 0
# for char in long_word:
#     count =count+ 1
# print(count)
#Create a file and write "Hello World" into it.
# with open ("file.txt", "w") as file:
#     file.write("Hello World")
# #Read and print the contents of a file.
# with open("file.txt", "r") as file:
#     print(file.read())
#Append a new line of text to an existing file.
# with open("file.txt", "a") as file:
#     file.write(" My name is liya")
#Count how many lines are in a file.
#Read a file and print each line in uppercase.
#Write 5 user-input names into a file.
# names = ["Ali", "Ben", "Chloe", "Dana", "Ethan"]
# found = False
# searchname = "Dana"
# for name in names:
#     if name != searchname:
#         found = False
#     else:
#         print("Dana is in the list")

names = ["Ali", "Ben", "Chloe", "Dana", "Ethan"]
found = False
searchname = "Dana"   
index = 0
while found == False and index < len(names):
    if searchname == names[index]:
        found = True
        print("Dana is found at", index)
    index = index + 1

