#parallel arrays
cities = ["London","Edinburgh","Glasgow","Belfast","Cardiff"] 
population = [8908, 482, 366, 341, 635]
# for counter in range (len(cities)):
#     print(cities[counter])

# for counter in range (len(cities)):
#     print(cities[counter] + " has a population of " + str(population[counter]))

#Linear Search
found = False
userCity = input("What city would you like population for?:")
for counter in range(len(cities)):
    if userCity == cities[counter]:
     print(cities[counter] + " has a population of " + str(population[counter]))
     found = True

if not found:
   print("Your city was not found")

