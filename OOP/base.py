#oop

#class :design pattern/blueprint
#object:real world entity
#reference:to perform operations on object

#
#
# class person:
#     def walk(self):  #functions are called methods
#             print('person walking')
#     def read(self): #method2
#         print('person reading')
#
# obj1=person() #varname=classname () is object
# obj1.walk()   #varname.functionname()
# obj1.read()
#
#



class person:
    def setval(self,name,age):
        self.name=name #instance variable variable under a class
        self.age=age
    def printval(self):
        print('name:',self.name)
        print('age:',self.age)

obj=person()
obj.setval('anu',28)
obj.printval()



