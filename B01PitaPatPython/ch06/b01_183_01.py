#ch6 page 183
# 반복문
import random

times=0
guess = 0
answer=random.randint(1,100)
limit=2

print("1 부터 100 사이의 숫자를 입력하시오")

while (guess != answer and times <limit):
    guess = int(input("숫자를 입력하시오 : "))
    times=times+1
    if( guess <  answer):
        print(times,"번째 시도 - 낮음")
    elif(guess > answer):
        print(times,"번째 시도 - 높음")
    if(times==limit):
        print("횟수를 다 사용했습니다.")

if guess==answer:
    print("축하합니다. 시도 횟수",times)
else:
    print("정답은 ",answer)