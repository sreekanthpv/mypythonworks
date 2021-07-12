a=[11,2,5,3,5,2,11]
b=[]
c=[]

for i in a:
    if i not in b:
        b.append(i)
    else:
        c.append(i)
c.sort()
print(c)

