weather = input("Enter weater (sunny/rainy)")
timeOfDay = input("Enter time (day/night)")

if weather == "sunny" and timeOfDay == "day":
    print("No need umbrella")
elif weather == "rain" and (timeOfDay == "day" or timeOfDay =="night"):
    print(" Take a umbrella")
