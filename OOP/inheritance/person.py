
#single inheritance


class Person: #parent class/base class/super class
    def pdetails(self,name,age,add):
        self.name=name
        self.age=age
        self.add=add
        # print(self.name,self.age,self.add)
class student(Person):#child class/derrived class/sub class
    def sdetails(self,rollno,dep,mark):
        self.rollno=rollno
        self.dep=dep
        self.mark=mark
        print(self.rollno,self.dep,self.mark)
        print(self.name, self.age, self.add)
# pe=person()
s=student()
s.pdetails('anu',24,'aaa')
s.sdetails(5,'cs',100)

