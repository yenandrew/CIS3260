import turtle

radius = eval(input("Enter radius (100 works well here)"))
turtle.pensize(25)
turtle.color("blue")
turtle.penup()
turtle.goto(-150,-25)
turtle.pendown()
turtle.circle(radius)
turtle.color("black")
turtle.penup()
turtle.goto(-0,-25)
turtle.pendown()
turtle.circle(radius)
turtle.color("red")
turtle.penup()
turtle.goto(150,-25)
turtle.pendown()
turtle.circle(radius)
turtle.color("yellow")
turtle.penup()
turtle.goto(-55,-75)
turtle.pendown()
turtle.circle(radius)
turtle.color("green")
turtle.penup()
turtle.goto(55,-75)
turtle.pendown()
turtle.circle(radius)
turtle.done()