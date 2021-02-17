#a-29(x/50분)
n,c=map(int, input().split())
nlist=[]
for _ in range(n):
    nlist.append(int(input()))
nlist.sort()

min=nlist[1]-nlist[0]
max=nlist[-1]-nlist[0]

while start<=end:
