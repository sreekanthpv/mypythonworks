
# authenticate(acno,pass):
#bal_enquiry(acno)
#funf transfer(acno,toac,amt):



class bank:
  users={
    1000:{"acconu_num":1000,"password":"user1","balance":3000},
    1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
    1002: {"acconu_num": 1002, "password": "user3", "balance": 5000},
    1003: {"acconu_num": 1003, "password": "user4", "balance": 6000}
  }
  session={}
  def validate(self,accno):
    if accno in self.users:
      return True
    else:
      return False

  def authenticate(self,**kwargs):

        accno=kwargs['accno']
        password=kwargs['password']
        user=self.validate(accno)
        # print(user)
        if user:        #means user==True
          if password==self.users[accno]['password']:
              # print('login success')
              self.session['user']=accno
              return accno

          else:

              print('invalid password')
              return -1
        else:

           print('invalid account number')
           return 0

  def balenquiry(self,accno):
      if accno==self.session['user']:
        print('bal is ',self.users[accno]['balance'])
      else:
          print('you must login')

  def fund_transfer(self,user,to_acno,amt):
      if self.validate(to_acno):
          # print(user)
          balance=self.users[user]['balance']
          if balance < amt:
               print('insufficient balance')
          else:
               self.users[user]['balance']-=amt
               self.users[to_acno]['balance']+=amt
  def logout(self):
      self.session['user']=0
      print('logout success')



obj1=bank()
user=obj1.authenticate(accno=1002,password='user3')
# print(user)
if (user==-1) | (user==0):
    print('authentication  failed')
else:
    obj1.balenquiry(user)
obj1.fund_transfer(user,1001,500)
obj1.balenquiry(user)
obj1.logout()










