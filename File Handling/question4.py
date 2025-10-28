with open("/workspaces/gcse-24-27-laya04/Holiday.txt", "r") as file:
    counter = 0 
    for line in file:
        print(line)
        counter = counter + 1
    print(" there are", counter, "lines")