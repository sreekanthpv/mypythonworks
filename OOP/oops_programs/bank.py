class bank:
    def acc(self,bname,name,acno):
        self.bname=bname
        self.name=name
        self.acno=acno
        print('bank is :',self.bname)
        print('your name :',self.name)
        print('account number :',self.acno)
    def set(self,dpw,bal):
          self.dpw=dpw
          self.bal=bal
    def withdraw(self):
        if self.dpw>self.bal:
            print('insufficient')
        else:
            self.bal=self.bal-self.dpw
            print('bal',self.bal)
    def dep(self):

        self.bal=self.dpw+self.bal
        print('balance',self.bal)

obj=bank()
obj.acc('sbi','purushu',3)
print('1.deposit','2.withdraw')
c=int(input('enter choice'))
b=1000
if c==2:
 a=int(input('enter amount'))
 obj.set(a,b)
 obj.withdraw()
elif c==1:
   d=int(input('enter the amount'))
   obj.set(d,b)
   obj.dep()

