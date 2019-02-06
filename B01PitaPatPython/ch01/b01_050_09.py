#Ch1. 연습문제(50p) - 9번

## 함수 가져오기
import turtle

# 거북이 함수 상속(생성)
t=turtle.Turtle()

# 거북이 포인터 지정
t.shape("turtle")
t.width(4)
# 색깔지정 원 그리기
t.color("black")
t.circle(100)
# 색없애고 180 이동  색 다시 켜고 원그리기 
t.up()
t.fd(210)
t.down()
t.color("red")
t.circle(100)

# 색없애고 뒤로 360 이동  색 다시 켜고 원그리기
t.up()
t.backward(420)
t.down()
t.color("blue")
t.circle(100)

# 색없애고 오른쪽 90도  이동30  색 다시 켜고 원그리기
t.up()
t.right(90)
t.fd(30)
t.down()
t.color("yellow")
t.circle(100)
#색없애고 왼쪽으로 90 방향 전환 180 이동 색켜고 원그리기
t.up()
t.left(90)
t.fd(210)
t.left(270)
t.down()
t.color("green")
t.circle(100)
