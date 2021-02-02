#a-03(9분/20분)
n=input()

l0=n.split('0')
l1=n.split('1')
len_sp0=0
len_sp1=0
for i in l0:
    if i:
        len_sp0+=1
    else:pass
for i in l1:
    if i:
        len_sp1+=1
    else:pass


if len_sp0>len_sp1:
    print(len_sp1)
else:
    print(len_sp0)
print(l0, l1)
print(len_sp0,len_sp1)
