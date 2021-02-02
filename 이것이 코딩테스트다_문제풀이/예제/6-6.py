#6-6 계수정렬
a=[6,4,5,5,7,9,1,2,0,9,4,2,1]

count=[0]*(max(a)+1)
for o in a:
    count[o]+=1
for i in range(len(count)):
    if count[i]==0:pass
    else:
        for j in range(count[i]):
            print(i, end=' ')
