q=[]
f=0
r=0
s=int(input('enter the size'))
def insert():
    global q,f,r
    if r>=s:
        print('queue is full')
    else:
     ele=int(input('enter the element'))
     q.append(ele)
     r=r+1
     for i in range(f,r):
         print(q[i])
def delete():
    global r,f,q
    if r<=f:
        print('queue is empty')
    else:
        # for i in range(1):
        #     q.remove(q[i])
        #     r=r-1

        for i in range(f,r):
            print(q[i])
def display():
    print(q)
n=0
while(n!=1):
    print('1.enque,2.deque,3.display')
    c=int(input('enter choice'))
    if c==1:
        insert()
    elif c==2:
        delete()
    elif c==3:
        display()
    else:
        print('select valid option')
    n=int(input('press 2 to contiue 1 to exit'))

