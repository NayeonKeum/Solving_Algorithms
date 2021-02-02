#a-21(+60분/40분)
#포기..
def printmap(mapp):
    for i in range(len(mapp)):
        for j in range(len(mapp)):
            print(mapp[i][j], end=' ')
        print()

def bfs_check(mapp):
    global l
    global r
    global checklist
    dx=[-1,0,1,0]
    dy=[0,1, 0, -1]
    for i in range(len(mapp)):
        for j in range(len(mapp)):
            if checklist[i][j]==0:
                for n in range(4):
                    nx=i+dx[n]
                    ny=j+dy[n]
                    if nx>len(mapp)-1 or nx<0 or ny>len(mapp)-1 or ny<0:continue
                    elif abs(mapp[nx][ny]-mapp[i][j])>=l and abs(mapp[nx][ny]-mapp[i][j])<=r:
                        checklist[nx][ny] = 1
                        checklist[i][j]=1
                    else:continue
            else:continue


def check_all_visited(visited):
    for i in range(len(visited)):
        for j in range(len(visited)):
            if visited[i][j]==0:
                return False
    return True


def dfs_find1(mapp,visited,start):
    global checklist
    global total#합
    global count#개수
    visited[start[0]][start[1]]=1
    if check_all_visited(visited) is True:
        #print("+"*15)
        #print(total, count)
        #이부분이 이상함...
        #####1. 여기 return 이 None으로 나옴..!
        return (total/count)
    else:
        total += mapp[start[0]][start[1]]
        count += 1
        dx=[-1, 0, 1, 0]
        dy=[0, 1, 0, -1]
        for i in range(4):
            nx = start[0] + dx[i]
            ny = start[1] + dy[i]
            if nx>len(mapp)-1 or nx<0 or ny>len(mapp)-1 or ny<0:continue
            elif visited[nx][ny]==0:
                dfs_find1(mapp, visited, [nx,ny])
            else:continue


def assign_avg(checklist, value):
    global mapp
    for i in range(len(checklist)):
        for j in range(len(checklist)):
            if checklist[i][j]==1:
                mapp[i][j]=value


n, l, r=map(int, input().split())
mapp=[]
for i in range(n):
    mapp.append(list(map(int, input().split())))

checklist=[[0 for _ in range(n) ]for _ in range(n)]#n by n checklist
visited=[[0 for _ in range(n) ]for _ in range(n)]


#전체 합
total=0
#전체 개수
count=0

#checklist에 조건에 맞으면 전부 1 넣어줌
bfs_check(mapp)
printmap(checklist)

#이거하면 한 묶음에서 가질 값(평균) 알려줌
value=dfs_find1(mapp, visited, [0, 0])
print(value)
#mapp에 직접 assign
assign_avg(checklist, value)
#printmap(mapp)

####2. 이걸 여러번 돌려야 하는 거잖아...그거 감당 안 될 것 같은데..

'''
2 20 50
50 30
30 40
'''


