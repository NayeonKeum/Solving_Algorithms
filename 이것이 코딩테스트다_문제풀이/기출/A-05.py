#a-05(8분/30분)
n,m=map(int, input().split())
data=list(map(int, input().split()))
listy=[]
for i in range(n):
    for j in range(i+1,n):
        listy.append([data[i],data[j]])
num=0
for k in range(len(listy)):
    if listy[k][0]==listy[k][1]:
        pass
    else: num+=1
print(num)
        
