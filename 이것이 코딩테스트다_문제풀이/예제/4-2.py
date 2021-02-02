#4-2 시각(15분/15분)이해를 제대로 못함 문제->계산으로 풀려고 하니까 그르지 멍충아
N=int(input())
n=0
'''
if (N>=0)&(N<3):
    n=(N+1)*1575
elif (N>=3)&(N<13):
    n=N*1575+3600
elif (N>=13)&(N<23):
    n=(N-1)*1575+3600*2
else:
    n=(N-2)*1575+3600*3
print(n)
'''
for i in range(0,N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                n+=1
print(n)
    
    
