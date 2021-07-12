import re
n=input('enter the number')
x='[\d]{10}'
v=re.fullmatch(x,n)
if v is not None:
    print('valid')
else:
    print('invalid')