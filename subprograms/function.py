#Find the area of a rectangle (Function)

#length and breadth are parameters
def getAreaRectangle( length, breadth):
    return length*breadth

# Call a subprogram
print("start")
print(getAreaRectangle(10,20))
#OR
returnedArea = getAreaRectangle(10,30)
print(returnedArea)
#OR
secondReturnedArea = getAreaRectangle(5,4)
if returnedArea > secondReturnedArea:
    print("first area is bigger")