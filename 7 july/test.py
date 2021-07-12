dic={'ab':{'bname':'abin'},'abc':{'bnam':'abn'}

}
dic1={}
# print(dic)
for i in dic:
    print(dic[i])
    dic1.update({dic[i]:dic[i]['bname']})
print(dic1)