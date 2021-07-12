dic={}
a="hello hai hello"
b=a.split(' ')
print(b)
for i in b:
    if i not in dic:
        dic.update({i:1})
    else:
        val=int(dic[i])
        val+=1
        dic.update({i:val})
print(dic)