totalHeight = 0
counter = 0
for i in range(12):
    userHeight = int(input("Enter your height "))
    totalHeight = totalHeight + userHeight
    counter = counter + 1
print("average height is", totalHeight/counter)

