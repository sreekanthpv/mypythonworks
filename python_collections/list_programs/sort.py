a=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
sort=[]
while a:
    min=a[0]
    for i in a:
        if i<min:
            min=i
    sort.append(min)
    a.remove(min)

print(sort)
print(a)