n,m=map(int, input().split())
mlist=[]
for _ in range(n):
    mlist.append(int(input()))
mlist.sort()
d=[10001]*(m+1)

d[0]=0
for i in range(n):
    for j in range(mlist[i], m+1):
        if d[j-mlist[i]]!=10001:
            d[j]=min(d[j], d[j-mlist[i]]+1)


if d[m]==10001:print(-1)
else: print(d[m])