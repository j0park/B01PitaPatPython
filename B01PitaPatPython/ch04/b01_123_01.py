#ch4 page 123 연습문제 08
#08 세개 좌표 입력 받고 거북이로 그리기 -- 리스트 기본 저장은 스트링이므로 만약 활용을
# 정수로 한다면 인트로 저장 하거나 인트로 형변환해야 함
fill4_list=[]
fill4=input("x1 : ")
fill4_list.append(int(fill4))
fill4=input("y1 : ")
fill4_list.append(int(fill4))
fill4=input("x2 : ")
fill4_list.append(int(fill4))
fill4=input("y2 : ")
fill4_list.append((int(fill4)))
fill4=input("x3 : ")
fill4_list.append((int(fill4)))
fill4=input("y3 : ")
fill4_list.append((int(fill4)))

import turtle

a4=turtle.Turtle()
a4.shape("turtle")
a4.goto((fill4_list[0]),(fill4_list[1]))
a4.fd(100)
a4.goto((fill4_list[2]),(fill4_list[3]))
a4.fd(100)
a4.goto((fill4_list[4]),(fill4_list[5]))
a4.fd(100)
