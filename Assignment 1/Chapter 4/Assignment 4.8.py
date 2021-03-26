# (Sort three integers) Write a program that prompts the user to enter three integers
# and displays them in increasing order.

n1, n2, n3 = eval(input("Enter 3 integers separated by commas no spaces"))
if n1 > n2:
    n1, n2 = n2, n1
if n2 > n3:
    n2, n3 = n3, n2
if n1 > n2:
    n1, n2 = n2, n1

print("Sorted: " + str(n1) + " " + str(n2) + " " + str(n3))