#a-02(10분/30분)->근데 좀 망함
n=input()
total=1
i=1
while i<len(n):
    if n[i]=='0':
        pass
    elif n[i]=='1':
        if i==len(n)-1:
            total+=1
            break
        else:
            total*=(int(n[i])+int(n[i+1]))
            i+=1
    else: total*=int(n[i])
    i+=1
print(total)

        
        
