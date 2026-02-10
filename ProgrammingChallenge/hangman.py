LetterList =[]
chances = int(input("Enter a number of chances: "))
word = input("Enter a word to guess: ")
userguess = ""
blankword = ""
for i in range (len(word)):
    blankword = blankword + "_"
print(blankword)
while chances > 0:
    while word != blankword:
        userguess = input("Enter a new letter: ")
        found = False
        chances = chances -1
        print("you have chances", chances, "left")
        for i in range (len(word)):
            if word [i] == userguess:
                found = True
                #print(i)
                blankword = blankword [:i]+ userguess + blankword[i+1:]
        print(blankword)

print("end game")