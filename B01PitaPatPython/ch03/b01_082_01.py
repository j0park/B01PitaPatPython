#ch3 page 82
# 자판기  구하

# 변수
inpc= int(input("투입한 돈은 : "))
itmc= int(input("물건 값 : "))
modc = inpc%itmc
mod500= modc//500
mod100=(modc%500)//100
mod50=(modc%100)//50
mod10=(modc%50)//10
print ("잔돈 :: ",modc)

print ("500원 잔돈 개수 :: ",mod500,"100원 잔돈 개수 :: ",mod100)
print (" 50원 잔돈 개수 :: ",mod50,"  10원 잔돈 개수 :: ",mod10)


