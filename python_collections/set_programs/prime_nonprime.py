s1={1,2,3,4,5,6,7,8,9,0,15}
prime=set()
notprime=set()
for i in s1:
    if i>1:
        for j in range(2,i):
            if i%j==0:
                notprime.add(i)
                break

        else: 
            prime.add(i)
print('prime',prime)
print('notprime',notprime)


