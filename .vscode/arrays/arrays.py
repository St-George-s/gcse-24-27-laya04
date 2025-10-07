#create arrays
# heights = [2.4, 3.8, 0.4]
# names = ["Bob", "Dave", "Simon"]
# print(heights[1])
# print(names[1])

# for counter in range(3):
#     print(names[counter])# counter is 0 then 1 then 2
#     print (heights[counter])

heights = [2.4, 3.8, 0.4, 1.9]
names = ["Bob", "Dave", "Simon","john"]
print(heights[1])
print(names[1])

for counter in range(len(names)):
    print(names[counter])# counter is 0 then 1 then 2
    print (heights[counter])

#append (add) to an array
heights.append(2.2)
names.append(Jimmy)

print(heights)
print(names)