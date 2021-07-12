# 6.create a function with arguments and return type which find sum of prime numbers between 1 - 50?
def fun(n):
 sum=0
 c=0

 if n < 1:
     return n

 else:
        for j in range(2,n):
               if n%j==0:
                c=c+1
               break
        else:
            return n




for i in range(1,50):
      print(fun(i))


