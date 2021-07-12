# the number which can only divided by 1 or that number also remaider will not be 0
#in case of number 2 , range will be range(2,2) so it will not execute
a=int(input("enter the number"))
if a>1:

   for i in range(2,a):
      if a % i  == 0:
        print(" not prime")
        break
   else:
      print(" prime")

# sum=0
# c=int(input("enter inital"))
# b=int(input('enter final'))
# for a in range(c,b):
#  if a>1:
#     for i in range (2,a):
#         if a%i==0:
#         # sum=sum+
#          break
#     else:
#
#             #print(a)
#             sum=sum+a


# print('sum is :',sum)





