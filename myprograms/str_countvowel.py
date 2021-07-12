a='aeiou'
b=input('enter the string')
c=0
for i in a:
    if i in b:
        c=c+1
if c==0:
    print('no vowels')
else:
    print(c)
