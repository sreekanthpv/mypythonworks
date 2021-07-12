
# 5. What is method overriding give an example using Teacher class?


class Teacher1:
    def values(self,tname1):
        self.tname1=tname1
        print('teacher 1:',self.tname1)
class Teacher2(Teacher1):
    def values(self,tname2):
        self.tname2=tname2
        print('teacher 2:',self.tname2)
ob=Teacher2()
ob.values('anu')