def ugly(num):
    if num==1:return True
    if num % 2==0:
        return ugly(num//2)
    elif num % 3 == 0:
        return ugly(num//3)
    elif num%5==0:
        return ugly(num//5)
    else: return False

n=int(input())
ugly_list=[0,]#index와 동일하게 맞추려고
'''
i=0
while len(ugly_list)<=n:
    i+=1
    if ugly(i) is True:
        ugly_list.append(i)
    else:
        continue
print(ugly_list[n])
'''
ugly_list2=[]
ugly=[0]*n
ugly[0]=1
i2=i3=i5=0
next2, next3, next5=2, 3, 5

for l in range(1,n):
    ugly[l]=min(next2, next3, next5)
    if ugly[l]==next2:
        i2+=1
        next2=ugly[i2]*2
    if ugly[l]==next3:
        i3+=1
        next3=ugly[i3]*3
    if ugly[l]==next5:
        i5+=1
        next5=ugly[i5]*5

print(ugly[n-1])