# 1. Create a child class Car that will inherit all of the variables and methods of Vehicle class?



class Vehicle:
    def vvalues(self,regno,model,color):
        self.regno=regno
        self.model=model
        self.color=color
class Car(Vehicle):
    def cvalues(self,chaseno):
        self.chaseno=chaseno
    def print(self):
        print(self.regno,self.model,self.color,self.chaseno)
obj=Car()
obj.vvalues('1234','m1','red')
obj.cvalues('C1')
obj.print()

