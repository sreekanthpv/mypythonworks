import re
a=input('enter number')
x='[+][9][1]\d{10}' #'[+91]'means either + 9 1
v=re.fullmatch(x,a)
if v is not None:
    print('valid')
else:
    print('invalid')
