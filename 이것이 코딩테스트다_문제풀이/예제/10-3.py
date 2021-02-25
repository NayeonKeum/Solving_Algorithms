n,m=map(int, input().split())
team=[0]*(n+1)

for i in range(1, n+1):
    team[i]=i

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

edges=[]
result=0

for _ in range(m):
    a, b, c=map(int, input().split())
    edges.append((c, a, b))

edges.sort()
for edge in edges:
    cost, a, b=edge
    if find_team(team, a)!=find_team(team, b):
        union_team(team, a, b)
        last=cost
        result+=cost

print(result-last)
"""
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""