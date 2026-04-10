# #Linear Search
# #Create an array
# names = ["Debbie", "Jessie", "Vigdis", "Emilia"]
# searchValue = "Jessie"
# found = False
# index = 0

# #conditional loop that stops when 
# #1. search value is found
# #2. the search is at the end of the array

# while not found and index < len(names):
#     if searchValue == names[index]:
#         found = True
#     else:
#         index += 1

# # after the loop
# if found:
#     print("Found in index:", index)
# else:
#     print("Not found")

# #17/03/2026 
# #1)
# authorised = ["True", "True", "False"]
# searchValue = "False"
# found = False
# index = 0

# #conditional loop that stops when 
# #1. search value is found
# #2. the search is at the end of the array

# while not found and index < len(authorised):
#     if searchValue == authorised[index]:
#         found = True
#     else:
#         index += 1

# # after the loop
# if found:
#     print("False found in index:", index)
# else:
#     print("False not found")




#2)
def linearSearch(searchValue, searchList, names):
    found= True
    index = 0 

    while not found and index < len(searchList):
        if searchValue == searchList[index]:
            found = True
        else:
            index += 1

    # after the loop
    if found:
        print("False found in index:", index)
        print("Student is ", names[index])
    else:
        print("False not found")
#Call out
linearSearch(False, [True,True,False], ["Jessie", "Debbie", "Maggie"])

