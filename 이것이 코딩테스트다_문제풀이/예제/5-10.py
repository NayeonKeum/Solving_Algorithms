#5-10(36/30분)
from collections import deque
n,m=map(int,input().split())
graph=[]
for i in range(n):
    listy=list(map(int, input()))#스플릿을 안하는겨
    graph.append(listy)


def bfs(graph, start):#한 개 돌 때
    dx=[1,0,-1,0]#오른쪽 부텀 시계 방향
    dy=[0,1,0,-1]

    x=start[0]
    y=start[1]
    queue=deque([[x,y]])
    graph[x][y]=1
    #print(queue)
    
    while queue:
        v=queue.popleft()
        x=v[0]
        y=v[1]
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if nx>n-1 or nx<0 or ny>m-1 or ny<0: continue
            elif graph[nx][ny]==0:
                queue.append([nx,ny])
                graph[nx][ny]=1
        


def find1(graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j]==0:
                return i,j
    return False




count=0
while True:
    if not find1(graph): break
    else:
        count+=1
        bfs(graph,find1(graph))
print(count)
    
