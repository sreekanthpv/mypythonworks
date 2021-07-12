a='luminar'
b=input('enter the letter to search : ')
for i in a:
    if b==i: #or if i in b:
        print('letter is found : ',i)
        break
else:
     print('not found')