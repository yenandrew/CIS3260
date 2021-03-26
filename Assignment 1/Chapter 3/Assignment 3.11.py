# Write a program that prompts the user to enter a four-digit integer and displays the number in reverse order.
number = str(input("Input number to be reversed"))
numList = list(number)
numList.reverse()
print(numList)
