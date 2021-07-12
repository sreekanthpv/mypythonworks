import re      #Assd6
x=input('enter string')
v='[a-zA-z]+\d$'
c=re.fullmatch(v,x)
if c is not None:
    print('valid')
else:
    print('invalid')