a='aeiou'
c=[]
b=(input('enter the string'))
for i in b:
    if i not in a:
        c.append(i)
print(c)