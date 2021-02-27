
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

g=int(input())
p=int(input())

team=[0]*(g+1)

for i in range(1, g+1):
    team[i]=i

result=0
for _ in range(p):
    data=find_team(team, int(input()))
    if data==0:break
    union_team(team, data, data-1)
    result+=1

print(result)
"""
4
3
4
1
1

4
6
2
2
3
3
4
4
"""