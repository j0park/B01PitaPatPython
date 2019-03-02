#ch6 page 193 연습문제
#4
answer= int(input("3*9는 "))
while answer != 27:
    answer=int(input("3*9는 "))
#출력 및 입력 받기
#결과 보여주기
print("맞았습니다.")

#5
sum=0
answer=int(input("정수를 입력하시오"))
while answer != 0 :
    sum=sum + answer
    answer = int(input("정수를 입력하시오"))
print("합은", sum,"입니다.")

#6
import random #라이브러리
for i in range(3):
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    print("첫번째 주사위 = ",r1,"두번째 주사위 = ",r2)
