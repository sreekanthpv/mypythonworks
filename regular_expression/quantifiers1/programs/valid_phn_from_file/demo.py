import re
x='[+][9][1]\d{10}'
a=open('file','r')
for i in a:
    z=i.rstrip('\n')
    v=re.fullmatch(x,z)
    if v is not None:
        print(z)