#a-25
n=int(input())
stages=list(map(int, input().split()))
level=[0]*(n+2)#0부터 n+1번째까지 stage1은 1번째 index의 [인원수]
for s in stages:
    level[s]+=1

per=[[]for _ in range(n+2)]#[index,per]
for i in range(len(level)):
    if sum(level[i:])==0:
        per[i]=[i,0]
    else:
        per[i]=[i,level[i]/sum(level[i:])]

per=per[1:-1]
per.sort(key=lambda x:(-x[1], x[0]))
print(per)
perlist=[]
for p in per:
    perlist.append(p[0])
print(perlist)
'''
5
2 1 2 6 2 4 3 3
'''