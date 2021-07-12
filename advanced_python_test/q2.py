# 2. Create an example for three types of inheritance in one program by using College as main class?


class College:
    def cvalues(self,cname):
        self.cname=cname
        print('college name :',cname)
class Teacher(College):
    def tvalues(self,tname,id,dep):
        self.tname=tname
        self.id=id
        self.dep=dep
        print('teacher name :',self.tname,'id :',self.id,'department:',self.dep)
class Student(Teacher):
    def svalues(self,sname,sid):
        self.sname=sname
        self.sid=sid
        print('student name:',self.sname,'class :',self.sid)
class Parent(Student,Teacher):
        def pvalues(self,pname,age):
            self.pname=pname
            self.age=age
            print('parent :',self.pname,'age:',self.age)
obj1=Teacher()
obj1.cvalues('ABC college')
obj1.tvalues('anu','id1','bcom')

obj2=Student()
obj2.cvalues('BAC college')
obj2.tvalues('anil','id4','bca')
obj2.svalues('hari','id12')

obj3=Parent()
obj3.cvalues('AAAcolege')
# obj3.tvalues('sruthy','id7','cs')
obj3.pvalues('sunil',23)
obj3.svalues('ak','id13')
