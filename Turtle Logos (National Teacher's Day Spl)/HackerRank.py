#HackerRank logo
import turtle
t = turtle.Turtle()
t.speed(5)
turtle.Screen().bgcolor("#100D2B")
t.penup()
t.backward(300)
t.pendown()
#Green Hex
t.color("#27B343")
t.pensize(5)
t.right(90)
t.begin_fill()
for i in range(6):
    t.forward(60)
    t.right(60)
t.end_fill()
#Special H
t.color("white")
t.penup()
t.left(90)
t.backward(85)
t.pendown()
t.pensize(1)
t.begin_fill()
t.left(45)
t.forward(20)
t.right(90)
t.forward(20)
t.right(135)
t.forward(6.14)
for i in range(3):
    t.left(90)
    t.forward(20)
t.right(90)
t.forward(16)
t.right(90)
t.forward(56)
t.left(90)
t.forward(6.14)
t.right(135)
t.forward(20)
t.right(90)
t.forward(20)
t.left(225)
t.forward(6.14)
for i in range(3):
    t.left(90)
    t.forward(20)
t.right(90)
t.forward(16)
t.right(90)
t.forward(56)
t.left(90)
t.forward(6.14)
t.end_fill()
t.penup()
t.left(90)
t.forward(85)
t.left(90)
t.forward(100)
t.write("HackerRank", move=False, align="left", font=("Arial", 72, "bold"))
t.forward(570)
t.left(90)
t.forward(25)
t.pendown()
#Green Box
t.color("#27B343")
t.begin_fill()
t.pensize(5)
for i in range(2):
    t.forward(75)
    t.right(90)
    t.forward(50)
    t.right(90)
t.right(45)
t.forward(15)
t.end_fill()
turtle.done()