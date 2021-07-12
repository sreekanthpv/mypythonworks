class Person:
    def pdetails(self,name,age,add):
        self.name=name
        self.age=age
        self.add=add
class Employee(Person):
    def edetails(self,empname,id,company):
        self.empname=empname
        self.id=id
        self.company=company
        print(self.name,self.age,self.add)
        print(self.empname,self.id,self.company)
e=Employee()

e.pdetails('anu',32,'cvb')
e.edetails('lal','id2','asus')
