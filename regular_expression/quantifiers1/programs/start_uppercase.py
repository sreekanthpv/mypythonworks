import re  #start at upper follwed by any lower,symbols,digits,no uppercase
a=input('enter string')
x='^[A-Z]+[a-z\d\W]*[^A-Z]+'
v=re.fullmatch(x,a)
if v is not None:
    print('valid')
else:
    print('invalid')
