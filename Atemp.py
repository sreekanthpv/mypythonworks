def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
a=int(input('enter the number'))
sum=0
for i in range (0,a):
 print(fib(i))
 sum=fib(i)+sum
 # sum+=x

print('sum is ',sum)