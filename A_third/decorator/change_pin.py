def admin_req(fun):
    def wrapper(name,id):
        if name=='admin':
            return fun(name,id)
        else:
            raise Exception ('you are not allowed')
    return wrapper

@admin_req
def change_pin(user,pin):
    us=user
    mypin=pin
    return str(mypin)+ ' by '+us
@admin_req
def del_ac(user,acno):
    return str(acno)+' is '+'deleted' #string concatenation
print('pin changed',(change_pin('admin',1008)))
print(del_ac('admin',1000))