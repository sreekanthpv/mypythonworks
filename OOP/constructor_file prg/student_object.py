class Student:
    def __init__(self,name,roll,dep,mark):
        self.name=name
        self.roll=roll
        self.dep=dep
        self.mark=mark
    def print(self):
        print(self.name,self.roll,self.dep,self.mark)
v=open('student','r')
for i in v:
    z=i.rstrip('\n').split(',')
    # print(z)
    name=z[0]
    roll=z[1]
    dep=z[2]
    mark=z[3]
    obj=Student(name,roll,dep,mark)
    obj.print()
