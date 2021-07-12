# *args
# a *args is a function used to add the numbers or perform other operations
def add(*args):
    print(args) #tuple
    sum=0
    for i in args:
        sum+=i
    print(sum)
add(1,2,3,4)