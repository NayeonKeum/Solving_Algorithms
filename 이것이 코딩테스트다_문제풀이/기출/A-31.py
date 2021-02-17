#a-31
t=int(input())
n,m=map(int, input().split())
nlist=list(map(int, input().split()))
graph=[[]for _ in range(n)]
mm=m
nn=0
ind=0
while nn<n and mm<=len(nlist):
    graph[nn]=nlist[ind:mm]
    nn+=1
    ind+=(m)
    mm+=m

def getRU(x, y):
    global graph
    if x-1>=0 and x-1<len(graph) and y+1>=0 and y+1<len(graph[0]):
        return [graph[x-1][y+1],x-1]
    else:return [-1,x-1]

def getR(x, y):
    global graph
    if x>=0 and x<len(graph) and y+1>=0 and y+1<len(graph[0]):
        return [graph[x][y+1],x]
    else:return [-1,x]


def getRD(x, y):
    global graph
    if x+1>=0 and x+1<len(graph) and y+1>=0 and y+1<len(graph[0]):
        return [graph[x+1][y+1],x+1]
    else:return [-1,x+1]



max_list=[]
for i in range(n):
    total = 0
    x, y = i, 0
    total += graph[x][y]
    for j in range(m):
        mlist=[getRU(x, y),getR(x, y),getRD(x, y)]
        mlist.sort(key=lambda x:x[0])
        if mlist[-1][0]==-1:break
        else:
            total+=mlist[-1][0]
            x=mlist[-1][1]
            y+=1
    max_list.append(total)


print(max(max_list))




'''
1
3 4
1 3 3 2 2 1 4 1 0 6 4 7
'''
'''
1
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''