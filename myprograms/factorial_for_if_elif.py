a=int(input('enter the number'))
fact=1
if a==0:
    print('fact of 0 is 1')
elif a<0:
    print('enter positive number')
else:
    for i in range(1,a+1):
        fact=fact*i

    print('fact is',fact)
