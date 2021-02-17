#a-39
import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

def dijkstra(graph):
    global distance
    x, y = 0, 0
    dx = [1, 0, -1, 0]  # 아래부터 반시계
    dy = [0, 1, 0, -1]

    q = [(graph[x][y], x, y)]
    distance[x][y]=graph[x][y]

    while q:  # q가 안 비워져 있다면
        dist, x, y = heapq.heappop(q)  # 하나 꺼내
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>len(graph)-1 or ny<0 or ny>len(graph)-1:
                continue
            cost= dist+graph[nx][ny]
            if cost < distance[nx][ny]:  # 인덱스(노드)
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx,ny))


t=int(input())
for _ in range(t):
    graph=[]
    n=int(input())
    distance = [[INF] * n for _ in range(n)]
    for i in range(n):
        graph.append(list(map(int, input().split())))
    dijkstra(graph)
    print(distance[n-1][n-1])



'''
3
5 5 4
3 9 1
3 2 7

5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5

'''





