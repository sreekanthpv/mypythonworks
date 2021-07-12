# 11. Write a Python program to find the sequences of one upper case letter followed by lower case letters?

import re
x='[A-Z]{1}[a-z]+'
a=input('enter string')
v=re.fullmatch(x,a)
if v is not None:
    print('valid')
else:
    print('invalid')