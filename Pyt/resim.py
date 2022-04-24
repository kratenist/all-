import turtle
turtle.speed(20)
turtle.pensize(5)

turtle.forward(300)
turtle.backward(600)
turtle.left(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(300)

turtle.color("red")
turtle.circle(-90)
turtle.color("black")
turtle.right(90)
turtle.forward(600)
turtle.left(90)
turtle.color("red")
turtle.circle(90)
turtle.color("black")
turtle.backward(300)


turtle.right(90)
turtle.backward(300)

turtle.color("red")
turtle.right(90)
turtle.backward(150)
turtle.right(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(300)
turtle.backward(150)
turtle.circle(75)
turtle.left(90)
turtle.forward(150)
turtle.backward(75)
turtle.left(90)
turtle.forward(73)
turtle.backward(146)
turtle.penup()
turtle.goto(0,0)

#YARIM DAİTE
"""
from turtle import *
import math

speed(2)
shape("triangle")
color("red")

for i in range(12):
	pendown()
	circle(120, 180)  # yarım daire çizelim
	penup()
	right(30)
	goto(0,0)


for a in range(12):
	pendown()
	circle(120, -180)  # yarım daire çizelim
	penup()
	right(30)
	goto(0,0)
		
exitonclick()

"""



#doldurma
"""
import turtle
pencere=turtle.Screen()
tosbaga = turtle.Turtle()
tosbaga.shape("turtle") #"arrow", "turtle", "circle", "square", "triangle", "classic" değerlerinden birini verebiliriz
tosbaga.color("green","#0000FF") # renk adını veya hex ("#00FF00") değerini yazabiliriz
tosbaga.pensize(3) # çizgi kalınlığı

tosbaga.begin_fill() #dolguya başla

for i in range(8):
	tosbaga.right(45)
	tosbaga.circle(50)

tosbaga.end_fill() # dolguyu bitir

pencere.exitonclick()
"""
#KARE ŞEKİL
"""
from turtle import *
pensize(2)
speed(50)
color("pink")
for i in range(36):
     forward(100)
     backward(100)
     left(15)
 
color("orange")
setpos(100,100)
for i in range(36):
     forward(100)
     backward(100)
     left(15)
 
color("yellow")
goto(-100,100)
for i in range(36):
     forward(100)
     backward(100)
     left(15)
 
color("blue")
goto(-100,-100)
for i in range(36):
     forward(100)
     backward(100)
     left(15)
 
color("green")
goto(100,-100)
for i in range(36):
     forward(100)
     backward(100)
     left(15)
done()
 
"""







#ŞEKİLKE
"""
a = turtle.Turtle()
a.color("blue")
a.pensize("1")
a.speed(500)
for i in range (669):
    a.forward(200)
    a.left(523)
    a.color("red")
    a.circle(123)
    a.color("blue")
    a.forward(100)
    a.right(-123)
    a.backward(90)
    a.right(90)
    a.forward(90)
    a.left(120)
    
"""


#ARABA
"""
turtle.speed(20)
turtle.pensize(5)

turtle.forward(300)
turtle.backward(600)
turtle.left(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(300)

turtle.color("red")
turtle.circle(-90)
turtle.color("black")
turtle.right(90)
turtle.forward(600)
turtle.left(90)
turtle.color("red")
turtle.circle(90)
turtle.color("black")
turtle.backward(300)


turtle.right(90)
turtle.backward(300)

turtle.color("red")
turtle.right(90)
turtle.backward(150)
turtle.right(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(300)

"""
