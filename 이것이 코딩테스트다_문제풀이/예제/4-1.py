#여행자 도착 프로그램(5분/30분)
n=int(input())
x=y=1
move_list=map(str, input().split())
for move in move_list:
    if move=='R':
        if y==n:continue
        else: y+=1
    elif move=='L':
        if y==1:continue
        else: y-=1
    elif move=='U':
        if x==1:continue
        else: x-=1
    else:
        if x==n:continue
        else: x+=1


print(x, y)
