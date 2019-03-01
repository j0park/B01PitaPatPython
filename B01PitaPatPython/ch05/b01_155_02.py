import turtle
import math
t = turtle.Turtle()
t.shape("turtle")

#좌표평면그리기
t.penup()
t.goto(-300,0)
t.pendown()
t.goto(300,0)

t.penup()
t.goto(0,-300)
t.pendown()
t.goto(0,300)

#원의 중심좌표와 반지름입력
x1 = int(turtle.numinput("input", "큰 원의 중심좌표 x1: "))
y1 = int(turtle.numinput("input", "큰 원의 중심좌표 y1: "))
r1 = int(turtle.numinput("input", "큰 원의 반지름: "))
x2 = int(turtle.numinput("input", "작은 원의 중심좌표 x2: "))
y2 = int(turtle.numinput("input", "작은 원의 중심좌표 y2: "))
r2 = int(turtle.numinput("input", "작은 원의 반지름: "))

#원 그리기
t.penup()
t.goto(x1, y1-r1)
t.pendown()
t.circle(r1)

t.penup()
t.goto(x2, y2-r2)
t.pendown()
t.circle(r2)

#두 원사이의 관계구하기
check = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

if check < r1 - r2 :
    turtle.write("작은원이 큰원의 내부에 있습니다")
elif check > r1 + r2 :
    turtle.write("작은원이 큰원의 외부에 있습니다")
else :   
    turtle.write("작은원과 큰원이 겹칩니다")
input("아무키나 누ㅡㄹ시오: ")