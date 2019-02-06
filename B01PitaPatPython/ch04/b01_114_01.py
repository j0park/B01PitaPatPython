#ch4 page 114
# 연월일 합하여 출력
import time
now= time.time()
thisYear = int(1970 + now//(365*24*3600))
print("올해는 "+str(thisYear)+"입니다.")

age=int(input("올해 몇살 이에요? "))
print("2050년에는 "+str(age+2050-thisYear+1)+"살 이시군요")