
lst=[1,2,3,4]
from functools import reduce
res=reduce(lambda n1,n2: n1 if n1>n2 else n2,lst)
print(res)