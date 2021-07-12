class Employee:
    company='abc company'
    def setval(self,name,id,sal,dep):
        self.name=name
        self.id=id
        self.sal=sal
        self.dep=dep

    def printval(self):
        print('name:',self.name)
        print('id:',self.id)
        print('sal:',self.sal)
        print('dep',self.dep)
        print(Employee.company)

obj=Employee()
obj.setval('pp','id1',20000,'computer')
obj.printval()

ob2=Employee()
obj.setval('dd','id2',2000,'biology')
obj.printval()