#ch3 page 93 연습문제 07~ 08

#07시간 구하기 구하기

print("\n\n#0정수 받아서 한자리식 합  구하기")
import time
fseconds=time.time()


print ("현재시 :: ",fseconds/60%60,fseconds/60/60/24/365//24) #분


#08 움직이는 물체의 운동에너지
print("\n\n##08 움직이는 물체의 운동에너지")
#변수
x11 = int(input("물체의 무게: "))
y11 = int(input("물체의 속도 : "))

va=1/2*x11*y11**2
print ("물체의운동 에너지  ",va)

