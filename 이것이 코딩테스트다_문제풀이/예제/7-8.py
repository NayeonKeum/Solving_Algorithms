#7-8
n,m=map(int, input().split())
ddlist=list(map(int, input().split()))
##이거는 훼이크-> 시간초과 나옴
height=max(ddlist)
for h in range(height-1,0,-1):
    total=0
    for dd in ddlist:
        if dd>=h:
            total+=(dd-h)
        else:pass
    if total>=m:
        print(h)
        break
    elif total<m:
        continue

####이진 탐색
def cutdd(height, ddlist):
    total=0
    for dd in ddlist:
        if dd>=h:
            total+=(dd-height)
        else:pass
    return total



max_h=max(ddlist)
def bs(ddlist, min, max, m):#인덱스가 아닌 길이를 변수로 두자
    if min>max:return None
    mid=(min+max)//2
    if cutdd(mid, ddlist)==m:
        return mid
    elif cutdd(mid, ddlist)<m:
        max = mid - 1
        return bs(ddlist, min, max, m)
    else:
        min = mid + 1
        return bs(ddlist, min, max, m)

print(bs(ddlist, 0, max_h, m))

'''
4 6
19 15 10 17
'''