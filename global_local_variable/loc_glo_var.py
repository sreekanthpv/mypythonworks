#variable that can be accessed only in a function is local
#variable that can be accssed in any where of a program is global

def glob():
    global x,a
    x=10
    a=3
    print(x)
glob()
print(x)
print(a)