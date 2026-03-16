#Linear Search
#Create an array
def linearSearch(searchValue, searchList):
    names = ["Debbie", "Jessie", "Vigdis", "Emilia"]
    found = False
    index = 0

    while not found and index < len(names):
        if searchValue == names[index]:
            found = True
        else:
            index += 1

    # after the loop
    if found: 
        print("Found")
    else:
        print("Not found")


linearSearch("Emilia", ["Debbie", "Jessie", "Vigdis", "Emilia"])
linearSearch(10, [34, 4, 5,6,9,10])


