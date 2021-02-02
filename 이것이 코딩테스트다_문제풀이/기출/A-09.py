#a-09(27분/30분)
s=input()

def apchuk(str, n):
    list=[]
    i=0
    while i<=len(str):
        list.append(str[i:i+n])
        i+=n
    #리스트에 n개별로 잘라 넣은 거 들어있음
    count=1
    result=''
    for k in range(len(list)-1):
        if list[k]==list[k+1]:
            count+=1
        elif count!=1:
            result=result+repr(count)+list[k]
            count=1
        else:result+=list[k]
    if len(list[-1])!=len(list[-2]):
        result+=list[-1]
    return len(result)

def solution(s):
    length=[]
    for i in range(1,len(s)//2+1):
        length.append(apchuk(s,i))
    answer = min(length)
    return answer
print(solution(s))


