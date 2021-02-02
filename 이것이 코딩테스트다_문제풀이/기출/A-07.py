#a-07(4분/20분)
str=input()
a=len(str)//2
left=0
right=0
for i in range(len(str)):
    if i<a:
        left+=int(str[i])
    else: right+=int(str[i])
if left==right:
    print("Lucky")
else: print("Ready")
        
