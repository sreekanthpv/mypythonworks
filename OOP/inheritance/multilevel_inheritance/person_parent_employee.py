class Person:
    def pvalue(self,name,age):  #person child parent student
                                        # child parent in herit person
                                        #student inherit child
        self.name=name
        self.age=age
        print(self.name,self.age)
class Parent(Person):
    def pavalue(self,pname,page):
        self.pname=pname
        self.page=page
        print(self.pname,self.page)
class Employee(Parent):
    def evalue(self,ename,eid):
        self.ename=ename
        self.eid=eid
        print(self.ename,self.eid)
ob=Parent()
ob.pvalue('anu',28)
ob.pavalue('sasi',70)

obj=Employee()
obj.pvalue('abu',28)
obj.pavalue('ak',100)
obj.evalue('sam','id2')
