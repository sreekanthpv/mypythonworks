# 9.write a code to validate -string starting and ending with a uppercase letter -
# except special characters -minimum length 5 -maximum length 10


import re
x='[^[A-Z][\da-zA-Z]{3,8}[A-Z]$]'
a=input('enter string')
v=re.fullmatch(x,a)
if v is not None:
    print('valid')
else:
    print('invalid')
