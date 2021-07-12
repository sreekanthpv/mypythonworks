class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # print(self.name,self.age)
    def print(self):
        print('name',self.name)
        print('age',self.age)
class Student(Person):
    def __init__(self,roll,mark,name,age):
        super().__init__(name,age)
        self.roll=roll
        self.mark=mark
    def print1(self):
        print(self.roll)
        print(self.mark)
obj=Student(1,22,'anu',18)
obj.print()
obj.print1()
