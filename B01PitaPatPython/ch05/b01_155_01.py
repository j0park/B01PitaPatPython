#ch5 page 155 연습문제 08

# if-else and if-else

#08 두개의 원 정보 받아 포함여부 확인하기
#다른 소스 봐도 안됨 뭔가 놓친게 있음
#import
import turtle
import math

#입력받기
x1=int(input(" 큰원의 중심좌표 x1 : "))
y1=int(input(" 큰원의 중심좌표 y1 : "))
r1=int(input(" 큰원의 반지름 r1 : "))
x2=int(input(" 작은원의 중심좌표 x2 : "))
y2=int(input(" 작은원의 중심좌표 y2 : "))
r2=int(input(" 작은원의 반지름 r2 : "))

# X축 그리기
t=turtle.Turtle()

#두 점사이 거리 구하기
x_len = int(x2-x1)
y_len = int(y2-y1)
d8=math.sqrt((x_len**2)+y_len**2)
d81=(x_len**2+y_len**2)**0.5 # 출처 https://mathbang.net/138
print("d8",d8,"d81",d81, "x_len",x_len,"y_len",y_len,"x1",x1,"y1",y1,"x2",x2,"y2",y2)



# 포함여부 확인하기 https://m.blog.naver.com/dmswl2781/221238812044
t1=turtle.Turtle()
t1.color("yellow")
if d81 < r1 - r2:
    t1.write("작은원이 큰원의 내부에 있습니다")
elif d81 > r1 + r2:
    t1.write("작은원이 큰원의 외부에 있습니다")
else:
    t1.write("작은원과 큰원이 겹칩니다")

if r1>=r2  :
    # 큰원 그리기 https://chriskhj6296.tistory.com/64
    t=turtle.Turtle()
    t.pu()
    t.goto(x1 - r1, y1)
    t.pd()
    t.circle(r1)
    # 작은원 그리기 https://chriskhj6296.tistory.com/64
    t.pu()
    t.goto(x2 - r2, y2)
    t.pd()
    t.circle(r2)

    # 내것
    a8 = turtle.Turtle()
    a8.shape("turtle")
    a8.color("blue")
    a8.penup()
    a8.goto(x1 - r1, y1)
    a8.pendown()
    a8.circle(r1)
    a8.penup()
    a8.goto(x2 - r2, y2)
    a8.pendown()
    a8.circle(r2)


    # 두원의 위치 상태 구하기 출처 : https://chriskhj6296.tistory.com/64
    if (r1 - r2) > d8:
        t.write("#5두번째 원이 첫번째 원의 내부에 있습니다.\n")
        # 버그 0 0 100 20 20 10
    elif (r1 - r2) == d8 or (r1 + r2) == d8:
        t.write("#6두번째 원이 첫번째 원과 겹칩니다.\n")
    elif (r1 - r2) < d8 and (r1 + r2) > d8:
        t.write("#1두번째 원과 첫번째 원이 두점에서 만납니다.\n")
        # bug 0 0 40 40 40 20
    else:
        t.write("두번째 원이 첫번째 원과 겹치지 않습니다.\n")

# 두원의 위치 관계, 내접 , 외접  출처 https://mathbang.net/101
    if (r1-r2 < d81)  and (  d81 < r1 + r2 ):
        a8.goto(-100,-100) # bug 0 0 40 40 40 20
        a8.write("\n 큰원안에 작은원이 포함되지 않고 \n 작은원과 큰원이 만난다.#1")
    elif  d81 ==0 and x1==x2 and y1==y2 and r1==r2:
        a8.goto(-100, -100)
        a8.write(" \n 큰원안에 작은원이 포함된 \n 동심원이다.#6")
    elif r2 + r1 == d81 :
        a8.goto(-100,-100)
        a8.write(" \n 큰원안에 작은원이 포함되지 않고 \n 작은원과 큰원이 만난다.#2")
    elif r1 - r2 ==  d81  :
        a8.goto(-100, -100)
        a8.write("\n 큰원안에 작은원이 포함되고 \n 작은원과 큰원이 내접한다.#3")
    elif r2 + r1 < d81 and r1 - r2 < d81: # 0 0 40 90 90 20
        a8.goto(-100,-100)
        a8.write("\n 큰원안에 작은원이 포함되지 않고 \n 작은원과 큰원이 만나지 않는다..#4")
    elif  d81 < r1- r2 :
        a8.goto(-100,-100) # 0 0 100 20 20 10
        a8.write("\n 큰원안에 작은원이 포함되고 \n 작은원과 큰원이 만나지 않는다..#5")
    else :
        a8.write("에러")
else :
    print("다시 입력하시오")

input("아무키나 누ㅡㄹ시오: ")