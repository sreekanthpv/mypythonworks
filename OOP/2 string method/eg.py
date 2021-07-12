class College:
    collegename='lt'
    def __init__(self,name,roll):
        self.roll=roll
        self.name=name

    def print(self):
        print('collehename',self.collegename,self.name,self.roll)
    def __str__(self):
        return str(self.roll)+self.name+' '+College.collegename
obj=College('anu',5)
print(obj)
ob=College('amal',5)
print(ob)

ob1=College()