# The US Census Bureau projects population based on the
# following assumptions:
# One birth every 7 seconds
# One death every 13 seconds
# One new immigrant every 45 seconds
# Write a program to display the population for each of the next five years. Assume the
# current population is 312032486 and one year has 365 days. Hint: in Python, you
# can use integer division operator // to perform division. The result is an integer. For
# example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).
print ((312032486) + (4505142.857142857 + 700800 - 2425846.153846154) // 1 )

print ((312032486) + (2 * (4505142.857142857 + 700800 - 2425846.153846154)) // 1 )

print ((312032486) + (3 * (4505142.857142857 + 700800 - 2425846.153846154)) // 1 )

print ((312032486) + (4 * (4505142.857142857 + 700800 - 2425846.153846154)) // 1 )

print ((312032486) + (5 * (4505142.857142857 + 700800 - 2425846.153846154)) // 1 )