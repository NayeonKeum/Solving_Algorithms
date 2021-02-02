#a-10
def solution(key, lock):
    answer=all1
    return answer
def all1(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]==0:
                return False
            else:continue
    return True

#lock의 빈 부분 찾기 빛 간단화
def find_lock(lock):
    list=[]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]==0:
                list.append([i,j])
    miny=min(map(min, list))
    for i in range(len(list)):
        for j in range(len(list)):
            list[i][j]-=miny#올리올리
            
            
    return list

def move(x,y,matrix):
    #와...개모르겠다....
    


    
'''
def spin(matrix):

'''

#입력은 일단 재끼고 생각해
key=[[0,0,0],[1,0,0],[0,1,1]]
lock=[[1,1,1],[1,1,0],[1,0,1]]

matrix=lock
print(find_lock(lock))
