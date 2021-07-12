class Person:
    def pvalues(self,pname,age):
        self.pname=pname
        self.age=age
        print(self.pname,self.age)
    def __str__(self):
        return self.pname+str(self.age)
obj=Person()
obj.pvalues('anu',18)
print(obj)