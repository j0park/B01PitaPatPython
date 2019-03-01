#ch6 page 172
# 반복문

n = int(input("정수를 입력하시오 : "))
i2=1
for i in range(1,n+1,1):
    i2=i*i2
print(n,"!은", i2,"이다")