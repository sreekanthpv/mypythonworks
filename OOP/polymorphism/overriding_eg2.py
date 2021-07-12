class Employee1:
    def evalue(self,empname):
        self.empname=empname
        print(self.empname)
class Employee2(Employee1):
    def evalue(self,name):
        self.name=name
        print('employe2',self.name)
obj=Employee2()
obj.evalue('sarkar')

#employee2 over rides emp1