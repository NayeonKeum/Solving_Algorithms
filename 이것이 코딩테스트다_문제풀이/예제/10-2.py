n,m=map(int, input().split())
nlist=[]

for _ in range(m):
    nlist.append(list(map(int, input().split())))


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

team=[0]*(m+1)

for i in range(1, m+1):
    team[i]=i

for i in range(m):
    cal= nlist[i][0]
    a=nlist[i][1]
    b=nlist[i][2]

    if cal==0:
        union_team(team, a, b)
    if cal==1:
        if find_team(team, a)==find_team(team, b):
            print("YES")
        else: print("NO")
"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1 
0 3 7
0 4 2
0 1 1
1 1 1
"""