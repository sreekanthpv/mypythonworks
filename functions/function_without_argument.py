#function without arg

# def fun():
#     a=1
#     b=2
#     print(a+b)
# fun()
#

#fun with args
#
# def add(n1,n2):
#     print(n1+n2)
# add(1,2)


#fun with args and return type

#
# def add(n1,n2):
#     return n1+n2
# print(add(1,8))



# prg to perfom arthmetic operation using fn

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x//y

print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
c=int(input('enter the choice'))
while True:
  if c in (1,2,3,4):
     a=int(input('enter the value1'))
     b=int(input('enter the val 2'))
     if c==1:
       print(add(a,b))
     elif c==2:
       print(sub(a,b))
     elif c==3:
       print(mul(a,b))
     elif c==4:
       print(div(a,b))

  else:
    print('select a valid')

  break