#avail book
#sort author based on sold
# if same author name with different books (is duplicating possible//same keyname) doubt

products={
    1:{"item_name":"boost","mrp":290,"stock":50},
    2:{"item_name":"complan","mrp":240,"stock":10},
    3:{"item_name":"bournvita","mrp":320,"stock":20},
    4:{"item_name":"horlicks","mrp":280,"stock":13},
    5:{"item_name":"nutricharge","mrp":275,"stock":0},
}
# print(type(products))
res=sorted(products.items(),key=lambda x:x[1]['stock'],reverse=True)
print(res)
