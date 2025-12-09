for counter in range (1,11):
    import random
    childScore = random.randint(1,100)

    if childScore > 50:
         print("Child", counter, "'s score is", childScore, ", child is good")
    elif childScore <= 50:
        print("Child", counter, "'s score is", childScore, ", child is naughty")
