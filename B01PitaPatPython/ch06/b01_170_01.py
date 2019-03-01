#ch6 page 170
# 반복문

import turtle
import random
t=turtle.Turtle()
t.shape("turtle")

#s = turtle.textinput("","몇 각형을 원하시나요?:")
#length1 = turtle.textinput("","한변 크기는 얼마인가요?:")
#n=int(s)
#len1=int(length1)

for i in range(30):
    len1 = random.randint(1, 100)
    t.fd(len1)
    angle1 = random.randint(-180, 180)
    t.left(angle1)

#도전 과제
for i in range(30):
    len1 = random.randint(1, 100)
    t.fd(len1)
    angle1 = random.randint(1, 4)
    t.left(angle1*90)
