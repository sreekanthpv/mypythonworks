#pattern matching
# re --package for pattern matching

import re
count=0
matcher=re.finditer('ab','abaabaab') #finditer is a method re package
# print(matcher)
for i in matcher:
    count+=1
print(count)