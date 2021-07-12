class Person:#derrived class is Student
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child: #derrived class is Student
    def cvalue(self,add,cls):
        self.add=add
        self.cls=cls
        print(self.add,self.cls)
class Student(Child,Person):   #Student is derrived from person and child
    def svalue(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno,self.mark)
st=Student()
st.pvalue('anu',28)
st.cvalue('aaaa',9)
st.svalue(1,100)