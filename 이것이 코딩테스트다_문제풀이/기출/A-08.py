#a-08(7분/20분)
str=input()
result=[]
total=0
for i in range(len(str)):
    if ord(str[i])>=65 and ord(str[i])<=90:
        result.append(str[i])
    else: total+=int(str[i])
total=str(total)
result.sort()
result="".join(result)
print(result+total)
