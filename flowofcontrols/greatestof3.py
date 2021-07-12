a=int(input("enter the 1st"))
b=int(input("enter the 2nd"))
c=int(input("enter the 3rd"))

# if a>b:
#     if a>c:
#         print("greater is : ",a)
# elif b>c:
#     print("greater is : ",b)
# else:
#     print('greater is : ',c)


if (a>b) & (a>c):
          print("greater is : ",a)
elif (b>a) & (b>c):
          print("greater is: ",b)
elif (c>a) & (c>b):
          print("greater is: ",c)