#ch6 page 194 연습문제
import turtle # 라이브러리

#7
#기본 세팅
t=turtle.Turtle()
ang=-90
t.shape("turtle")
t.color("blue")
#반복 for
for i in range(6):
    t.right(ang)
    t.fd(100); t.fd(-30);t.left(60);t.fd(30);t.fd(-30);t.right(120);t.fd(30);t.fd(-30);t.home()
    ang=ang+60

#8별그리기
t=turtle.Turtle()

t.home()
t.color("purple")
for j in range(36):
    for i in range(5):
        t.fd(50)
        t.right(144)
    t.left(10)

t.home()
t.color("black")
for j in range(36):
    for i in range(5):
        t.fd(150)
        t.right(144)
    t.left(10)


