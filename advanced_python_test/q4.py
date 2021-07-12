# 4. Create an Person class using constructor and build a child class for Employee?


class Person:
    def __init__(self,pname,age,add):
        self.pname=pname
        self.age=age
        self.add=add
        print(self.pname,self.age,self.add)
class Employee(Person):
    def __init__(self,ename,id,pname,age,add):
        super().__init__(pname,age,add)
        self.ename=ename
        self.id =id
        print('employ name',self.ename,'employ id',self.id)
obj=Employee('sarath','id1','anu',19,'asc address')