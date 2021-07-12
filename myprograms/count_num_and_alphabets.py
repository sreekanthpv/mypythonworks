a=input('enter the element')
b='0123456789'
c1=0
c2=0
for i in a:
    if i not in b:
        c1=c1+1
    else:
        c2=c2+1
print('alphabets ',c1)
print('numbers ',c2)

