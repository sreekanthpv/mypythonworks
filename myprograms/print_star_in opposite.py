



def star(r):
  for i in range(r,0,-1):
      for j in range(0,i):
          print('*',end=' ')
      print()
star(5)