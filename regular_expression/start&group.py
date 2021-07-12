
# start() method return position
#group()  method shows which objects to find

import re
count=0
matcher=re.finditer('ab','abaabaab')
# print(matcher)
for i in matcher:
    print('match valable at',i.start())
    print('group=',i.group())
    count+=1
print(count)