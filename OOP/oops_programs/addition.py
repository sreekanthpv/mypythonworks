class addition:
    def set(self,v1,v2):
        self.v1=v1
        self.v2=v2
    def print(self):
        print(self.v1+self.v2)
obj=addition()
a=int(input('enter1'))
b=int(input('enter2'))
obj.set(a,b)
obj.print()