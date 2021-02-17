#a-33.
n=int(input())
t=[]
p=[]
dp=[0]*(n+1)
max_value=0
for _ in range(n):
    x,y=map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1,-1,-1):
    time=t[i]+i
    if time<=n:
        dp[i]=max(p[i]+dp[time],max_value)
        max_value=dp[i]
    else: dp[i]=max_value
print(max_value)




'''
mlist=[]
for _ in range(n):
    mlist.append(list(map(int, input().split())))

profit=[0]*n

max_list=[]
for index in range(len(mlist)):
    i=index
    e = 0
    while True:
        if i+mlist[i][0]<n:
            profit[i+mlist[i][0]]=max(profit[i+mlist[i][0]],mlist[i][1]) # 어떤 날짜의 최대 이익
            i += mlist[i][0]
            e += profit[i]
        else:break
    max_list.append(e)

print(profit)
print(max_list)
'''
'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

'''

