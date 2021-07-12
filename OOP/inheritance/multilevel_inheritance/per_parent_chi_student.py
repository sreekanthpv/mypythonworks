class Person:
    def pvalues(self,pname,job):
        self.pname=pname
        self.job=job
        print(self.pname,self.job)
class Parent(Person):
    def pavalues(self,paname,paage):
        self.paname=paname
        self.paage=paage
        print(self.paname,self.paage)
class Child(Person):
    def cvalue(self,cname,cls):
        self.cname=cname
        self.cls=cls
        print(self.cname,self.cls)
class Student(Child):
    def svalue(self,sname,clg):
        self.sname=sname
        self.clg=clg
        print(self.sname,self.clg)
obj1=Parent()
obj1.pvalues('anu','prog')
obj1.pavalues('sasi',81)


obj2=Child()
obj2.pvalues('ammu','clerk')
obj2.cvalue('boby',2)

obj3=Student()
obj3.cvalue('babby',6)
obj3.svalue('stu1','sscollege')

