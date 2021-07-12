def par(n):
    v1=n
    for i in range(0,n):
        for j in range(0,i):
            print(end=' ')
        for k in range(0,v1):
            print('*',end=' ')
        print('\r')
par(5)