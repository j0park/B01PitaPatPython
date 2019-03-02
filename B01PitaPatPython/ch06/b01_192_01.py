#ch6 page 192 연습문제
#1 2- 100 모든 짝수 출력
#변스 선언
i=0
# 반복문
for i in range(100):
    if (i % 2 ) ==0: # 짝수여부 확인
        print(i,end=" ") #출력

print(" ")
#2 복리 이자 7% 1,000만 저축  2,000만 되는 해
year=0 #변수선언
balance = 1000

while balance <= 2000 :
    year= year+1
    interest = balance *0.07
    balance = interest + balance
print(year,"년이 걸립니다.")

#3 출력 예상값
n=1234
sum=0
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
    print(digit, sum,n)
print(sum)  #123 +12+1 = 136