#a-38(28분/40분)

INF=int(1e9)
n, m=map(int, input().split())
graph=[[INF]*(n+1)for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i]=0
for _ in range(m):
    a,b=map(int, input().split())
    graph[a][b]=1



def find(start, graph,num):
    global check
    for i in range(1,n+1):
        if graph[start][i]==1:
            check[i]=num
            find(i, graph, num)
        else:
            continue
    return
count=0
for l in range(1,n+1):
    # 1은 작은거, 2는 큰거
    check = [0] * (n + 1)
    check[l]=INF
    find(l, graph, 2)
    new_g = list(map(list, zip(*graph)))
    find(l, new_g, 1)

    check=check[1:]
    print(check)
    if check.count(0)==0:
        count+=1
print(count)



'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''
