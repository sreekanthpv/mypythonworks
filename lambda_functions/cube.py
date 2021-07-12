#normal prg
def fun(n):
    return n**3
a=3
print(fun(a))




# lambda function

a=lambda n:n**3    #lambda function can have only 1 expr and can take any number of argumetns
print('cube',a(2))
print(a(4))


# addition
a=lambda b,c:b+c
x=int(input('enter'))
y=int(input('enter2'))
print(a(x,y))