#try..exceptional case
#except...solving code
#finally.....anything


a=int(input('enter n1'))
b=int(input('enter n2'))
try:
    print('hello')
    print(a/b)
except Exception as z:
    print(z)
finally:
    print('inside finally')


