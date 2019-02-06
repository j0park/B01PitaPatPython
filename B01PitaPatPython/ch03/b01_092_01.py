#ch3 page 92 연습문제 03~ 05

#03  정수 받아서 한자리식 합  구하기

print("\n\n#0정수 받아서 한자리식 합  구하기")
# 변수
a1=int(input("수를 입력 : "))


c2=a1- (a1%1000) #1000  
c3=a1 -c2 -(a1%100) #200
c4=a1-c2-c3-a1%10 #30
c5=a1%10
c1=(a1//100)//100
sum3=c2/1000+c3/100+c4/10+c5

print ("자리수의 합 :: ",sum3,c1)


#04 두점사이 거리  구하기
print("\n\n##04 두점사이 거리  구하기")
#변수
x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))

va=((x1-x2)**2+(y1-y2)**2)**0.5
print ("두점 사이의 거리는  ",va)


#05 거북이로 두점사이 거리  구한거 검증
print("\n\n##05 거북이로 두점사이 거리  구한거 검증")
#변수
import turtle
a3=turtle.Turtle()
a4=turtle.Turtle()

a3.up()
a3.goto(x1,y1)
a3.down()
a3.fd(x2-x1)
a3.left(90)
a3.fd(y2-y1)

a4.shape("turtle")
a4.up()
a4.goto(x1,y1)
a4.down()
a4.left(45)
a4.fd(va)


