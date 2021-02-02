#7-2 이진 탐색
a=[0,2,3,5,7,8,9,12]

def bs(a, s, e, num):
    mid=(s+e)//2
    if a[mid]==num:
        return mid
    elif a[mid]>num:
        e=mid-1
        return bs(a, s, e, num)##########왜 retrun 해야하는거지????
    elif a[mid]<num:
        s=mid+1
        return bs(a, s, e, num)

print(bs(a,0,len(a)-1,3))
