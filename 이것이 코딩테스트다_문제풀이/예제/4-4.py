#4-4 게임개발(+40분/40분)class 쓸 수 있을 것 같은데 까먹음
# 잘 못함...왜지...
# 한참 고민하다 나온 결론은 초기화를 제대로 안했고, 토씨 하나 틀려서..(+,-)

def turnleft():
    global d
    d=(d+3)%4
    
def gostraight():
    global d
    global r
    global c
    if d==0:r-=1
    elif d==1:c+=1
    elif d==2:r+=1
    else:c-=1
    maze[r][c]=1
    
def goback():
    global d
    global r
    global c
    if d==0:r+=1
    elif d==1:c-=1
    elif d==2:r-=1
    else:c+=1

def Isback():
    global d
    global r
    global c
    global m
    global n
    nr=r
    nc=c
    if d==0:nr+=1
    elif d==1:nc-=1
    elif d==2:nr-=1
    else:nc+=1
    if (nr<0) or nr>(n-1) or (nc<0) or nc>(m-1):
        return False
    elif (maze[nr][nc]==0) is True:
        return True
    else: return False

    
def Isleft():
    global d
    global r
    global c
    global m
    global n
    nr=r
    nc=c
    if d==0:nc-=1
    elif d==1:nr-=1
    elif d==2:nc+=1
    else:nr+=1
    if (nr<0) or nr>(n-1) or (nc<0) or nc>(m-1):
        return False
    elif (maze[nr][nc]==0) is True:
        return True
    else: return False



def printmap(n,m,maze):
    for i in range(n):
        for j in range(m):
            print(maze[i][j], end=" ")
        print()


n,m=map(int, input().split())
r,c,d=map(int, input().split())
maze=[]
for i in range(n):
    maze.append(list(map(int, input().split())))
  
move=1
cnt=0
maze[r][c]=1
while True:
    #print(r,c)
    #print(cnt)
    if (cnt==4) is True:
        if Isback() is False:
            break
        else:
            goback()
            continue
    if Isleft() is True:
        turnleft()
        gostraight()
        move+=1
        cnt=0
    else:
        turnleft()
        cnt+=1

print(move)
#printmap(n,m,maze)










