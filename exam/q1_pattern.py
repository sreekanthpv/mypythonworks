a=1
b=5
c=5

for i in range(a,b+1):
    if i%2==0:
        for j in range(c,0,-1):
            for l in range(j):
             print(i,end=' ')
            print('\r')
    else:
        for m in range(c):
          for k in range(0,m+1):
              print(i,end=' ')
          print('\r')


