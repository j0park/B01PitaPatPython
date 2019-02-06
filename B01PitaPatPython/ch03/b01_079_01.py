#ch3 page 79 
#coffe gmv
# 판매개수 및 가격
am_num = 10
am_pri=2000
lt_num=20
lt_pri=3000
cp_num=30
cp_pri=3500
sale=am_num*am_pri+lt_num*lt_pri+cp_num*cp_pri
un_co=100000
# 판매 현황
#am_num = int(input("아메리카노 판매 개수는 : "))
#lt_num = int(input("카페라떼 판매 개수는 : "))
#cp_num = int(input("카포치노 판매 개수는 : "))
#sale=am_num*am_pri+lt_num*lt_pri+cp_num*cp_pri

print ("아메리카노 판매 개수 : ",am_num,"\n카페라떼 판매 개수 : ",lt_num)
print("카포치노 판매 개수 : ",cp_num,"\n 총 판매매출은 ",
     sale,"입니다.")
print("판매 이익은 ",sale-un_co,"입니다.")
