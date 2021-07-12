#list index out of range
a=[1,2,3,4]

b=int(input('enter'))

try:
    print(a[b])
except Exception as x:
     print('exception',x)
finally:
    print('finished')



