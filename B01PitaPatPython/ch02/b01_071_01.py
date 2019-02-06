#ch3 page 78 
#n각형 거북이 그림 그려

import turtle
a3=turtle.Turtle()
a3.shape("turtle")
side3 = int(input(" 몇 각형 그림을 ?"))
a3.up()
a3.goto(0,-270)
a3.speed(side3)

for i2 in range(side3) :
    a3.down()
    #a3.speed(side3)
    for  i in range(side3):
        a3.down()
        a3.fd(20)
        a3.left(360//side3)
        a3.up()
        #a3.fd(1)
    side3=side3-1
    print("지금 ",side3,"각형 그리는중....")
    #90 ~ 73
    #72 ~ 61
    #60 ~ 52
    #51 ~ 46
    #45 ~ 40 36 33 32 30 27 25 22 21 



