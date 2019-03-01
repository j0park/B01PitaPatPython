#ch6 page 169
# 반복문

import turtle
t=turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("","몇 각형을 원하시나요?:")
length1 = turtle.textinput("","한변 크기는 얼마인가요?:")
n=int(s)
len1=int(length1)

for i in range(n):
    t.fd(len1)
    t.left(360/n)
