class teacher:
    cname='abc college'
    def __init__(self,name,sub,id):
        self.name=name
        self.sub=sub
        self.id=id

    def print(self):
        print('name',self.name,'  sub',self.sub,'  id',self.id,'  college',teacher.cname)
obj=teacher('anu','cpp',1,)
obj2=teacher('sree','python',2,)
obj.print()
obj2.print()
