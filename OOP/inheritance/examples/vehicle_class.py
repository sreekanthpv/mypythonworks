class Vehicle:
    def __init__(self,reg,model,color):
        self.reg=reg
        self.model=model
        self.color=color
    def print(self):
        print(self.reg,self.model,self.color)

class Bus(Vehicle):
    def __init__(self,name,reg,model,color):
        super().__init__(reg,model,color)
        self.name=name
        print(self.name)
obj=Bus('bus1',10,1998,'red')
obj.print()