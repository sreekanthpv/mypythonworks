emp={
    1000:{'eid':1000,'ename':'anu','sal':3000,'des':'developer'},  #nested dictionery
1001:{'eid':1001,'ename':'ani','sal':7000,'des':'hr'},
1002:{'eid':1002,'ename':'anakha','sal':6000,'des':'analyst'},
1003:{'eid':1003,'ename':'amslu','sal':4000,'des':'developer'},
}
# print(emp[1000]['ename'])

# a=int(input('enter id'))
# c=int(input('select 1.ename,2.sal,3.designation '))
# if c==1:
#     print(emp[a]['ename'])
# elif c==2:
#     print(emp[a]['sal'])
# elif c==3:
#     print(emp[a]['des'])
# else:
#     print('invalid')



# a=int(input('enter id'))
# if a not in emp: #
#     print('invalid id')
# else:
#
#     b = input('enter ename,sal,des')
#     if b not in emp[a]:
#         print('invalid key')
#     else:
#         print(emp[a][b])




a = int(input('enter id'))
b = input('enter ename,sal,des')
if a not in emp and b not in emp[a]:
        print('invalid id')
else:

        # b = input('enter ename,sal,des')
        # if b not in emp[a]:
        #     print('invalid key')
        # else:
            print(emp[a][b])