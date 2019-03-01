#ch6 page 177 연습문제
# 반복문
#1 구구단 9단 출력

dan=int(input("원하는 단은 : "))

for i in range(1,10,1):
    print(dan,"*",i,"=",dan*i)

i=1
while i < 10:
    print(dan,"*", i, "=", dan * i)
    i=i+1

for i in range(1,10,1):
    for j in range(1, 10, 1):
        print("%s * %s = %s " % (j, i, i * j),end="   ")
    #   print(j, "*", i, "=", i * j, end="   ")
    print(" ")


