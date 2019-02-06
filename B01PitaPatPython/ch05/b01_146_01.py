#ch5 page 146

# 종달새 노래하기

# 라이브러리 추가
import random

print("종달새 노래 시키기 게임을 시작합니다.")

time1 = random.randint(1,24)
sunny1 = random.choice([True,False])

print("지금 시각은 ",time1,"시입니다.")
if sunny1 == True :
    print("날씨가 화창합니다.")
else :
    print("날씨가 흐립니다.")

#
if ((time1 >= 6 and time1 <= 9) or (time1 >= 14 and time1 <= 16)) and sunny1 == True :
    print("좋은 아침입니다. ")
    print("종달새가 노래 합니다.")
else :
    print(" 종달새는 노래하지 않습니다.")
