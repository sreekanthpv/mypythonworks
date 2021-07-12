


def add(x,y):
    return x+y

def sub(x,y):
    return x-y


def mul(x,y):
    return x*y


def div(x,y):
    return x//y


print("1.adition")
print("2.sub")
print("3.mul")
print("4.div")
c=int(input("enter your choice"))
while True:
       if c in (1,2,3,4):
         a=int(input("enter 1st : "))
         b=int(input("enter the 2nd : "))

         if c==1:
            print(add(a,b))
         elif c==2:
            print(sub(a,b))
         elif c==3:
            print(mul(a,b))
         elif c==4:
            print(div(a,b))
       else:
            print('select a valid option')

       break


