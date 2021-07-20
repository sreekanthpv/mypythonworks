a=[5,4,3,2,1]
c=len(a)
temp=0
for i in range(c):
    for j in range(i+1,c):
        if a[i]>a[j]:
         temp=a[i]
         a[i]=a[j]
         a[j]=temp
print(a)