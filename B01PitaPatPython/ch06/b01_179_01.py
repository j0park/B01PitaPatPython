#ch6 page 179
# 반복문

colors=["red","purple","blue","green","yellow","orange"]

import turtle
t=turtle.Turtle()
t.shape("turtle")
t.speed(0)
turtle.bgcolor("black")
t.width(3)

for i in range(10,160,1):
    t.color(colors[i%6])
    t.fd(i*3)
    t.left(89)

t.penup()
i=10
t.goto(0,0)
t.pendown()
while i < 161:
    t.color(colors[i%6])
    t.fd(i*4)
    t.right(89)
    i=i+1

