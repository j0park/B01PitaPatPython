#Ch2 Page 60
# 변수활용하여 거북이 원그리기
# 라이브러리 추가
import turtle

radius=100

t=turtle.Turtle()

t.shape("turtle")
t.circle(radius)
t.fd(radius/3)
t.circle(radius-10)
t.fd(radius/3)
t.circle(radius-20)


radius=50
t.shape("turtle")
t.circle(radius)
t.fd(radius/3)
t.circle(radius-5)
t.fd(radius/3)
t.circle(radius-10)


t.up()
t.right(200)
t.down()
t.circle(radius)
t.circle(radius-10)
t.circle(radius-20)

radius=20
t.circle(radius)
t.circle(radius-5)
t.circle(radius-10)
