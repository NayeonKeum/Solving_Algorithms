#4-3 왕실의 나이트(11분/20분)
#튜플 빼고는 거의 똑같아
a=input()
r=int(a[1])
c=int(ord(a[0])-ord('a'))+1#그냥 아스키로 해도 될 것 같은데
print(r,c)

r_move=[2,2,-2,-2,1,1,-1,-1]
c_move=[1,-1,1,-1,2,-2,2,-2]
count=0



for k in range(len(r_move)):
    nr=r
    nc=c
    nr+=r_move[k]
    nc+=c_move[k]
    if (nr<1) or (nr>8) or (nc<1) or (nc>8):
        continue
    else:
        count+=1
print(count)

