import re
r='KL36E1234'
x='[K][L]+\d{2}[A-Z]{1,2}\d{1,4}'
v=re.fullmatch(x,r)
if v is not None:
    print('valid')
else:
    print('invalid')
