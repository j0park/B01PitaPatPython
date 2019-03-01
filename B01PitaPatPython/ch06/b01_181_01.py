#ch6 page 181
# 반복문

sum=0
f1=int(input("숫자를 입력하시오 : "))
sum = sum + f1
answer1 = input("계속?(Yes/No) : ")

while answer1 =='yes':
    f1 = int(input("숫자를 입력하시오 : "))
    sum=sum+f1
    answer1=input("계속?(Yes/No) : ")
print("합계는 : ",str(sum))
