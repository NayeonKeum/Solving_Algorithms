#9-4(13분/40분)
INF=int(1e9)
n,m=map(int, input().split())
graph=[[INF]*(n+1) for i in range(n+1)]

for a in range(1, n+1):
    graph[a][a]=0

for i in range(m):
    a,b=map(int, input().split())
    graph[a][b]=1
    graph[b][a] = 1

x,k=map(int, input().split())

for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][i]+graph[i][b])
if int(graph[1][k])==INF or int(graph[k][x])==INF:
    print(-1)
else:
    print(int(graph[1][k])+int(graph[k][x]))

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5'''
'''
4 2
1 3
2 4
3 4
'''