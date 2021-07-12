def rev(fun):
    def wrapper(a,b):
        if a<b:
            return fun(b,a)
            # (a,b)=(b,a)
            # temp=a
            # a=b
            # b=temp
            # return fun(a,b)
        else:
            return fun(a,b)
    return wrapper

@rev
def sub(n1,n2):
    print(n1-n2)
sub(6,7)

@rev
def div(n3,n4):
    print('div is',n3/n4)
div(1,2)
