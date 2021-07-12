a=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
b=[]
while a:
    min=a[0]
    for j in a:
        if j<min:
            min=j
    b.append(min)
    a.remove(min)
print(b)
print('second largest element is',b[-2])