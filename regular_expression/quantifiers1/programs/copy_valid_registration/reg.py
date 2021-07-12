import re

x = '[K][L]+\d{2}[A-Z]{1,2}\d{1,4}'
v1 = open('file1', 'r')
v2 = open('file2', 'w')
for i in v1:
   # print(i)
   r=i.rstrip('\n')
   v=re.fullmatch(x,r)
   if  v!=None:
      v2.write(i)

# for i in v2:
#     print(i)
