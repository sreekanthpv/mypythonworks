class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Parent(Person):
    def pvalue(self,pname):
        self.pname=pname
        print(self.pname)
obj=Parent()
obj.pvalue('ajay',2)

