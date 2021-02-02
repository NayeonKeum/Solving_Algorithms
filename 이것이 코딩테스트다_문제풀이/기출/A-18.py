#a-18(50분/20분) kakao.....네이년...

string=input()


def is_right(string):
    if string[0]==")":return False
    stack=[string[0]]
    for s in range(1,len(string)):
        try:
            if string[s]==string[0]:
                stack.append(string[s])
            elif string[s]!=string[0]:
                stack.pop()
        except IndexError:
            return False
    if len(stack)==0:
        return True
    else: return False

def rverse(string):
    str=''
    for s in string:
        if s=="(":
            str+=")"
        else:
            str+="("
    return str

stack=[]
def makeright(u,v):
    line="("
    if v=='':pass
    else:
        line+=makeright(slice_u(v),slice_v(v))
    line+=")"
    line+=rverse(u[1:-1])
    return line

    
def slice_u(string):
    count=0
    u=''
    for s in string:
        if s=="(":
            count+=1
            u+=s
        else:
            count-=1
            u+=s
        if count==0:
            break
    return u

def slice_v(string):
    count=0
    v=''
    for s in range(len(string)):
        if string[s]=="(":
            count+=1
        else:
            count-=1
            
        if count==0:
            if s==len(string)-1:
                print("no v")
                break
            else:
                print("yes v")
                v+=string[s+1:]
                break
    return v

while True:
    if is_right(string):
        print(string)
        break
    elif is_right(slice_u(string)):
        print("1")
        v=slice_v(string)
        string=slice_u(string)+makeright(slice_u(v),slice_v(v))
    else:
        print("2")
        string=makeright(slice_u(string),slice_v(string))
    
