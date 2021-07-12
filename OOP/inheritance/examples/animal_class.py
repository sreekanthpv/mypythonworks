class Animal:
    def __init__(self,catagory,color):
        self.catagory=catagory
        self.color=color
    def print(self):
        print(self.color,self.catagory)
class Dog(Animal):
    def __init__(self,name,catagory,color):
        super().__init__(catagory, color)
        self.name=name
        print(self.name)
obj=Dog('pp','dog','red')
obj.print()