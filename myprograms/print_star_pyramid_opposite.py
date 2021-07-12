def star(n):
    v1=n

    for i in range(0,n):
        for i in range(0,i):
            print(end=' ')
        for k in range(0,v1):
            print('*',end=' ')
        v1=v1-1
        print('\r')

star(6)