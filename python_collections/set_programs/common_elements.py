a={1,2,3,4}
b={3,4,5,6}
s1=set()
for i in a:
    if i in b:
        s1.add(i)
print(s1)