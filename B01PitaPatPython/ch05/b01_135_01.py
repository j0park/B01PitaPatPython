#ch5 page 135

#함수 선언
import turtle

 # 거북이 객체 생성 및 등장
a5=turtle.Turtle()
a5.shape("turtle")
#이동 경로 감추기
a5.penup()
# 세값의 글자 표시 및 이동
a5.goto(100,100)
a5.write("거북이가 여기로 오면 양수 입니다.")
a5.goto(100,-100)
a5.write("거북이가 여기로 오면 음수 입니다.")
a5.goto(100,0)
a5.write("거북이가 여기로 오면 0 입니다.")
a5.goto(0,0)
# 거북이 라인 노출 대기
a5.pendown()

# 숫자 입력
s5=turtle.textinput("","숫자를 입력하 : ")
# 책예제
if int(s5)> 0 :
    a5.goto(100,100)
if int(s5) < 0 :
    a5.goto(100,-100)
if int(s5) == 0 :
        a5.goto(100,0)
# 혼자 한 것  IF ELSE 알려주고 IF를 세번 쓰다니
#if int(s5)> 0 :
#    a5.goto(100,100)
#else :
#    if int(s5) < 0 :
#        a5.goto(100,-100)
#    else :
#        a5.goto(100,0)
