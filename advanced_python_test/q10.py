# # 10.lambda function to check a number is prime or not?
# a=int(input('enter'))
# if a>=2:
#  for i in range(2,a):
#     if a%i==0:
#         print('not')
#  else:
#         print('prime')


a=lambda n:n%2==0
print(a(4))



