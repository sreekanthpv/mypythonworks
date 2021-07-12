import re
x='[+][9][1]\d{10}'
v=open('file','r')
for i in v:
    w=i.rstrip('\n')
    q=re.fullmatch(x,w)
    if q!=None:
        print(w)