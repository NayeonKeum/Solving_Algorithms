#5-11(15분/30분)
n,m=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

dx=[1,0,-1,0]#오른쪽이랑 아
dy=[0,1,0,-1]

def move(graph):
    global x
    global y
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if nx>n-1 or nx<0 or ny>m-1 or ny<0:
            continue
        elif graph[nx][ny]==1:
            x,y=nx,ny
            break


x,y=0,0
goal_x=n-1
goal_y=m-1
count=1


while True:
    if x==goal_x and y==goal_y:
        print(count)
        break
    else:
        print(x,y)
        count+=1
        move(graph)

