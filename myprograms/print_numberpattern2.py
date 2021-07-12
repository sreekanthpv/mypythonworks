# 1
# 1 2
# 1 2 3
# 1 2 3 4
#
#
#


def row(r):
   c=0
   for i in range(0,r):
       c=0
       for j in range(0,i+1):
           c = c+1
           print(c,end=' ')
       print()
row(5)