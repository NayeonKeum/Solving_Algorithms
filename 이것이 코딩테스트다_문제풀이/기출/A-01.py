#a-01(17분/30분)-> 잘못 이
n=int(input())
data=list(map(int, input().split()))
index=n-1
remain=n
group=0
data.sort()
while True:
    if remain>=data[index]:
        group+=1
        remain-=data[index]
        index-=data[index]
    else: break
print(group)
