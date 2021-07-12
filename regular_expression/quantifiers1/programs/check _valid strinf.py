# import re
# n='hello'
# x='\w+'
# m=re.fullmatch(x,n)
# if m is not None:
#     print('valid')
# else:
#     print('invalid')

#
import re

n='56kg'
x='[0-9]{2}[a-z]{2}'
v=re.fullmatch(x,n)
if v is not None:
    print('valid')
else:
    print('invalid')
