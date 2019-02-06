#ch5 page 139
#함수 선언
import turtle


 # 거북이 객체 생성 및 등장
a5=turtle.Turtle()
a5.shape("turtle")

#거북이 크기 3배 확대
a5.shapesize(3,3)

# 숫자 입력


while  1 :
    s5 = turtle.textinput("", "명령을 입력하시오 : ")
    if s5 == "l" :
        a5.left(90)
        a5.fd(50)
    if s5 == "r" :
        a5.right(90)
        a5.fd(50)
