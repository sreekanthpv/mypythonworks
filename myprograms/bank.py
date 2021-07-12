#bank account


f=50000
a=float(input("enter the amount to withdraw : "))
if a>f:
    print("insufficient bal")
else:
    bal=f-a
    print("your balance is : ",bal)