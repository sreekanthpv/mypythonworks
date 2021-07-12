# from functools import reduce
l=[1,2,3,4,5,6,7]
res=list(map(lambda n1: n1-1 if n1<5 else n1+1 if n1>5 else n1,l))
print(res)

