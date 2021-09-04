#Linked in logo
import turtle
t = turtle.Turtle()
t.speed(5)
t.color("blue")
t.pensize(10)
t.begin_fill()
for i in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()
t.penup()
t.forward(100)
t.right(90)
t.forward(40)
t.color("white")
t.write("in", move=False, align="center", font=("Century Gothic", 180, "bold")) 
turtle.done()