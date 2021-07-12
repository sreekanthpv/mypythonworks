class Person:
    def pvalue(self,name,age,add):
        self.name=name
        self.age=age
        self.add=add
        # print(self.name,self.age,self.add)
class Parent:
    def pavalue(self,pname,page,padd):
        self.pname=pname
        self.page=page
        self.padd=padd
        # print(self.pname,self.page,self.padd)
class Employee(Parent,Person):
    def evalue(self,ename,id,comp):
        self.ename=ename
        self.id=id
        self.comp=comp
        print(self.name, self.age, self.add)
        print(self.pname, self.page, self.padd)
        print(self.ename,self.id,self.comp)
obj=Employee()
obj.pvalue('anu',30,'assddf')
obj.pavalue('basi',80,'qwerty')
obj.evalue('sabu',2,'asus')
