#3-1 거스름돈
'''
#500,100,50,10원 무한개
#개수 각각 a, b, c, d
def change(m):
    a=b=c=d=0
    while m>0:
        if m>500:
            m-=500
            a+=1
        elif m>100:
            m-=100
            b+=1
        elif m>50:
            m-=50
            c+=1
        else:
            m-=10
            d+=1
    print("거슬러 줘야할 동전의 개수 : ", a+b+c+d)
    print(a,b,c,d)

m=int(input("거슬러 줘야 할 돈 : "))
change(m)
'''
m=1260
n=0
coin_types=[500,100,50,10]
for coin in coin_types:
    n+=m//coin
    m%=coin
print(n)

    
