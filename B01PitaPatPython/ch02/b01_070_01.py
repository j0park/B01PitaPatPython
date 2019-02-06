#ch2 page 69 연습문제 04 ~ 06
#04 거북이 그림 그려
import turtle
a2=turtle.Turtle()
radis=50
a2.shape("turtle")

a2.goto(0,0)
a2.circle(radis)
a2.up()

a2.goto(100,0)
radis=radis+20
a2.down()
a2.circle(radis)

a2.up()
a2.goto(200,0)
radis=radis+20
a2.down()
a2.circle(radis)


#04 거북이 그림 그려

##int(input("한변길이를 입력하세요"))
a2.up()
a2.goto(-200,-100)
a2.down()
a2.fd(100)
a2.left(120)
a2.fd(100)
a2.left(120)
a2.fd(100)
a2.up()

#05 변수 사용
side2 = 200
a2.up()
a2.goto(50,-50)
a2.down()
a2.fd(side2)
a2.left(120)
a2.fd(side2)
a2.left(120)
a2.fd(side2)
a2.up()

