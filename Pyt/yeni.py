import turtle 

a = turtle.Turtle()
a.speed(50)
a.begin_fill()
a.left(90)
a.forward(300)
a.right(90)
a.forward(300)
a.right(90)
a.forward(300)
a.right(90)
a.forward(300)
a.color("blue")
a.left(90)
a.forward(300)
a.left(90)
a.forward(300)
a.left(90)
a.forward(300)
a.goto(0,0)
a.left(-45)
a.forward(425)

a.goto(0,0)
a.left(90)
a.backward(425)
a.right(90)
a.forward(425)
a.left(90)
a.forward(425)
a.backward(425)
a.left(45)
a.forward(302)
a.end_fill()
a.penup()


a.color("red")
a.goto(-200,0)
a.pendown()

a.right(90)
a.left(45)
a.forward(100)
a.backward(100)
a.right(45)
a.forward(100)
a.backward(200)
a.begin_fill()
a.circle(90)
a.left(90)
a.forward(185)
a.end_fill()

