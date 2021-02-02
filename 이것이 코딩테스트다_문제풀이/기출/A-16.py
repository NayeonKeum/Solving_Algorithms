#a-16(x/40분) 나머지는 다 짰는데 최소 벽개수 알고리즘을 몼짬...
n,m=map(int, input().split())
maze=[]
for i in range(n):
    maze.append(list(map(int, input().split())))

def count_safe(mazey):
    count=0
    for i in range(len(mazey)):
        for j in range(len(mazey[0])):
            if mazey[i][j]==0:
                count+=1
    return count
##new
def find_safe(maze):
    listy=[]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j]==0:
                listy.append([i,j])
    return listy

##new
'''
def mark_wall(maze,cdts):
    mazey=maze.copy()
    for c in cdts:
        mazey[c[0]][c[1]]=1
    return mazey
'''

def find_virus(maze):
    listy=[]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j]==2:
                listy.append([i,j])
    return listy

from collections import deque
def virus_spread(mazey):
    # 북쪽부터 시계방향
    dc=[0,1,0,-1]
    dr=[-1,0,1,0]
    virus_list=find_virus(mazey)
    queue=deque()
    for node in virus_list:
        queue.append(node)
    while queue:
        v=queue.popleft()
        for i in range(4):
            nr=v[0]+dr[i]
            nc=v[1]+dc[i]
            if nr>n-1 or nr<0 or nc>m-1 or nc<0: pass
            elif mazey[nr][nc]==0:
                queue.append([nr,nc])
                mazey[nr][nc]=2
                

def printmaze(mazey):
    for i in range(len(mazey)):
        for j in range(len(mazey[0])):
            print(mazey[i][j], end=" ")
        print()
def maze_copy(maze):
    listy=[[] for _ in range(len(maze))]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            listy[i].append(maze[i][j])
    return listy



###다해보래...엄청난데..?
from itertools import combinations
def maxsafe(maze):
    candidates=list(combinations(find_safe(maze),3))
    count=-1
    
    for cdts in candidates:
        mazey=maze_copy(maze)
        
        for c in cdts:
            mazey[c[0]][c[1]]=1
            
        virus_spread(mazey)
        count=max(count,count_safe(mazey))     
    return count
print(maxsafe(maze))
















