# Write a program that plays the popular scissor-rockpaper game. (A scissor can cut a paper, a rock can knock a scissor, and a paper can
# wrap a rock.) The program randomly generates a number 0, 1, or 2 representing
# scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
# 2 and displays a message indicating whether the user or the computer wins, loses,
# or draws.

import random
from random import randint

list = ["scissors","rock","paper"]

computer = randint(0,2)

ans = list[computer]

attempt = False

while attempt == False:

    player_in = int(input("scissors(0) rock(1), paper(2) ?"))

    if player_in == computer:

        print("Draw: The computer is", ans, " You: ", player_in )

    elif player_in == 1:

        if computer == 2:

            print("You lose: The computer is", ans, " You: rock")

        else:

            print("You win: The computer is", ans, " You: rock")

    elif player_in == 2:

        if computer == 0:

            print("You lose: The computer is", ans, " You: paper")

        else:

            print("You win: The computer is", ans, " You: paper")

    elif player_in == 0:

        if computer == 1:

            print("You lose: The computer is", ans, " You: scissors" )

        else:

            print("You win: The computer is", ans, " You: scissors")

    attempt = True

