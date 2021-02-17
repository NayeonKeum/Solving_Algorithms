#a-40
import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)


n,m=map(int, input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def dijkstra(graph):
    global distance
    q=[]
    heapq.heappush(q, (0,1))
    distance[1]=0
    while q:
        dist, now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist + 1  # 거리
            if cost < distance[i]:  # 인덱스(노드)
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(graph)
for i in range(len(distance)):
    if distance[i]==INF:
        distance[i]=-1
print(distance.index(max(distance)), end=' ')
print(max(distance), end=' ')
print(distance.count(max(distance)))

'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''