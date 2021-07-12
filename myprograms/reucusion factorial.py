def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)



a=int(input('enter the numebr'))
for i in range(a+1):
    if i<0:
        print('enter positive value')
    elif i ==0:
        print(' fact of 0 is 1')
    else:
        z=fact(i)
print('fact is ' ,z)