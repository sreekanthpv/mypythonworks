a='aplee'
b={}
for i in a:
    if i not in b:
        b.update({i:1})
    else:
        print(i)
        break
# print(b)
