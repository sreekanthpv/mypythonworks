# imported from functools ,uses 2 variables---reduce is used to return a single value
# i.e sum of a list,largest,smallest etc.

from functools import reduce
lst=[1,2,3,4,5]
res=reduce(lambda n1,n2:n1+n2,lst)
print(res)