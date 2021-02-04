#a-23


n=int(input())
nlist=[]
for i in range(n):
    nlist.append(list(map(str, input().split())))


def setting1(data):
    return data[1]
def setting2(data):
    return data[2]
def setting3(data):
    return data[3]
def setting4(data):
    return data[0]

nlist.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))


for r in nlist:
    print(r[0])

'''
5
Jun 50 60 100
Sang 80 60 50
Sun 80 70 100
Soong 50 60 90
Hae 50 60 100
'''