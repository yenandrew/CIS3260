# Write a program that displays a random uppercase letter
# using the time.time() function.
import time

value = time.time()
value = round(value)
character = value%26+65
letter = chr(character)

print(letter)