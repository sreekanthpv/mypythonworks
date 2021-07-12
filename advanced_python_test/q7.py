# . Create a valid phone numbers file from the following file? +915678905432 +914567890321 765432167 123450987765 +919976532456



import re
x='[+][9][1]\d{10}'
v=open('file7a','r')
v1=open('file7b','w')
for i in v:
    q=i.rstrip('\n')
    r=re.fullmatch(x,q)
    if r is not None:
        v1.write(q)
