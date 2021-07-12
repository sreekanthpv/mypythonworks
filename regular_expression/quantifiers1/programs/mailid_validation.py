import re
a=input('enter the mail id')
x='[a-z]+[@]+[gmail yahoo]+[.]+[in com]+'
v=re.fullmatch(x,a)
if v!=None:
    print('valid')
else:
    print('invalid')