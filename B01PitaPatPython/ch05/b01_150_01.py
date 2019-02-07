#ch5 page 150

# if-else and if-else
#  도형 그리기
import turtle
#선언부
t=turtle.Turtle()
t.shape("turtle")
s=turtle.textinput("","도형을 입력하시오")

if s == "사각형" :
    s= turtle.textinput("","가로:")
    w=int(s)
    s = turtle.textinput("", "세로:")
    h=int(s)
    t.fd(w)
    t.left(90)
    t.fd(h)
    t.left(90)
    t.fd(w)
    t.left(90)
    t.fd(h)

options1=["사각형","삼각형","원"]
options2=[int(90),int(120),int(0)]
#기초 함수
a5=turtle.Turtle()
a5.shape("turtle")
#입력받기
a51 = turtle.textinput("","도형을 입력하시오") ## 따옴표가 빠져서 처리가 안되었음
#판단후 그리기
a52 = int(turtle.textinput("", " 가로값을 입력하시오"))
#사각형 그리기
if a51 == options1[0]:

    a53 = int(turtle.textinput("", "세로값을 입력하시오"))
    a5.fd(a52)
    a5.left(options2[0])
    a5.fd(a53)
    a5.left(options2[0])
    a5.fd(a52)
    a5.left(options2[0])
    a5.fd(a53)

elif a51 == options1[1]:
    a5.fd(a52)
    a5.left(options2[1])
    a5.fd(a52)
    a5.left(options2[1])
    a5.fd(a52)
# 원 그리기
elif a51 == options1[2]:
    a5.circle(a52)
else :
    print("에러.")
