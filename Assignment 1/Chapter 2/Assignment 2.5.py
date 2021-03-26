# Write a program that reads the subtotal and
# the gratuity rate and computes the gratuity and total. For example, if the user
# enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
# as the gratuity and 11.5 as the total

subTotal = float(input("Enter the subtotal"))
rate = float(input("Enter the gratuity rate: "))
subTotal = float(subTotal)
rate = float(rate)
gratuity = subTotal * (rate / 100)
total = subTotal + gratuity
total = round(total, 2)
total = str(total)
gratuity = round(gratuity, 2)
gratuity = str(gratuity)
print("The gratuity is " + gratuity + " and the total is " + total)
