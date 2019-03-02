#ch6 page 195 연습문제
import turtle # 라이브러리
import random

#기본세팅
t=turtle.Turtle()
t.shape("turtle")

#09 반복 10번
for i in range(10):
    r=random.randint(1,100)
    t.pendown()
    t.circle(r)
    t.penup()
    t.goto(r,r)

#10


for ii in range(10):
    t.fd(100)
    if ii % 2 == 0 :
        t.right(90)
    else:
        t.left(90)
    t.fd(20)
    if ii % 2 == 0 :
        t.right(90)
    else:
        t.left(90)
