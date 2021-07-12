# subject marks
a=int(input("enter m1"))
b=int(input("enter m2"))
c=int(input("enter m3"))
d=int(input("enter m4"))
e=int(input("enter m5"))
f=a+b+c+d+e
print('total marks are : ',f)
avg=f//5
print("average is : ",avg)
if avg >= 91 & avg < 100:
    print('a grade')
elif avg>=81 and avg<91:
    print('b grade')