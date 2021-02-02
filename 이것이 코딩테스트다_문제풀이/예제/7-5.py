#7-5 부품 찾기(2+4+4분/30분)(각 in, 이진, 계수)
n=int(input())
nlist=list(map(int, input().split()))
nlist.sort()
m=int(input())
mlist=list(map(int, input().split()))

#파이썬
print("\n그냥 in")
for ms in mlist:
    if ms in nlist:
        print("yes", end=' ')
    else:print("no", end=' ')

#이진 탐색
def bs(nlist, s, e, target):
    if s>e:return None
    mid=(s+e)//2
    if nlist[mid]==target:
        return mid
    elif nlist[mid]>target:
        e=mid-1
        return bs(nlist, s, e, target)
    else:
        s=mid+1
        return bs(nlist, s, e, target)

print("\n이진 탐색")
for ms in mlist:
    if bs(nlist, 0, len(nlist)-1, ms) == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')


#계수 정렬
print("\n계수 정렬")
stat=[0]*(max(nlist)+1)
for ns in nlist:
    stat[ns]+=1
for ms in mlist:
    for s in range(len(stat)):
        if s==ms:
            if stat[s] == 0:
                print("no", end=' ')
            else:
                print("yes", end=' ')



'''
5
8 3 7 9 2
3
5 7 9
'''