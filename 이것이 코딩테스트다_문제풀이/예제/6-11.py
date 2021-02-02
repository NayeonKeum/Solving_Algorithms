#6-11
n=int(input())
dic={}
for i in range(n):
    k,v=map(str, input().split())
    dic[k]=int(v)

def settings(dic):
    return dic[1]
result=sorted(dic, key=settings, reverse=True)
#or settings 대신 key=lambda s:s[1]
for r in result:
    print(r, end=' ')