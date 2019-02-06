#ch5 page 144

# 동전에 이미지 입혀 던지기

# 라이브러리 추가
import random
import turtle
a5 = turtle.Turtle()
screen5 = turtle.Screen()
image1=".\\c1.GIF"
image2=".\\c2.GIF"
screen5.addshape(image1)
screen5.addshape(image2)
a5.shape(image1)
a5.stamp()

print("동전 던지기 게임을 시작합니다.")
coin = random.randrange(2)
if coin == 0 :
    print("앞면이니다.")
    a5.shape(image1)
    a5.stamp()
else :
    print("뒷면입니다.")
    a5.shape(image2)
    a5.stamp()
print("게임이 종료되었습니다.")
