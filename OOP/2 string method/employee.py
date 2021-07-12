class Employee:
    def __init__(self,ename,exp):
        self.ename=ename
        self.exp=exp
        print(self.ename,self.exp)
    def __str__(self):
        return self.ename+' '+str(self.exp)
obj=Employee('anu',2)
print(obj)