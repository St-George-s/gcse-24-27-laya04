# print("Hello! Welcome to Fortune MadLibs")

# # Get input from the user
# userName = input("Enter your name: ")
# userZodiac = input("Enter your zodiac sign: ").lower()
# userDate = input("Enter a special date: ")

# # Zodiac fortunes
# if userZodiac == "aries":
#     fortune = "all your problems will go away"
# elif userZodiac == "taurus":
#     fortune = "you will step on something sharp"
# elif userZodiac == "gemini":
#     fortune = "you will get praised for something you didn't even try that hard at"
# elif userZodiac == "cancer":
#     fortune = "you will receive a LOOOOtttttt of money"
# elif userZodiac == "leo":
#     fortune = "you will have a very very very bad day today"
# elif userZodiac == "virgo":
#     fortune = "you will travel to the Maldives and have fresh coconut water"
# elif userZodiac == "scorpio":
#     fortune = "you will get fired"
# elif userZodiac == "sagittarius":
#     fortune = "you will finally buy the unicorn co-op ice cream"
# elif userZodiac == "capricorn":
#     fortune = "you will be the most successful person to ever exist and become the architect of the 8th world wonder"
# elif userZodiac == "aquarius":
#     fortune = "you will get a very good bonus on this day"
# elif userZodiac == "pisces":
#     fortune = "you will become a taxi driver and drive the Queen of England to Scotmid to get tomatoes, milk, and bread"
# else:
#     fortune = "something unexpected will happen… be ready!"

# Print result
# print("On " + userDate + ", " + userName + " will " + fortune + " because they are a " + userZodiac + ".")

#question 1
# name = "Laya"
# for counter in range (1, 11):
#     print(name)

#question2 
# name = input("Enter your name: ")
# for counter in range (1, 31):
#     print(name)
#question3 
# name = input("Enter your name: ")
# for counter in range (1, 3):
#     print("Hello,", name)
#question4
# number = 8 
# for counter in range (1, 13):
#     print(number*counter)
#question5
# number = 8 
# for counter in range (1,21):
#     print(" 8 x",counter,"=", counter*number)
#question6
# number = 7
# for counter in range (1,13):
#     print(" 7 x",counter,"=", counter*number)
#question7
# for counter in range (1,11):
#     age = int(input("Enter your age"))
#     print(age)
#question8
# for counter in range (1,11):
#     age = int(input("Enter age of person"+ str(counter)+":"))
#     print("Age of person", counter,"in ten years is:", age+10)
#question9
# total_age = 0
# for counter in range (1,11):
#     age = int(input("Enter person"+str(counter)+"age"))
#     total_age += age
# print("the total age is " +str(total_age))
#question10
# code = input("enter a password ")
# while code != "rzy":
#     code=input("Enter a another password")
# print("code accepted")
#question11
# code = int(input("enter a 4 digit code: "))
# while code != 4132:
#     code=int(input("try again!:  "))
# print("Code 4132 is correct")
#question12
# age = int(input("enter my age"))
# while age != 14:
#     age=int(input("try again"))
# print("14 is correct")
# password=input(" enter a password")
# while len(password) >5:
#     password=input("enter a longer password: ")
# print("password is accepted")

# password = "blue123"
# attempts = 0
# while attempts < 3:
#     userPassword = input("enter a password: ")
#     attempts = attempts + 1
#     if userPassword == password:
#         print("access granted")
#         break
# if attempts >=3:
#         print("locked out")
 
# temperature = []
# for counter in range (1, 8):
#     userTemp = int(input("enter a temperature"))
#     temperature.append(userTemp)
# print( sum(temperature)/counter)


# adultTicket = 2.50
# childrenTicket = 1.50
# cost = 0

# userAdultTickets = int(input(" enter adult ticket number"))
# userChildrenTickets =  int(input(" enter child ticket number"))
# cost = (userAdultTickets*2.50) + (userChildrenTickets*1.50)
# print("total cost is", cost)