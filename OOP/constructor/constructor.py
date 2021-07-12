#constructor : to initialize instance variables
#constructor automatically invoke\start when creating object


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name,self.age)
obj=Person('anu',24)
obj1=Person('biju',23)
obj1.print()
obj.print()
