#a-15(22분/30분)
n,m,k,x=map(int, input().split())
graphy=[]
for i in range(m):
    graphy.append(list(map(int, input().split())))

graph=[[] for _ in range(n+1)]
for node in graphy:
    graph[node[0]].append(node[1])
'''
graph = [
    [],
    [2, 3].
    [3, 4].
    [],
    []
]
'''
lengths=[0]*(n+1)#([[0],[0],[1],[1],[0]])
length=0
for node in graph[x]:
    lengths[node]=1
    if graph[node]:
        for nodey in graph[node]:
            if not lengths[nodey]:
                lengths[nodey]=2
def find(lengths):
    l=0
    for i in range(len(lengths)):
        if k==lengths[i]:
            l=1
            print(i)
    if l==0:print(-1)

find(lengths)


            
    
    
