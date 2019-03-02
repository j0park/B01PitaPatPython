#ch6 page 184
# 반복문
import random



while True:
    answer1 = random.randint(1, 100)
    answer2 = random.randint(1, 100)
    sum = answer2 + answer1
    print(answer1, "+", answer2, "= ",end=" ")
    guess = int(input())
    if( guess == sum):
        print("잘했어요!!")
    elif(guess != sum):
        print("다음번에는 잘 할 수 있죠?")
