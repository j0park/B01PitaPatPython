#ch6 page 168
# 반복문

import turtle
t=turtle.Turtle()
t.shape("turtle")

for count in range(3):
    t.fd(100)
    t.left(120)

t.penup()
t.fd(200)
t.pendown()

for count in range(4):
    t.fd(100)
    t.left(90)

t.penup()
t.goto(-200,-100)
t.pendown()

#도전 과제
for count in range(6):
    t.fd(100)
    t.left(360/6)
