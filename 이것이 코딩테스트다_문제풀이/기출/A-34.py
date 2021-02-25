n=int(input())
slist=list(map(int, input().split()))

slist.reverse()
dp=[1]*(n+1)

for i in range(n):
    for j in range(0,i):
        if slist[j]<slist[i]:
            dp[i]=max(dp[i], dp[j]+1)

print(n-max(dp))
print(slist)
print(dp)















'''
#엉터리
i=-1
count=0
while i<n-1:
    i+=1
    if slist[i]<slist[i+1]:
        del slist[i]
        n-=1
        count+=1
        i-=1
    else:continue


print(count)
print(slist)
'''
'''
7
15 11 4 5 8 5 2 4
'''