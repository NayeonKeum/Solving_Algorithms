#a-27(O(logN이라네.. 이진탐색으로 풀어야 하는건가봐)

n,x=map(int, input().split())
nlist=list(map(int, input().split()))
if x<nlist[0] or x>nlist[-1]:print(-1)
else:
    end=n-1
    s=-1
    e=-1
    for i in range(n):
        if s==-1:
            if nlist[i]==x:
                s=i
        if e==-1:
            if nlist[end-i]==x:
                e=end-i
    print(e-s+1)