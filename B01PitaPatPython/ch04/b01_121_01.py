#ch4 page 121 연습문제 01 ~ 04
#01 수식오류

# print('나는'+12+'개의 사과를 먹었다. ')  # 정수는 스트링으로 변황해야 하니면 따로 찍던가
print('나는'+str(12)+'개의 사과를 먹었다. ')


#02 수식 결과갑
print('apple'+'grape')  # applegrape 합쳐짐
print('apple'*3) # appel 3번


#03  입력 문자열 중 처음 2글자와 마지막 2글자만 추출후 합쳐라
str_list=input("문자열을 입력하시오")
print(str_list[0:2]+str_list[-2:])

lenst=len(str_list)-2
print(str_list[0]+str_list[1]+str_list[lenst]+str_list[lenst+1])


#04 문자열 뒤 항중 하는 중
str4=input("문자열 입력하시오 ")
print(str4+"하는 중")

