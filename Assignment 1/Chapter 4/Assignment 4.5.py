#Write a program that prompts the user to enter an integer for
#today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
#prompt the user to enter the number of days after today for a future day and display the future day of the week.

today = eval(input("Enter today day (0-6 with 0 Being Sunday)"))
dayAfter = eval(input("Enter number of days since then"))

dayList = {0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}

print("Today is", dayList[today], "the days after is", dayList[(dayAfter+today)%7])

