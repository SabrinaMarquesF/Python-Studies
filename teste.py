import turtle

tela = turtle.Screen()
tela.bgcolor("white")
tela.title("Coração")

caneta = turtle.Turtle()
caneta.speed(10)
caneta.color("red", "pink")
caneta.penup()

caneta.goto(0, -150)
caneta.pendown()
caneta.begin_fill()
caneta.left(140)
caneta.forward(180)
caneta.circle(-90, 200)
caneta.setheading(60)
caneta.circle(-90, 200)
caneta.forward(180)
caneta.end_fill()

caneta.penup()
caneta.goto(0, 0)
caneta.color("white")
caneta.write("Love", align="center", font=("Arial", 40, "bold"))

caneta.hideturtle()
turtle.done()