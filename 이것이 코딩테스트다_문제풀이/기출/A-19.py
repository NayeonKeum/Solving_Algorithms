#a-19(34분/30분)
def calculation(n1, n2, op):
    n1 = int(n1)
    n2 = int(n2)
    if op=='+':
        return n1+n2
    elif op=='-':
        return n1-n2
    elif op=='*':
        return n1 * n2
    elif op=='/':
        if n1<0:
            result=-((-n1)//n2)
            return result
        else: return n1//n2
    else:print("smths wrong")

n=int(input())
nlist=list(map(int, input().split()))
oplist=list(map(int, input().split()))

#oplist를 operator list로 변환
coplist=[]
ops=['+','-','*','/']
for i in range(len(oplist)):
    for n in range(oplist[i]):
        coplist.append(ops[i])
#coplist에 op list들어있다


from itertools import permutations
def dfs(nlist, coplist):
    candidates = list(permutations(coplist, len(coplist)))
    callist=[]
    for ncoplist in candidates:
        tmp = nlist[0]
        for i in range(len(nlist)-1):
            tmp = calculation(tmp, nlist[i+1], ncoplist[i])
        callist.append(tmp)
    print(max(callist))
    print(min(callist))


print(dfs(nlist, coplist))




