#a function calls itself or function called inside that function

def fib(n):
    if n==0:
        return n
    elif n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)


a=int(input('enter the limit'))
c=0
for i in range(0,a):
    print(fib(i))
    c=fib(i)+c

print('sum of first',a,'terms is' ,c)