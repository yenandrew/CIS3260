#Write a program that prompts the user to enter the
#center and radius of a circle, and then displays the circle and its area, as shown
#in Figure 2.5.
import turtle
x, y = eval(input("Enter center coordinates"))
radius = eval(input("Enter radius"))

turtle.goto(x, y)
turtle.write(int(radius*radius*3.1415))
turtle.penup()
turtle.goto(x, y - radius)
turtle.pendown()
turtle.circle(radius)
turtle.hideturtle()
turtle.done()
