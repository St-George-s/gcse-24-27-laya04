print("Hello! Welcome to Fortune MadLibs")

# Get input from the user
userName = input("Enter your name: ")
userZodiac = input("Enter your zodiac sign: ").lower()
userDate = input("Enter a special date: ")

# Zodiac fortunes
if userZodiac == "aries":
    fortune = "all your problems will go away"
elif userZodiac == "taurus":
    fortune = "you will step on something sharp"
elif userZodiac == "gemini":
    fortune = "you will get praised for something you didn't even try that hard at"
elif userZodiac == "cancer":
    fortune = "you will receive a LOOOOtttttt of money"
elif userZodiac == "leo":
    fortune = "you will have a very very very bad day today"
elif userZodiac == "virgo":
    fortune = "you will travel to the Maldives and have fresh coconut water"
elif userZodiac == "scorpio":
    fortune = "you will get fired"
elif userZodiac == "sagittarius":
    fortune = "you will finally buy the unicorn co-op ice cream"
elif userZodiac == "capricorn":
    fortune = "you will be the most successful person to ever exist and become the architect of the 8th world wonder"
elif userZodiac == "aquarius":
    fortune = "you will get a very good bonus on this day"
elif userZodiac == "pisces":
    fortune = "you will become a taxi driver and drive the Queen of England to Scotmid to get tomatoes, milk, and bread"
else:
    fortune = "something unexpected will happen… be ready!"

# Print result
print("On " + userDate + ", " + userName + " will " + fortune + " because they are a " + userZodiac + ".")
