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

n,m=map(int, input().split())

team=[0]*(n+1)

for i in range(1,n+1):
    team[i]=i

edges=[]
result=0
total=0

for _ in range(m):
    x, y, z=map(int, input().split())
    edges.append((z, x, y))

edges.sort()
for edge in edges:
    cost, a, b=edge
    total+=cost
    if find_team(team, a)!=find_team(team, b):
        union_team(team, a, b)
        result+=cost
print(total-result)

"""
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11

"""