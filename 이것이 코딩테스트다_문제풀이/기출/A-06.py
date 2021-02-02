#a-06(+30분/30분)-실패... 몰라...머리 안돌아가...

def solution(food_times, k):
    answer = 0
    return answer
k=7
food_times=[3,1,2,4]

def countmin(list):
    count=0
    for val in list:
        if val==min(list):
            count+=1
    return count

def minlist(n,list):
    listy=[]
    for val in list:
        if val==0: listy.append(0)
        else:
            listy.append(val-n)
    return listy

lefttime=food_times.copy()
while True:
    if min(food_times)==0:#만약 0이 있다면 그 원소들을 lefttime에서 삭제!
        for n in range(countmin(food_times)):#0 개수
            try:
                del lefttime[lefttime.index(min(food_times))]
            except(ValueError): break
        print(lefttime, food_times)
    if k>=min(lefttime)*len(lefttime):
        k-=min(lefttime)*len(lefttime)
        food_times=minlist(min(lefttime),food_times)
        lefttime=minlist(min(lefttime),lefttime)
    else:
        index=0
        indexlist=[]
        for index in range(len(food_times)):
            if food_times[index]!=0:
                indexlist.append(index)
            else:continue
        print(indexlist[k-1]+1,"번째")
        break









