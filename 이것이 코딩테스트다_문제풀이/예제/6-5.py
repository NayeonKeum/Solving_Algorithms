#6-3 삽입 정렬
'''
a=[7,3,6,4,9,0,2,1,5,8,5]

for i in range(1,len(a)):
    for j in range(i,0,-1):
        if a[j]>=a[j-1]:
            break
        else:
            a[j],a[j-1]=a[j-1],a[j]
print(a)
'''
#6-4 퀵 정렬
a=[7,3,6,4,9,0,2,1,5,8]

def quicksort(a, start, end):
    if start>=end:return a
    pivot=start
    left=start+1
    right=end
    while left<=right:
        while left<=end and a[left]<=a[pivot]:
            left+=1
        while right>start and a[right]>=a[pivot]:
            right-=1
        if left<=right:
            a[left],a[right]=a[right],a[left]
        else:
            a[right],a[pivot]=a[pivot],a[right]
    #right이 피벗이 됐으니까!
    quicksort(a, start, right-1)
    quicksort(a, right+1, end)

quicksort(a, 0, len(a)-1)
print(a)

#6-5 퀵퀵
def quick_sort(a):
    if len(a)<=1:
        return a
    pivot=a[0]
    tail=a[1:]

    left_side=[x for x in tail if x<=pivot]
    right_side=[x for x in tail if x>pivot]

    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(a))

