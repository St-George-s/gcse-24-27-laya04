for counter in range (1,11):
    childName = input("enter your name")
    import random
    childScore = random.randint(1,100)
    if childScore > 50:
         child = "good"
    elif childScore <= 50:
        child = "Naughty"
    print("child's name is", childName, ",child " +str(counter)+ " score is" +str(childScore)+ child)
