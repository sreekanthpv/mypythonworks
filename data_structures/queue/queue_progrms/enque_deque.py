que=[]
size=int(input('enetr size'))
front=0
rear=0
n=0
def insert():
    global front,rear,size,que
    if rear>=size:
        print('que is full')
    else:
        p=int(input('enter element'))
        que.insert(rear,p)
        rear=rear+1
        for i in range(front,rear):
            print(que[i])
def delete():
    global front,rear,size,que
    if rear==front:
        print('que is empty')
    else:
        front+=1
        for i in range(front,rear):
            print(que[i])
while n!=1:
    print('enter operation to perform')
    opt=int(input('1 enque,2 deque'))
    if opt ==1:
        insert()
    elif opt==2:
        delete()
    n=int(input('press 1 to exit or continue'))
