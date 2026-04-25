#Linear Search
#Create an array
def linearSearch(searchValue, searchList):
    #searchList = ["Debbie", "Jessie", "Vigdis", "Emilia"]
    found = False
    index = 0

    while not found and index < len(searchList):
        if searchValue == searchList[index]:
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


