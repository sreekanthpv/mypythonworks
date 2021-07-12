class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):
    def cvalue(self,add,cls):
        self.add=add
        self.cls=cls
        print(self.add,self.cls)
class Student(Child):
    def svalue(self,roll,mark):
        self.roll=roll
        self.mark=mark
        print(self.roll,self.mark)
ch=Child()
ch.pvalue('ani',2)
ch.cvalue('asdf',5)

st=Student()
st.pvalue('sabu',3)
st.cvalue('aaaa',10)
st.svalue(9,100)