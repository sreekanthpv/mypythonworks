class Student:
    school='abcschool'
    def set(self,name,roll,mark):
            self.name=name
            self.roll=roll
            self.mark=mark

    def print(self):
        print('name',self.name)
        print('roll',self.roll)
        print('mark',self.mark)
        print(Student.school)
obj=Student()
# a=input('enter name')
# b=input('enter age')
# c=input('enter mark')

obj.set('anu',2,0)
obj.print()
ob2=Student()
ob2.set('vijay',3,1)
ob2.print()