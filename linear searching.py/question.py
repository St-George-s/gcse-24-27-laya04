#Create a Python program that meets the following requirements:
	#• Define a function calculate_discount(price, discount_percentage) that takes a price and a discount percentage as arguments.
	#• The function should return the discounted price.
#Call the function with different values and print the results.

def calculate_dicount(price, discount_percentage):
    discount= price*discount_percentage / 100
    discount_price = price - discount
    return discount_price

original_price = int(input("Enter the original price"))
discount1= int(input("Enter discount"))
print("original price was ", original_price, "the price after the discount ", discount1, "is ", discount_price)