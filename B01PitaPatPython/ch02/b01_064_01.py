#Ch2 Page 64
# 집그리기
import turtle
a1=turtle.Turtle()

size1 = int(input("집 크기를 입력하세요 : "))
print ("이제 그립니다.")
a1.fd(size1) #밑변
a1.left(120)
a1.fd(size1)   #우변
a1.left(120)
a1.fd(size1) # 좌변

a1.left(30)  #아래로
a1.fd(size1) #좌변
a1.left(90)
a1.fd(size1) #밑면
a1.left(90)
a1.fd(size1) #우변
a1.left(90)
print ("다  그렸다.")

#창문 프레임
a1.up()
a1.fd(size1/3*2)
a1.left(90)
a1.fd(size1/3)
a1.down()
a1.fd(size1/3)
a1.left(90)
a1.fd(size1/3)
a1.left(90)
a1.fd(size1/3)
a1.left(90)
a1.fd(size1/3)
a1.left(90)

a1.up()
a1.fd(size1/3/2)
a1.left(90)
a1.down()
a1.fd(size1/3)
a1.backward(size1/3/2)
a1.left(90)
a1.fd(size1/3/2)
a1.backward(size1/3)
