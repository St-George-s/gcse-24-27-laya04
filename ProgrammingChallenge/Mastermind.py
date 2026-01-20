import random
RandomNumber = str(random.randint (1000, 9999))
userNumber = input("Enter a random number: ")

for index in range(len(RandomNumber)):
    for indexTwo in range(len(userNumber)):
        if RandomNumber[index] == userNumber[indexTwo]:
            print("found")
            counter = ()

   