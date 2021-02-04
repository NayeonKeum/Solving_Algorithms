#a-24
n=int(input())
nlist=list(map(int, input().split()))
result=[]#[위치, 거리]
for g in nlist:
    l=0
    for others in nlist:
        l+=abs(g-others)
    result.append([g,l])
result.sort(key=lambda x:(x[1], x[0]))
print(result)
print(result[0][0])
'''
4
5 1 7 9
'''
