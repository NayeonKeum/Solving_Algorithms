#5-8
def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=' ')
    for node in graph[v]:
        if visited[node]==False:
            dfs(graph,node,visited)





graph=[
    [],
    [2,3,8],
    [1,7],
    [4,5],
    [3,5],
    [3,4],
    [7],
    [6,8],
    [1,7],
    ]
visited=[False]*9

dfs(graph, 1, visited)
