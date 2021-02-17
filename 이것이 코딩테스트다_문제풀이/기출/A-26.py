#a-26
n=int(input())
clist=[]
for i in range(n):
    clist.append(int(input()))
clist.sort()
clist_sub=[0]
for i in range(len(clist)):
    clist_sub.append(clist_sub[i]+clist[i])
print(clist_sub)
clist_sub=clist_sub[2:]#맨 앞의 0과 초항은 제외
print(clist_sub)
print(sum(clist_sub))