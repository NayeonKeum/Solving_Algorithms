#a-28
n=int(input())
nlist=list(map(int, input().split()))

def bs(nlist, start, end):
    if start>end:
        return None
    mid=(start+end)//2
    if nlist[mid] == mid:
        return mid
    elif nlist[mid]<mid:
        return bs(nlist, mid+1, end)
    else:
        return bs(nlist, start, mid-1)

index=bs(nlist, 0, n-1)
if index==None:
    print(-1)
else:print(index)


'''
7
-15 -4 2 8 9 13 15
7
-15 -4 3 8 9 13 15
'''