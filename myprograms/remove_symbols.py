a=input('enter the string')
b='!@#$%^&*()'
c=''
for i in a:
    if i  in b:
        continue
    else:
        c=c+i
print(c)

