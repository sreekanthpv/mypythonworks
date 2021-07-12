class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name,'+',self.age)
    def __str__(self):
        return self.name
v=open('file1','r')
for i in v:
     z=i.rstrip('\n').split(',')

     n=z[0]
     a=z[1]
     obj=Person(n,a)
     obj.print()
     # print(obj)