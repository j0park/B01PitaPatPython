#ch5 page 149

# if-else and if-else
# soccer  program
import random

options=["왼쪽","중앙","오른쪽"]
computer_choice = random.choice(options)
user_choice = input("어디를 수비하시겠어요?(왼쪽,중앙,오른쪽)  : ")

if computer_choice == user_choice :
    print("수비에 성공하였습니다.")
else :
    print("패널티킥이 성공하였습니다.")
#
#goal5=random.choice(["왼쪽","중앙","오른쪽"])
#id5=(input("어디를 수비하시겠어요?(왼쪽,중앙,오른쪽) 입력하시오 : "))
#if id5 == goal5 :
#    print("공을 막아서 패널티킥이 실패하였습니다...공격도", goal5, "...")
#else :
#    print("공을 못 막아서 패널티킥이 성공하였습니다...공격은", goal5, "...")


