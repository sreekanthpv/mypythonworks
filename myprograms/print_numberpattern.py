
# 1
# 2 3
# 4 5 6
# 7 8 9 10
def row(r):
   c=0
   for i in range(0,r):

       for j in range(0,i+1):
           c = c+1
           print(c,end=' ')
       print()
row(5)