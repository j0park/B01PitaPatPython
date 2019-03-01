#ch6 page 178
# 반복문
# 5번 반복


import turtle
t=turtle.Turtle()
t.shape("turtle")

for i in range(1,6,1):
    t.fd(50)
    t.left(144)


i=1
while i < 6:
    t.fd(150)
    t.right(144)
    i=i+1

