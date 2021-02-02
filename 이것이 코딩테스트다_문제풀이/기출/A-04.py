#a-04(35분/30분)
n=int(input())
list=list(map(int, input().split()))
numlist=[]
'''
numlist.append(list)
k=2**len(list)-1-len(list)#가능한 부분집합 개수, 공집합과 하나짜리 제외
for i in range(len(list)):
    for j in range(1,len(list)):
'''
'''
import itertools
temp=list(map(' '.join, itertools.permutations(list)))
numlist.extend(temp)
print(numlist)
'''
def printAllSubset(A,numlist):
    printAllSubsetHelper(A, 0)

def printAllSubsetHelper(A, index):
    if index == len(A):
        numlist.append(A)
        return
    printAllSubsetHelper(A[:], index + 1) #index번째 원소를 건드리 않고 다음으로 넘어가는 경우
    A.pop(index) #index번째의 원소를 제외하고
    printAllSubsetHelper(A[:], index)#주의할 점은 앞서 뺀 원소가 아예 사라졌기 때문에 index를 증가시키면 안된다!
printAllSubset(list,numlist)

for i in range(len(numlist)):
    numlist[i]=sum(numlist[i])
set(numlist)
for n in range(1000000):
    if n in numlist:
        continue
    else:
        print(n)
        break

