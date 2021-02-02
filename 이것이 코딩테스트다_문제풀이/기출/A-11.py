#a-11 
n=int(input())
k=int(input())

applist=[]
for i in range(k):
    listy=list(map(int,input().split()))
    listy[0]-=1
    listy[1]-=1#0으로 시작하려고
    applist.append(listy)
    
l=int(input())
movelist=[]
for i in range(l):
    listy=list(map(str, input().split()))
    listy[0]=int(listy[0])
    movelist.append(listy)

#틀
board=[]
for i in range(n):
    listy=[]
    for j in range(n):
        listy.append(0)
    board.append(listy)
    
#사과 배치(삼중...가능..?oo)
for i in range(n):
    for j in range(n):
        for k in range(len(applist)):
            if i==applist[k][0] and j==applist[k][1]:
                board[i][j]=1#사과는 1
            

#몸이나 벽을 만나면 True
def iswrong():
    global x
    global y
    global board
    global n
    if (x>n-1) or (x<0) or (y>n-1) or (y<0):
        return True
    elif board[x][y]==2: return True
    else:return False

def tailslice():
    global board
    global bodylist
    board[bodylist[0][0]][bodylist[0][1]]=0
    del bodylist[0]

def turnright():
    global direction
    direction=(direction+1)%4

def turnleft():
    global direction
    direction=(direction+3)%4
    
def printboard():
    global board
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' ')
        print()



x,y=0,0
board[x][y]=2
direction=1
dx=[-1,0,1,0]
dy=[0,1,0,-1]
bodylist=[[0,0]]#index -1인 것이 머리

time=0
while True:#방향대로 전진하고 뒤에 자취를 없애는!
    time+=1

    x+=dx[direction]
    y+=dy[direction]
    
    if iswrong()is True:
        print(time)
        break
    elif board[x][y]==1:#사과조아 꼬리 안자르고 기기
        board[x][y]=2
        bodylist.append([x,y])
    else:
        board[x][y]=2 # 흔적 남기기
        bodylist.append([x,y])
        tailslice()
        
    #방향 바꾸귀
    if len(movelist)!=0:
        if time==movelist[0][0]:
            if movelist[0][1]=='D':
                turnright()
            else:turnleft()
            del movelist[0]
        else:pass
    #printboard()
    #print(bodylist)


        
    














    
