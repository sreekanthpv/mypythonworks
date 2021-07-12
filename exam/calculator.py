

# 5.create a calculator with functions(addition,subtraction,multiplication,division,floor division,exponent)?


def add(x,y):
    return x+y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    return x / y
def floor(x,y):
    return x // y
def exp(x, y):
    return x ** y

a= int(input('enter the value 1'))
b= int(input('enter the value 2'))

print('1.addition')
print('2.subtraction')
print('3.multiplication')
print('4.division')
print('5.floordiv')
print('6.exponent')
c= int(input('enter the choice'))

if c==1:
    print('add',add(a,b))
elif c==2:
    print('sub ',sub(a,b))
elif c==3:
    print('mul ',mul(a,b))
elif c == 4:
    print('div ', div(a, b))
elif c == 5:
    print('floor ', floor(a, b))
elif c == 6:
    print('exponent', exp(a, b))
else:
    print('choose valid option')
