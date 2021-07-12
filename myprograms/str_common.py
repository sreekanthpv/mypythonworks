# find common elements
a = 'maay'
b = 'zzzam'
c = ''
for i in a:
    if i in b:
        c = c + i
if c == '':
    print('no')


else:
    print(c)



