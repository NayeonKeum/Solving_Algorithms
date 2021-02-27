n, m=map(int, input().split())
nlist=[]
for _ in range(n):
    nlist.append(list(map(int, input().split())))
wantlist=list(map(int, input().split()))

def find_team(team, x):
    if team[x]!=x:
        team[x]=find_team(team, team[x])
    return team[x]

def union_team(team, a, b):
    a=find_team(team, a)
    b=find_team(team, b)
    if a<b:
        team[b]=a
    else: team[a]=b

team=[0]*(n+1)
for i in range(1, n+1):
    team[i]=i

# 상반 저장
for i in range(n):
    for j in range(i, n):
        if nlist[i][j]==1:
            union_team(team, i+1, j+1)

tf=-1
for i in range(len(wantlist)-1):
    if find_team(team,wantlist[i])!=find_team(team,wantlist[i+1]):
        tf=0
        break
    elif find_team(team,wantlist[i])==find_team(team,wantlist[i+1]):
        tf=1

if tf==0:print("NO")
elif tf==1: print("YES")

'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
'''





