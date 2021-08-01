# **KWARGS.
#
# def PrintEmp(**kwargs):
#     print(kwargs)
# PrintEmp(id=1,name='anu',designation='developer')
# #gives clarity to the arguments and return dictionery output
#
#
#


users={
    1000:{"acconu_num":1000,"password":"user1","balance":3000},
    1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
    1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
    1003: {"acconu_num": 1003, "password": "user3", "balance": 6000}
}


def valid(**kwargs):
    user=kwargs['accno']
    password=kwargs['password']
    if user in users:
        if password==users[user]['password']:
            print('success')
        else:
            print('invalid')
valid(accno=1000,password='user1')

def getbal(user):
    # print(user)
    if user in users:
        print(users[user]['balance'])
    else:
        print('invalid')
getbal(100)

