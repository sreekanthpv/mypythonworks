class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name)
        print(self.age)
class Employee(Person):
    def __init__(self,empname,id,name,age):
        super().__init__(name,age)
        self.empname=empname
        self.id=id
    def print2(self):
        print(self.empname)
        print(self.id)
obj=Employee('sasi','id2','person3',22)
obj.print()
obj.print2()
