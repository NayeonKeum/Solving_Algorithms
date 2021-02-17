#9-5(14분/60분)
import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

n,m,c=map(int, input().split())

graph=[[]for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    x,y,z=map(int, input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))
    while q:
        dist, now=heapq.heappop(q)
        if distance[now]<dist:continue
        for i in graph[now]:
            cost=dist+i[1]
            if distance[i[0]]<cost:continue
            else:
                distance[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)
count=0
time=-1
for n in graph[c]:
    if n!=0:
        count+=1
        time=max(time, distance[n[0]])
print(count, time)

'''
3 2 1
1 2 5
1 3 2
'''