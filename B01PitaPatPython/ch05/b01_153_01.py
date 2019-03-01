#ch5 page 153 연습문제 01~04

# if-else and if-else
#01 출력값   '20살이상
age=20
if age < 20 :
    print ("20살 미만입니다 .")
else :
    print("20살 이상입니다.")

#02 1번 연속 30이상 50이하
if age>= 30 and age <= 50 :
    print("30살이상 50살이하")
else :
    print("아니여")

#03 25도이상인 경우 반바지 추천
tempater = int(input("현재 온도를 입력하시오 "))
if tempater >=25 :
    print("반바지를 입으시오 ")
else :
    print("긴 바지를 입으시오")

#04 학생 시험점수 등급 구분
score5 = int(input("성적을 입력하시오 : "))
if score5 >= 90 :
    print("A학점입니다.")
elif score5 >= 80 :
    print("B학점입니다. ")
elif score5 >= 70:
    print("C학점입니다. ")
elif score5 >= 60 :
    print("D학점입니다. ")
else :
    print("F학점입니다. ")
