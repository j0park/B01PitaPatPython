#ch5 page 148

# if-else and if-else
# login program
id4=["ilovepython",'123456']
id5=(input("아이디를 입력하시오 : "))
if id5 == id4[0] :
    id6 = (input("패스워드를 입력하시오 : "))
    if id6==id4[1] :
        print("환영합니다..")
    else:
        print("패스워드가 틀려요")
else :
    print("아이디를 찾을수 없습니다.")
