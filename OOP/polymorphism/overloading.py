# polymorphism...is a feature in python (inheritance) ie is the child class
# contain same fun name in the parent class
#in method overloading...the methods have same fun name and def num of arguments



class Operators:
    def num(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(self.n1,self.n2)
class Display(Operators):
    def num(self,n3):
        self.n3=n3
        print(self.n3)
d=Display()
d.num(3,2)

