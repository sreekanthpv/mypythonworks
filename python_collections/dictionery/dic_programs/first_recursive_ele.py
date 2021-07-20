a='abcc'
dic={}
for i in a:
    if i not in dic:
        dic.update({i:1})
    else:
        print(i)
        break