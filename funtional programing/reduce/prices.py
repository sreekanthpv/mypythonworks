from functools import reduce
products=[
    {"item_name":"boost","mrp":290,"stock":50},
    {"item_name":"complan","mrp":240,"stock":10},
    {"item_name":"bournvita","mrp":320,"stock":20},
    {"item_name":"horlicks","mrp":280,"stock":13},
    {"item_name":"nutricharge","mrp":275,"stock":0},
]

res=list(map(lambda p:p['mrp'],products))
# print(res)
a=reduce(lambda n1,n2:n1 if n1>n2 else n2,res)
print(a)

print(max(res))