# Write a program that reads in an investment amount, the annual interest rate, and the number of years,
# and displays the future investment value using the following formula:

investmentAmount = float(input("Enter investment amount: "))
interestRate = float(input("Enter annual interest rate: ")) / 1200
numberOfMonths = int(input("Enter number of years: ")) * 12

future = investmentAmount * ((1 + interestRate) ** numberOfMonths)

future = round(future, 2)
future = str(future)

print("Accumulated value is "+ future)