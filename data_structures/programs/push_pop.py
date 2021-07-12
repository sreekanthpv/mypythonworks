#stack is a data structure that follows the LIFO principle
# to implement stack we need two operations PUSH and POP
# PUSH..adds an elemnt at the top of the stack
#POP removes an element from the top of the stack

top=0
s=int(input('size'))
stk=[]
def push():
    global top,s
    if top>=s:
        print('stack is full')
    else:
        ele=int(input('enter element'))
        stk.append(ele)
        top=top+1
def pop():
    global top,s
    if top<=0:
        print('stack empty')
    else:
        stk.pop()
        top=top-1
def display():
    print(stk)
n=0
while n!=1:
    print('1.push,2.pop,3.display')
    c=int(input('enter choice'))
    if c==1:
        push()
    elif c==2:
        pop()
    elif c==3:
        display()
    else:
        print('invalid choice')
    n=int(input('press 1 to exit press 2 to contine'))







