#ch6 page 188
# 반복문

#라이브러리
import turtle

#객체 생성
t=turtle.Turtle()
t.shape("turtle")
t.color("red")


t.stamp()
move=30
for i in range(12):
    t.penup()
    t.fd(50)
    t.pendown()
    t.fd(25)
    t.penup()
    t.fd(15)
    t.stamp()
    t.home()
    t.penup()
    t.right(move)
    move=move+30

t.color("blue")

# 그리는
# 기준점(0.0)
for i in range(12):
     t.penup()
     t.fd(40)
     t.pendown()
     t.fd(100)
     t.penup()
     t.fd(40)
     t.stamp()
     t.penup()
     t.backward(180)
     t.right(360 / 12)
