l=[1,2,4,3,6,5,8,7,10,9]
def binary():
    l.sort()
    print(l)
    low=0
    up=len(l)-1
    flag=0
    ele=int(input('enter the element'))
    while low<=up:
        mid=(up+low)//2
        if ele<l[mid]:
            up=mid-1
        elif ele>l[mid]:
            low=mid+1
        elif ele==l[mid]:
            flag=1
            break

    if flag==1:
      print('found')
    else:
      print('not found')
binary()


