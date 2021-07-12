import re  #start at a end at b any type included in middle
a=input('enter strings')
x='^a[a-zA-Z0-9\W]+b$'
v=re.fullmatch(x,a)
if v is not None:
    print('valid')
else:
    print('notvalid')