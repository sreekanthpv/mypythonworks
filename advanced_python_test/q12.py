# 12. Write a Python program that matches a string that has an 'a' followed by numbers, ending in 'b'

import re
x='[a]{1}\d+[b]{1}'
a=input('enter string')
v=re.fullmatch(x,a)
if v is not None:
    print('valid')
else:
    print('invalid')
