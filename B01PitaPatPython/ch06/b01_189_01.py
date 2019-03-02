#ch6 page 189
# 반복문


import random
import sys


#인적사항
while True:
    name1=input("이름 : (종료하려면 엔터키)")
    if name1=="":
        sys.exit()

    ques1=input('무엇에 대하여 알고 싶은가요?')
    print(name1+"님","\"",ques1,"\"에 대하여 질문 주셨군요.")
    print("운명의 주사위를 굴려볼게요")
    number = random.randint(1, 8)
 #답주기
    if number == 1:
        print("네 확실합니다.")
    elif number ==2:
        print("전말이 좋은 것 같은데요.")
    elif number ==3:
        print("믿으셔도 됩니다.")
    elif number ==4:
        print("글쎄요 아닌것 같군요.")
    elif number ==5:
        print("한 점의 으심도 없이 맞습니다.")
    elif number ==6:
        print("그럼요, 명백히 올바른 선택을 했습니다.")
    elif number ==7:
        print("제답변은 No입니다.")
    else :
        print("나중에 다시 물어보세요")
