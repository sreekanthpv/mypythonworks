#to search an element is present in a string or not
#
flag = 0
a='malayalam'
b=input('enter the letter')
for i in a:
    if i in b:
        flag=1
        break
if flag==0:
    print('element not present')
else:
    print('present')
