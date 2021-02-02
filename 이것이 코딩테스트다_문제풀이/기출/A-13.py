#a-13

def find_house(listy):
    hlist=[]
    for i in range(len(listy)):
        for j in range(len(listy)):
            if listy[i][j]==1:
                hlist.append((i,j))
    return hlist
def find_chicken(listy):
    clist=[]
    for i in range(len(listy)):
        for j in range(len(listy)):
            if listy[i][j]==2:
                clist.append((i,j))
    return clist


def till_chicken(hlist,clist):#선택할 m개의 clist가 정해졌을 때
    smallest=[]
    for i in range(len(hlist)):
        till_list=[]#한 집에서 부터 근방 치킨집까지 거리 전부 구한것
        for j in range(len(clist)):
            till_list.append(abs(hlist[i][0]-clist[j][0])+abs(hlist[i][1]-clist[j][1]))
        till_list.sort()#의 가장 작은 값
        smallest.append(till_list[0])  
    return sum(smallest)
    


n,m=map(int, input().split())
listy=[]
for i in range(n):
    line=list(map(int,input().split()))
    listy.append(line)



from itertools import combinations
candidates=list(combinations(find_chicken(listy),m))#clist candidates 생성
hlist=find_house(listy)
cands=[]
for clist in candidates:
    cands.append(till_chicken(hlist,clist))
print(min(cands))
