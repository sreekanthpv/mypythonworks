users={
    1000:{'empid':1000,'empname':'ajay','job':'developer','sal':25000},
    1001:{'empid':1001,'empname':'ram','job':'developer','sal':20000},
    1002:{'empid':1002,'empname':'arun','job':'qa','sal':3000},
    1003:{'empid':1003,'empname':'nithin','job':'qa','sal':15000}

}

def valid(**kwargs):
    user=kwargs['acno']
    password=kwargs['password']
    if user in users:
        if password == users[user]['password']:
            print('success')
        else:
            print('invalid password')
    else:
        print('invalid account no')



valid(acno=1000,password='user0')