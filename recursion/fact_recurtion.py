def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


a = int(input('enter the num'))
if a < 0:
    print("enter a positive num")
elif a == 0:
    print('fact of 0 is 1')
else:
     print('fact is ',fact(a))

