#if we use same method for parent and child class the child class overrides parent class
#same method name and same num of arguments

class Parent:
    def pvalue(self,name):
        self.name=name
        print(self.name)
class Child(Parent):
    def pvalue(self,name2):
        self.name2=name2
        print('child class',self.name2)
obj=Child()
obj.pvalue('sasi')
