#3-4 1이 될 때까지(30분/30분)->아니 내 논리 완벽한데 왜 안되지
## 안 완벽하니까 안되지 ㅎ.... 크게 나누는 법 공부

n,k=map(int, input().split())
count=0
while n>=k:
    if (n%k)==0:
        count+=1
        n//=k
        print(count,2)
    else:
        count+=(n%k)
        n-=(n%k)
        print(count,1)

if n>1:
    count+=(n-1)
print(count)
