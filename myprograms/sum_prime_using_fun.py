def fun(i):
    c=0
    if i>1:
        for k in range(2,i):
            if i%k==0:
                c=c+1
                break
        else:
            return i
a=0
b=0
z=0
for j in range(1,7):
   a=(fun(j))
   if a==None:
    b=b+1
   else:
    print(a)
    z=z+a
print('sum',z)




