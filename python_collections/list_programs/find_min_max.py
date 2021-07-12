a=[3,2,1,6,5,4]
b=[]
while  a:
    min=a[0]
    for i in a:
        if i<min:
            min=i
    b.append(min)
    a.remove(min)
print(b)
print(b[0])
print(b[-1])



#
#
# # or
# a.sort()
# print(a)