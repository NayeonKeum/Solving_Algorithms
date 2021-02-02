#a-20(38분/60분)
def print_map(mapp):
    for i in range(len(mapp)):
        for j in range(len(mapp)):
            print(mapp[i][j], end=' ')
        print()
def find_teacher(mapp):
    listy=[]
    for i in range(len(mapp)):
        for j in range(len(mapp)):
            if mapp[i][j]=='T':
                listy.append([i,j])
    return listy

def find_student(mapp):
    listy=[]
    for i in range(len(mapp)):
        for j in range(len(mapp)):
            if mapp[i][j]=='S':
                listy.append([i,j])
    return listy
#장애물 배치하기
def put_obstacles(mapp, candidate):
    for can in candidate:
        for i in range(len(mapp)):
            for j in range(len(mapp)):
                if can[0]==i and can[1]==j:
                    mapp[i][j]='O'
    return mapp
# spot
def bfs_spot(mapp):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    for tcr in find_teacher(mapp):#[0,1]이런 식
        for i in range(4):
            nx = tcr[0]
            ny = tcr[1]
            while True:
                nx+= dx[i]
                ny+= dy[i]
                if nx>len(mapp)-1 or nx<0 or ny>len(mapp)-1 or ny<0:
                    break
                elif mapp[nx][ny]=="O":
                    break
                elif mapp[nx][ny]=="S":
                    return "NO"
                else:pass

    return "YES"

#맵 복사해서 원래꺼 지키기
def copy_map(mapp):
    mapy=[[]for _ in range(len(mapp))]
    for i in range(len(mapp)):
        for j in range(len(mapp)):
                mapy[i].append(mapp[i][j])
    return mapy


n=int(input())
mapp=[]
for i in range(n):
    mapp.append(list(map(str, input().split())))

#장애물 놓을 위치 찾기 및 조합으로 갯수 찾기
obslist = []
for i in range(len(mapp)):
    for j in range(len(mapp)):
        if mapp[i][j] == 'X':
            obslist.append([i, j])
from itertools import combinations
candidates=list(combinations(obslist,3))

for candidate in candidates:
    cnt=-1
    mapy=copy_map(mapp)
    #장애물 놓고
    mapy=put_obstacles(mapy, candidate)
    #print_map(mapy)
    if bfs_spot(mapy) == "NO":
        cnt=1
    else:
        cnt=0
        print(bfs_spot(mapy))
        break
if cnt==1: print("NO")
'''
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
'''