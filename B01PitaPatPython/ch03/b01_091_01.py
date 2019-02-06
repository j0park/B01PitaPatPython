#ch3 page 91 연습문제
#01 두개 정수 받아서 합 차 곱 평균 큰 수 작은수 구하기


# 변수
a1=int(input("첫째수를 입력 : "))
a2=int(input("둘째수를 입력 : "))
big=max(a1,a2)
smal=min(a1,a2)
avg = (a1+a2) /2

print ("두수의 합 :: ",a1+a2)
print ("두수의 차 :: ",a1-a2)
print ("두수의 곱 :: ",a1*a2)
print ("두수의 평균 :: ",avg)
print ("두수의 큰수: ",big)
print ("두수의 작은 :: ",smal)

#02 원기둥 부피 구하기
print("\n\n#02 원기둥 부피 구하기")
#변수
r3 = int(input("면적은 : "))
hi3 = int(input("높이는 : "))
v3= 3.14*(r3**2)*hi3
print ("면적 ",r3,"이고 높이 ",hi3,"인 원기둥의 부피는 ",v3,"이다")

