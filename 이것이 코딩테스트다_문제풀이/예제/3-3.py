#3-3 숫자 카드 게임(7분/30분)
n,m=map(int, input().split())
miny=0
for i in range(0,n):
    data=map(int, input().split())
    miny=max(miny, min(data))
print(miny)
    
