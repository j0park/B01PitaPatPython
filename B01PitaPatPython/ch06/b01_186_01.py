#ch6 page 186
# 반복문
bread1=["호밀빵","위트","화이트"]
meat1=["미트볼","소시지","닭가슴살"]
vergitabl1=["양상추","토마토","오이"]
source1=["마요네즈","허니 머스타드","칠리"]

times=1
for b in bread1:
    for m in meat1:
        for v in vergitabl1:
            for s in source1:
                print(times,"째 조합 : ",end=" ")
                print(b+"+"+m+"+"+v+"+"+s)
                times=times+1