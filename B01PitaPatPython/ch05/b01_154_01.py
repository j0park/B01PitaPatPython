#ch5 page 154 연습문제 05~07

# if-else and if-else

#05 난수 사용 1~100 숫자로 뺄셈 문제   '20살이상
#import
import random
#상수 2개
a1=random.randint(1,100)
a2=random.randint(1,100)
print(str(a1),"-",str(a2),"=",end=' ')
s5=int(input(""))

if a1-a2 == s5 :
    print("맞았습니다.")
else :
    print("틀렸습니다. 정답은",a1-a2,"입니다.")

#06 정수 입력받아 비교하기
a6=int(input("정수를 입력하시오"))
if (a6 % 2 == 0 and a6 % 3 == 0) :
    print("2와 3으로 나누어 떨어 집니다..")
else :
    print("2와 3으로 나누어 떨어지지 않습니다.")

#07 복권번호
import random
a7= int(input("복권번호를 입력하시오(0에서 99사이) : "))
a71 = (a7 // 10)
a72 = (a7 % 10)
lottery = random.randint(0,99)
lottery1 = lottery // 10
lottery2 = lottery %10

if (a71 == lottery1 or a71 == lottery2 ) and (a72 == lottery1 or a72 == lottery2 ) :
    print("당첨번호는 ",str(lottery),"입니다")
    print("상금은 100만원입니다")
elif (a71 == lottery1 or a71 == lottery2 ) or (a72 == lottery1 or a72 == lottery2 ):
    print("당첨번호는 ",str(lottery),"입니다")
    print("상금은 50만원입니다")
else :
    print("당첨번호는 ", str(lottery), "입니다")
    print("상금은 없습니다.")

