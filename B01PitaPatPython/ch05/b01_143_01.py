#ch5 page 143

# 동전 던지기

# 라이브러리 추가
import random

print("동전 던지기 게임을 시작합니다.")
coin = random.randrange(2)
if coin == 0 :
    print("앞면이니다.")
else :
    print("뒷면입니다.")
print("게임이 종료되었습니다.")


print("주사위  던지기 게임을 시작합니다.")
bees = random.randrange(6)
print("주사위 ",bees+1,"이(가) 나왔습니다.")
