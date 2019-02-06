#ch5 page 141

# 윤년 파악
year5 =int(input("연도를 입력하시오 : "))

if ((year5 % 4 == 0 ) and (year5 % 100 != 0) ) or (year5 % 400 ==0):
    print (year5,"년은 윤년 입니다.")
else :
    print (str(year5)+"년은 윤년이 아닙니다.")


