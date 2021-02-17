n=int(input())
flist=(list(map(int, input().split())))

i=0
total=0
while True:
    if i==len(flist)-1:
        total+=flist[i]
        break
    if flist[i]>flist[i+1]:
        total+=flist[i]
        i+=2
    else:
        total+=flist[i+1]
        i+=3
print(total)






