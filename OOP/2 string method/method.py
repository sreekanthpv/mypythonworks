# 2 string method
class Vehicle:
    def values(self,model,reg,color):
        self.model=model
        self.reg=reg
        self.color=color
    def Print(self):
        print(self.model,self.color,self.reg)
    def __str__(self):     # 2 string method (usage in jango)
        return self.model  #return the model name to print(obj)
obj=Vehicle()
obj.values('i20',1100,'blue')
obj.Print()
print(obj)