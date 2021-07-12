  #   *
  #  *  *
  # *  *  *
  #

def star(n):
    k=n
    for i in range(0,n):
        for j in range(0,k):
            print(end=' ')
        k=k-1
        for p in range(0,i+1):
            print('*',end=' ')
        print('\r')
star(5)