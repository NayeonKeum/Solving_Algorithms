#3-2 큰 수의 법칙(23/20분, 문제 이해 부족)
n,m,k=map(int, input().split())
data=list(map(int, input().split()))
data.sort()
result=0
'''
while True:
    if m>=(k+1):
        m-=(k+1)
        result+=k*data[n-1]
        result+=data[n-2]
        print(result)
    else:
        result+=m*data[n-1]
        print(result)
        break
'''
#천재적인 나머지 연산자
a=(m//(k+1))*k#한 세트의 큰 수
b=m//(k+1)#한 세트의 작은 수
m%=(k+1)
c=m
result=data[n-1]*(a+c)+data[n-2]*b
print(result)
