#5-5
n=int(input())

#1. 반복문
def iter_fac(n):
    total=1
    for i in range(1,n+1):
        total*=i
    return total




#2. recursive

def re_fac(n):
    if n<=0:return 1
    elif n==1:return 1
    else:
        return n*re_fac(n-1)




print(iter_fac(n))
print(re_fac(n))
