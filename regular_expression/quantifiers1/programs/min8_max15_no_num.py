# min 8 max 15 no numbers  (upper lower and symbols)

import re   #
s=input('enter string')
x='[\D]{8,15}'
v=re.fullmatch(x,s)
if v is not None:
    print('valid')
else:
    print('invalid')