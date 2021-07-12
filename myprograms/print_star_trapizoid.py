def tra(n):
    v1=n
    v2=n
    for i in range(0,n):
        for j in range(0,v1):
            print(end=' ')
        v1=v1-1
        for k in range(0,v2):
            print('*',end=' ')
        v2=v2+1
        print('\r')
tra(5)