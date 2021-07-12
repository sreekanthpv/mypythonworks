a=int(input("enter the number1\n"))
b=int(input("enter the number 2\n"))


#1st method only in python

# (a,b)=(b,a)
# print('numbers after swaping is')
# print(a,'\n',b)

#2nd method
t=a
a=b
b=t
print('numbers after swaping is')
print(a,'\n',b)


#3rd method



a=a+b
b=a-b
a=a-b
print('numbers after swaping is')
print(a,'\n',b)