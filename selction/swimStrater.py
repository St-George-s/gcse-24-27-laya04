# swimTime = float(input("Enter swim time:"))
# if swimTime < 60.0:
#     print("Participant Qualifies!")
# else:
#     print("Participant does not qualify")

swimTime = float(input("Enter swim time:"))
if swimTime < 60.0:
    print("Participant Qualifies for Gold catagory!")
elif swimTime > 55.0 and swimTime < 60.0:
    print("Participant qualifies for silver catagory")
elif swimTime > 60.0 and swimTime < 65.0:
    print("Participant qualifies for bronze catagory")
else:
    print(" Participant does not qualify")

    