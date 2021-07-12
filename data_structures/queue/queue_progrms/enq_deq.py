front=0
rear=0
size=int(input('enter size of queue'))
q=[]

def insert():
    global front,rear,q,size
    if rear>=size:
        print('queue is full')
    else:
        ele=int(input('enter the element'))
        q.insert(rear,ele)
        rear=rear+1
        for i in range(front,rear):
         print(q[i])
def delete():
    global front,rear,q,size
    if rear==front:
        print('queue is empty')
    else:
        front+=1
        for i in range(front,rear):
         print(q[i])
def display():
    print(q)
n=0
while n!=1:
    print('1.enque,2.deque,3.display')
    c=int(input('enter choice'))
    if c==1:
        insert()
    elif c==2:
        delete()
    elif c==3:
        display()
    else:
        print('select avalid option')
    n=int(input('press 2 to continue 1 to exit'))



