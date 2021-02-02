#6-10
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
a.sort()
a.reverse()
##or 합쳐서 a=sorted(a, reverse=True)
for i in a:
    print(i, end=' ')
