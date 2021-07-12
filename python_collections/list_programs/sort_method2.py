a=[3,2,4,2,1]
print(len(a))
b=[]
c=5
temp=0
for i in range(5):
    for j in range(i+1,5):
        if a[i]>a[j]:
         temp=a[i]
         a[i]=a[j]
         a[j]=temp
print(a)