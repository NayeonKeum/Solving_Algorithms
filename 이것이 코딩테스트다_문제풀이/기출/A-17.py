#a-17
n,k=map(int,input().split())
place=[]
for i in range(n):
    place.append(list(map(int, input().split())))
s,x,y=map(int, input().split())
x-=1
y-=1


#0에서 k 까지 각 자리의 index와 같은 값을 가지는 place의 좌표를 [x,y]로 넣는다
#[[[1,2],[0,1],[2,2]],[[3,4],[5,6]],,,]
def find(place,k):
    listy=[[] for _ in range(k+1)]
    for i in range(len(place)):
        for j in range(len(place[0])):
            listy[place[i][j]].append([i,j])
    return listy

def print2(place):
    for i in range(len(place)):
        for j in range(len(place)):
            print(place[i][j], end=' ')
        print()


def bfs(place, k, s):
    dx=[-1,0,1,0]#북쪽부터 시계방향
    dy=[0,1,0,-1]
    time=0
    cnt=0
    while True:
        virus_list=find(place, k)
        if time==s:
            return place
        for i in range(1,k+1):
            if cnt>=len(virus_list[i]):continue
            else:
                xx=virus_list[i][cnt][0]
                yy=virus_list[i][cnt][1]
                #print("x and y found" ,xx,yy)
                for j in range(4):
                    nx=xx+dx[j]
                    ny=yy+dy[j]
                    if nx>len(place)-1 or nx<0 or ny>len(place)-1 or ny<0:continue
                    elif place[nx][ny]==0:
                        #print("found it", nx, ny)
                        place[nx][ny]=i       
        cnt+=1
        time+=1

nowplace=bfs(place, k, s)#k=3, s=2
print(nowplace[x][y])
                    
