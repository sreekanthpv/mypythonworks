a='malayalam'
b=input('enter the element')
c=0
for i in a:
    if i in b:
        c=c+1
if c==0:
    print('invalid')
else:
    print(c)