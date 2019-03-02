#ch6 page 196 연습문제
import turtle # 라이브러리
import random

#기본세팅
t=turtle.Turtle()
t.shape("turtle")


#11 반복 10번
t.color('red','yellow')
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos())<1:
        break
    t.end_fill()


#12 사인 그래프 그리기
import math
for x in range(0,360):
     t.goto(x,200*math.sin(x*3.14/180))