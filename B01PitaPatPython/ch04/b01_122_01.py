#ch4 page 122 연습문제 05 ~ 07
#05 기호와 문자 합 -- 리스트 배열을 이용
str50_list=input("기호를 입력하시오")
str51_list=input("중간에 삽입할 문자열을 입력하시오")

print(str50_list[0:1]+str51_list+str50_list[-1:])


#06  4개 숫자 리스트  합계계산 -- 리스트에 저장하고 스트링을 정수로 변환하여 합 그런데
# 리스트 형인 건 어떻게 알지? 스트링일수도 있잖아
str6_list=input("리스트(4개)")
print('리스스 숫자합 : ',int(str6_list[0])+int(str6_list[1])+int(str6_list[2])+int(str6_list[3]))
str6=input("리스트(4개)")
print('리스스 숫자합 : ',int(str6[0])+int(str6[1])+int(str6[2])+int(str6[3]), str6,int(str6)+1)

# 만약 INT로 넣을 려면 int함수 사용

#07  세가지 색 저장 리스트 저장 하나씩 꺼내어
fill4_list=[]
fill4=input("첫번째 색은 : ")
fill4_list.append(fill4)
fill4=input("두번째 색은 : ")
fill4_list.append(fill4)
fill4=input("세번째 색은 : ")
fill4_list.append(fill4)

import turtle

a4=turtle.Turtle()
a4.shape("turtle")
a4.fillcolor(fill4_list[0])
a4.begin_fill()
a4.down()

a4.circle(50)
a4.end_fill()
a4.up()
a4.fd(100)
a4.fillcolor(fill4_list[1])
a4.begin_fill()
a4.down()

a4.circle(50)
a4.end_fill()
a4.up()

a4.fd(100)
a4.fillcolor(fill4_list[2])
a4.begin_fill()
a4.down()
a4.circle(50)
a4.end_fill()