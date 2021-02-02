#6-12
n,k=map(int, input().split())
list_a=list(map(int, input().split()))
list_b=list(map(int, input().split()))

list_a.sort()
list_b.sort()

for i in range(k):
    if list_a[i]<list_b[n-i-1]:
        list_a[i], list_b[n-i-1]=list_b[n-i-1], list_a[i]
    else:break

print(sum(list_a))